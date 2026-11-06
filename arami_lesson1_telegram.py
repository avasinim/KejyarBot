"""Telegram handlers for the isolated Course 1 Lesson 1 flow."""
import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from arami_course1_runtime import load_arami_lesson1_interactions, load_arami_lesson1_content
from arami_course1_telegram import load_manifest, _send_source, send_lesson_infographic
from arami_lesson1_interaction import (
    create_session, current_question, select_answer, submit_answer, session_result, retry_missed,
)

logger = logging.getLogger(__name__)


def menu_keyboard(assessment_available=False):
    rows = [
        [InlineKeyboardButton("📖 خوێندنەوەی وانەی ١", callback_data="arami1:lesson")],
        [InlineKeyboardButton("🎯 ڕاهێنانی وانەی ١", callback_data="arami1:practice")],
        [InlineKeyboardButton("📚 وانەی ٥ — پیتەکان و هاوتای لاتینی", callback_data="arami5:menu")],
        [InlineKeyboardButton("📚 هەموو ٢١ وانەی کۆرس ١", callback_data="aramiC:menu")],
    ]
    if assessment_available:
        rows.insert(2, [InlineKeyboardButton("📝 تاقیکردنەوەی وانەی ١", callback_data="arami1:assessment")])
    return InlineKeyboardMarkup(rows)


def _assessment_result(session, user_id, award_assessment, feedback=""):
    result = session_result(session)
    if award_assessment is not None:
        if award_assessment(user_id, "arami_course1_lesson_01"):
            session["assessment_reward_granted"] = True
    reward_note = (
        "\n\n🎁 +20 XP — یەکەم تەواوکردنی تاقیکردنەوە"
        if session.get("assessment_reward_granted") else ""
    )
    text = (
        f"{feedback}\n\n🏁 کۆتایی هات\n"
        f"ئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪{reward_note}"
    )
    rows = []
    if result["missed"]:
        rows.append([InlineKeyboardButton("🔁 دووبارەکردنەوەی پرسیارە هەڵەکان", callback_data="arami1:retry")])
    rows.append([InlineKeyboardButton("↩️ گەڕانەوە بۆ منیووی کۆرسی ١", callback_data="arami1:menu")])
    return text, InlineKeyboardMarkup(rows)


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


async def callback(update, context, base_dir, can_open=None, award_assessment=None, get_completed_lessons=None):
    query = update.callback_query
    action = query.data.removeprefix("arami1:")
    defer_ack = action.startswith("pick:") or action == "submit"
    if not defer_ack:
        await query.answer()

    if action == "menu":
        await query.message.reply_text(
            "📕 کۆرسی ١: ڕێنووسی سەرەتاییی کوردی — وانەی ١\n«پیتەکان و دەنگەکان»\n\n"
            "خوێندنەوە، ڕاهێنان یان تاقیکردنەوە هەڵبژێرە:",
            reply_markup=menu_keyboard(
                assessment_available=(
                    get_completed_lessons is not None
                    and "arami_course1_lesson_01" in set(get_completed_lessons(query.from_user.id))
                )
            ),
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
        await _send_source(
            query.message,
            'پوختەی وانەی ١',
            '## کورتەی وانە\n\n' + lesson['conclusion'],
        )
        # Lesson 1 uses this dedicated reader, so it must explicitly send
        # its approved PNG just like lessons routed through the shared reader.
        await send_lesson_infographic(query.message, lesson_record, base_dir=base_dir)
        await query.message.reply_text(
            '⭐ وانەکە تەواو بوو؛ بۆ تۆمارکردنی پێشکەوتنت دوگمەی خوارەوە هەڵبژێرە.',
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✅ تەواوکردنی وانە", callback_data=f"finish_{lesson_record['id']}")
            ]]),
        )
        await query.message.reply_text("📚 بۆ بینینی وانەکانی تر، منیووی کۆرسی ١ بکەرەوە.", reply_markup=menu_keyboard(
            assessment_available=(
                get_completed_lessons is not None
                and "arami_course1_lesson_01" in set(get_completed_lessons(query.from_user.id))
            )
        ))
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
        if action == "assessment" and get_completed_lessons is not None:
            if lesson_record["id"] not in set(get_completed_lessons(query.from_user.id)):
                await query.message.reply_text("🔒 سەرەتا وانەکە بخوێنەوە و تەواوی بکە؛ پاشان تاقیکردنەوەکە دەکرێتەوە.")
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
        if defer_ack:
            await query.answer()
        await query.message.reply_text("ℹ️ هیچ ڕاهێنانێکی وانەی ١ چالاک نییە.")
        return
    if query.message.message_id != context.user_data.get("arami_lesson1_message_id"):
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
        try:
            await query.answer()
        except Exception:
            session["selected_index"] = None
            logger.exception("Could not acknowledge Arami Lesson 1 answer selection")
            raise
        try:
            await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(rows))
        except Exception:
            session["selected_index"] = None
            logger.exception("Could not update Arami Lesson 1 answer-selection keyboard")
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
            correct_option = question["options"][question["answer_index"]]
            feedback = "✅ وەڵامت ڕاستە." if answer["correct"] else f"❌ وەڵامت هەڵەیە. وەڵامی ڕاست: {correct_option}"
        else:
            feedback = "✅ وەڵامەکەت وەرگیرا."
        if session["closed"]:
            if session["mode"] == "assessment":
                text, markup = _assessment_result(
                    session, query.from_user.id, award_assessment, feedback
                )
                await query.edit_message_text(text, reply_markup=markup)
            else:
                result = session_result(session)
                rows = []
                if result["missed"]:
                    rows.append([InlineKeyboardButton("🔁 دووبارەکردنەوەی پرسیارە هەڵەکان", callback_data="arami1:retry")])
                rows.append([InlineKeyboardButton("↩️ گەڕانەوە بۆ منیووی کۆرسی ١", callback_data="arami1:menu")])
                await query.edit_message_text(
                    f"{feedback}\n\n🏁 کۆتایی هات\nئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪",
                    reply_markup=InlineKeyboardMarkup(rows),
                )
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
            # Claim this next-question action before the first await so a
            # duplicate tap on the same feedback message cannot send twice.
            context.user_data["arami_lesson1_message_id"] = None
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
