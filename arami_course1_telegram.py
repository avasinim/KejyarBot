"""Telegram catalogue, source reader, and isolated quizzes for Arami Course 1."""
import json
import logging
import re
from pathlib import Path

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from arami_lesson1_interaction import (
    InvalidQuestionBank,
    create_session,
    current_question,
    retry_missed,
    select_answer,
    session_result,
    submit_answer,
    validate_question_bank,
)

logger = logging.getLogger(__name__)
COURSE_ID = "arami_orthography_foundations"
LESSON_COUNT = 20
QUESTION_BANK_FILE = "course_data/arami_course1_source_quiz_banks.json"


class AramiCourseTelegramError(ValueError):
    """Raised when a lesson source or question bank cannot safely be delivered."""


def load_manifest(base_dir):
    path = Path(base_dir).resolve() / "course_data" / "arami_course1_manifest.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AramiCourseTelegramError("Course 1 manifest is unavailable") from exc
    lessons = manifest.get("lessons")
    if manifest.get("course_id") != COURSE_ID or manifest.get("round") != 1:
        raise AramiCourseTelegramError("Unexpected Arami Course 1 manifest")
    if manifest.get("course_total_lessons") != LESSON_COUNT or not isinstance(lessons, list) or len(lessons) != LESSON_COUNT:
        raise AramiCourseTelegramError("Course 1 must contain exactly 20 registered lessons")
    numbers = [item.get("number") for item in lessons if isinstance(item, dict)]
    if sorted(numbers) != list(range(1, LESSON_COUNT + 1)):
        raise AramiCourseTelegramError("Course 1 lesson numbering is incomplete or duplicated")
    return manifest


