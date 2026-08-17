import os
import json
import logging

# Load .env locally without requiring python-dotenv.
ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
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

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

from database import init_db, get_user, add_score, complete_lesson, get_completed_lessons, add_badge, get_badges, get_user_level, open_chest, add_chest

logging.basicConfig(level=logging.INFO)

MENU = ReplyKeyboardMarkup([
    ['📚 وانەکان','🔤 ئەلفوبێی کوردی'],
    ['🗣 وشەکانی ڕۆژانە','🔢 ژمارەکان'],
    ['🎨 ڕەنگەکان','👤 پێشکەوتنم'],
    ['🎁 صندوقی جایزه','🧭 ڕێگای فێربوون']
], resize_keyboard=True)

with open('lessons.json','r',encoding='utf-8') as f:
    LESSON_DATA=json.load(f)

LESSONS={
'🔤 ئەلفوبێی کوردی':('درس_2',LESSON_DATA['درس_2']['content']),
'🗣 وشەکانی ڕۆژانە':('درس_3',LESSON_DATA['درس_3']['content']),
'🔢 ژمارەکان':('درس_4',LESSON_DATA['درس_4']['content']),
'🎨 ڕەنگەکان':('درس_5',LESSON_DATA['درس_5']['content'])}

ORDER=['درس_2','درس_3','درس_4','درس_5']


def level_by_xp(xp):
    if xp<50:return 'A1.1 🌱'
    if xp<100:return 'A1.2 🌿'
    if xp<150:return 'A2.1 📘'
    if xp<300:return 'A2.2 📖'
    if xp<450:return 'B1.1 🚀'
    if xp<600:return 'B1.2 🔥'
    if xp<800:return 'B2.1 🏆'
    return 'B2.2 👑'


def can_open(uid,lesson):
    done=get_completed_lessons(uid)
    i=ORDER.index(lesson)
    return i==0 or ORDER[i-1] in done


def check_badges(uid):
    for k,v in {'درس_2':'🏅 دەستپێکەری کوردی','درس_3':'🏅 خوێندکاری وشەکان','درس_4':'🏅 ژمارەناس','درس_5':'🏅 ڕەنگناس'}.items():
        if k in get_completed_lessons(uid): add_badge(uid,v)


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
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

 


async def finish_lesson(update:Update,context:ContextTypes.DEFAULT_TYPE):
    q=update.callback_query
    await q.answer()
    uid=q.from_user.id
    old=get_user_level(uid)
    complete_lesson(uid,q.data.replace('finish_',''))
    add_score(uid,10)
    add_chest(uid)
    check_badges(uid)
    new=get_user_level(uid)
    msg='✅ وانەکە تەواو بوو!\n🔥 +10 XP\n🪙 +5 Coin\n🎁 +1 صندوقی جایزه'
    if old!=new:
        msg+=f'\n\n🎉 پیرۆزە! بەرزبوویتەوە بۆ {new}'
    await q.edit_message_text(msg)


async def message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    text=update.message.text
    uid=update.effective_user.id

    if text in LESSONS:
        lesson,content=LESSONS[text]
        if not can_open(uid,lesson):
            await update.message.reply_text('🔒 وانەی پێشووتر تەواو بکە')
            return
        kb=InlineKeyboardMarkup([[InlineKeyboardButton('✅ تەواوکردنی وانە',callback_data=f'finish_{lesson}')]])
        await update.message.reply_text(content,reply_markup=kb)

    elif text=='🎁 صندوقی جایزه':
        reward=open_chest(uid)
        if reward:
            await update.message.reply_text(f'🎁 صندوق کراوە!\n🪙 {reward} Coin وەرگرت.')
        else:
            await update.message.reply_text('📦 هیچ صندوقێک نییە. وانە تەواو بکە بۆ وەرگرتنی صندوق.')

    elif text=='👤 پێشکەوتنم':
        u=get_user(uid)
        await update.message.reply_text(f'👤 پێشکەوتنم\n\n⭐ امتیاز: {u[1]}\n🔥 XP: {u[2]}\n🎓 ئاست: {u[3]}\n🪙 Coin: {u[8]}\n🎁 صندوق: {u[9]}\n\n🏅 نشانەکان:\n'+'\n'.join(get_badges(uid)))

    elif text=='🧭 ڕێگای فێربوون':
        await update.message.reply_text('\n'.join(('✅ ' if x in get_completed_lessons(uid) else '🔒 ')+x for x in ORDER))

    else:
        await update.message.reply_text('لە منووی کەژیار هەڵبژێرە 👇',reply_markup=MENU)


def main():
    init_db()
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        raise RuntimeError('TELEGRAM_BOT_TOKEN is missing. Add it to the .env file in the project folder.')
    app=Application.builder().token(token).build()
    app.add_handler(CommandHandler('start',start))
    app.add_handler(CallbackQueryHandler(finish_lesson))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,message))
    app.run_polling()


if __name__=='__main__':
    main()
