import json
import html
import logging
import os
import re
from pathlib import Path

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from database import (
    init_db,
    get_user,
    complete_lesson_with_rewards,
    get_completed_lessons,
    add_badge,
    get_badges,
    get_user_level,
    open_chest,
    complete_quiz_with_rewards,
)
from daily_chat import PROMPTS, reply_to_daily_message
from course_runtime import can_open_lesson, visible_course_lessons
from quiz_option_order import randomized_question_copy
from course_lesson_adapters import adapt_conversation_lessons, adapt_unified_orthography_lessons
from course_quiz_review import quiz_is_available
from latin_course_runtime import load_latin_courses
from arami_lesson1_telegram import callback as arami_lesson1_callback
from arami_lesson5_telegram import callback as arami_lesson5_callback
from arami_course1_runtime import (
    load_arami_lesson1_content,
    load_arami_lesson1_interactions,
    load_arami_lesson5_interactions,
    load_arami_lesson5_source,
)
from kurdish_months import months_menu_keyboard, get_months_lesson
from arami_course1_telegram import (
    callback as arami_course1_callback,
    course_menu_keyboard as arami_course1_menu_keyboard,
    load_manifest as load_arami_course1_manifest,
    load_question_banks as load_arami_course1_question_banks,
)

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def award_arami_assessment(user_id, lesson_id):
    """Grant 20 XP once for a Course 1 assessment, never for practice or retries."""
    return complete_quiz_with_rewards(
        user_id, f"arami_assessment:{lesson_id}", points=20
    )

# Load .env without requiring an extra dependency. Environment variables already
# set by the host always take precedence.
ENV_FILE = BASE_DIR / ".env"
if ENV_FILE.is_file():
    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

def load_json(filename):
    path = BASE_DIR / filename
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def format_lesson_draft(markdown):
    """Render lesson Markdown as readable Telegram text while preserving table values."""
    source_lines = markdown.splitlines()
    lines = []
    index = 0
    while index < len(source_lines):
        stripped = source_lines[index].strip()
        if re.fullmatch(r"(?:---+|\*{3,}|_{3,})", stripped):
            index += 1
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            table = []
            while index < len(source_lines):
                candidate = source_lines[index].strip()
                if not (candidate.startswith("|") and candidate.endswith("|")):
                    break
                cells = [cell.strip() for cell in candidate.strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
                    table.append(cells)
                index += 1
            if table:
                headers = table[0]
                for row in table[1:]:
                    pairs = [
                        f"{headers[cell]}: {value}"
                        for cell, value in enumerate(row)
                        if cell < len(headers) and value
                    ]
                    lines.append(" • ".join(pairs) if pairs else " | ".join(row))
                if len(table) == 1:
                    lines.append(" | ".join(headers))
            continue
        if stripped.startswith("#"):
            line = stripped.lstrip("#").strip()
        elif stripped.startswith(">"):
            line = stripped.lstrip(">").strip()
        else:
            line = source_lines[index]
        line = re.sub(r"</?text>", "", line)
        line = line.replace("**", "").replace("__", "").replace("`", "")
        lines.append(line)
        index += 1
    return "\n".join(lines).strip()

# The retired 22-lesson Course 1 remains in course_data for historical audit only.
# It is intentionally not loaded into runtime; the active 21-lesson Arami course
# uses isolated, namespaced lesson IDs and interaction banks.
LESSON_DATA = {}
QUIZ_DATA = {}
LESSON_BUTTONS = {}


# Courses 2 and 3 are activated by the project owner. Editorial review
# metadata stays attached to lesson data; it is not an activation gate.
COURSE_MANIFEST = load_json("courses.json")
COURSES = sorted(COURSE_MANIFEST.get("courses", []), key=lambda item: item.get("order", 999))
CONVERSATION_DRAFTS = [
    load_json("course_data/daily_conversation_lessons_01_06.json"),
    load_json("course_data/daily_conversation_lessons_07_30.json"),
    load_json("course_data/daily_conversation_lessons_31_36.json"),
    load_json("course_data/daily_conversation_lessons_37_42.json"),
]
CONVERSATION_LESSONS, CONVERSATION_QUIZZES = adapt_conversation_lessons(
    "daily_conversation", CONVERSATION_DRAFTS
)
UNIFIED_ORTHOGRAPHY_DRAFT = load_json("course_data/unified_orthography_lessons_01_66.json")
UNIFIED_LESSONS, UNIFIED_QUIZZES = adapt_unified_orthography_lessons(UNIFIED_ORTHOGRAPHY_DRAFT)
for course_lessons, course_quizzes in (
    (CONVERSATION_LESSONS, CONVERSATION_QUIZZES),
    (UNIFIED_LESSONS, UNIFIED_QUIZZES),
):
    duplicate_ids = set(LESSON_DATA).intersection(course_lessons)
    if duplicate_ids:
        raise ValueError(f"Duplicate lesson IDs across courses: {sorted(duplicate_ids)}")
    LESSON_DATA.update(course_lessons)
    QUIZ_DATA.update(course_quizzes)

# The two Kurmanji Latin courses remain separate by source part, lesson IDs and quiz keys.
LATIN_COURSE_DRAFT = load_json("course_data/latin_courses_manifest_draft.json")
LATIN_LESSONS, LATIN_QUIZZES, LATIN_COURSE_RECORDS = load_latin_courses()
latin_manifest_courses = LATIN_COURSE_DRAFT.get("courses", [])
if [item.get("id") for item in latin_manifest_courses] != [
    item["id"] for item in LATIN_COURSE_RECORDS
]:
    raise ValueError("Latin course manifest and runtime parser course IDs do not match")
for manifest_course, parsed_course in zip(latin_manifest_courses, LATIN_COURSE_RECORDS):
    if manifest_course.get("lesson_ids") != parsed_course["lesson_ids"]:
        raise ValueError(f"Latin lesson manifest mismatch for {parsed_course['id']}")
    registered_course = next(
        (item for item in COURSES if item.get("id") == parsed_course["id"]),
        None,
    )
    if registered_course is None or registered_course.get("status") != "active":
        raise ValueError(f"Latin course is missing or inactive in courses.json: {parsed_course['id']}")
    if registered_course.get("lesson_ids") != parsed_course["lesson_ids"]:
        raise ValueError(f"Runtime course lesson IDs mismatch for {parsed_course['id']}")
    if registered_course.get("source_part") != parsed_course["source_part"]:
        raise ValueError(f"Runtime source part mismatch for {parsed_course['id']}")

duplicate_latin_ids = set(LESSON_DATA).intersection(LATIN_LESSONS)
if duplicate_latin_ids:
    raise ValueError(f"Duplicate lesson IDs across courses: {sorted(duplicate_latin_ids)}")
for lesson_id, lesson in LATIN_LESSONS.items():
    lesson["content"] = format_lesson_draft(lesson["content"])
LESSON_DATA.update(LATIN_LESSONS)
QUIZ_DATA.update(LATIN_QUIZZES)
COURSES.sort(key=lambda item: item.get("order", 999))

async def send_lesson_infographic(message, lesson_id):
    """Compatibility no-op: lessons are intentionally delivered as text only."""
    return

# Legacy 22-lesson Course 1 is retained only as archived source data.
ORDER = []
COURSE_LESSON_ORDER = {
    course["id"]: visible_course_lessons(course, LESSON_DATA)
    for course in COURSES
}
# Arami lessons are delivered by their dedicated source reader rather than
# LESSON_DATA, but still participate in the shared learner-progress ledger.
ARMI_MANIFEST = load_arami_course1_manifest(BASE_DIR)
ARMI_LESSON_IDS = [item["id"] for item in sorted(ARMI_MANIFEST["lessons"], key=lambda item: item["number"])]
ARMI_COURSE_RECORD = next(
    (course for course in COURSES if course.get("id") == "arami_orthography_foundations"),
    None,
)
if ARMI_COURSE_RECORD is None or ARMI_COURSE_RECORD.get("lesson_ids") != ARMI_LESSON_IDS:
    raise RuntimeError("Arami Course 1 manifest and registered progress lesson IDs do not match")
COURSE_LESSON_ORDER["arami_orthography_foundations"] = ARMI_LESSON_IDS
ORDER = COURSE_LESSON_ORDER.get("orthography_basic", [])
LESSON_COURSE = {
    lesson_id: course_id
    for course_id, lesson_ids in COURSE_LESSON_ORDER.items()
    for lesson_id in lesson_ids
}

def course_is_active(course_id):
    course = next((item for item in COURSES if item.get("id") == course_id), None)
    return bool(course and course.get("status") == "active")


LATIN_COURSE_IDS = {
    "kurmanji_latin_orthography",
    "kurmanji_latin_grammar",
}


def quiz_requires_submission(lesson):
    """Use explicit select-then-submit controls for interactive learning courses."""
    course_id = LESSON_COURSE.get(lesson)
    return lesson == "وانە_3" or course_id in LATIN_COURSE_IDS or course_id == "unified_orthography"


def lesson_practice_callback(lesson):
    """Build the existing source-aligned interactive practice callback."""
    suffix = lesson.removeprefix("وانە_") if lesson.startswith("وانە_") else lesson
    return f"quiz_{suffix}_start"


def validate_activated_course_runtime():
    """Fail fast unless every activated course and its interactive lessons are ready."""
    if not course_is_active("arami_orthography_foundations"):
        raise RuntimeError("Required course arami_orthography_foundations is not active in courses.json")
    arami_manifest = load_arami_course1_manifest(BASE_DIR)
    arami_banks = load_arami_course1_question_banks(BASE_DIR)
    if len(arami_manifest.get("lessons", [])) != 21:
        raise RuntimeError("Arami Course 1 must load exactly 21 lessons")
    expected_shared_banks = set(range(2, 5)) | set(range(6, 22))
    if set(arami_banks) != expected_shared_banks:
        raise RuntimeError("Arami Course 1 must load the 19 lesson-scoped shared question banks")
    lesson1_content = load_arami_lesson1_content(BASE_DIR)
    lesson1_bank = load_arami_lesson1_interactions(BASE_DIR)
    lesson5_source = load_arami_lesson5_source(BASE_DIR)
    lesson5_bank = load_arami_lesson5_interactions(BASE_DIR)
    if not lesson1_content or not lesson5_source:
        raise RuntimeError("Arami Course 1 dedicated Lesson 1 or Lesson 5 source is unavailable")
    for lesson_number, bank in ((1, lesson1_bank), (5, lesson5_bank)):
        for mode in ("practice", "assessment"):
            if not bank.get(mode):
                raise RuntimeError(f"Arami Course 1 Lesson {lesson_number} {mode} is unavailable")
    logger.info(
        "Course runtime ready: %s status=active lessons=21 readers=21 practice=21 assessment=21 shared_banks=19 dedicated_banks=2",
        "arami_orthography_foundations",
    )
    expected_counts = {"daily_conversation": 42, "unified_orthography": 66, "kurmanji_latin_orthography": 12, "kurmanji_latin_grammar": 12}
    for course_id, expected_count in expected_counts.items():
        if not course_is_active(course_id):
            raise RuntimeError(f"Required course {course_id} is not active in courses.json")
        lesson_ids = COURSE_LESSON_ORDER.get(course_id, [])
        if len(lesson_ids) != expected_count:
            raise RuntimeError(
                f"Required course {course_id} loaded {len(lesson_ids)} lessons; "
                f"expected {expected_count}"
            )
        missing_lessons = [lesson_id for lesson_id in lesson_ids if lesson_id not in LESSON_DATA]
        missing_quizzes = [lesson_id for lesson_id in lesson_ids if not QUIZ_DATA.get(lesson_id)]
        if missing_lessons or missing_quizzes:
            raise RuntimeError(
                f"Required course {course_id} is incomplete at startup: "
                f"missing_lessons={missing_lessons}, missing_quizzes={missing_quizzes}"
            )
        logger.info(
            "Course runtime ready: %s status=active lessons=%d quizzes=%d",
            course_id, len(lesson_ids), sum(bool(QUIZ_DATA.get(key)) for key in lesson_ids),
        )

def next_course_lesson(lesson):
    course_id = LESSON_COURSE.get(lesson)
    order = COURSE_LESSON_ORDER.get(course_id, [])
    if lesson not in order:
        return None
    index = order.index(lesson)
    return order[index + 1] if index + 1 < len(order) else None

def resource_link_keyboard(message_html):
    """Build compact, tappable resource links without changing their destinations."""
    links = re.findall(r'<a href="([^"]+)">([^<]+)</a>', message_html)
    buttons = [
        InlineKeyboardButton(
            (label.strip()[:48] + ("…" if len(label.strip()) > 48 else "")),
            url=url,
        )
        for url, label in links
    ]
    rows = [buttons[index:index + 2] for index in range(0, len(buttons), 2)]
    return InlineKeyboardMarkup(rows) if rows else None


def active_course_lessons():
    return [
        lesson
        for course in COURSES
        if course_is_active(course.get("id"))
        for lesson in COURSE_LESSON_ORDER.get(course.get("id"), [])
        if lesson in LESSON_DATA
    ]
MENU = ReplyKeyboardMarkup(
    [
        ["📚 وانەکان", "📘 کۆرسەکان"],
        ["ڕێنووسی لاتینی کوردیی"],
        ["📕 ڕێنووسی سەرەتاییی کوردی"],
        ["🗓️ مانگەکانی ساڵ لەناو کورداندا"],
        ["🌐 گۆڕینی زمانی تەلەگرام"],
        ["⌨️ تەختەکلیلی کوردی"],
        ["📖 وشەنامەی کوردی"],
        ["💬 گفتوگۆی ڕۆژانە"],
        ["👤 پێشکەوتنم", "🧭 ڕێگای فێربوون"],
        ["🎁 سەنوقی خەڵات", "📝 تاقیکردنەوەکان"],
    ],
    resize_keyboard=True,
)

def can_open(user_id, lesson):
    course_id = LESSON_COURSE.get(lesson)
    if course_id is None or not course_is_active(course_id):
        return False
    completed = set(get_completed_lessons(user_id))
    order = COURSE_LESSON_ORDER.get(course_id, [])
    # Every course follows one strict sequence. A stale/non-contiguous progress
    # record must never unlock a later lesson while any earlier lesson is missing.
    return can_open_lesson(order, completed, lesson)

BADGE_COURSE_TITLES = {
    "arami_orthography_foundations": "کۆرسی ١: ڕێنووسی سەرەتاییی کوردی",
    "daily_conversation": "کۆرسی ٢: وتووێژ",
    "unified_orthography": "کۆرسی ٣: ڕێنووسی یەکگرتوو",
    "kurmanji_latin_orthography": "Kursa 1: Bingehên Rastnivîsîna Kurmancî ya Latînî",
    "kurmanji_latin_grammar": "Kursa 2: Bingehên Gramera Kurmancî",
}


def current_progress_badges(user_id):
    """Build visible badges from current active lesson IDs, never stale stored labels."""
    completed = set(get_completed_lessons(user_id))
    visible = []
    for course in COURSES:
        course_id = course.get("id")
        if not course_is_active(course_id):
            continue
        title = BADGE_COURSE_TITLES.get(course_id)
        if not title:
            continue
        for number, lesson_id in enumerate(COURSE_LESSON_ORDER.get(course_id, []), 1):
            if lesson_id not in completed:
                break
            visible.append(f"🏅 {title} — وانەی {number}")
    return visible


def check_badges(user_id):
    """Keep the legacy badge ledger compatible; progress display uses canonical labels."""
    completed = set(get_completed_lessons(user_id))
    for course_id, title in BADGE_COURSE_TITLES.items():
        if not course_is_active(course_id):
            continue
        for number, lesson_id in enumerate(COURSE_LESSON_ORDER.get(course_id, []), 1):
            if lesson_id not in completed:
                break
            add_badge(user_id, f"🏅 {title} — وانەی {number}")

def lesson_keyboard(lesson):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ تەواوکردنی وانە", callback_data=f"finish_{lesson}")
    ]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["daily_chat_mode"] = False
    context.user_data.pop("daily_chat_scenario", None)
    context.user_data.pop("daily_chat_stage", None)
    context.user_data.pop("quiz", None)
    get_user(update.effective_user.id)
    welcome = """🌱 سڵاو، بەخێربێیت بۆ کەژیار

خوایە وەتەن ئاوا کەی
چەند دڵگیر و شیرینە
دەشتی خۆش و ڕەنگینە
ئاوی کەوسەرە، خاکی گەوهەرە
پڕ لە گوڵ و نەسرینە

ئامادەیت دەست پێ بکەیت؟ 🌱"""
    await update.message.reply_text(welcome, reply_markup=MENU)

