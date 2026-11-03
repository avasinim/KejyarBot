"""Telegram handlers for the isolated Course 1 Lesson 1 flow."""
import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from arami_course1_runtime import load_arami_lesson1_interactions, load_arami_lesson1_content
from arami_course1_telegram import load_manifest, send_lesson_audio, _send_source
from arami_lesson1_interaction import (
    create_session, current_question, select_answer, submit_answer, session_result, retry_missed,
)

logger = logging.getLogger(__name__)


def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 خوێندنەوەی وانەی ١", callback_data="arami1:lesson")],
        [InlineKeyboardButton("🎯 ڕاهێنانی وانەی ١", callback_data="arami1:practice")],
        [InlineKeyboardButton("📝 تاقیکردنەوەی وانەی ١", callback_data="arami1:assessment")],
        [InlineKeyboardButton("📚 وانەی ٥ — پیتەکان و هاوتای لاتینی", callback_data="arami5:menu")],
        [InlineKeyboardButton("📚 هەموو ٢١ وانەی کۆرس ١", callback_data="aramiC:menu")],
    ])


async def send_question(message, context):
    session = context.user_data.get("arami_lesson1_session")
    question = current_question(session) if isinstance(session, dict) else None
    if question is None:
        await message.reply_text("🏁 ئەم هەوڵە تەواو بوو.")
        return
    number = session["index"] + 1
    total = len(session["questions"])
    heading = "🎯 ڕاهێنان" if session["mode"] == "practice" else "📝 تاقیکردنەوە"
    rows = [
        [InlineKeyboardButton(option, callback_data=f"arami1:pick:{i}")]
        for i, option in enumerate(question["options"])
    ]
    sent = await message.reply_text(
        f"{heading} — پرسیاری {number}/{total}\n\n{question['prompt']}",
        reply_markup=InlineKeyboardMarkup(rows),
    )
    context.user_data["arami_lesson1_message_id"] = sent.message_id


def _lesson_source_markdown(lesson):
    """Adapt Lesson 1's structured source without changing its wording."""
    lines = ['# ' + lesson['title'], '', '## ئامانجەکانی فێربوون']
    lines.extend('- ' + item for item in lesson['objectives'])
    for section in lesson['sections']:
        lines.extend(['', '## ' + section['title']])
        if section.get('body'):
            lines.extend(['', section['body']])
        if section.get('table'):
            lines.append('')
            lines.extend('| ' + ' | '.join(str(cell) for cell in row) + ' |' for row in section['table'])
        if section.get('note'):
            lines.extend(['', section['note']])
        for question in section.get('questions', []):
            lines.extend(['', question['prompt']])
            lines.extend(chr(65 + i) + ') ' + option for i, option in enumerate(question['options']))
    return '\n'.join(lines)


