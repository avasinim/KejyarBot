"""Telegram delivery for Arami Course 1 Lesson 5; isolated from Lesson 1."""
import logging
import re
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from arami_course1_runtime import load_arami_lesson5_interactions, load_arami_lesson5_source
from arami_course1_telegram import load_manifest, send_lesson_audio
from arami_lesson1_interaction import create_session, current_question, select_answer, submit_answer, session_result, retry_missed
logger = logging.getLogger(__name__)

def _plain_source(markdown):
    lines = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line or line.startswith("---"):
            continue
        if line.startswith("|") and line.endswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
                continue
            lines.append(" • ".join(cells))
            continue
        line = re.sub(r"^#{1,6}\s*", "", line).replace("**", "").replace(chr(96), "")
        if line.startswith(">"):
            line = line[1:].strip()
        lines.append(line)
    return "\n".join(lines)

def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 خوێندنەوەی وانەی ٥", callback_data="arami5:lesson")],
        [InlineKeyboardButton("🎯 ڕاهێنانی وانەی ٥", callback_data="arami5:practice")],
        [InlineKeyboardButton("📝 تاقیکردنەوەی وانەی ٥", callback_data="arami5:assessment")],
        [InlineKeyboardButton("📚 هەموو ٢١ وانەی کۆرس ١", callback_data="aramiC:menu")],
    ])

async def _send_question(message, context):
    session = context.user_data.get("arami_lesson5_session")
    question = current_question(session) if isinstance(session, dict) else None
    if question is None:
        await message.reply_text("🏁 ئەم هەوڵە تەواو بوو.")
        return
    rows = [[InlineKeyboardButton(option, callback_data=f"arami5:pick:{i}")] for i, option in enumerate(question["options"])]
    sent = await message.reply_text(
        f"{'🎯 ڕاهێنان' if session['mode'] == 'practice' else '📝 تاقیکردنەوە'} — پرسیاری {session['index'] + 1}/{len(session['questions'])}\n\n{question['prompt']}",
        reply_markup=InlineKeyboardMarkup(rows))
    context.user_data["arami_lesson5_message_id"] = sent.message_id

async def callback(update, context, base_dir, can_open=None):
    query = update.callback_query
    await query.answer()
    action = query.data.removeprefix("arami5:")
    if action == "menu":
        await query.message.reply_text("وانەی ٥ — هەڵبژاردنی خوێندنەوە یان تاقیکردنەوە:", reply_markup=menu_keyboard())
        return
    if action == "lesson":
        try:
            source = _plain_source(load_arami_lesson5_source(base_dir))
            manifest = load_manifest(base_dir)
            lesson_record = next(item for item in manifest["lessons"] if item["number"] == 5)
        except (OSError, ValueError, StopIteration):
            logger.exception("Could not load Arami Lesson 5 source")
            await query.message.reply_text("⚠️ دەقی ڕەسەنی وانەی ٥ ئامادە نییە.")
            return
        if can_open is not None and not can_open(query.from_user.id, lesson_record["id"]):
            await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە؛ ئەم وانەیە هێشتا نەکراوەتەوە.")
            return
        while source:
            end = min(3800, len(source))
            if end < len(source):
                boundary = source.rfind("\n", 0, end)
                if boundary > 0:
                    end = boundary
            await query.message.reply_text(source[:end])
            source = source[end:].lstrip("\n")
        await send_lesson_audio(query.message, base_dir, lesson_record)
        await query.message.reply_text(
            "⭐ کۆتایی وانەی ٥",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✅ تەواوکردنی وانە", callback_data=f"finish_{lesson_record['id']}")
            ]]),
        )
        await query.message.reply_text("📚 بۆ بینینی وانەکانی تر، منیووی کۆرسی ١ بکەرەوە.", reply_markup=menu_keyboard())
        return
    if action in {"practice", "assessment"}:
        if can_open is not None:
            try:
                manifest = load_manifest(base_dir)
                lesson_record = next(item for item in manifest["lessons"] if item["number"] == 5)
            except (OSError, ValueError, StopIteration):
                await query.message.reply_text("⚠️ زانیاریی وانەکە ئامادە نییە.")
                return
            if not can_open(query.from_user.id, lesson_record["id"]):
                await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە؛ ڕاهێنان و تاقیکردنەوەی ئەم وانەیە هێشتا نەکراونەتەوە.")
                return
        try:
            bank = load_arami_lesson5_interactions(base_dir)
            context.user_data["arami_lesson5_session"] = create_session(bank[action], action)
            context.user_data["arami_lesson5_message_id"] = None
        except (OSError, ValueError):
            logger.exception("Could not start Arami Lesson 5 interaction")
            await query.message.reply_text("⚠️ ڕاهێنان/تاقیکردنەوەی وانەی ٥ ئامادە نییە.")
            return
        await _send_question(query.message, context)
        return
    session = context.user_data.get("arami_lesson5_session")
    if not isinstance(session, dict) or query.message.message_id != context.user_data.get("arami_lesson5_message_id"):
        return
    if action.startswith("pick:"):
        raw = action.removeprefix("pick:")
        if not raw.isdigit():
            return
        try:
            selected = select_answer(session, int(raw))
        except (ValueError, TypeError):
            return
        question = current_question(session)
        rows = [[InlineKeyboardButton(("☑️ " if i == selected else "▫️ ") + option, callback_data=f"arami5:pick:{i}")] for i, option in enumerate(question["options"])]
        rows.append([InlineKeyboardButton("📨 ناردنی وەڵام", callback_data="arami5:submit")])
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
            correct = question["options"][question["answer_index"]]
            feedback = "✅ وەڵامت ڕاستە." if answer["correct"] else f"❌ وەڵامت هەڵەیە. وەڵامی ڕاست: {correct}"
        else:
            feedback = "✅ وەڵامەکەت تۆمار کرا."
        if session["closed"]:
            result = session_result(session)
            rows = []
            if session["mode"] == "practice" and result["missed"]:
                rows.append([InlineKeyboardButton("🔁 دووبارەکردنەوەی پرسیارە هەڵەکان", callback_data="arami5:retry")])
            rows.append([InlineKeyboardButton("↩️ گەڕانەوە بۆ وانەی ٥", callback_data="arami5:menu")])
            await query.edit_message_text(f"{feedback}\n\n🏁 کۆتایی هات\nئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪", reply_markup=InlineKeyboardMarkup(rows))
        else:
            await query.edit_message_text(feedback, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ پرسیاری دواتر", callback_data="arami5:next")]]))
        return
    if action == "next":
        if not session.get("closed"):
            await _send_question(query.message, context)
        return
    if action == "retry":
        try:
            retry = retry_missed(session)
        except ValueError:
            retry = None
        if retry is None:
            await query.message.reply_text("🌟 هیچ پرسیارێکی هەڵە نەماوە.")
            return
        context.user_data["arami_lesson5_session"] = retry
        context.user_data["arami_lesson5_message_id"] = None
        await _send_question(query.message, context)
