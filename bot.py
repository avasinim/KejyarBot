import io
import json
from datetime import datetime, timezone
import logging
import os
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
    reserve_speech_quota,
    refund_speech_quota,
)
from voice import get_voice
from daily_chat import PROMPTS, reply_to_daily_message
from speech import generate_speech, speech_is_configured
from course_runtime import can_open_lesson, visible_course_lessons

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    """Convert simple draft Markdown to readable plain text for Telegram."""
    lines = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            line = stripped.lstrip("#").strip()
        elif stripped.startswith(">"):
            line = stripped.lstrip(">").strip()
        line = line.replace("**", "").replace("__", "").replace("`", "")
        lines.append(line)
    return "\n".join(lines).strip()

# Course 1 uses the user's own original texts, not the older editorial drafts.
# Keep all lesson IDs stable so existing student progress and rewards are preserved.
ORTHOGRAPHY_COURSE = load_json("course_data/orthography_foundations.json")
COURSE_MANIFEST = load_json("courses.json")
ORIGINAL_LESSONS = load_json("course_data/orthography_original_lessons.json").get("lessons", [])
ORIGINAL_LESSONS_BY_NUMBER = {item["number"]: item for item in ORIGINAL_LESSONS}
COURSES = sorted(COURSE_MANIFEST.get("courses", []), key=lambda item: item.get("order", 999))
ORTHOGRAPHY_QUIZ_DRAFT = load_json("course_data/orthography_foundations_quiz_draft.json")
LESSON_DATA = {}
QUIZ_DATA = {}
LESSON_BUTTONS = {}

def kurdish_digits(value):
    return str(value).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))

for course_lesson in ORTHOGRAPHY_COURSE.get("lessons", []):
    number = course_lesson["number"]
    lesson_key = f"وانە_{number}"
    original = ORIGINAL_LESSONS_BY_NUMBER.get(number)
    if original:
        title = original["title"]
        lesson_body = original["content"].strip()
        lesson_card = (
            "╭━━━━━━━━━━━━━━━━━━╮\n"
            f"🌿 کەویار  •  وانەی {kurdish_digits(number)}\n"
            f"📖 {title}\n"
            "╰━━━━━━━━━━━━━━━━━━╯\n\n"
            f"{lesson_body}\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "✨ بە هێواشی بخوێنەوە و نموونەکان تێبینی بکە.\n"
            "🎯 کاتێک تەواو بوویت، دوگمەی «تەواوکردنی وانە» دابگرە."
        )
    else:
        title = course_lesson["title"]
        lesson_card = "⚠️ دەقی ئەسڵی ئەم وانەیە هێشتا لە فایلەکەدا نییە."
    LESSON_DATA[lesson_key] = {
        "title": title,
        "content": f"📚 {ORTHOGRAPHY_COURSE['title']}\n\n{lesson_card}",
    }
    # Prefix each label with its lesson number so repeated titles remain independently accessible.
    LESSON_BUTTONS[f"وانەی {kurdish_digits(number)}: {title}"] = lesson_key
    QUIZ_DATA[lesson_key] = []

for quiz_lesson in ORTHOGRAPHY_QUIZ_DRAFT.get("quizzes", []):
    number = quiz_lesson.get("lesson_number", quiz_lesson.get("number"))
    if number is None:
        logger.warning("Skipping quiz entry without lesson_number or number: %r", quiz_lesson)
        continue
    lesson_key = f"وانە_{number}"
    for question in quiz_lesson.get("questions", []):
        options = question.get("options", [])
        correct_index = question.get("correct_option_index", -1)
        if 0 <= correct_index < len(options):
            QUIZ_DATA.setdefault(lesson_key, []).append({
                "question": question["question"],
                "options": options,
                "answer": options[correct_index],
                "explanation": question.get("explanation", ""),
            })

# Optional local image assets. Keep the original lesson text available if an image is absent.
LESSON_INFOGRAPHICS = {
    "وانە_1": BASE_DIR / "photo_2026-10-27_00-13-52.jpg",
}