async def finish_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    lesson = query.data.removeprefix("finish_")
    if lesson not in LESSON_COURSE:
        await query.answer()
        await query.message.reply_text("❌ ئەم وانەیە نەناسراوە.")
        return
    if not can_open(user_id, lesson):
        await query.answer()
        await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە.")
        return

    old_level = get_user_level(user_id)
    first_completion = complete_lesson_with_rewards(user_id, lesson)
    # Acknowledge only after the idempotent database claim has completed.
    await query.answer()
    if first_completion:
        check_badges(user_id)
        new_level = get_user_level(user_id)
        message_text = "✅ وانەکە تەواو بوو!\n\n🔥 +10 XP\n🪙 +5 Coin\n🎁 +1 سەنوقی خەڵات"
        if old_level != new_level:
            message_text += f"\n\n🎉 بەرزبوویتەوە بۆ: {new_level}"
    else:
        # Idempotent completion must still help a learner resume the sequence.
        # Rewards and badges are never repeated.
        message_text = "✅ ئەم وانەیە پێشتر تەواو کراوە؛ خەڵاتی دووبارە نادرێت."

    next_lesson = next_course_lesson(lesson)
    if next_lesson is not None and quiz_requires_submission(lesson) and QUIZ_DATA.get(lesson) and quiz_is_available(lesson):
        next_title = LESSON_DATA.get(next_lesson, {}).get("title", next_lesson)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                f"➡️ دەستپێکردنی {next_title}",
                callback_data=f"next_lesson_{next_lesson}",
            )],
            [InlineKeyboardButton(
                "🎯 ڕاهێنانی کرتەیی ئەم وانەیە",
                callback_data=lesson_practice_callback(lesson),
            )],
        ])
        await query.message.reply_text(
            message_text + f"\n\n🔓 وانەی دواتر ئامادەیە: {next_title}\n🎯 دەتوانیت ئێستا ڕاهێنانی کرتەیی ئەم وانەیەش بکەیت.",
            reply_markup=keyboard,
        )
    elif next_lesson is not None and LESSON_COURSE.get(lesson) == "arami_orthography_foundations":
        next_number = int(next_lesson.rsplit("_", 1)[1])
        arami_manifest = load_arami_course1_manifest(BASE_DIR)
        next_title = next(item["title"] for item in arami_manifest["lessons"] if item["number"] == next_number)
        next_callback = (
            "arami5:lesson" if next_number == 5
            else f"aramiC:lesson:{next_number}"
        )
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                f"➡️ دەستپێکردنی وانەی {next_number}",
                callback_data=next_callback,
            )
        ]])
        await query.message.reply_text(
            message_text + f"\n\n🔓 وانەی دواتر ئامادەیە: {next_title}",
            reply_markup=keyboard,
        )
    elif next_lesson is None and LESSON_COURSE.get(lesson) == "arami_orthography_foundations":
        final_number = int(lesson.rsplit("_", 1)[1])
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "📝 تاقیکردنەوەی کۆتایی کۆرسی ١",
                callback_data=f"aramiC:assessment:{final_number}",
            )
        ]])
        await query.message.reply_text(
            message_text + "\n\n🏁 کۆرسی ١ تەواو بوو؛ ئێستا تاقیکردنەوەی کۆتایی ئەنجام بدە.",
            reply_markup=keyboard,
        )
    elif next_lesson is None:
        if lesson.startswith("وانە_"):
            last_lesson_number = lesson.removeprefix("وانە_")
            quiz_suffix = last_lesson_number
        else:
            last_lesson_number = None
            quiz_suffix = lesson
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "🎯 ڕاهێنانی کرتەیی وانەی کۆتایی" if quiz_requires_submission(lesson) else "📝 تاقیکردنەوەی وانەی کۆتایی",
                callback_data=f"quiz_{last_lesson_number}_start" if last_lesson_number is not None else f"quiz_{quiz_suffix}_start",
            )
        ]])
        if QUIZ_DATA.get(lesson) and quiz_is_available(lesson):
            await query.message.reply_text(
                message_text + ("\n\n🎯 ئێستا ڕاهێنانی کرتەیی بکە." if quiz_requires_submission(lesson) else "\n\n🎓 ئێستا تاقیکردنەوەکەش بکە."),
                reply_markup=keyboard,
            )
        elif QUIZ_DATA.get(lesson):
            await query.message.reply_text(message_text + "\n\n📚 تاقیکردنەوەی ئەم وانەیە هێشتا لە پێداچوونەوەدایە.")
        else:
            await query.message.reply_text(message_text + "\n\n🎓 ئەم کۆرسە تەواو بوو.")
    else:
        next_title = LESSON_DATA.get(next_lesson, {}).get("title", next_lesson)
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                f"➡️ دەستپێکردنی {next_title}",
                callback_data=f"next_lesson_{next_lesson}"
            )
        ]])
        await query.message.reply_text(
            message_text + f"\n\n🔓 وانەی دواتر ئامادەیە: {next_title}",
            reply_markup=keyboard
        )
    # Course 3 advances automatically after a successful completion. The next
    # lesson remains protected by can_open(), and its own completion button is
    # required before another lesson can be unlocked.
    if first_completion and LESSON_COURSE.get(lesson) == "unified_orthography" and next_lesson is not None:
        next_data = LESSON_DATA.get(next_lesson)
        if next_data and can_open(user_id, next_lesson):
            await send_lesson_text(query.message, next_data["content"], lesson_keyboard(next_lesson))

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    suffix = query.data.removeprefix("quiz_").removesuffix("_start")
    if suffix.isdigit():
        lesson = f"وانە_{suffix}"
        if lesson not in ORDER:
            await query.answer()
            await query.message.reply_text("⚠️ ئەم وانەیە لە ڕێڕەوی فێربووندا نیە.")
            return
    else:
        lesson = suffix
        if lesson not in LESSON_COURSE:
            await query.answer()
            await query.message.reply_text("⚠️ ئەم وانەیە لە ڕێڕەوی فێربووندا نیە.")
            return
    if not course_is_active(LESSON_COURSE[lesson]):
        await query.answer()
        await query.message.reply_text("🔒 ئەم کۆرسە هێشتا چالاک نەکراوە.")
        return
    if not quiz_is_available(lesson):
        await query.answer()
        await query.message.reply_text("📚 تاقیکردنەوەی ئەم وانەیە هێشتا لە پێداچوونەوەی سەرچاوەدایە.")
        return
    source_questions = QUIZ_DATA.get(lesson)
    if not source_questions:
        await query.answer()
        await query.message.reply_text("⚠️ تاقیکردنەوەی ئەم وانەیە ئامادە نیە.")
        return
    completed_lessons = set(get_completed_lessons(user_id))
    if lesson not in completed_lessons:
        await query.answer()
        await query.message.reply_text("🔒 سەرەتا خودی ئەم وانەیە تەواو بکە، پاشان تاقیکردنەوەکە بکە.")
        return
    # A stale or non-contiguous completion record must not bypass the course
    # sequence when a learner opens a quiz through an old Telegram button.
    if not can_open(user_id, lesson):
        await query.answer()
        await query.message.reply_text("🔒 ڕێڕەوی وانەکان بە پێی ڕیزبەندی پێویستە؛ سەرەتا وانەکانی پێشوو تەواو بکە.")
        return
    active_quiz = context.user_data.get("quiz")
    if (
        isinstance(active_quiz, dict)
        and active_quiz.get("lesson") == lesson
        and active_quiz.get("start_message_id") == getattr(query.message, "message_id", None)
    ):
        # Ignore duplicate callbacks from the same launch button.
        await query.answer()
        return

    context.user_data["quiz"] = {
        "index": 0,
        "lesson": lesson,
        "questions": randomized_question_copy(source_questions),
        "score": 0,
        "question_message_id": None,
        "start_message_id": getattr(query.message, "message_id", None),
        "selected_answer_index": None,
        "answer_in_progress": False,
    }
    try:
        await query.answer()
    except Exception:
        # A failed callback acknowledgement must not make a retry look like
        # a duplicate launch of a quiz that never displayed its first question.
        context.user_data.pop("quiz", None)
        raise
    try:
        await send_question(query.message, context.user_data["quiz"])
    except Exception:
        context.user_data.pop("quiz", None)
        logger.exception("Could not deliver the first quiz question; active quiz was cleared")
        raise

