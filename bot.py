import os
import json
import logging

from voice import get_voice


ENV_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '.env'
)


if os.path.exists(ENV_FILE):
    with open(
        ENV_FILE,
        'r',
        encoding='utf-8'
    ) as env_file:

        for line in env_file:
            line = line.strip()

            if not line or line.startswith('#') or '=' not in line:
                continue

            key, value = line.split('=', 1)

            os.environ.setdefault(
                key.strip(),
                value.strip().strip('"').strip("'")
            )


from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
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
    add_chest
)


logging.basicConfig(
    level=logging.INFO
)
USER_QUIZ = {}

MENU = ReplyKeyboardMarkup(
    [
        ['📚 وانەکان'],
        ['👤 پێشکەوتنم', '🧭 ڕێگای فێربوون'],
        ['🎁 سەنوقی خەڵات', '📝 تاقیکردنەوەکان'],
        ['🔤 ئەلفوبێی کوردی', '🗣 وشەکانی ڕۆژانە'],
        ['🔢 ژمارەکان', '🎨 ڕەنگەکان']
    ],
    resize_keyboard=True
)



with open(
    'lessons.json',
    'r',
    encoding='utf-8'
) as f:

    LESSON_DATA = json.load(f)
with open(
    'quiz.json',
    'r',
    encoding='utf-8'
) as f:

    QUIZ_DATA = json.load(f)
with open(
    'quiz.json',
    'r',
    encoding='utf-8'
) as f:

    QUIZ_DATA = json.load(f)

LESSONS = {

    '🔤 ئەلفوبێی کوردی':
        (
            'وانە_2',
            LESSON_DATA['وانە_2']['content']
        ),


    '🗣 وشەکانی ڕۆژانە':
        (
            'وانە_3',
            LESSON_DATA['وانە_3']['content']
        ),


    '🔢 ژمارەکان':
        (
            'وانە_4',
            LESSON_DATA['وانە_4']['content']
        ),


    '🎨 ڕەنگەکان':
        (
            'وانە_5',
            LESSON_DATA['وانە_5']['content']
        )

}



ORDER = [
    'وانە_2',
    'وانە_3',
    'وانە_4',
    'وانە_5'
]



def level_by_xp(xp):

    if xp < 50:
        return 'A1.1 🌱'

    if xp < 100:
        return 'A1.2 🌿'

    if xp < 150:
        return 'A2.1 📘'

    if xp < 300:
        return 'A2.2 📖'

    if xp < 450:
        return 'B1.1 🚀'

    if xp < 600:
        return 'B1.2 🔥'

    if xp < 800:
        return 'B2.1 🏆'

    return 'B2.2 👑'



def can_open(uid, lesson):

    done = get_completed_lessons(uid)

    index = ORDER.index(lesson)

    return index == 0 or ORDER[index - 1] in done



def check_badges(uid):

    badges = {

        'وانە_2':
            '🏅 دەستپێکەری کوردی',

        'وانە_3':
            '🏅 خوێندکاری وشەکان',

        'وانە_4':
            '🏅 ژمارەناس',

        'وانە_5':
            '🏅 ڕەنگناس'

    }


    for lesson, badge in badges.items():

        if lesson in get_completed_lessons(uid):

            add_badge(
                uid,
                badge
            )
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    get_user(
        update.effective_user.id
    )


    welcome = """
🌱 سڵاو، بەخێربێیت بۆ کەژیار

خوایە وەتەن ئاوا کەی
چەند دڵگیر و شیرینە
دەشتی خۆش و ڕەنگینە
ئاوی کەوسەرە، خاکی گەوهەرە
پڕ لە گوڵ و نەسرینە

ئامادەیت دەست پێ بکەیت؟ 🌱
"""


    await update.message.reply_text(
        welcome,
        reply_markup=MENU
    )


    try:

        voice_file = get_voice(
            "kejyar.mp3"
        )

        if voice_file:

            await update.message.reply_voice(
                voice=open(
                    voice_file,
                    "rb"
                )
            )

    except Exception as e:

        logging.error(e)



async def finish_lesson(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    q = update.callback_query

    await q.answer()


    uid = q.from_user.id


    old_level = get_user_level(uid)


    lesson = q.data.replace(
        'finish_',
        ''
    )


    complete_lesson(
        uid,
        lesson
    )


    add_score(
        uid,
        10
    )


    add_chest(uid)


    check_badges(uid)


    new_level = get_user_level(uid)



    msg = """
✅ وانەکە تەواو بوو!

🔥 +10 XP
🪙 +5 Coin
🎁 +1 سەنوقی خەڵات
"""


    if old_level != new_level:

        msg += f"""

🎉 بژی!

بەرزبوویتەوە بۆ:

{new_level}
"""


    await q.edit_message_text(
        msg
    )



    # بعد از پایان وانەی ٥ آزمون باز شود

    if lesson == 'وانە_5':

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'دەست پێکردنی تاقیکاری وانەی ٥',
                        callback_data='quiz_5_start'
                    )
                ]
            ]
        )


        await q.message.reply_text(
            '🎓 بژی! وانەی ٥ تەواو بوو.\nئێستا دەتوانیت تاقیکردنەوە بکەیت.',
            reply_markup=keyboard
        )



    done_voice = get_voice(
        "lesson_done.mp3"
    )


    if done_voice:

        await q.message.reply_voice(
            voice=open(
                done_voice,
                "rb"
            )
        )