async def callback(update, context, base_dir, can_open=None, award_assessment=None):
    query = update.callback_query
    await query.answer()
    action = query.data.removeprefix("arami1:")

    if action == "menu":
        await query.message.reply_text(
            "📕 کۆرسی ١: ڕێنووسی سەرەتاییی کوردی — وانەی ١\n«پیتەکان و دەنگەکان»\n\n"
            "دەنگی ڕەسەن، ڕاهێنان یان تاقیکردنەوە هەڵبژێرە:",
            reply_markup=menu_keyboard(),
        )
        return

    if action == "lesson":
        try:
            lesson = load_arami_lesson1_content(base_dir)
            manifest = load_manifest(base_dir)
            lesson_record = next(item for item in manifest["lessons"] if item["number"] == 1)
        except (OSError, ValueError, StopIteration):
            logger.exception("Could not load Arami Lesson 1 source text")
            await query.message.reply_text("⚠️ دەقی ڕەسەنی وانەی ١ ئامادە نییە.")
            return
        if can_open is not None and not can_open(query.from_user.id, lesson_record["id"]):
            await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە؛ ئەم وانەیە هێشتا نەکراوەتەوە.")
            return
        await _send_source(
            query.message,
            'وانەی ١ — ' + lesson['title'],
            _lesson_source_markdown(lesson),
        )
        lesson_audio = lesson_record
        await send_lesson_audio(query.message, base_dir, lesson_audio)
        await _send_source(
            query.message,
            'پوختەی وانەی ١',
            '## کورتەی وانە\n\n' + lesson['conclusion'],
        )
        await query.message.reply_text(
            '⭐ وانەکە تەواو بوو؛ بۆ تۆمارکردنی پێشکەوتنت دوگمەی خوارەوە هەڵبژێرە.',
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✅ تەواوکردنی وانە", callback_data=f"finish_{lesson_record['id']}")
            ]]),
        )
        await query.message.reply_text("📚 بۆ بینینی وانەکانی تر، منیووی کۆرسی ١ بکەرەوە.", reply_markup=menu_keyboard())
        return

    if action == "audio":
        await query.message.reply_text(
            "ℹ️ دەنگی پشتڕاستکراو بۆ وانەی ٢ تۆمار کراوە؛ وانەی ١ دەنگی تایبەتی نییە."
        )
        return

    if action in {"practice", "assessment"}:
        if can_open is not None:
            try:
                manifest = load_manifest(base_dir)
                lesson_record = next(item for item in manifest["lessons"] if item["number"] == 1)
            except (OSError, ValueError, StopIteration):
                await query.message.reply_text("⚠️ زانیاریی وانەکە ئامادە نییە.")
                return
            if not can_open(query.from_user.id, lesson_record["id"]):
                await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە؛ ڕاهێنان و تاقیکردنەوەی ئەم وانەیە هێشتا نەکراونەتەوە.")
                return
        try:
            bank = load_arami_lesson1_interactions(base_dir)
            context.user_data["arami_lesson1_session"] = create_session(bank[action], action)
            context.user_data["arami_lesson1_message_id"] = None
        except (OSError, ValueError) as exc:
            logger.exception("Could not start Arami Lesson 1 interaction")
            await query.message.reply_text("⚠️ ڕاهێنان/تاقیکردنەوەکە ئامادە نییە.")
            return
        await send_question(query.message, context)
        return

    session = context.user_data.get("arami_lesson1_session")
    if not isinstance(session, dict):
        await query.message.reply_text("ℹ️ هیچ ڕاهێنانێکی وانەی ١ چالاک نییە.")
        return
    if query.message.message_id != context.user_data.get("arami_lesson1_message_id"):
        return

    if action.startswith("pick:"):
        raw = action.removeprefix("pick:")
        if not raw.isdigit():
            return
        try:
            selected = select_answer(session, int(raw))
        except (ValueError, TypeError):
            await query.message.reply_text("⚠️ هەڵبژاردەکە دروست نییە؛ تکایە دووبارە هەڵبژێرە.")
            return
        question = current_question(session)
        rows = [
            [InlineKeyboardButton(
                ("☑️ " if i == selected else "▫️ ") + option,
                callback_data=f"arami1:pick:{i}",
            )]
            for i, option in enumerate(question["options"])
        ]
        rows.append([InlineKeyboardButton("📨 ناردنی وەڵام", callback_data="arami1:submit")])
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(rows))
        return

    if action == "submit":
        question = current_question(session)
        try:
            answer = submit_answer(session)
        except (ValueError, TypeError):
            await query.message.reply_text("سەرەتا وەڵامێک هەڵبژێرە.")
            return
        if session["mode"] == "practice":
            correct_option = question["options"][question["answer_index"]]
            feedback = "✅ وەڵامت ڕاستە." if answer["correct"] else f"❌ وەڵامت هەڵەیە. وەڵامی ڕاست: {correct_option}"
        else:
            feedback = "✅ وەڵامەکەت وەرگیرا."
        if session["closed"]:
            result = session_result(session)
            reward_note = ""
            if session["mode"] == "assessment" and award_assessment is not None:
                if award_assessment(query.from_user.id, "arami_course1_lesson_01"):
                    reward_note = "\\n\\n🎁 +20 XP — یەکەم تەواوکردنی تاقیکردنەوە"
            text = (
                f"{feedback}\n\n🏁 کۆتایی هات\n"
                f"ئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪{reward_note}"
            )
            rows = []
            if result["missed"]:
                rows.append([InlineKeyboardButton("🔁 دووبارەکردنەوەی پرسیارە هەڵەکان", callback_data="arami1:retry")])
            rows.append([InlineKeyboardButton("↩️ گەڕانەوە بۆ منیووی کۆرسی ١", callback_data="arami1:menu")])
            await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(rows))
        else:
            await query.edit_message_text(
                feedback,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("➡️ پرسیاری دواتر", callback_data="arami1:next")
                ]]),
            )
        return

    if action == "next":
        if not session.get("closed"):
            await send_question(query.message, context)
        return

    if action == "retry":
        try:
            retry_session = retry_missed(session)
        except ValueError:
            retry_session = None
        if retry_session is None:
            await query.message.reply_text("🌟 هیچ پرسیارێکی هەڵە نەماوە.")
            return
        context.user_data["arami_lesson1_session"] = retry_session
        context.user_data["arami_lesson1_message_id"] = None
        await send_question(query.message, context)