async def send_question(message, quiz):
    question = quiz["questions"][quiz["index"]]
    quiz["selected_answer_index"] = None
    quiz["answer_in_progress"] = False
    callback_prefix = "select_answer_" if quiz_requires_submission(quiz["lesson"]) else "answer_"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(option, callback_data=f"{callback_prefix}{index}")]
        for index, option in enumerate(question["options"])
    ])
    prefix = "🎯 ڕاهێنان" if quiz_requires_submission(quiz["lesson"]) else "📝"
    sent = await message.reply_text(prefix + " " + question["question"], reply_markup=keyboard)
    quiz["question_message_id"] = sent.message_id


async def select_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Store a learner's choice before awaiting Telegram callback acknowledgement."""
    query = update.callback_query
    quiz = context.user_data.get("quiz")
    if not isinstance(quiz, dict) or not quiz_requires_submission(quiz.get("lesson")):
        await query.answer()
        return
    questions = quiz.get("questions")
    index = quiz.get("index")
    if (
        not isinstance(questions, list)
        or not isinstance(index, int)
        or isinstance(index, bool)
        or index < 0
        or index >= len(questions)
        or not isinstance(questions[index], dict)
        or query.message.message_id != quiz.get("question_message_id")
    ):
        await query.answer()
        return
    raw_index = query.data.removeprefix("select_answer_")
    if not raw_index.isdigit():
        await query.answer()
        return
    choice_index = int(raw_index)
    options = questions[index].get("options")
    if not isinstance(options, list) or choice_index < 0 or choice_index >= len(options):
        await query.answer()
        return

    # Commit the selection before the first await. If the learner presses
    # submit immediately, submit_quiz_answer must see this selected index.
    quiz["selected_answer_index"] = choice_index
    try:
        await query.answer()
    except Exception:
        # Keep the previous selection state if Telegram did not acknowledge
        # the callback; the learner can safely retry selecting an option.
        quiz["selected_answer_index"] = None
        raise
    rows = [
        [
            InlineKeyboardButton(
                ("☑️ " if option_index == choice_index else "▫️ ") + option,
                callback_data=f"select_answer_{option_index}",
            )
        ]
        for option_index, option in enumerate(options)
    ]
    rows.append([
        InlineKeyboardButton("📨 ناردنی وەڵام", callback_data="submit_answer")
    ])
    try:
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(rows))
    except Exception:
        # Without the submit button, do not retain a hidden selection that
        # the learner cannot submit from the visible Telegram keyboard.
        quiz["selected_answer_index"] = None
        logger.exception("Could not update quiz selection keyboard; selection was cleared")
        raise