async def send_lesson_infographic(message, lesson):
    image_path = LESSON_INFOGRAPHICS.get(lesson)
    if image_path and image_path.is_file():
        try:
            with image_path.open("rb") as image_file:
                await message.reply_photo(
                    photo=image_file,
                    caption="🌿 کەویار | وانەی ١: پیتەکان و دەنگەکان",
                )
            return
        except Exception:
            logger.exception("Could not send lesson infographic for %s", lesson)
    # Missing/unreadable image must never prevent the lesson text from being sent.

ORDER = list(LESSON_DATA.keys())
COURSE_LESSON_ORDER = {course['id']: visible_course_lessons(course, LESSON_DATA) for course in COURSES}
LESSON_COURSE = {lesson_id: course_id for course_id, ids in COURSE_LESSON_ORDER.items() for lesson_id in ids}
MENU = ReplyKeyboardMarkup(
    [
        ["📚 وانەکان"],
        ["💬 گفتوگۆی ڕۆژانە"],
        ["👤 پێشکەوتنم", "🧭 ڕێگای فێربوون"],
        ["🎁 سەنوقی خەڵات", "📝 تاقیکردنەوەکان"],
    ],
    resize_keyboard=True,
)

def can_open(user_id, lesson):
    course_id = LESSON_COURSE.get(lesson)
    if course_id is None:
        return False
    completed = set(get_completed_lessons(user_id))
    return can_open_lesson(COURSE_LESSON_ORDER.get(course_id, []), completed, lesson)


def next_course_lesson(lesson):
    course_id = LESSON_COURSE.get(lesson)
    course_order = COURSE_LESSON_ORDER.get(course_id, [])
    if lesson not in course_order:
        return None
    index = course_order.index(lesson)
    return course_order[index + 1] if index + 1 < len(course_order) else None

def check_badges(user_id):
    completed = set(get_completed_lessons(user_id))
    for lesson in completed:
        number = int(lesson.removeprefix("وانە_")) if lesson.startswith("وانە_") and lesson.removeprefix("وانە_").isdigit() else 0
        if 1 <= number <= len(ORDER):
            add_badge(user_id, f"🏅 کۆرسی ڕێنووسی — وانەی {number}")

def lesson_keyboard(lesson):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ تەواوکردنی وانە", callback_data=f"finish_{lesson}")
    ]])

async def send_voice(update, filename):
    path = get_voice(filename)
    if not path:
        return
    try:
        with open(path, "rb") as audio:
            await update.message.reply_voice(voice=audio)
    except Exception:
        logger.exception("Could not send voice file %s", filename)

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
    await send_voice(update, "kejyar.mp3")

