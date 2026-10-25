import json
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
    add_score,
    complete_lesson,
    get_completed_lessons,
    add_badge,
    get_badges,
    get_user_level,
    open_chest,
    add_chest,
    complete_quiz,
)
from voice import get_voice

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
ORDER = ["وانە_2", "وانە_3", "وانە_4", "وانە_5"]
LESSON_BUTTONS = {
    "🔤 ئەلفوبێی کوردی": "وانە_2",
    "🗣 وشەکانی ڕۆژانە": "وانە_3",
    "🔢 ژمارەکان": "وانە_4",
    "🎨 ڕەنگەکان": "وانە_5",
}
MENU = ReplyKeyboardMarkup(
    [
        ["📚 وانەکان"],
        ["👤 پێشکەوتنم", "🧭 ڕێگای فێربوون"],
        ["🎁 سەنوقی خەڵات", "📝 تاقیکردنەوەکان"],
        ["🔤 ئەلفوبێی کوردی", "🗣 وشەکانی ڕۆژانە"],
        ["🔢 ژمارەکان", "🎨 ڕەنگەکان"],
    ],
    resize_keyboard=True,
)

def can_open(user_id, lesson):
    if lesson not in ORDER:
        return False
    completed = set(get_completed_lessons(user_id))
    index = ORDER.index(lesson)
    return index == 0 or ORDER[index - 1] in completed

def check_badges(user_id):
    badges = {
        "وانە_2": "🏅 دەستپێکەری کوردی",
        "وانە_3": "🏅 خوێندکاری وشەکان",
        "وانە_4": "🏅 ژمارەناس",
        "وانە_5": "🏅 ڕەنگناس",
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

    already_done = lesson in get_completed_lessons(user_id)
    old_level = get_user_level(user_id)
    complete_lesson(user_id, lesson)
    if already_done:
        await query.message.reply_text("✅ ئەم وانەیە پێشتر تەواو کراوە؛ خەڵاتی دووبارە نادرێت.")
        return

    add_score(user_id, 10)
    add_chest(user_id)
    check_badges(user_id)
    new_level = get_user_level(user_id)
    message_text = "✅ وانەکە تەواو بوو!\n\n🔥 +10 XP\n🪙 +5 Coin\n🎁 +1 سەنوقی خەڵات"
    if old_level != new_level:
        message_text += f"\n\n🎉 بەرزبوویتەوە بۆ: {new_level}"

    if lesson == ORDER[-1]:
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton("📝 تاقیکردنەوەی وانەی ٥", callback_data="quiz_5_start")
        ]])
        await query.message.reply_text(message_text + "\n\n🎓 ئێستا تاقیکردنەوەکەش بکە.", reply_markup=keyboard)
    else:
        await query.message.reply_text(message_text)
    path = get_voice("lesson_done.mp3")
    if path:
        try:
            with open(path, "rb") as audio:
                await query.message.reply_voice(voice=audio)
        except Exception:
            logger.exception("Could not send lesson completion voice")

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    suffix = query.data.removeprefix("quiz_").removesuffix("_start")
    if not suffix.isdigit():
        await query.message.reply_text("❌ ناسنامەی تاقیکردنەوە دروست نیە.")
        return
    lesson = f"وانە_{suffix}"
    questions = QUIZ_DATA.get(lesson)
    if not questions:
        await query.message.reply_text("⚠️ تاقیکردنەوەی ئەم وانەیە ئامادە نیە.")
        return
    if lesson in ORDER and not can_open(user_id, lesson):
        await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە.")
        return
    context.user_data["quiz"] = {"index": 0, "lesson": lesson, "questions": questions, "score": 0}
    await send_question(query.message, context.user_data["quiz"])

async def send_question(message, quiz):
    question = quiz["questions"][quiz["index"]]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(option, callback_data=f"answer_{index}")]
        for index, option in enumerate(question["options"])
    ])
    await message.reply_text("📝 " + question["question"], reply_markup=keyboard)

async def quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    quiz = context.user_data.get("quiz")
    if not quiz:
        await query.message.reply_text("ℹ️ تاقیکردنەوەیەکی چالاک نیە؛ لە منوودا دووبارە دەستی پێ بکە.")
        return
    raw_index = query.data.removeprefix("answer_")
    if not raw_index.isdigit():
        return
    question = quiz["questions"][quiz["index"]]
    choice_index = int(raw_index)
    if choice_index < 0 or choice_index >= len(question["options"]):
        return
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
    first_completion = complete_quiz(update.effective_user.id, lesson)
    result = (
        f"🎉 تاقیکردنەوە تەواو بوو!\\n"
        f"✅ وەڵامی دروست: {earned}/{len(quiz['questions'])}\\n"
    )
    if first_completion:
        add_score(update.effective_user.id, 20)
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

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id
    get_user(user_id)

    if text == "📚 وانەکان":
        rows = []
        completed = set(get_completed_lessons(user_id))
        for lesson in ORDER:
            status = "✅" if lesson in completed else ("🔓" if can_open(user_id, lesson) else "🔒")
            title = LESSON_DATA.get(lesson, {}).get("title", lesson)
            rows.append(f"{status} {lesson}: {title}")
        await update.message.reply_text("\n".join(rows))
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
        path = get_voice("lesson_start.mp3")
        if path:
            try:
                with open(path, "rb") as audio:
                    await update.message.reply_voice(voice=audio)
            except Exception:
                logger.exception("Could not send lesson start voice")
        await update.message.reply_text(data["content"], reply_markup=lesson_keyboard(lesson))
        return

    if text == "📝 تاقیکردنەوەکان":
        buttons = [[InlineKeyboardButton(f"📝 تاقیکردنەوەی {lesson}", callback_data=f"quiz_{lesson.split('_')[1]}_start")] for lesson in ORDER if QUIZ_DATA.get(lesson) and can_open(user_id, lesson)]
        if not buttons:
            await update.message.reply_text("🔒 سەرەتا وانەیەک بکەرەوە و تەواوی بکە.")
            return
        await update.message.reply_text("تاقیکردنەوە هەڵبژێرە 👇", reply_markup=InlineKeyboardMarkup(buttons))
        return

    if text == "🎁 سەنوقی خەڵات":
        reward = open_chest(user_id)
        if reward:
            await update.message.reply_text(f"🎁 سەنوق کراوەتەوە!\n🪙 {reward} Coin وەرگرت.")
            path = get_voice("reward.mp3")
            if path:
                try:
                    with open(path, "rb") as audio:
                        await update.message.reply_voice(voice=audio)
                except Exception:
                    logger.exception("Could not send reward voice")
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
