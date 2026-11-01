"""Isolated runtime adapter for Arami Course 1; never touches Latin course data."""
import json
from pathlib import Path

from arami_lesson1_interaction import validate_question_bank, InvalidQuestionBank

COURSE_ID = "arami_orthography_foundations"
LESSON_1_ID = "arami_course1_lesson_01"


class AramiCourseError(ValueError):
    """Arami course manifest is invalid or incomplete."""


def load_arami_course1(base_dir):
    """Load the separately namespaced Arami manifest and validate its structure."""
    path = Path(base_dir).resolve() / "course_data" / "arami_course1_manifest.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AramiCourseError("Arami Course 1 manifest could not be loaded") from exc
    if manifest.get("course_id") != COURSE_ID:
        raise AramiCourseError("unexpected Arami course id")
    lessons = manifest.get("lessons")
    if not isinstance(lessons, list) or len(lessons) != 4:
        raise AramiCourseError("Arami Course 1 must declare exactly four lessons")
    ids = [lesson.get("id") for lesson in lessons if isinstance(lesson, dict)]
    if len(ids) != 4 or len(set(ids)) != 4:
        raise AramiCourseError("Arami lessons need four unique namespaced ids")
    first = lessons[0]
    if first.get("id") != LESSON_1_ID:
        raise AramiCourseError("Arami Lesson 1 id mismatch")
    if first.get("content_status") != "do_not_edit":
        raise AramiCourseError("user-supplied Lesson 1 content must remain immutable")
    if first.get("audio_asset") != "دەنگەکانی ئەلفبێ.ogg":
        raise AramiCourseError("Lesson 1 audio must use its user-confirmed recording")
    if manifest.get("safety", {}).get("separate_from_latin_courses") is not True:
        raise AramiCourseError("Arami and Latin courses must remain isolated")
    return manifest


def get_arami_lesson1_audio_path(base_dir, manifest=None):
    """Return only the explicitly assigned Arami Lesson 1 recording path."""
    manifest = manifest or load_arami_course1(base_dir)
    lessons = manifest.get("lessons", [])
    lesson = next((item for item in lessons if item.get("id") == LESSON_1_ID), None)
    if lesson is None:
        raise AramiCourseError("Arami Lesson 1 is missing")
    if lesson.get("audio_status") != "user_confirmed_asset_repository_root":
        raise AramiCourseError("Arami Lesson 1 audio assignment is not confirmed")
    root = Path(base_dir).resolve()
    audio = (root / lesson["audio_asset"]).resolve()
    try:
        audio.relative_to(root)
    except ValueError as exc:
        raise AramiCourseError("Lesson 1 audio path escapes project root") from exc
    if audio.suffix.lower() != ".ogg" or not audio.is_file():
        raise AramiCourseError("confirmed Lesson 1 OGG recording is unavailable")
    return audio


def load_arami_lesson1_interactions(base_dir):
    """Load and validate only the explicitly approved Lesson 1 practice/assessment bank."""
    root = Path(base_dir).resolve()
    bank_path = root / "course_data" / "arami_course1_lesson_01_interactions.json"
    try:
        bank = json.loads(bank_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AramiCourseError("Arami Lesson 1 interaction bank could not be loaded") from exc
    if bank.get("course_id") != COURSE_ID or bank.get("lesson_id") != LESSON_1_ID:
        raise AramiCourseError("interaction bank belongs to a different course or lesson")
    if bank.get("source_correction", {}).get("lesson_1_vowel_count") != 8:
        raise AramiCourseError("Lesson 1 must preserve the user-confirmed count of eight vowels")
    for mode in ("practice", "assessment"):
        questions = bank.get(mode)
        try:
            validate_question_bank(questions)
        except (InvalidQuestionBank, TypeError) as exc:
            raise AramiCourseError(f"invalid Lesson 1 {mode} bank") from exc
        vowel_items = [
            item for item in questions
            if item.get("section_id") == "lesson1_vowel_count"
        ]
        if len(vowel_items) != 1:
            raise AramiCourseError(f"Lesson 1 {mode} must contain exactly one verified vowel-count item")
        item = vowel_items[0]
        if item["options"][item["answer_index"]] != "٨ بزوێن":
            raise AramiCourseError(f"Lesson 1 {mode} vowel-count answer must be eight")
        color_items = [
            item for item in questions
            if item.get("section_id") == "lesson1_chart_categories"
        ]
        if len(color_items) != 1:
            raise AramiCourseError(f"Lesson 1 {mode} must contain exactly one chart color-key item")
        color_item = color_items[0]
        if color_item["options"][color_item["answer_index"]] != "سوور":
            raise AramiCourseError(f"Lesson 1 {mode} chart color-key answer must remain red")
        if any(not isinstance(item.get("source_evidence"), str) or not item["source_evidence"].strip() for item in questions):
            raise AramiCourseError(f"Lesson 1 {mode} questions require source evidence")
    return bank
