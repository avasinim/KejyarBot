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

LESSON_DATA = load_json("lessons.json")
QUIZ_DATA = load_json("quiz.json")
COURSE_DATA = load_json("courses.json")
COURSES = sorted(COURSE_DATA.get("courses", []), key=lambda item: item.get("order", 999))
COURSE_BY_LESSON = {lesson: course for course in COURSES for lesson in course.get("lesson_ids", [])}

def course_lessons(course_id):
    course = next((item for item in COURSES if item["id"] == course_id), {})
    return [lesson for lesson in course.get("lesson_ids", []) if lesson in LESSON_DATA]

def next_lesson_in_course(lesson):
    course = COURSE_BY_LESSON.get(lesson)
    if not course:
        return None
    lessons = course_lessons(course["id"])
    index = lessons.index(lesson)
    return lessons[index + 1] if index + 1 < len(lessons) else None

LESSON_INFOGRAPHICS = {
    "وانە_1": "assets/infographics/lesson-01-greetings.svg",
    "وانە_2": "assets/infographics/lesson-02-letters-sample.svg",
    "وانە_3": "assets/infographics/lesson-03-daily-words.svg",
    "وانە_4": "assets/infographics/lesson-04-numbers.svg",
    "وانە_5": "assets/infographics/lesson-05-colors.svg",
    "وانە_6": "assets/infographics/lesson-06-home-school.svg",
    "وانە_7": "assets/infographics/lesson-07-family.svg",
    "وانە_8": "assets/infographics/lesson-08-food-drink.svg",
    "وانە_9": "assets/infographics/lesson-09-days-time.svg",
    "وانە_10": "assets/infographics/lesson-10-simple-sentences.svg",
}

async def send_lesson_infographic(message, lesson):
    relative_path = LESSON_INFOGRAPHICS.get(lesson)
    if not relative_path:
        return
    image_path = BASE_DIR / relative_path
    if not image_path.is_file():
        logger.warning("Lesson infographic missing: %s", image_path)
        return
    try:
        with image_path.open("rb") as infographic:
            await message.reply_document(
                document=infographic,
                filename=image_path.name,
                caption="🖼 وێنەی ڕوونکەرەوەی ئەم وانەیە",
            )
    except Exception:
        logger.exception("Could not send lesson infographic for %s", lesson)
ORDER = list(LESSON_DATA.keys())
LESSON_BUTTONS = {
    "👋 سڵاو و ناساندنی خۆ": "وانە_1",
    "🔤 ئەلفبێی کوردی": "وانە_2",
    "🗣 وشەکانی ڕۆژانە": "وانە_3",
    "🔢 ژمارەکان": "وانە_4",
    "🎨 ڕەنگەکان": "وانە_5",
    "🏠 لە ماڵ و قوتابخانە": "وانە_6",
    "👪 خێزان و کەسانی نزیک": "وانە_7",
    "🍽️ خواردن و خواردنەوە": "وانە_8",
    "📅 ڕۆژەکانی هەفتە و کات": "وانە_9",
    "🧱 ڕستەی سادە و پرسیارکردن": "وانە_10",
}
MENU = ReplyKeyboardMarkup(
    [
        ["🎓 دەورەکان", "📚 وانەکان"],
        ["💬 گفتوگۆی ڕۆژانە"],
        ["👤 پێشکەوتنم", "🧭 ڕێگای فێربوون"],
        ["🎁 سەنوقی خەڵات", "📝 تاقیکردنەوەکان"],
        ["👋 سڵاو و ناساندنی خۆ"],
        ["🔤 ئەلفبێی کوردی", "🗣 وشەکانی ڕۆژانە"],
        ["🔢 ژمارەکان", "🎨 ڕەنگەکان"],
        ["🏠 لە ماڵ و قوتابخانە"],
        ["👪 خێزان و کەسانی نزیک"],
        ["🍽️ خواردن و خواردنەوە"],
        ["📅 ڕۆژەکانی هەفتە و کات"],
        ["🧱 ڕستەی سادە و پرسیارکردن"],
    ],
    resize_keyboard=True,
)

def can_open(user_id, lesson):
    if lesson not in ORDER:
        return False
    completed = set(get_completed_lessons(user_id))
    course = COURSE_BY_LESSON.get(lesson)
    if course:
        lessons = course_lessons(course["id"])
        index = lessons.index(lesson)
        return index == 0 or lessons[index - 1] in completed
    index = ORDER.index(lesson)
    return index == 0 or ORDER[index - 1] in completed