async def finish_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lesson = query.data.removeprefix("finish_")
    if lesson not in LESSON_COURSE:
        await query.message.reply_text("❌ ئەم وانەیە نەناسراوە.")
        return
    if not can_open(user_id, lesson):
        await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە.")
        return

    old_level = get_user_level(user_id)
    first_completion = complete_lesson_with_rewards(user_id, lesson)
    if not first_completion:
        await query.message.reply_text("✅ ئەم وانەیە پێشتر تەواو کراوە؛ خەڵاتی دووبارە نادرێت.")
        return

    check_badges(user_id)
    new_level = get_user_level(user_id)
    message_text = "✅ وانەکە تەواو بوو!\n\n🔥 +10 XP\n🪙 +5 Coin\n🎁 +1 سەنوقی خەڵات"
    if old_level != new_level:
        message_text += f"\n\n🎉 بەرزبوویتەوە بۆ: {new_level}"

    next_lesson = next_course_lesson(lesson)
    if next_lesson is None:
        # Keep legacy numeric callbacks stable while allowing namespaced course IDs.
        quiz_lesson_id = lesson.removeprefix("وانە_") if lesson.startswith("وانە_") else lesson
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "📝 تاقیکردنەوەی وانەی کۆتایی",
                callback_data=f"quiz_{quiz_lesson_id}_start",
            )
        ]])
        if QUIZ_DATA.get(lesson):
            await query.message.reply_text(
                message_text + "\n\n🎓 ئێستا تاقیکردنەوەکەش بکە.",
                reply_markup=keyboard,
            )
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
    # Generate event-specific narration in the configured Kejyar voice.
    # The repository's legacy event MP3s are byte-identical, so do not replay
    # the welcome clip as if it were a lesson-completion announcement.
    await send_conversation_voice(query.message, message_text, context.user_data, user_id)

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    suffix = query.data.removeprefix("quiz_").removesuffix("_start")
    # Numeric callback suffixes belong to Course 1; namespaced suffixes are
    # used by future courses without colliding with existing SQLite progress.
    lesson = f"وانە_{suffix}" if suffix.isdigit() else suffix
    if not lesson or lesson not in LESSON_COURSE:
        await query.message.reply_text("❌ ناسنامەی تاقیکردنەوە دروست نیە.")
        return
    if lesson not in LESSON_COURSE:
        await query.message.reply_text("⚠️ ئەم وانەیە لە ڕێڕەوی فێربووندا نیە.")
        return
    questions = QUIZ_DATA.get(lesson)
    if not questions:
        await query.message.reply_text("⚠️ تاقیکردنەوەی ئەم وانەیە ئامادە نیە.")
        return
    if lesson not in get_completed_lessons(user_id):
        await query.message.reply_text("🔒 سەرەتا خودی ئەم وانەیە تەواو بکە، پاشان تاقیکردنەوەکە بکە.")
        return
    context.user_data["quiz"] = {
        "index": 0,
        "lesson": lesson,
        "questions": questions,
        "score": 0,
        "question_message_id": None,
    }
    await send_question(query.message, context.user_data["quiz"])

async def send_question(message, quiz):
    question = quiz["questions"][quiz["index"]]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(option, callback_data=f"answer_{index}")]
        for index, option in enumerate(question["options"])
    ])
    sent = await message.reply_text("📝 " + question["question"], reply_markup=keyboard)
    quiz["question_message_id"] = sent.message_id

async def quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    quiz = context.user_data.get("quiz")
    if not quiz:
        await query.message.reply_text("ℹ️ تاقیکردنەوەیەکی چالاک نیە؛ لە منوودا دووبارە دەستی پێ بکە.")
        return
    # Ignore stale/double-clicked buttons from an earlier question.
    if query.message.message_id != quiz.get("question_message_id"):
        return
    # Validate callback data before claiming the question. Malformed callbacks
    # must not leave question_message_id=None and strand the active quiz.
    raw_index = query.data.removeprefix("answer_")
    if not raw_index.isdigit():
        return
    question = quiz["questions"][quiz["index"]]
    choice_index = int(raw_index)
    if choice_index < 0 or choice_index >= len(question["options"]):
        return
    # Claim this question before the first await so duplicate callbacks cannot
    # both score an answer while the next question is being sent.
    quiz["question_message_id"] = None
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
    explanation = question.get("explanation", "").strip()
    if explanation:
        feedback += f"\n\n📘 ڕوونکردنەوە: {explanation}"
    await query.message.reply_text(feedback)

    quiz["index"] += 1
    if quiz["index"] < len(quiz["questions"]):
        await send_question(query.message, quiz)
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
    await query.message.reply_text(result)
    context.user_data.pop("quiz", None)