async def submit_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Submit the currently selected answer; selection alone never scores it."""
    quiz = context.user_data.get("quiz")
    selected = quiz.get("selected_answer_index") if isinstance(quiz, dict) else None
    if not isinstance(selected, int) or isinstance(selected, bool):
        await update.callback_query.answer("سەرەتا وەڵامێک هەڵبژێرە.", show_alert=True)
        return
    await quiz_answer(update, context, selected_index=selected)


async def quiz_answer(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    selected_index=None,
):
    query = update.callback_query
    quiz = context.user_data.get("quiz")
    if not quiz:
        await query.answer()
        await query.message.reply_text("ℹ️ تاقیکردنەوەیەکی چالاک نیە؛ لە منوودا دووبارە دەستی پێ بکە.")
        return
    # Claim the answer synchronously before acknowledging the callback. Telegram
    # can deliver duplicate submit callbacks while query.answer() is awaiting;
    # the flag prevents both handlers from scoring the same question.
    if quiz.get("answer_in_progress"):
        await query.answer()
        return

    # Treat corrupted/stale in-memory quiz state as recoverable, not as an
    # uncaught IndexError/KeyError that leaves the learner stuck.
    questions = quiz.get("questions") if isinstance(quiz, dict) else None
    index = quiz.get("index") if isinstance(quiz, dict) else None
    if (
        not isinstance(questions, list)
        or not questions
        or not isinstance(index, int)
        or isinstance(index, bool)
        or index < 0
        or index >= len(questions)
        or not isinstance(questions[index], dict)
    ):
        await query.answer()
        context.user_data.pop("quiz", None)
        await query.message.reply_text(
            "⚠️ دۆخی تاقیکردنەوە نادروست بوو؛ تکایە لە منوودا دووبارە دەستی پێ بکە."
        )
        return
    question = questions[index]
    options = question.get("options")
    answer = question.get("answer")
    if (
        not isinstance(options, list)
        or not options
        or not all(isinstance(option, str) and option for option in options)
        or len(options) != len(set(options))
        or answer not in options
        or not isinstance(quiz.get("question_message_id"), int)
        or isinstance(quiz.get("question_message_id"), bool)
        or not isinstance(quiz.get("score"), int)
        or isinstance(quiz.get("score"), bool)
        or quiz.get("score") < 0
    ):
        await query.answer()
        context.user_data.pop("quiz", None)
        await query.message.reply_text(
            "⚠️ پرسیاری تاقیکردنەوە نادروست بوو؛ تکایە لە منوودا دووبارە دەستی پێ بکە."
        )
        return

    # Ignore stale/double-clicked buttons from an earlier question.
    if query.message.message_id != quiz.get("question_message_id"):
        await query.answer()
        return
    # Validate callback data before claiming the question. Malformed callbacks
    # must not leave question_message_id=None and strand the active quiz.
    if quiz_requires_submission(quiz.get("lesson")):
        if selected_index is None:
            await query.answer()
            return
        choice_index = selected_index
    else:
        raw_index = query.data.removeprefix("answer_")
        if not raw_index.isdigit():
            await query.answer()
            return
        choice_index = int(raw_index)
    if not isinstance(choice_index, int) or isinstance(choice_index, bool):
        await query.answer()
        return
    if choice_index < 0 or choice_index >= len(options):
        await query.answer()
        return
    # No await may occur between claiming and setting this flag. Duplicate
    # callbacks then observe the claim and cannot score the same answer twice.
    quiz["answer_in_progress"] = True
    quiz["question_message_id"] = None
    try:
        await query.answer()
    except Exception:
        # Telegram acknowledgement failed before the answer was scored.
        # Release the in-memory claim so the learner can safely retry.
        quiz["answer_in_progress"] = False
        quiz["question_message_id"] = query.message.message_id
        raise
    quiz["selected_answer_index"] = None
    try:
        await query.edit_message_reply_markup(reply_markup=None)
    except Exception:
        logger.debug("Quiz keyboard was already removed or could not be edited")
    answer = question["options"][choice_index]
    if answer == question["answer"]:
        quiz["score"] += 1
        feedback = "✅ ئافەرین! وەڵامی دروستە."
    else:
        feedback = f"❌ وەڵامەکە دروست نیە. وەڵامی دروست: {question['answer']}"
    try:
        await query.message.reply_text(feedback)
    except Exception:
        # The answer was not committed to the reward ledger. Clear the
        # in-memory quiz so a failed Telegram send cannot strand a locked quiz.
        context.user_data.pop("quiz", None)
        logger.exception("Could not deliver quiz answer feedback; active quiz was cleared")
        raise

    quiz["index"] += 1
    if quiz["index"] < len(quiz["questions"]):
        try:
            await send_question(query.message, quiz)
        except Exception:
            context.user_data.pop("quiz", None)
            logger.exception("Could not deliver the next quiz question; active quiz was cleared")
            raise
        return

    lesson = quiz["lesson"]
    earned = quiz["score"]
    first_completion = complete_quiz_with_rewards(update.effective_user.id, lesson)
    result = (
        f"🎉 تاقیکردنەوە تەواو بوو!\n"
        f"✅ وەڵامی دروست: {earned}/{len(quiz['questions'])}\n"
    )
    if first_completion:
        result += "⭐ +20 XP"
    else:
        result += "ℹ️ خەڵاتی ئەم تاقیکردنەوەیە پێشتر وەرگیراوە؛ XPی دووبارە نادرێت."
    # The reward ledger is already committed. Clear the in-memory quiz
    # before sending the result so a failed Telegram delivery cannot replay it.
    context.user_data.pop("quiz", None)
    await query.message.reply_text(result)

def render_lesson_html_blocks(content):
    """Render lesson text in a clean, consistent academic Telegram layout."""
    blocks = []
    section_titles = {
        "ئامانجەکانی فێربوون",
        "خۆت تاقی بکەرەوە",
        "ڕاهێنانی فێرخواز",
        "نموونەی شیکردنەوە",
        "نموونەی ڕاهێنان",
        "هەڵەی باو",
        "🎯 ئامانج",
        "🗣️ گفتوگۆ",
        "📚 وشە و دەستەواژە",
        "✍️ ڕاهێنان",
        "🧠 تێگەیشتن",
        "🔎 ڕوونکردنەوە و خاڵە سەرەکییەکان",
        "✍️ نموونەکان",
        "🧩 ڕاهێنان",
        "🧠 پرسیارەکانی تێگەیشتن",
        "🛠️ کاری پڕاکتیکی",
    }
    source_lines = content.splitlines()
    index = 0
    while index < len(source_lines):
        line = source_lines[index].strip()
        # Accept both Markdown tables (| a | b |) and the plain pipe tables
        # used in the supplied lessons (a | b | c), without requiring edge pipes.
        if line.count("|") >= 2:
            table_lines = []
            while index < len(source_lines):
                candidate = source_lines[index].strip()
                if candidate.count("|") < 2:
                    break
                cells = [cell.strip() for cell in candidate.strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
                    table_lines.append(cells)
                index += 1
            if table_lines:
                headers = table_lines[0]
                for row in table_lines[1:]:
                    pairs = [
                        f"<b>{html.escape(headers[i], quote=False)}:</b> {html.escape(value, quote=False)}"
                        for i, value in enumerate(row)
                        if i < len(headers) and value
                    ]
                    if pairs:
                        blocks.append("<blockquote>" + "  •  ".join(pairs) + "</blockquote>")
            continue
        if not line:
            blocks.append("")
            index += 1
            continue

        escaped = html.escape(line, quote=False)
        if line.startswith("🤖 کەژیار — KejyarBot@"):
            blocks.append(f"<b>{escaped}</b>")
        elif line.startswith("📘 "):
            blocks.append(f"<b>{escaped}</b>")
        elif line.startswith("وانەی "):
            blocks.append(f"<b>{escaped}</b>")
        elif line.startswith(("💬 ", "📖 ", "## ")):
            title = line.removeprefix("## ").strip()
            blocks.append(f"<b>📖 {html.escape(title, quote=False)}</b>")
        elif line in section_titles or line.startswith(("کورتەی وانە:", "کورتەی وانە")):
            blocks.append(f"<b>{escaped}</b>")
        elif re.match(r"^[٠-٩0-9]+[.)]\s+\S", line) and len(line) <= 100:
            blocks.append(f"<b>{escaped}</b>")
        elif line.startswith(("نموونە:", "**نموونە:**", "هەڵە:", "ڕێگای دروست:", "• ", "- ")):
            blocks.append(f"<blockquote>{escaped}</blockquote>")
        elif " • " in line and len(line) < 1200:
            blocks.append(f"<blockquote>{escaped}</blockquote>")
        else:
            blocks.append(escaped)
        index += 1
    return blocks

def split_lesson_html(blocks, limit=3500):
    """Pack complete HTML blocks into Telegram-safe messages."""
    chunks = []
    current = []
    current_length = 0
    for block in blocks:
        pieces = [block]
        if len(block) > limit:
            plain = re.sub(r"<[^>]+>", "", block)
            pieces = []
            while plain:
                cut = min(limit - 32, len(plain))
                if cut < len(plain):
                    boundary = plain.rfind(" ", 0, cut)
                    if boundary > cut // 2:
                        cut = boundary
                pieces.append(html.escape(plain[:cut], quote=False))
                plain = plain[cut:].lstrip()
        for piece in pieces:
            extra = len(piece) + (1 if current else 0)
            if current and current_length + extra > limit:
                chunks.append("\n".join(current))
                current = []
                current_length = 0
            current.append(piece)
            current_length += len(piece) + (1 if len(current) > 1 else 0)
    if current:
        chunks.append("\n".join(current))
    return chunks or ["⚠️ ناوەڕۆکی ئەم وانەیە بەردەست نییە."]


def split_lesson_text(content, limit=3800):
    """Legacy plain-text splitter retained for callers and regression compatibility."""
    content = content.strip()
    if not content:
        return ["⚠️ ناوەڕۆکی ئەم وانەیە بەردەست نییە."]
    chunks = []
    start = 0
    while start < len(content):
        end = min(start + limit, len(content))
        if end < len(content):
            newline = content.rfind("\n", start, end)
            space = content.rfind(" ", start, end)
            boundary = max(newline, space)
            if boundary > start + limit // 2:
                end = boundary + (1 if content[boundary] == "\n" else 1)
        chunks.append(content[start:end])
        start = end
    return chunks


def add_kejyar_brand_signature(content):
    """Give every lesson a consistent KejyarBot identity without altering its source."""
    signature = "🤖 کەژیار — KejyarBot@"
    content = content.rstrip()
    if signature not in content:
        content = f"{content}\n\n{signature}"
    return content


async def send_lesson_text(message, content, reply_markup=None):
    """Send lessons in a consistent academic layout, preserving all lesson wording."""
    content = re.sub(
        r"(?im)^\s*⚠️?\s*دەنگی وانەکە.*(?:پڕۆژەدا|پەیوەست نەکراوە).*$",
        "",
        content,
    )
    content = add_kejyar_brand_signature(content)
    chunks = split_lesson_html(render_lesson_html_blocks(content))
    for index, chunk in enumerate(chunks):
        await message.reply_text(
            chunk,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=reply_markup if index == len(chunks) - 1 else None,
        )


async def open_selected_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lesson = query.data.removeprefix("open_lesson_")
    user_id = query.from_user.id
    if lesson not in LESSON_COURSE:
        await query.message.reply_text("❌ ئەم وانەیە نەناسراوە.")
        return
    if not can_open(user_id, lesson):
        await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە.")
        return
    data = LESSON_DATA.get(lesson)
    if not data:
        await query.message.reply_text("⚠️ ناوەڕۆکی ئەم وانەیە نەدۆزرایەوە.")
        return
    await send_lesson_text(query.message, data["content"], lesson_keyboard(lesson))


async def open_next_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lesson = query.data.removeprefix("next_lesson_")
    user_id = query.from_user.id
    if lesson not in LESSON_COURSE or not can_open(user_id, lesson):
        await query.message.reply_text("🔒 وانەی پێشووتر تەواو بکە.")
        return
    data = LESSON_DATA.get(lesson)
    if not data:
        await query.message.reply_text("⚠️ ناوەڕۆکی ئەم وانەیە نەدۆزرایەوە.")
        return
    await send_lesson_text(query.message, data["content"], lesson_keyboard(lesson))

COURSE_MENU_PAGE_SIZE = 12


def course_menu_keyboard(course_id, user_id, page=0):
    """Build a compact, progress-aware page of one course's lesson catalogue."""
    order = COURSE_LESSON_ORDER.get(course_id, [])
    page_count = max(1, (len(order) + COURSE_MENU_PAGE_SIZE - 1) // COURSE_MENU_PAGE_SIZE)
    if not isinstance(page, int) or isinstance(page, bool) or not 0 <= page < page_count:
        raise ValueError("invalid course menu page")
    completed = set(get_completed_lessons(user_id))
    start_index = page * COURSE_MENU_PAGE_SIZE
    rows = []
    for lesson in order[start_index:start_index + COURSE_MENU_PAGE_SIZE]:
        is_open = can_open(user_id, lesson)
        status = "🔒" if not is_open else ("✅" if lesson in completed else "🔓")
        title = LESSON_DATA[lesson]["title"]
        label = title if len(title) <= 38 else title[:35] + "…"
        rows.append([InlineKeyboardButton(
            f"{status} {label}",
            callback_data=f"open_lesson_{lesson}",
        )])
    navigation = []
    if page > 0:
        navigation.append(InlineKeyboardButton(
            "⬅️ پێشوو",
            callback_data=f"coursepage:{course_id}:{page - 1}",
        ))
    if page + 1 < page_count:
        navigation.append(InlineKeyboardButton(
            "➡️ وانەکانی دواتر",
            callback_data=f"coursepage:{course_id}:{page + 1}",
        ))
    if navigation:
        rows.append(navigation)
    return InlineKeyboardMarkup(rows), page_count


async def send_course_page(message, course_id, user_id, page=0, *, edit=False):
    course = next((item for item in COURSES if item.get("id") == course_id), None)
    if course is None or not course_is_active(course_id):
        await message.reply_text("⚠️ ئەم کۆرسە چالاک نییە یان نەدۆزرایەوە.")
        return
    try:
        keyboard, page_count = course_menu_keyboard(course_id, user_id, page)
    except ValueError:
        await message.reply_text("⚠️ ئەم لاپەڕەیە لە لیستی وانەکاندا نییە.")
        return
    order = COURSE_LESSON_ORDER.get(course_id, [])
    first = page * COURSE_MENU_PAGE_SIZE + 1
    last = min(first + COURSE_MENU_PAGE_SIZE - 1, len(order))
    description = course.get("description", "")
    text = (
        f"{course['title']}\n{description}\n\n"
        f"📚 وانەکانی {first}–{last} لە کۆی {len(order)} — لاپەڕەی {page + 1}/{page_count}"
    )
    if edit:
        await message.edit_text(text, reply_markup=keyboard)
    else:
        await message.reply_text(text, reply_markup=keyboard)


async def open_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    course_id = query.data.removeprefix("course_")
    if course_id == "arami_orthography_foundations":
        try:
            arami_manifest = load_arami_course1_manifest(BASE_DIR)
            arami_banks = load_arami_course1_question_banks(BASE_DIR)
        except Exception:
            logger.exception("Could not open Arami Course 1 from the generic course menu")
            await query.message.reply_text("⚠️ لیستی ٢١ وانەی ڕێنووسی سەرەتاییی کوردی ئامادە نییە.")
            return
        await query.message.reply_text(
            "📚 کۆرسی ١ — ڕێنووسی سەرەتاییی کوردی\n٢١ وانە؛ وانەی خۆت هەڵبژێرە.",
            reply_markup=arami_course1_menu_keyboard(
                arami_manifest,
                arami_banks,
                completed_lessons=get_completed_lessons(query.from_user.id),
                can_open=lambda lesson_id: can_open(query.from_user.id, lesson_id),
            ),
        )
        return
    course = next((item for item in COURSES if item.get("id") == course_id), None)
    if course is None:
        await query.message.reply_text("⚠️ ئەم کۆرسە نەدۆزرایەوە.")
        return
    if not course_is_active(course_id):
        await query.message.reply_text(f"{course['title']}\n\n📌 ئەم کۆرسە هێشتا چالاک نییە.")
        return
    await send_course_page(query.message, course_id, query.from_user.id, 0)


async def open_course_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prefix, _, remainder = query.data.partition(":")
    course_id, separator, raw_page = remainder.rpartition(":")
    if prefix != "coursepage" or not separator or not raw_page.isdigit():
        await query.message.reply_text("⚠️ داواکاریی لاپەڕەی وانەکان نادروستە.")
        return
    await send_course_page(query.message, course_id, query.from_user.id, int(raw_page), edit=True)


QUIZ_MENU_PAGE_SIZE = 12

def quiz_menu_items(user_id, mode):
    completed = set(get_completed_lessons(user_id))
    items = []
    for lesson in active_course_lessons():
        if not QUIZ_DATA.get(lesson) or lesson not in completed or not can_open(user_id, lesson):
            continue
        practice = quiz_requires_submission(lesson)
        if (mode == "practice") != practice:
            continue
        suffix = lesson.removeprefix("وانە_") if lesson.startswith("وانە_") else lesson
        prefix = "🎯" if practice else "📝"
        items.append((f"{prefix} {LESSON_DATA.get(lesson, {}).get('title', lesson)}", f"quiz_{suffix}_start"))
    if course_is_active("arami_orthography_foundations"):
        manifest = load_arami_course1_manifest(BASE_DIR)
        for item in sorted(manifest["lessons"], key=lambda x: x["number"]):
            lesson_id = item["id"]
            if lesson_id not in completed or not can_open(user_id, lesson_id):
                continue
            n = item["number"]
            callback_mode = "practice" if mode == "practice" else "assessment"
            callback = f"arami1:{callback_mode}" if n == 1 else (f"arami5:{callback_mode}" if n == 5 else f"aramiC:{callback_mode}:{n}")
            prefix = "🎯" if mode == "practice" else "📝"
            items.append((f"{prefix} وانەی {n} — {item['title']}", callback))
    return items

def quiz_menu_keyboard(items, page, mode):
    count = max(1, (len(items) + QUIZ_MENU_PAGE_SIZE - 1) // QUIZ_MENU_PAGE_SIZE)
    if not isinstance(page, int) or isinstance(page, bool) or page < 0 or page >= count:
        raise ValueError("invalid quiz menu page")
    rows = [[InlineKeyboardButton(label, callback_data=callback)] for label, callback in items[page * QUIZ_MENU_PAGE_SIZE:(page + 1) * QUIZ_MENU_PAGE_SIZE]]
    nav = []
    if page:
        nav.append(InlineKeyboardButton("⬅️ پێشوو", callback_data=f"quizmenu:{mode}:{page - 1}"))
    if page + 1 < count:
        nav.append(InlineKeyboardButton("➡️ دواتر", callback_data=f"quizmenu:{mode}:{page + 1}"))
    if nav:
        rows.append(nav)
    return InlineKeyboardMarkup(rows), count

async def send_quiz_menu(message, user_id, mode, page=0):
    items = quiz_menu_items(user_id, mode)
    if not items:
        await message.reply_text("🔒 سەرەتا وانەیەک بکەرەوە و تەواوی بکە.")
        return
    try:
        keyboard, count = quiz_menu_keyboard(items, page, mode)
    except ValueError:
        await message.reply_text("⚠️ ئەم لاپەڕەیەی منووی تاقیکردنەوە دروست نیە.")
        return
    title = "🎯 ڕاهێنانی کرتەیی" if mode == "practice" else "📝 تاقیکردنەوەکان"
    first = page * QUIZ_MENU_PAGE_SIZE + 1
    last = min(first + QUIZ_MENU_PAGE_SIZE - 1, len(items))
    await message.reply_text(f"{title} — {first}–{last} لە کۆی {len(items)} (لاپەڕەی {page + 1}/{count})", reply_markup=keyboard)

async def open_quiz_menu_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prefix, sep, rest = query.data.partition(":")
    mode, sep2, raw_page = rest.partition(":")
    if prefix != "quizmenu" or not sep or not sep2 or mode not in {"practice", "assessment"} or not raw_page.isdigit():
        await query.message.reply_text("⚠️ داواکاریی لاپەڕەی تاقیکردنەوە نادروستە.")
        return
    await send_quiz_menu(query.message, query.from_user.id, mode, int(raw_page))


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id
    get_user(user_id)

    if text == "📕 ڕێنووسی سەرەتاییی کوردی":
        try:
            arami_manifest = load_arami_course1_manifest(BASE_DIR)
            arami_banks = load_arami_course1_question_banks(BASE_DIR)
        except Exception:
            logger.exception("Could not open the 21-lesson Arami Course 1 catalogue")
            await update.message.reply_text("⚠️ لیستی ٢١ وانەی ڕێنووسی سەرەتاییی کوردی ئێستا بار ناکرێت.")
            return
        await update.message.reply_text(
            "📚 کۆرسی ١ — ڕێنووسی سەرەتاییی کوردی\n"
            "٢١ وانە؛ وانەی خۆت هەڵبژێرە. بۆ هەر وانەیەک ڕێگای خوێندنەوە و ڕاهێنان/تاقیکردنەوەی تایبەت هەیە.",
            reply_markup=arami_course1_menu_keyboard(
                arami_manifest,
                arami_banks,
                completed_lessons=get_completed_lessons(user_id),
                can_open=lambda lesson_id: can_open(user_id, lesson_id),
            ),
        )
        return

    if text == "🗓️ مانگەکانی ساڵ لەناو کورداندا":
        await update.message.reply_text(
            "╭━━━━━━━━━━━━━━━━━━━━╮\n"
            "       📅 <b>ساڵنامەی کوردی</b>\n"
            "╰━━━━━━━━━━━━━━━━━━━━╯\n\n"
            "🌿 ناوی مانگەکان لە شێوەزارە جیاوازەکاندا\n"
            "شێوەزارێک هەڵبژێرە بۆ بینینی لیستی ١٢ مانگەکە.",
            parse_mode="HTML",
            reply_markup=months_menu_keyboard(),
        )
        return

    if text == "📖 وشەنامەی کوردی":
        dictionary_help = """📖 <b>وشەنامەی کوردی</b>
کۆمەڵەیەک فەرهەنگ و سەرچاوەی وشەسازیی کوردی؛ بە پێی شێوەزار و جۆری فەرهەنگ ڕێکخراون.

🌐 <b>فەرهەنگە گشتییەکان و چەندشێوەزارییەکان</b>
🔹 <a href="https://bradost.net/ferheng/">تۆڕی زاراوەپارێزیی وشەدان</a> — کۆکردنەوەی واتا و زاراوە لە چەندین فەرهەنگ و سەرچاوەی کوردی
🔹 <a href="https://lex.vejin.net/ck">ڤەژینلێکس</a> — ١٩ فەرهەنگ؛ سۆرانی، کورمانجی، هەورامی و کوردیی باشووری
🔹 <a href="https://myrebar.de/ku-ckb/ferheng">ڕێبەر فەرهەنگ</a> — ١٩ فەرهەنگ و گەڕانێکی یەکگرتوو بۆ سۆرانی، کورمانجی، هەورامی و کوردیی باشووری
🔹 <a href="https://ferheng.info/">فەرهەنگی ئاناهیتا</a> — فەرهەنگی زمانی یەکگرتووی کوردی هاوچەرخ
🔹 <a href="https://www.kurdishlo.org/dictionary.php">کۆگای فەرهەنگی کوردی</a> — لیستی فەرهەنگی گشتی و زاراوەیی و زانستی
🔹 <a href="https://jinzar.krd/">ژینزار</a> — فەرهەنگی کوردی بۆ کوردی، هاومانا و پەیوەندیی وشەکان

🟡 <b>سۆرانی و فەرهەنگی فارسی ـ کوردی</b>
🔹 <a href="https://ferhengikaawa.com/">فەرهەنگی کاوە</a> — فارسی بۆ کوردی و کوردی بۆ فارسی
🔹 <a href="https://ferheng.info/">ئاناهیتا</a> — وشە و زاراوەی شێوەزارە جیاوازەکانی کوردی
🔹 <a href="https://lex.vejin.net/ck">ڤەژینلێکس</a> — هەنبانە بۆرینە، خاڵ، مەردۆخ و فەرهەنگەکانی تر

🟢 <b>کورمانجی</b>
🔹 <a href="https://ferheng-kurd.com/en">Ferheng — Kurmanji</a> — فەرهەنگی کورمانجی بە ئینگلیزی، زیاتر لە ١٣٠ هەزار وشە
🔹 <a href="https://lex.vejin.net/ck">ڤەژینلێکس</a> — فەرهەنگا دەستی، کانی و فەرهەنگی کۆما کوردییا کورمانجی
🔹 <a href="https://en.wiktionary.org/wiki/Category:Kurdish_lemmas">Wiktionary — وشەکانی کوردی</a>

🔵 <b>هەورامی / گۆرانی</b>
🔹 <a href="https://hawramy.com/">وەرقوڵ</a> — فەرهەنگی هەورامی بۆ سۆرانی و بە پێچەوانەوە؛ زیاتر لە ٦٢ هەزار جووتە وشە
🔹 <a href="https://lex.vejin.net/ck">ڤەژینلێکس — فەرهەنگی وشەنامە</a> — هەورامی بۆ کوردیی ناوەندی
🔹 <a href="https://myrebar.de/ku-ckb/ferheng">ڕێبەر فەرهەنگ</a> — فەرهەنگی هەورامی لەگەڵ شێوەزارەکانی تر

🟠 <b>کوردیی باشووری / کەڵهوڕی و گەڕووسی</b>
🔹 <a href="https://lex.vejin.net/ck">ڤەژینلێکس — فەرهەنگی گەڕووس</a> — کوردیی باشووری بۆ کوردیی ناوەندی و فارسی
🔹 <a href="https://myrebar.de/ku-ckb/ferheng">ڕێبەر فەرهەنگ</a> — تۆمارەکانی کوردیی باشووری
🔹 <a href="https://bradost.net/ferheng/">وشەدان</a> — گەڕان لە سەرچاوە و فەرهەنگە ناوچەییەکان

🟣 <b>زازاکی</b>
🔹 <a href="https://kurdish-tech.github.io/">Ferheng — Kurmancî, Soranî, Zazakî</a> — فەرهەنگی دیجیتاڵی بە وشەکانی زازاکی، کورمانجی و سۆرانی
🔹 <a href="https://de.wiktionary.org/wiki/Wiktionary:Zazaki">Wiktionary — سەرچاوەکانی زازاکی</a>

🟤 <b>لەکی</b>
🔹 <a href="https://bradost.net/ferheng/">وشەدان</a> — بۆ گەڕان لە وشە و زاراوە ناوچەییەکان
🔹 <a href="https://lex.vejin.net/ck">ڤەژینلێکس</a> — سەرچاوەی کوردیی باشووری و فەرهەنگە نزیکەکان
📌 فەرهەنگێکی سەرهێڵی تایبەت بە زمانی لەکی کە پشتڕاست بکرێتەوە لەم گەڕانەدا نەدۆزرایەوە؛ بۆیە بەستەری ناپشتڕاستکراو زیاد نەکراوە.

📚 <b>کۆگای فەرهەنگ و توێژینەوە</b>
🔹 <a href="https://lex.vejin.net/ck/project/online-dictionaries">لیستی فەرهەنگە سەرهێڵەکان لە ڤەژین</a>
🔹 <a href="https://zkurd.org/وشەنامەکانی-زمانی-کوردی/">زانستپەروەرانی کورد — وشەنامەکان</a>
🔹 <a href="https://sinaahmadi.github.io/posts/list-of-kurdish-dictionaries.html">لیستی توێژینەوەیی فەرهەنگە کوردییەکان</a>

⚠️ <b>تێبینی</b>
هەموو فەرهەنگێک هەموو شێوەزارەکان ناگرێتەوە. کەڵهوڕی، گەڕووسی و لەکی هەندێک جار لە ژێر ناونیشانی کوردیی باشووری یان زاراوە ناوچەییەکاندا دێن؛ جیاوازییەکانیان لەبەرچاو بگرە. واتای وشە لە فەرهەنگێکەوە بۆ فەرهەنگێکی تر دەکرێت جیاواز بێت."""
        dictionary_help = (
            "╭━━━━━━━━━━━━━━━━━━━━╮\n"
            "       📚 <b>کتێبخانەی وشەنامەی کوردی</b>\n"
            "╰━━━━━━━━━━━━━━━━━━━━╯\n"
            "🔎 سەرچاوەی فەرهەنگی، وشەسازی و زاراوەناسی\n"
            "بەشەکان بەپێی شێوەزار و جۆری فەرهەنگ ڕێکخراون.\n\n"
            + "\n".join(dictionary_help.splitlines()[1:])
        )
        await update.message.reply_text(
            dictionary_help,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=MENU,
        )
        dictionary_links = resource_link_keyboard(dictionary_help)
        if dictionary_links:
            await update.message.reply_text(
                "🔗 <b>بەستەرەکانی وشەنامە</b> — بۆ کردنەوە کرتە لەسەر ناوی سەرچاوەکە بکە:",
                parse_mode="HTML",
                reply_markup=dictionary_links,
            )
        return

    if text == "⌨️ تەختەکلیلی کوردی":
        keyboard_help = """⌨️ <b>تەختەکلیلی کوردی</b>
بەستەری تەختەکلیل و ڕێنمایی دامەزراندن بەپێی ئامێر و شێوەزاری کوردی.

🪟 <b>Windows</b>
🔹 <a href="https://keyman.com/keyboards/basic_kbdkurd">کوردیی ناوەندی / سۆرانی — Central Kurdish Basic</a>
🔹 <a href="https://keyman.com/keyboards/sorani_behdini_arab_qwerty">سۆرانی و بادینی — Sorani Behdini QWERTY</a>
🔹 <a href="https://keyman.com/keyboards/horami">هەورامی / گۆرانی — Horami</a>
🔹 <a href="https://github.com/Kurdish-Tech/kurdish-kurmanci-keyboard-layout">کورمانجی بە پیتی لاتینی — Windows</a>
🔹 <a href="https://support.microsoft.com/en-us/windows/hardware/input-devices/manage-the-language-and-keyboard-input-layout-settings-in-windows">ڕێنمایی فەرمی زیادکردنی تەختەکلیل لە Windows</a>

🤖 <b>Android</b>
🔹 <a href="https://play.google.com/store/apps/details?id=com.app.jayesh.customkeyboard">Hawrami Keyboard — هەورامی، سۆرانی، کورمانجی و کوردیی خوارین</a>
🔹 <a href="https://support.google.com/gboard/answer/7068494">ڕێنمایی Gboard بۆ زیادکردنی زمان و تەختەکلیل</a>
🔹 <a href="https://keyman.com/keyboards/basic_kbdkurd">Keyman — سۆرانی / کوردیی ناوەندی</a>
🔹 <a href="https://keyman.com/keyboards/sorani_behdini_arab_qwerty">Keyman — سۆرانی و بادینی</a>
🔹 <a href="https://keyman.com/keyboards/horami">Keyman — هەورامی</a>

🍎 <b>iPhone و iPad</b>
🔹 <a href="https://apps.apple.com/de/app/kurdtype/id6823184454">KurdType — سۆرانی</a>
🔹 <a href="https://apps.apple.com/de/app/kurd-keyboard-%DA%A9%DB%8C%D8%A8%DB%86%D8%B1%D8%AF%DB%8C-%DA%A9%D9%88%D8%B1%D8%AF%DB%8C/id6792407069">Kurd Keyboard — سۆرانی و بادینی</a>
🔹 <a href="https://keyman.com/keyboards/basic_kbdkurd">Keyman — سۆرانی / کوردیی ناوەندی</a>
🔹 <a href="https://keyman.com/keyboards/sorani_behdini_arab_qwerty">Keyman — سۆرانی و بادینی</a>
🔹 <a href="https://keyman.com/keyboards/horami">Keyman — هەورامی</a>
🔹 <a href="https://support.apple.com/en-us/guide/iphone/iph73b71eb/ios">ڕێنمایی فەرمی Apple بۆ زیادکردنی تەختەکلیل</a>

💻 <b>macOS و Linux</b>
🔹 <a href="https://github.com/Kurdish-Tech/kurdish-kurmanci-keyboard-layout">کورمانجی لاتینی — Windows / macOS / Linux</a>
🔹 <a href="https://keyman.com/keyboards/basic_kbdkurd">سۆرانی — Keyman بۆ هەموو سیستەمەکان</a>
🔹 <a href="https://keyman.com/keyboards/horami">هەورامی — Keyman بۆ هەموو سیستەمەکان</a>
🔹 <a href="https://keyman.com/en/">Keyman — گەڕان بۆ تەختەکلیلەکانی تر</a>
🔹 <a href="https://kurdi.sh/en/keyboard">تەختەکلیل و ڕێنمایی ئۆنلاین بۆ ئامێرە جیاوازەکان</a>
🔹 <a href="https://kurdisch-akademie.de/tastatur">تەختەکلیلی ئۆنلاین سۆرانی</a>

📌 <b>تێبینی گرنگ</b>
هەموو ئەم تەختەکلیلانە بۆ هەموو شێوەزارەکان یەکسان نین. هەورامی و کوردیی خوارین لە هەندێک ئەپدا پشتگیری دەکرێن؛ بەڵام بۆ کەڵهوڕی و هەندێک شێوەزاری ناوچەیی، تەختەکلیلی تایبەتی و پشتڕاستکراوەمان نەدۆزیوەتەوە. پێش دامەزراندن، ناوی زمان و شێوەزاری پشتگیریکراو لە لاپەڕەی ئەپەکەدا بپشکنە.
⚠️ تەختەکلیلی Unicode بەکاربهێنە؛ فۆنت و تەختەکلیلە کۆنەکانی Ali-font دەتوانن دەقەکە لە ئامێری تر تێکبدەن."""
        keyboard_help = (
            "╭━━━━━━━━━━━━━━━━━━━━╮\n"
            "       ⌨️ <b>ناوەندی تەختەکلیلی کوردی</b>\n"
            "╰━━━━━━━━━━━━━━━━━━━━╯\n"
            "📱 ڕێنمایی و سەرچاوە بەپێی ئامێر و شێوەزاری کوردی\n"
            "ئامێرەکەت بدۆزەرەوە و تەختەکلیلی گونجاو هەڵبژێرە.\n\n"
            + "\n".join(keyboard_help.splitlines()[1:])
        )
        await update.message.reply_text(
            keyboard_help,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=MENU,
        )
        keyboard_links = resource_link_keyboard(keyboard_help)
        if keyboard_links:
            await update.message.reply_text(
                "🔗 <b>بەستەرەکانی دامەزراندن</b> — بۆ کردنەوە کرتە لەسەر ناوی سەرچاوەکە بکە:",
                parse_mode="HTML",
                reply_markup=keyboard_links,
            )
        return

    if text == "🌐 گۆڕینی زمانی تەلەگرام":
        language_help = (
            "🔴 <b>زمانی کوردی بۆ تەلەگرام</b>\n\n"
            "⚙ <b>زبان تلگرامتان را به کوردی تغییر دهید</b>\n\n"
            "⚙ <b>بەو لینکانەی خوارەوە بەدڵی خۆتان شێوەزارێک بۆ زمانی تەلەگرامەکانتان هەڵبژێرن</b>\n\n"
            "⚙ <b>پی لینکاو واریە، زمانو تەلەگرامی بەدڵو وێتا هۆرچندێ:</b>\n\n"
            "🔻 <b>کوردیی سۆرانی</b>\n"
            '① <a href="https://t.me/setlanguage/1kurdish">https://t.me/setlanguage/1kurdish</a>\n\n'
            "🔻 <b>کوردیی هەورامی</b>\n"
            '① <a href="https://t.me/setlanguage/horami">https://t.me/setlanguage/horami</a>\n\n'
            "🔻 <b>کوردیی کورمانجی</b>\n"
            '① <a href="https://t.me/setlanguage/kurmanji">https://t.me/setlanguage/kurmanji</a>\n\n'
            "🔻 <b>کوردیی کەڵهوڕی</b>\n"
            '① <a href="https://t.me/setlanguage/kurdish-kalhori">https://t.me/setlanguage/kurdish-kalhori</a>'
        )
        await update.message.reply_text(
            language_help,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=MENU,
        )
        return

    if text == "💬 گفتوگۆی ڕۆژانە":
        context.user_data["daily_chat_mode"] = True
        context.user_data.pop("daily_chat_scenario", None)
        context.user_data.pop("daily_chat_stage", None)
        await update.message.reply_text(
            "🌷 بەخێربێیت بۆ گفتوگۆی ڕۆژانەی کەژیار!\n"
            "بە کوردی بنووسە؛ دەتوانین لە سڵاوکردن، بازاڕ، خواردن و قوتابخانە گفتوگۆ بکەین.\n"
            "بۆ دەرچوون بنووسە «خواحافیز».\n\n"
            + PROMPTS[0]
        )
        return

    # Menu selections leave free conversation mode; ordinary text stays in it.
    if text in LESSON_BUTTONS or text in {
        "📚 وانەکان", "📘 کۆرسەکان", "ڕێنووسی لاتینی کوردیی", "📕 ڕێنووسی سەرەتاییی کوردی",
        "🗓️ مانگەکانی ساڵ لەناو کورداندا",
        "🌐 گۆڕینی زمانی تەلەگرام",
        "⌨️ تەختەکلیلی کوردی",
        "📖 وشەنامەی کوردی",
        "👤 پێشکەوتنم", "🧭 ڕێگای فێربوون",
        "🎁 سەنوقی خەڵات", "📝 تاقیکردنەوەکان", "🎯 ڕاهێنانی کرتەیی",
    }:
        context.user_data["daily_chat_mode"] = False
        context.user_data.pop("daily_chat_scenario", None)
        context.user_data.pop("daily_chat_stage", None)

    if text == "ڕێنووسی لاتینی کوردیی":
        latin_courses = [
            course for course in COURSES
            if course.get("id") in LATIN_COURSE_IDS and course_is_active(course.get("id"))
        ]
        rows = [[InlineKeyboardButton(
            course["title"],
            callback_data=f"course_{course['id']}",
        )] for course in latin_courses]
        await update.message.reply_text(
            "🔤 ڕێنووسی لاتینی کوردیی\n\nیەکێک لەم دوو کۆرسە جیاوازانە هەڵبژێرە:",
            reply_markup=InlineKeyboardMarkup(rows),
        )
        return

    if text == "📚 وانەکان":
        try:
            arami_manifest = load_arami_course1_manifest(BASE_DIR)
            arami_banks = load_arami_course1_question_banks(BASE_DIR)
        except Exception:
            logger.exception("Could not open the 21-lesson Arami Course 1 catalogue")
            await update.message.reply_text("⚠️ لیستی ٢١ وانەی ڕێنووسی سەرەتاییی کوردی ئێستا بار ناکرێت.")
            return
        await update.message.reply_text(
            "📚 کۆرسی ١ — ڕێنووسی سەرەتاییی کوردی\n٢١ وانە؛ وانەی خۆت هەڵبژێرە.",
            reply_markup=arami_course1_menu_keyboard(
                arami_manifest,
                arami_banks,
                completed_lessons=get_completed_lessons(user_id),
                can_open=lambda lesson_id: can_open(user_id, lesson_id),
            ),
        )
        return

    if text == "📘 کۆرسەکان":
        keyboard_rows = []
        for course in COURSES:
            if course.get("id") in LATIN_COURSE_IDS:
                continue
            # Retired courses are archived, not presented as planned or selectable.
            if course.get("status") in {"retired", "retired_replaced_by_arami_course1"}:
                continue
            status = "🟢 چالاک" if course_is_active(course.get("id")) else "⚪ پلاندانراو"
            keyboard_rows.append([InlineKeyboardButton(
                f"{status} · {course['title']}",
                callback_data=f"course_{course['id']}",
            )])
        active_count = sum(
            1 for course in COURSES
            if course_is_active(course.get("id")) and course.get("id") not in LATIN_COURSE_IDS
        )
        await update.message.reply_text(
            f"📚 کۆرسەکانی کەژیار\n\n{active_count} کۆرسی چالاک هەن.",
            reply_markup=InlineKeyboardMarkup(keyboard_rows),
        )
        return

    if text in LESSON_BUTTONS:
        lesson = LESSON_BUTTONS[text]
        if not can_open(user_id, lesson):
            await update.message.reply_text("🔒 وانەی پێشووتر تەواو بکە.")
            return
        data = LESSON_DATA.get(lesson)
        if not data:
            await update.message.reply_text("⚠️ ناوەڕۆکی وانەکە نەدۆزرایەوە.")
            return
        await send_lesson_text(update.message, data["content"], lesson_keyboard(lesson))
        await send_lesson_infographic(update.message, lesson)
        return

    if text in {"📝 تاقیکردنەوەکان", "🎯 ڕاهێنانی کرتەیی"}:
        mode = "practice" if text == "🎯 ڕاهێنانی کرتەیی" else "assessment"
        await send_quiz_menu(update.message, user_id, mode, 0)
        return

    if text == "🎁 سەنوقی خەڵات":
        reward = open_chest(user_id)
        if reward:
            await update.message.reply_text(f"🎁 سەنوق کراوەتەوە!\n🪙 {reward} Coin وەرگرت.")
        else:
            await update.message.reply_text("📦 سەنوقێکت نیە؛ وانە تەواو بکە بۆ وەرگرتنی سەنوق.")
        return

    if text == "👤 پێشکەوتنم":
        user = get_user(user_id)
        badges = current_progress_badges(user_id)
        await update.message.reply_text(
            f"👤 پێشکەوتنم\n\n⭐ خاڵ: {user[1]}\n🔥 XP: {user[2]}\n🎓 ئاست: {user[3]}\n"
            f"🪙 Coin: {user[8]}\n🎁 سەنوق: {user[9]}\n\n🏅 نیشانەکان:\n" +
            ("\n".join(badges) if badges else "هێشتا هیچ نیشانەیەک نیە.")
        )
        return

    if text == "🧭 ڕێگای فێربوون":
        completed = set(get_completed_lessons(user_id))
        manifest = load_arami_course1_manifest(BASE_DIR)
        lines = ["📘 ڕێگای فێربوونی کۆرسی ١ — ڕێنووسی سەرەتاییی کوردی"]
        completed_count = 0
        for item in sorted(manifest["lessons"], key=lambda lesson: lesson["number"]):
            lesson_id = item["id"]
            if lesson_id in completed:
                status = "✅ تەواو کراوە"
                completed_count += 1
            else:
                status = "🔓 ئامادەیە" if can_open(user_id, lesson_id) else "🔒 داخراوە"
            lines.append(f"{status} — وانەی {item['number']}: {item['title']}")
        lines.insert(1, f"پێشکەوتن: {completed_count}/{len(manifest['lessons'])} وانە")
        await update.message.reply_text("\n".join(lines))
        return

    if context.user_data.get("daily_chat_mode"):
        reply = reply_to_daily_message(text, context.user_data)
        await update.message.reply_text(reply, reply_markup=MENU)
        return

    await update.message.reply_text("لە منووی کەژیار هەڵبژێرە 👇", reply_markup=MENU)

async def open_kurdish_months(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    dialect = query.data.partition(":")[2]
    lesson = get_months_lesson(dialect)
    if lesson is None:
        await query.message.reply_text("⚠️ ئەم شێوەزارە نەناسراوە.")
        return
    # This lesson already contains intentional Telegram HTML tags. The generic
    # lesson renderer escapes source markup, so send this trusted generated
    # month lesson directly to preserve its bold headings.
    await query.message.reply_text(
        lesson,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=months_menu_keyboard(),
    )


async def log_polling_start(application):
    """Log readiness only after python-telegram-bot has initialized successfully."""
    logger.info("KejyarBot Telegram initialization succeeded; polling is starting")


def main():
    validate_activated_course_runtime()
    init_db()
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN (or BOT_TOKEN) is missing. Set it in .env or the host environment.")
    app = Application.builder().token(token).post_init(log_polling_start).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(open_kurdish_months, pattern=r"^months:(sorani|kurmanji|kalhuri|hawrami|laki)$"))
    app.add_handler(CallbackQueryHandler(
        lambda update, context: arami_lesson1_callback(
            update, context, BASE_DIR,
            can_open=lambda user_id, lesson_id: can_open(user_id, lesson_id),
            award_assessment=award_arami_assessment,
        ),
        pattern=r"^arami1:",
    ))
    app.add_handler(CallbackQueryHandler(
        lambda update, context: arami_course1_callback(
            update, context, BASE_DIR,
            can_open=lambda user_id, lesson_id: can_open(user_id, lesson_id),
            award_assessment=award_arami_assessment,
            get_completed_lessons=get_completed_lessons,
        ),
        pattern=r"^aramiC:",
    ))
    app.add_handler(CallbackQueryHandler(
        lambda update, context: arami_lesson5_callback(
            update, context, BASE_DIR,
            can_open=lambda user_id, lesson_id: can_open(user_id, lesson_id),
            award_assessment=award_arami_assessment,
        ),
        pattern=r"^arami5:",
    ))
    app.add_handler(CallbackQueryHandler(finish_lesson, pattern=r"^finish_"))
    app.add_handler(CallbackQueryHandler(open_course, pattern=r"^course_(arami_orthography_foundations|orthography_basic|daily_conversation|unified_orthography|grammar|kurmanji_latin_orthography|kurmanji_latin_grammar)$"))
    app.add_handler(CallbackQueryHandler(open_course_page, pattern=r"^coursepage:"))
    app.add_handler(CallbackQueryHandler(open_quiz_menu_page, pattern=r"^quizmenu:"))
    app.add_handler(CallbackQueryHandler(start_quiz, pattern=r"^quiz_.+_start$"))
    app.add_handler(CallbackQueryHandler(quiz_answer, pattern=r"^answer_\d+$"))
    app.add_handler(CallbackQueryHandler(select_quiz_answer, pattern=r"^select_answer_\d+$"))
    app.add_handler(CallbackQueryHandler(submit_quiz_answer, pattern=r"^submit_answer$"))
    app.add_handler(CallbackQueryHandler(open_next_lesson, pattern=r"^next_lesson_"))
    app.add_handler(CallbackQueryHandler(open_selected_lesson, pattern=r"^open_lesson_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
    app.run_polling()

if __name__ == "__main__":
    main()