async def start_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    q = update.callback_query

    await q.answer()

    uid = q.from_user.id

    with open(
        'quiz.json',
        'r',
        encoding='utf-8'
    ) as f:
        quiz_data = json.load(f)

    USER_QUIZ[uid] = {
        "index": 0,
        "questions": quiz_data["وانە_5"]
    }

    question = USER_QUIZ[uid]["questions"][0]

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    option,
                    callback_data=f"answer_{option}"
                )
            ]
            for option in question["options"]
        ]
    )

    await q.message.reply_text(
        "📝 " + question["question"],
        reply_markup=keyboard
    )


async def quiz_answer(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    q = update.callback_query

    await q.answer()

    uid = q.from_user.id

    answer = q.data.replace(
        "answer_",
        ""
    )

    quiz = USER_QUIZ.get(uid)

    if not quiz:
        return

    question = quiz["questions"][quiz["index"]]

    if answer == question["answer"]:

        await q.message.reply_text(
            "✅ ئافەرین! وەڵامی دروستە."
        )

    else:

        await q.message.reply_text(
            f"❌ هەڵەیە.\nوەڵامی دروست: {question['answer']}"
        )


    quiz["index"] += 1


    if quiz["index"] >= len(quiz["questions"]):

        await q.message.reply_text(
            "🎉 تاقیکردنەوە تەواو بوو!"
        )

        del USER_QUIZ[uid]
        return


    question = quiz["questions"][quiz["index"]]


    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    option,
                    callback_data=f"answer_{option}"
                )
            ]
            for option in question["options"]
        ]
    )


    await q.message.reply_text(
        "📝 " + question["question"],
        reply_markup=keyboard
    )


async def message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    uid = update.effective_user.id



    if text in LESSONS:


        lesson, content = LESSONS[text]


        start_voice = get_voice(
            "lesson_start.mp3"
        )


        if start_voice:

            await update.message.reply_voice(
                voice=open(
                    start_voice,
                    "rb"
                )
            )



        if not can_open(
            uid,
            lesson
        ):

            await update.message.reply_text(
                '🔒 وانەی پێشووتر تەواو بکە'
            )

            return



        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '✅ تەواوکردنی وانە',
                        callback_data=f'finish_{lesson}'
                    )
                ]
            ]
        )



        await update.message.reply_text(
            content,
            reply_markup=keyboard
        )



    elif text == '📝 تاقیکردنەوەکان':

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '📝 تاقیکردنەوەی وانەی ٥',
                        callback_data='quiz_5_start'
                    )
                ]
            ]
        )

        await update.message.reply_text(
            'تاقیکردنەوە هەڵبژێرە 👇',
            reply_markup=keyboard
        )


        reward = open_chest(uid)



        if reward:

            await update.message.reply_text(
                f'🎁 سەنوق کراوەتەوە!\n🪙 {reward} Coin وەرگرت.'
            )


            reward_voice = get_voice(
                "reward.mp3"
            )


            if reward_voice:

                await update.message.reply_voice(
                    voice=open(
                        reward_voice,
                        "rb"
                    )
                )


        else:

            await update.message.reply_text(
                '📦 هیچ سەنوقێک نییە. وانە تەواو بکە بۆ وەرگرتنی سەنوق.'
            )




    elif text == '👤 پێشکەوتنم':


        u = get_user(uid)



        await update.message.reply_text(

            f"""
👤 پێشکەوتنم

⭐ امتیاز: {u[1]}
🔥 XP: {u[2]}
🎓 ئاست: {u[3]}
🪙 Coin: {u[8]}
🎁 سەنوقی خەڵات: {u[9]}


🏅 نشانەکان:

{chr(10).join(get_badges(uid))}
"""
        )




    elif text == '🧭 ڕێگای فێربوون':


        path = []


        for lesson in ORDER:


            if lesson in get_completed_lessons(uid):

                path.append(
                    '✅ ' + lesson
                )

            else:

                path.append(
                    '🔒 ' + lesson
                )



        await update.message.reply_text(
            '\n'.join(path)
        )



    else:


        await update.message.reply_text(
            'لە منووی کەژیار هەڵبژێرە 👇',
            reply_markup=MENU
        )





def main():


    init_db()



    token = os.environ.get(
        'TELEGRAM_BOT_TOKEN'
    )


    if not token:

        raise RuntimeError(
            'TELEGRAM_BOT_TOKEN is missing.'
        )



    app = Application.builder().token(token).build()



    app.add_handler(
        CommandHandler(
            'start',
            start
        )
    )



    app.add_handler(
        CommandHandler(
            'start',
            start
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            finish_lesson,
            pattern="^finish_"
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            start_quiz,
            pattern="^quiz_5_start$"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            quiz_answer,
            pattern="^answer_"
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message
        )
    )


    print(
        "🌱 KejyarBot is running..."
    )


    app.run_polling()


    app.run_polling()



if __name__ == '__main__':

    main()