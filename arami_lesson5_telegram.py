"""Telegram delivery for Arami Course 1 Lesson 5; isolated from Lesson 1."""
import logging
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from arami_course1_runtime import load_arami_lesson5_interactions, load_arami_lesson5_source
from arami_course1_telegram import load_manifest, _send_source
from arami_lesson1_interaction import create_session, current_question, select_answer, submit_answer, session_result, retry_missed
logger = logging.getLogger(__name__)

def menu_keyboard(assessment_available=False):
    rows = [
        [InlineKeyboardButton("📖 خوێندنەوەی وانەی ٥", callback_data="arami5:lesson")],
        [InlineKeyboardButton("🎯 ڕاهێنانی وانەی ٥", callback_data="arami5:practice")],
        [InlineKeyboardButton("📚 هەموو ٢١ وانەی کۆرس ١", callback_data="aramiC:menu")],
    ]
    if assessment_available:
        rows.insert(2, [InlineKeyboardButton("📝 تاقیکردنەوەی وانەی ٥", callback_data="arami5:assessment")])
    return InlineKeyboardMarkup(rows)

def _assessment_result(session, user_id, award_assessment, feedback=""):
    result = session_result(session)
    if award_assessment is not None:
        if award_assessment(user_id, "arami_course1_lesson_05"):
            session["assessment_reward_granted"] = True
    reward_note = (
        "\n\n🎁 +20 XP — یەکەم تەواوکردنی تاقیکردنەوە"
        if session.get("assessment_reward_granted") else ""
    )
    rows = [[InlineKeyboardButton("↩️ گەڕانەوە بۆ وانەی ٥", callback_data="arami5:menu")]]
    text = (
        f"{feedback}\n\n🏁 کۆتایی هات\n"
        f"ئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪{reward_note}"
    )
    return text, InlineKeyboardMarkup(rows)


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
    if (
        context.user_data.get("arami_lesson5_session") is session
        and context.user_data.get("arami_lesson5_message_id") is None
    ):
        context.user_data["arami_lesson5_message_id"] = sent.message_id

async def callback(update, context, base_dir, can_open=None, award_assessment=None, get_completed_lessons=None):
    query = update.callback_query
    action = query.data.removeprefix("arami5:")
    defer_ack = action.startswith("pick:") or action == "submit"
    if not defer_ack:
        await query.answer()
    if action == "menu":
        await query.message.reply_text("وانەی ٥ — هەڵبژاردنی خوێندنەوە یان تاقیکردنەوە:", reply_markup=menu_keyboard(
            assessment_available=(
                get_completed_lessons is not None
                and "arami_course1_lesson_05" in set(get_completed_lessons(query.from_user.id))
            )
        ))
        return
    if action == "lesson":
        try:
            source = load_arami_lesson5_source(base_dir)
            manifest = load_manifest(base_dir)
            lesson_record = next(item for item in manifest["lessons"] if item["number"] == 5)
        except (OSError, ValueError, StopIteration):
            logger.exception("Could not load Arami Lesson 5 source")
            await query.message.reply_text("⚠️ دەقی ڕەسەنی وانەی ٥ ئامادە نییە.")
            return
        if can_open is not None and not can_open(query.from_user.id, lesson_record["id"]):
            await query.message.reply_text("🔒 سەرەتا وانەی پێشووتر تەواو بکە؛ ئەم وانەیە هێشتا نەکراوەتەوە.")
            return
        await _send_source(
            query.message,
            f"وانەی ٥ — {lesson_record.get('title', 'پیتەکان و هاوتای لاتینی')}",
            source,
        )
        await query.message.reply_text(
            "⭐ کۆتایی وانەی ٥",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✅ تەواوکردنی وانە", callback_data=f"finish_{lesson_record['id']}")
            ]]),
        )
        await query.message.reply_text("📚 بۆ بینینی وانەکانی تر، منیووی کۆرسی ١ بکەرەوە.", reply_markup=menu_keyboard(
            assessment_available=(
                get_completed_lessons is not None
                and "arami_course1_lesson_05" in set(get_completed_lessons(query.from_user.id))
            )
        ))
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
        if action == "assessment" and get_completed_lessons is not None:
            if lesson_record["id"] not in set(get_completed_lessons(query.from_user.id)):
                await query.message.reply_text("🔒 سەرەتا وانەکە بخوێنەوە و تەواوی بکە؛ پاشان تاقیکردنەوەکە دەکرێتەوە.")
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
        if defer_ack:
            await query.answer()
        return
    if action.startswith("pick:"):
        raw = action.removeprefix("pick:")
        if not raw.isdigit():
            await query.answer()
            return
        try:
            selected = select_answer(session, int(raw))
        except (ValueError, TypeError):
            await query.answer()
            return
        question_index = session["index"]
        question = current_question(session)
        try:
            await query.answer()
        except Exception:
            session["selected_index"] = None
            logger.exception("Could not acknowledge Arami Lesson 5 answer selection")
            raise
        rows = [[InlineKeyboardButton(("☑️ " if i == selected else "▫️ ") + option, callback_data=f"arami5:pick:{i}")] for i, option in enumerate(question["options"])]
        rows.append([InlineKeyboardButton("📨 ناردنی وەڵام", callback_data="arami5:submit")])
        if (
            context.user_data.get("arami_lesson5_session") is not session
            or context.user_data.get("arami_lesson5_message_id") != query.message.message_id
            or session.get("index") != question_index
            or session.get("selected_index") != selected
        ):
            return
        try:
            await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(rows))
        except Exception:
            session["selected_index"] = None
            logger.exception("Could not update Arami Lesson 5 answer-selection keyboard")
            raise
        return
    if action == "submit" and session.get("closed") and session.get("mode") == "assessment":
        await query.answer()
        result_text, result_markup = _assessment_result(
            session, query.from_user.id, award_assessment,
            "🏁 تاقیکردنەوەکەت پێشتر تەواو بوو."
        )
        await query.edit_message_text(result_text, reply_markup=result_markup)
        return
    if action == "submit":
        question = current_question(session)
        try:
            answer = submit_answer(session)
        except (ValueError, TypeError):
            await query.answer()
            await query.message.reply_text("سەرەتا وەڵامێک هەڵبژێرە.")
            return
        await query.answer()
        if session["mode"] == "practice":
            correct = question["options"][question["answer_index"]]
            feedback = "✅ وەڵامت ڕاستە." if answer["correct"] else f"❌ وەڵامت هەڵەیە. وەڵامی ڕاست: {correct}"
        else:
            feedback = "✅ وەڵامەکەت وەرگیرا."
        if session["closed"]:
            result = session_result(session)
            if session["mode"] == "assessment":
                text, markup = _assessment_result(
                    session, query.from_user.id, award_assessment, feedback
                )
            else:
                rows = []
                if result["missed"]:
                    rows.append([InlineKeyboardButton("🔁 دووبارەکردنەوەی پرسیارە هەڵەکان", callback_data="arami5:retry")])
                rows.append([InlineKeyboardButton("↩️ گەڕانەوە بۆ وانەی ٥", callback_data="arami5:menu")])
                text = f"{feedback}\n\n🏁 کۆتایی هات\nئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪"
                markup = InlineKeyboardMarkup(rows)
            await query.edit_message_text(text, reply_markup=markup)
        else:
            await query.edit_message_text(feedback, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ پرسیاری دواتر", callback_data="arami5:next")]]))
        return
    if action == "next":
        if not session.get("closed"):
            # Claim this next-question action before the first await so a
            # duplicate tap on the same feedback message cannot send twice.
            context.user_data["arami_lesson5_message_id"] = None
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
