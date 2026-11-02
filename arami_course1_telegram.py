"""Telegram catalogue and source reader for Arami Course 1 (21 lessons)."""
import json
import logging
import re
from pathlib import Path

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

logger = logging.getLogger(__name__)
COURSE_ID = "arami_orthography_foundations"
LESSON_COUNT = 21


class AramiCourseTelegramError(ValueError):
    """Raised when a lesson source cannot safely be delivered."""


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
        raise AramiCourseTelegramError("Course 1 must contain exactly 21 registered lessons")
    numbers = [item.get("number") for item in lessons if isinstance(item, dict)]
    if sorted(numbers) != list(range(1, LESSON_COUNT + 1)):
        raise AramiCourseTelegramError("Course 1 lesson numbering is incomplete or duplicated")
    return manifest


def course_menu_keyboard(manifest):
    lessons = sorted(manifest["lessons"], key=lambda item: item["number"])
    rows, row = [], []
    for lesson in lessons:
        number = lesson["number"]
        title = str(lesson.get("title") or "وانە")
        label = f"{number}. {title}"
        if len(label) > 48:
            label = f"{number}. {title[:42]}…"
        row.append(InlineKeyboardButton(label, callback_data=f"aramiC:lesson:{number}"))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
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
        line = line.replace("**", "").replace("__", "").replace("\`", "")
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


async def callback(update, context, base_dir):
    query = update.callback_query
    await query.answer()
    action = query.data.removeprefix("aramiC:")
    if action == "menu":
        try:
            manifest = load_manifest(base_dir)
        except AramiCourseTelegramError:
            logger.exception("Could not load Arami Course 1 catalogue")
            await query.message.reply_text("⚠️ لیستی ٢١ وانەکە ئامادە نییە.")
            return
        await query.message.reply_text(
            "📚 کۆرسی ١ — ڕێنووسی سەرەتاییی کوردی\nوانەیەک هەڵبژێرە بۆ خوێندنەوە:",
            reply_markup=course_menu_keyboard(manifest),
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
        except AramiCourseTelegramError:
            logger.exception("Could not deliver Arami Course 1 Lesson %s", number)
            await query.message.reply_text(
                f"⚠️ سەرچاوەی پشتڕاستکراوی وانەی {number} لە فایلەکانی پڕۆژەدا نییە؛ "
                "ناوەڕۆک دروست ناکەین و شوێنی بەتاڵ بە سەرچاوەی تر پڕ ناکەین."
            )
            return
        manifest = load_manifest(base_dir)
        await query.message.reply_text(
            f"⭐ کۆتایی خوێندنەوەی وانەی {number}.",
            reply_markup=course_menu_keyboard(manifest),
        )
