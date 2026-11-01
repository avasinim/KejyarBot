"""Telegram handlers for the isolated Arami Course 1 Lesson 1 flow."""
import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from arami_course1_runtime import load_arami_lesson1_interactions, get_arami_lesson1_audio_path
from arami_lesson1_interaction import (
    create_session, current_question, select_answer, submit_answer, session_result, retry_missed,
)

logger = logging.getLogger(__name__)


def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔊 دەنگی وانەی ١", callback_data="arami1:audio")],
        [InlineKeyboardButton("🎯 ڕاهێنانی وانەی ١", callback_data="arami1:practice")],
        [InlineKeyboardButton("📝 تاقیکردنەوەی وانەی ١", callback_data="arami1:assessment")],
    ])


async def send_question(message, context):
    session = context.user_data.get("arami_lesson1_session")
    question = current_question(session) if isinstance(session, dict) else None
    if question is None:
        await message.reply_text("🏁 ئەم هەوڵە تەواو بوو.")
        return
    number = session["index"] + 1
    total = len(session["questions"])
    heading = "🎯 ڕاهێران" if session["mode"] == "practice" else "📝 تاقیکردنەوە"
    rows = [
        [InlineKeyboardButton(option, callback_data=f"arami1:pick:{i}")]
        for i, option in enumerate(question["options"])
    ]
    sent = await message.reply_text(
        f"{heading} — پرسیاری {number}/{total}\n\n{question['prompt']}",
        reply_markup=InlineKeyboardMarkup(rows),
    )
    context.user_data["arami_lesson1_message_id"] = sent.message_id


async def callback(update, context, base_dir):
    query = update.callback_query
    await query.answer()
    action = query.data.removeprefix("arami1:")

    if action == "menu":
        await query.message.reply_text(
            "📕 کۆرسی ڕێنووسی ئارامی — وانەی ١\n«پیتەکان و دەنگەکان»\n\n"
            "دەنگی ڕەسەن، ڕاهێنان یان تاقیکردنەوە هەڵبژێرە:",
            reply_markup=menu_keyboard(),
        )
        return

    if action == "audio":
        try:
            path = get_arami_lesson1_audio_path(base_dir)
            with path.open("rb") as audio:
                await query.message.reply_voice(voice=audio)
        except (OSError, ValueError) as exc:
            logger.warning("Arami Lesson 1 audio unavailable: %s", exc)
            await query.message.reply_text("⚠️ دەنگی ڕەسەنی وانەی ١ ئێستا بەردەست نییە.")
        return

    if action in {"practice", "assessment"}:
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
        await query.message.reply_text("ℹ️ هیچ ڕاهێنانێکی ئارامی چالاک نییە.")
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
        correct_option = question["options"][question["answer_index"]]
        feedback = "✅ وەڵامت ڕاستە." if answer["correct"] else f"❌ وەڵامت هەڵەیە. وەڵامی ڕاست: {correct_option}"
        if session["closed"]:
            result = session_result(session)
            text = (
                f"{feedback}\n\n🏁 کۆتایی هات\n"
                f"ئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪"
            )
            rows = []
            if result["missed"]:
                rows.append([InlineKeyboardButton("🔁 دووبارەکردنەوەی پرسیارە هەڵەکان", callback_data="arami1:retry")])
            rows.append([InlineKeyboardButton("↩️ گەڕانەوە بۆ منیووی ئارامی", callback_data="arami1:menu")])
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
