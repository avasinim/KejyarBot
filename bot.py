import os
import json
import logging

# Load .env locally without requiring python-dotenv
ENV_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '.env'
)

if os.path.exists(ENV_FILE):
    with open(ENV_FILE, 'r', encoding='utf-8') as env_file:
        for line in env_file:
            line = line.strip()

            if not line or line.startswith('#') or '=' not in line:
                continue

            key, value = line.split('=', 1)

            key = key.strip()
            value = value.strip().strip('"').strip("'")

            if key:
                os.environ.setdefault(key, value)


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


# 🎙️ Voice system
from voice import get_voice_file


logging.basicConfig(level=logging.INFO)



MENU = ReplyKeyboardMarkup(
    [
        ['📚 وانەکان', '🔤 ئەلفوبێی کوردی'],
        ['🗣 وشەکانی ڕۆژانە', '🔢 ژمارەکان'],
        ['🎨 ڕەنگەکان', '👤 پێشکەوتنم'],
        ['🎁 سەنوقی خەڵات', '🧭 ڕێگای فێربوون']
    ],
    resize_keyboard=True
)



with open(
    'lessons.json',
    'r',
    encoding='utf-8'
) as f:

    LESSON_DATA = json.load(f)



LESSONS = {

    '🔤 ئەلفوبێی کوردی':
        (
            'درس_2',
            LESSON_DATA['درس_2']['content']
        ),


    '🗣 وشەکانی ڕۆژانە':
        (
            'درس_3',
            LESSON_DATA['درس_3']['content']
        ),


    '🔢 ژمارەکان':
        (
            'درس_4',
            LESSON_DATA['درس_4']['content']
        ),


    '🎨 ڕەنگەکان':
        (
            'درس_5',
            LESSON_DATA['درس_5']['content']
        )

}



ORDER = [
    'درس_2',
    'درس_3',
    'درس_4',
    'درس_5'
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

    i = ORDER.index(lesson)

    return i == 0 or ORDER[i - 1] in done




def check_badges(uid):

    badges = {

        'درس_2':
            '🏅 دەستپێکەری کوردی',

        'درس_3':
            '🏅 خوێندکاری وشەکان',

        'درس_4':
            '🏅 ژمارەناس',

        'درس_5':
            '🏅 ڕەنگناس'

    }


    for lesson, badge in badges.items():

        if lesson in get_completed_lessons(uid):

            add_badge(uid, badge)





async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    get_user(update.effective_user.id)


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


    # 🎙️ Send Kejyar voice

    try:

        voice_file = get_voice_file()


        if voice_file:

            await update.message.reply_voice(
                voice=open(
                    voice_file,
                    'rb'
                )
            )


    except Exception as e:

        logging.error(
            f"Voice error: {e}"
        )

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

🎉 پیرۆزە!

بەرزبوویتەوە بۆ:
{new_level}
"""



    await q.edit_message_text(
        msg
    )





async def message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    uid = update.effective_user.id



    if text in LESSONS:


        lesson, content = LESSONS[text]



        if not can_open(uid, lesson):

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




    elif text == '🎁 سەنوقی خەڵات':



        reward = open_chest(uid)



        if reward:


            await update.message.reply_text(

                f'🎁 سەنوق کراوەتەوە!\n🪙 {reward} Coin وەرگرت.'

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
            'TELEGRAM_BOT_TOKEN is missing. Add it to the .env file.'
        )



    app = Application.builder().token(token).build()



    app.add_handler(
        CommandHandler(
            'start',
            start
        )
    )



    app.add_handler(
        CallbackQueryHandler(
            finish_lesson
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





if __name__ == '__main__':

    main()