def load_question_banks(base_dir):
    root = Path(base_dir).resolve()
    manifest = load_manifest(root)
    try:
        payload = json.loads((root / QUESTION_BANK_FILE).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AramiCourseTelegramError("Arami Course 1 question banks are unavailable") from exc
    if payload.get("course_id") != COURSE_ID or not isinstance(payload.get("lessons"), dict):
        raise AramiCourseTelegramError("Question bank belongs to another course or has invalid structure")
    manifest_by_number = {str(item["number"]): item for item in manifest["lessons"]}
    banks = {}
    for raw_number, bank in payload["lessons"].items():
        if not raw_number.isdigit() or str(int(raw_number)) not in manifest_by_number:
            raise AramiCourseTelegramError("Question bank has an invalid lesson number")
        lesson = manifest_by_number[str(int(raw_number))]
        if bank.get("source_file") != lesson.get("content_file"):
            raise AramiCourseTelegramError(f"Lesson {raw_number} question bank points to a different source")
        source_path = (root / bank["source_file"]).resolve()
        try:
            source_path.relative_to(root)
        except ValueError as exc:
            raise AramiCourseTelegramError("Question source path escapes project directory") from exc
        if not source_path.is_file():
            raise AramiCourseTelegramError(f"Lesson {raw_number} source is unavailable")
        for mode in ("practice", "assessment"):
            try:
                validate_question_bank(bank.get(mode))
            except (InvalidQuestionBank, TypeError) as exc:
                raise AramiCourseTelegramError(f"Lesson {raw_number} {mode} bank is invalid") from exc
            if any(not isinstance(item.get("source_evidence"), str) or not item["source_evidence"].strip() for item in bank[mode]):
                raise AramiCourseTelegramError(f"Lesson {raw_number} questions need source evidence")
        banks[int(raw_number)] = bank
    return banks


def course_menu_keyboard(manifest, interactive_lessons=()):
    interactive_lessons = set(interactive_lessons)
    rows = []
    for lesson in sorted(manifest["lessons"], key=lambda item: item["number"]):
        number = lesson["number"]
        title = str(lesson.get("title") or "وانە")
        label = f"{number}. {title}"
        if len(label) > 40:
            label = f"{number}. {title[:34]}…"
        read_callback = "arami1:lesson" if number == 1 else ("arami5:lesson" if number == 5 else f"aramiC:lesson:{number}")
        row = [InlineKeyboardButton(f"📖 {label}", callback_data=read_callback)]
        if number == 1:
            row.extend([
                InlineKeyboardButton("🎯 ڕاهێنان", callback_data="arami1:practice"),
                InlineKeyboardButton("📝 تاقیکردنەوە", callback_data="arami1:assessment"),
            ])
        elif number == 5:
            row.extend([
                InlineKeyboardButton("🎯 ڕاهێنان", callback_data="arami5:practice"),
                InlineKeyboardButton("📝 تاقیکردنەوە", callback_data="arami5:assessment"),
            ])
        elif number in interactive_lessons:
            row.extend([
                InlineKeyboardButton("🎯 ڕاهێنان", callback_data=f"aramiC:practice:{number}"),
                InlineKeyboardButton("📝 تاقیکردنەوە", callback_data=f"aramiC:assessment:{number}"),
            ])
        rows.append(row)
    return InlineKeyboardMarkup(rows)


def _plain_markdown(markdown):
    lines = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line or re.fullmatch(r"(?:---+|\*{3,}|_{3,})", line):
            continue
        if line.startswith("|") and line.endswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
                continue
            lines.append(" • ".join(cells))
            continue
        line = re.sub(r"^#{1,6}\s*", "", line)
        line = line.replace("**", "").replace("__", "").replace(chr(96), "")
        if line.startswith(">"):
            line = line[1:].strip()
        lines.append(line)
    return "\n".join(lines).strip()


def load_lesson_source(base_dir, lesson_number):
    if not isinstance(lesson_number, int) or isinstance(lesson_number, bool) or not 1 <= lesson_number <= LESSON_COUNT:
        raise AramiCourseTelegramError("Invalid lesson number")
    root = Path(base_dir).resolve()
    manifest = load_manifest(root)
    lesson = next(item for item in manifest["lessons"] if item["number"] == lesson_number)
    relative = lesson.get("content_file")
    if not isinstance(relative, str) or not relative.strip():
        raise AramiCourseTelegramError(f"Lesson {lesson_number} has no verified source file")
    source_path = (root / relative).resolve()
    try:
        source_path.relative_to(root)
    except ValueError as exc:
        raise AramiCourseTelegramError("Lesson source path escapes the project directory") from exc
    try:
        source = source_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise AramiCourseTelegramError(f"Lesson {lesson_number} source is unavailable") from exc
    if not source.strip():
        raise AramiCourseTelegramError(f"Lesson {lesson_number} source is empty")
    return lesson, source


async def _send_source(message, title, source):
    rendered = _plain_markdown(source)
    if not rendered:
        raise AramiCourseTelegramError("Lesson source has no readable text")
    await message.reply_text(f"📖 {title}")
    while rendered:
        end = min(3800, len(rendered))
        if end < len(rendered):
            boundary = rendered.rfind("\n", 0, end)
            if boundary > 0:
                end = boundary
        await message.reply_text(rendered[:end])
        rendered = rendered[end:].lstrip("\n")


def load_lesson_audio_files(base_dir, lesson):
    assets = lesson.get("audio_files", [])
    if not isinstance(assets, list):
        raise AramiCourseTelegramError("Lesson audio mapping must be a list")
    root = Path(base_dir).resolve()
    resolved = []
    for item in assets:
        if not isinstance(item, dict) or not isinstance(item.get("file"), str) or not isinstance(item.get("label"), str):
            raise AramiCourseTelegramError("Invalid lesson audio entry")
        path = (root / item["file"]).resolve()
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise AramiCourseTelegramError("Lesson audio path escapes project directory") from exc
        if path.suffix.lower() not in {".ogg", ".mp3"} or not path.is_file():
            raise AramiCourseTelegramError("Lesson audio file is unavailable: " + item["file"])
        resolved.append((path, item["label"]))
    return resolved


async def send_lesson_audio(message, base_dir, lesson):
    try:
        assets = load_lesson_audio_files(base_dir, lesson)
    except AramiCourseTelegramError:
        logger.exception("Invalid audio mapping for Arami Course 1 lesson %s", lesson.get("number"))
        await message.reply_text("⚠️ دەنگی وانەکە لە فایلەکانی پڕۆژەدا بە دروستی پەیوەست نەکراوە.")
        return False
    if not assets:
        await message.reply_text(f"⚠️ دەنگی تایبەتی وانەی {lesson.get('number', '')} هێشتا بە فایلێکی پشتڕاستکراوەوە نەبەستراوەتەوە.")
        return False
    for path, label in assets:
        try:
            with path.open("rb") as audio:
                await message.reply_voice(voice=audio, caption=f"🔊 {label}")
        except Exception:
            logger.exception("Could not send Arami Course 1 lesson audio %s", path.name)
            await message.reply_text(f"⚠️ ناردنی دەنگی «{label}» سەرکەوتوو نەبوو.")
            return False
    return True


async def _send_question(message, context, lesson_number):
    active = context.user_data.get("arami_course1_active")
    sessions = context.user_data.get("arami_course1_sessions", {})
    session = sessions.get(str(lesson_number))
    question = current_question(session) if isinstance(session, dict) else None
    if question is None:
        await message.reply_text("🏁 ئەم هەوڵە تەواو بوو.")
        return
    heading = "🎯 ڕاهێنان" if session["mode"] == "practice" else "📝 تاقیکردنەوە"
    rows = [
        [InlineKeyboardButton(option, callback_data=f"aramiC:pick:{lesson_number}:{i}")]
        for i, option in enumerate(question["options"])
    ]
    sent = await message.reply_text(
        f"{heading} — وانەی {lesson_number} — پرسیاری {session['index'] + 1}/{len(session['questions'])}\n\n{question['prompt']}",
        reply_markup=InlineKeyboardMarkup(rows),
    )
    context.user_data["arami_course1_active"] = {"lesson": lesson_number, "message_id": sent.message_id}


def _active_session(context, query, lesson_number):
    active = context.user_data.get("arami_course1_active")
    if not isinstance(active, dict) or active.get("lesson") != lesson_number:
        return None
    if query.message.message_id != active.get("message_id"):
        return None
    sessions = context.user_data.get("arami_course1_sessions", {})
    return sessions.get(str(lesson_number))


async def callback(update, context, base_dir):
    query = update.callback_query
    await query.answer()
    action = query.data.removeprefix("aramiC:")
    if action == "menu":
        try:
            manifest = load_manifest(base_dir)
            banks = load_question_banks(base_dir)
        except AramiCourseTelegramError:
            logger.exception("Could not load Arami Course 1 catalogue")
            await query.message.reply_text("⚠️ لیستی وانەکانی کۆرسی ١ ئامادە نییە.")
            return
        await query.message.reply_text(
            "📚 کۆرسی ١ — ڕێنووسی سەرەتاییی کوردی\nوانەیەک هەڵبژێرە:",
            reply_markup=course_menu_keyboard(manifest, banks),
        )
        return
    if action.startswith("lesson:"):
        raw = action.removeprefix("lesson:")
        if not raw.isdigit():
            return
        number = int(raw)
        try:
            lesson, source = load_lesson_source(base_dir, number)
            await _send_source(query.message, f"وانەی {number} — {lesson.get('title', '')}", source)
            await send_lesson_audio(query.message, base_dir, lesson)
        except AramiCourseTelegramError:
            logger.exception("Could not deliver Arami Course 1 Lesson %s", number)
            await query.message.reply_text(
                f"⚠️ سەرچاوەی پشتڕاستکراوی وانەی {number} لە فایلەکانی پڕۆژەدا نییە؛ "
                "ناوەڕۆک دروست ناکەین و شوێنی بەتاڵ بە سەرچاوەی تر پڕ ناکەین."
            )
            return
        manifest = load_manifest(base_dir)
        banks = load_question_banks(base_dir)
        await query.message.reply_text(
            f"⭐ کۆتایی خوێندنەوەی وانەی {number}.",
            reply_markup=course_menu_keyboard(manifest, banks),
        )
        return
    if action.startswith(("practice:", "assessment:")):
        mode, raw = action.split(":", 1)
        if not raw.isdigit():
            return
        number = int(raw)
        try:
            banks = load_question_banks(base_dir)
            bank = banks[number]
            session = create_session(bank[mode], mode)
        except (AramiCourseTelegramError, KeyError, ValueError):
            logger.exception("No verified %s bank for Arami Course 1 Lesson %s", mode, number)
            await query.message.reply_text(f"⚠️ {mode}ی سەرچاوەیی بۆ وانەی {number} ئامادە نییە.")
            return
        sessions = context.user_data.setdefault("arami_course1_sessions", {})
        sessions[str(number)] = session
        context.user_data["arami_course1_active"] = {"lesson": number, "message_id": None}
        await _send_question(query.message, context, number)
        return
    parts = action.split(":")
    if len(parts) < 2 or not parts[1].isdigit():
        return
    kind, raw_number = parts[0], parts[1]
    number = int(raw_number)
    session = _active_session(context, query, number)
    if not isinstance(session, dict):
        return
    if kind == "pick" and len(parts) == 3 and parts[2].isdigit():
        try:
            selected = select_answer(session, int(parts[2]))
        except (ValueError, TypeError):
            return
        question = current_question(session)
        rows = [
            [InlineKeyboardButton(("☑️ " if i == selected else "▫️ ") + option,
                                  callback_data=f"aramiC:pick:{number}:{i}")]
            for i, option in enumerate(question["options"])
        ]
        rows.append([InlineKeyboardButton("📨 ناردنی وەڵام", callback_data=f"aramiC:submit:{number}")])
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(rows))
        return
    if kind == "submit":
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
                rows.append([InlineKeyboardButton("🔁 دووبارەکردنەوەی پرسیارە هەڵەکان", callback_data=f"aramiC:retry:{number}")])
            rows.append([InlineKeyboardButton("📚 گەڕانەوە بۆ لیستی وانەکان", callback_data="aramiC:menu")])
            await query.edit_message_text(
                f"{feedback}\n\n🏁 کۆتایی هات\nئەنجام: {result['correct']}/{result['total']} — {result['percentage']}٪",
                reply_markup=InlineKeyboardMarkup(rows),
            )
        else:
            await query.edit_message_text(
                feedback,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("➡️ پرسیاری دواتر", callback_data=f"aramiC:next:{number}")
                ]]),
            )
        return
    if kind == "next":
        if not session.get("closed"):
            await _send_question(query.message, context, number)
        return
    if kind == "retry":
        try:
            retry = retry_missed(session)
        except ValueError:
            retry = None
        if retry is None:
            await query.message.reply_text("🌟 هیچ پرسیارێکی هەڵە نەماوە.")
            return
        context.user_data.setdefault("arami_course1_sessions", {})[str(number)] = retry
        context.user_data["arami_course1_active"] = {"lesson": number, "message_id": None}
        await _send_question(query.message, context, number)