async def send_lesson_text(message, content, reply_markup=None):
    """Send lesson drafts in Telegram-safe chunks without splitting Unicode text."""
    limit = 3800
    chunks = []
    remaining = content.strip()
    while remaining:
        if len(remaining) <= limit:
            chunks.append(remaining)
            break
        split_at = remaining.rfind("\n", 0, limit)
        if split_at < limit // 2:
            split_at = remaining.rfind(" ", 0, limit)
        if split_at < limit // 2:
            split_at = limit
        chunks.append(remaining[:split_at].strip())
        remaining = remaining[split_at:].strip()
    if not chunks:
        chunks = ["⚠️ ناوەڕۆکی ئەم وانەیە بەردەست نییە."]
    for index, chunk in enumerate(chunks):
        await message.reply_text(
            chunk,
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
    await send_lesson_infographic(query.message, lesson)


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
    await send_lesson_infographic(query.message, lesson)

async def send_conversation_voice(message, text, user_state=None, user_id=None):
    """Send generated speech with an atomic, persistent per-user UTC daily cap."""
    if not speech_is_configured():
        return
    # Persist the quota in SQLite so a process restart cannot reset the cap.
    if user_id is None:
        logger.warning("Skipping dynamic speech because user ID is unavailable")
        return
    quota_date = datetime.now(timezone.utc).date().isoformat()
    if not reserve_speech_quota(user_id, quota_date, limit=20):
        logger.info("Daily speech cap reached; continuing with text only")
        return
    try:
        audio_bytes = await generate_speech(text)
        if not audio_bytes:
            refund_speech_quota(user_id, quota_date)
            logger.warning("Speech generation was unavailable for a daily-chat reply")
            return
        audio = io.BytesIO(audio_bytes)
        audio.name = "kejyar-reply.mp3"
        await message.reply_voice(voice=audio)
    except Exception:
        refund_speech_quota(user_id, quota_date)
        logger.exception("Could not generate or send generated daily-chat voice")

async def open_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    course_id = query.data.removeprefix("course_")
    course = next((item for item in COURSES if item["id"] == course_id), None)
    if course is None:
        await query.message.reply_text("⚠️ ئەم کۆرسە نەدۆزرایەوە.")
        return

    # A manifest entry alone never activates a course. Planned/draft courses
    # remain unavailable even if lesson IDs are added prematurely.
    if course.get("status") != "active":
        status_labels = {
            "planned": "لە پلانداناندا",
            "draft": "پێش‌نووس",
            "draft_for_review": "لە پێداچوونەوەدایە",
        }
        status = status_labels.get(course.get("status", "planned"), "چالاک نییە")
        await query.message.reply_text(
            f"{course['title']}\n\n📌 دۆخ: {status}\n"
            f"{course.get('description', '')}\n\n"
            "ئەم کۆرسە هێشتا چالاک نەکراوە."
        )
        return

    lesson_ids = [lesson for lesson in course.get("lesson_ids", []) if lesson in LESSON_DATA]
    if not lesson_ids:
        status_labels = {
            "planned": "لە پلانداناندا",
            "active": "چالاک",
            "draft": "پێش‌نووس",
        }
        status = status_labels.get(course.get("status", "planned"), "لە پلانداناندا")
        await query.message.reply_text(
            f"{course['title']}\n\n"
            f"📌 دۆخ: {status}\n"
            f"{course.get('description', '')}\n\n"
            "ئەم کۆرسە وانەی ڕێکخراوی ئامادەی نییە؛ وانە کۆنەکان بە ناوی ئەم کۆرسەوە پیشان نادرێن."
        )
        return

    completed = set(get_completed_lessons(query.from_user.id))
    keyboard_rows = []
    for lesson in lesson_ids:
        status = "✅" if lesson in completed else ("🔓" if can_open(query.from_user.id, lesson) else "🔒")
        title = LESSON_DATA[lesson]["title"]
        keyboard_rows.append([InlineKeyboardButton(
            f"{status} {lesson}: {title}",
            callback_data=f"open_lesson_{lesson}",
        )])
    await query.message.reply_text(
        f"{course['title']}\n\n{course.get('description', '')}",
        reply_markup=InlineKeyboardMarkup(keyboard_rows),
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id
    get_user(user_id)

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
        "📚 وانەکان", "👤 پێشکەوتنم", "🧭 ڕێگای فێربوون",
        "🎁 سەنوقی خەڵات", "📝 تاقیکردنەوەکان",
    }:
        context.user_data["daily_chat_mode"] = False
        context.user_data.pop("daily_chat_scenario", None)
        context.user_data.pop("daily_chat_stage", None)

    if text == "📚 وانەکان":
        keyboard_rows = [
            [InlineKeyboardButton(course["title"], callback_data=f"course_{course['id']}")]
            for course in COURSES
        ]
        await update.message.reply_text(
            "📚 کۆرسەکانی کەژیار\n\n"
            "کۆرسەکان جیاوازن. کۆرسی یەکەم ٢٢ وانەی ڕێنووسی سەرەتایی هەیە؛ کۆرسەکانی دیکە تا ئامادەبوونی وانە ڕێکخراوەکان بە ڕوونی نیشان دراون.",
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
        await send_conversation_voice(
            update.message,
            f"بەخێربێیت بۆ وانەی {data.get('title', lesson)}. با دەست پێ بکەین.",
            context.user_data,
            user_id,
        )
        await send_lesson_infographic(update.message, lesson)
        return

    if text == "📝 تاقیکردنەوەکان":
        completed = set(get_completed_lessons(user_id))
        buttons = [[InlineKeyboardButton(f"📝 تاقیکردنەوەی {lesson}", callback_data=f"quiz_{lesson.split('_')[1]}_start")] for lesson in ORDER if QUIZ_DATA.get(lesson) and lesson in completed]
        if not buttons:
            await update.message.reply_text("🔒 سەرەتا وانەیەک بکەرەوە و تەواوی بکە.")
            return
        await update.message.reply_text("تاقیکردنەوە هەڵبژێرە 👇", reply_markup=InlineKeyboardMarkup(buttons))
        return

    if text == "🎁 سەنوقی خەڵات":
        reward = open_chest(user_id)
        if reward:
            await update.message.reply_text(f"🎁 سەنوق کراوەتەوە!\n🪙 {reward} Coin وەرگرت.")
            await send_conversation_voice(
                update.message,
                f"پیرۆزە! {reward} کۆین وەرگرت. بەردەوام بە و وانەکانی دواتر تەواو بکە.",
                context.user_data,
                user_id,
            )
        else:
            await update.message.reply_text("📦 سەنوقێکت نیە؛ وانە تەواو بکە بۆ وەرگرتنی سەنوق.")
        return

    if text == "👤 پێشکەوتنم":
        user = get_user(user_id)
        badges = get_badges(user_id)
        await update.message.reply_text(
            f"👤 پێشکەوتنم\n\n⭐ خاڵ: {user[1]}\n🔥 XP: {user[2]}\n🎓 ئاست: {user[3]}\n"
            f"🪙 Coin: {user[8]}\n🎁 سەنوق: {user[9]}\n\n🏅 نیشانەکان:\n" +
            ("\n".join(badges) if badges else "هێشتا هیچ نیشانەیەک نیە.")
        )
        return

    if text == "🧭 ڕێگای فێربوون":
        completed = set(get_completed_lessons(user_id))
        lines = []
        for lesson in ORDER:
            status = "✅ تەواو کراوە" if lesson in completed else ("🔓 ئامادەیە" if can_open(user_id, lesson) else "🔒 داخراوە")
            lines.append(f"{status} — {lesson}: {LESSON_DATA.get(lesson, {}).get('title', lesson)}")
        await update.message.reply_text("\n".join(lines))
        return

    if context.user_data.get("daily_chat_mode"):
        reply = reply_to_daily_message(text, context.user_data)
        await update.message.reply_text(reply, reply_markup=MENU)
        await send_conversation_voice(update.message, reply, context.user_data, user_id)
        return

    await update.message.reply_text("لە منووی کەژیار هەڵبژێرە 👇", reply_markup=MENU)

def main():
    init_db()
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN (or BOT_TOKEN) is missing. Set it in .env or the host environment.")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(finish_lesson, pattern=r"^finish_"))
    app.add_handler(CallbackQueryHandler(start_quiz, pattern=r"^quiz_.+_start$"))
    app.add_handler(CallbackQueryHandler(quiz_answer, pattern=r"^answer_\d+$"))
    app.add_handler(CallbackQueryHandler(open_course, pattern=r"^course_(orthography_basic|daily_conversation|unified_orthography|grammar)$"))
    app.add_handler(CallbackQueryHandler(open_next_lesson, pattern=r"^next_lesson_"))
    app.add_handler(CallbackQueryHandler(open_selected_lesson, pattern=r"^open_lesson_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
    logger.info("KejyarBot is running")
    app.run_polling()

if __name__ == "__main__":
    main()