def check_badges(user_id):
    badges = {
        "وانە_1": "🏅 دەستپێکەری کەژیار",
        "وانە_2": "🏅 دەستپێکەری کوردی",
        "وانە_3": "🏅 خوێندکاری وشەکان",
        "وانە_4": "🏅 ژمارەناس",
        "وانە_5": "🏅 ڕەنگناس",
        "وانە_6": "🏅 زانای ماڵ و قوتابخانە",
        "وانە_7": "🏅 ناسەری خێزان",
        "وانە_8": "🏅 شارەزای خواردن",
        "وانە_9": "🏅 ناسەری کات",
        "وانە_10": "🏅 دروستکەری ڕستە",
    }
    completed = set(get_completed_lessons(user_id))
    for lesson, badge in badges.items():
        if lesson in completed:
            add_badge(user_id, badge)

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
    if lesson not in ORDER:
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

    next_lesson = next_lesson_in_course(lesson)
    if next_lesson is None:
        last_lesson_number = lesson.removeprefix("وانە_")
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton("📝 تاقیکردنەوەی وانەی کۆتایی", callback_data=f"quiz_{last_lesson_number}_start")
        ]])
        course = COURSE_BY_LESSON.get(lesson)
        course_title = course.get("title", "") if course else ""
        ending = f"\n\n🏁 ئەم دەورەیە تەواو بوو: {course_title}" if course_title else ""
        await query.message.reply_text(message_text + ending + "\n\n🎓 ئێستا تاقیکردنەوەکەش بکە.", reply_markup=keyboard)
    else:
        next_title = LESSON_DATA.get(next_lesson, {}).get("title", next_lesson)
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                f"➡️ دەستپێکردنی {next_title}",
                callback_data=f"next_lesson_{next_lesson}"
            )
        ]])
        await query.message.reply_text(
            message_text + f"\n\n🔓 وانەی دواتر لە هەمان دەورە ئامادەیە: {next_title}",
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
    if not suffix.isdigit():
        await query.message.reply_text("❌ ناسنامەی تاقیکردنەوە دروست نیە.")
        return
    lesson = f"وانە_{suffix}"
    if lesson not in ORDER:
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
        await query.message.reply_text("✅ ئافەرین! وەڵامی دروستە.")
    else:
        await query.message.reply_text(f"❌ وەڵامەکە دروست نیە. وەڵامی دروست: {question['answer']}")

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

async def open_next_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lesson = query.data.removeprefix("next_lesson_")
    user_id = query.from_user.id
    if lesson not in ORDER or not can_open(user_id, lesson):
        await query.message.reply_text("🔒 وانەی پێشووتر تەواو بکە.")
        return
    data = LESSON_DATA.get(lesson)
    if not data:
        await query.message.reply_text("⚠️ ناوەڕۆکی ئەم وانەیە نەدۆزرایەوە.")
        return
    await query.message.reply_text(data["content"], reply_markup=lesson_keyboard(lesson))
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
        "🎓 دەورەکان", "📚 وانەکان", "👤 پێشکەوتنم", "🧭 ڕێگای فێربوون",
        "🎁 سەنوقی خەڵات", "📝 تاقیکردنەوەکان",
    }:
        context.user_data["daily_chat_mode"] = False
        context.user_data.pop("daily_chat_scenario", None)
        context.user_data.pop("daily_chat_stage", None)

    if text in {"🎓 دەورەکان", "📚 وانەکان"}:
        completed = set(get_completed_lessons(user_id))
        lines = ["🎓 دەورەکانی کەژیار"]
        for course in COURSES:
            lessons = course_lessons(course["id"])
            done = sum(lesson in completed for lesson in lessons)
            state = f"{done}/{len(lessons)} وانە" if lessons else "بە پلانی پەرەپێدان"
            lines.append(f"\n{course['title']}\n{course.get('description', '')}\n📌 {state}")
            for lesson in lessons:
                status = "✅" if lesson in completed else ("🔓" if can_open(user_id, lesson) else "🔒")
                title = LESSON_DATA.get(lesson, {}).get("title", lesson)
                lines.append(f"  {status} {lesson}: {title}")
        await update.message.reply_text("\n".join(lines))
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
        await update.message.reply_text(data["content"], reply_markup=lesson_keyboard(lesson))
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
        lines = ["🧭 ڕێگای فێربوون بە جیاوازیی دەورەکان"]
        for course in COURSES:
            lessons = course_lessons(course["id"])
            lines.append(f"\n{course['title']}")
            if not lessons:
                lines.append("  ⏳ ناوەڕۆکەکە لە قۆناغی پلاندانانە.")
                continue
            for lesson in lessons:
                status = "✅ تەواو کراوە" if lesson in completed else ("🔓 ئامادەیە" if can_open(user_id, lesson) else "🔒 داخراوە")
                lines.append(f"  {status} — {lesson}: {LESSON_DATA.get(lesson, {}).get('title', lesson)}")
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
    app.add_handler(CallbackQueryHandler(start_quiz, pattern=r"^quiz_\d+_start$"))
    app.add_handler(CallbackQueryHandler(quiz_answer, pattern=r"^answer_\d+$"))
    app.add_handler(CallbackQueryHandler(open_next_lesson, pattern=r"^next_lesson_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
    logger.info("KejyarBot is running")
    app.run_polling()

if __name__ == "__main__":
    main()
