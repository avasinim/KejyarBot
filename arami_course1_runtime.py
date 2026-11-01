"""Isolated runtime adapter for Arami Course 1; never touches Latin course data."""
import json
from pathlib import Path

from arami_lesson1_interaction import validate_question_bank, InvalidQuestionBank

COURSE_ID = "arami_orthography_foundations"
LESSON_1_ID = "arami_course1_lesson_01"
LESSON_1_SECTIONS = {
    "lesson1_alphabet_count",
    "lesson1_vowel_count",
    "lesson1_dual_letters",
    "lesson1_short_i",
}


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
    declared_total = manifest.get("course_total_lessons", manifest.get("course_size"))
    if (
        not isinstance(lessons, list)
        or not isinstance(declared_total, int)
        or isinstance(declared_total, bool)
        or declared_total < 1
        or len(lessons) != declared_total
    ):
        raise AramiCourseError("Arami Course 1 lesson list must match its declared total")
    ids = [lesson.get("id") for lesson in lessons if isinstance(lesson, dict)]
    if len(ids) != declared_total or len(set(ids)) != declared_total:
        raise AramiCourseError("Arami lessons need unique namespaced ids")
    if manifest.get("round") == 1 and declared_total != 21:
        raise AramiCourseError("Arami introductory orthography round must declare 21 lessons")
    first = next((lesson for lesson in lessons if lesson.get("id") == LESSON_1_ID), None)
    if first is None:
        raise AramiCourseError("Arami Lesson 1 is missing")
    # The content status records its delivery state and may evolve; immutability
    # is represented by the stable source marker, not the old status label.
    if first.get("content_source") != "user_supplied_immutable":
        raise AramiCourseError("user-supplied Lesson 1 content must remain immutable")
    if first.get("audio_asset") != "دەنگەکانی ئەلفبێ.ogg":
        raise AramiCourseError("Lesson 1 audio must use its user-confirmed recording")
    if first.get("audio_commit") != "5642e5310cc856f7bfd8c821086a9f2febe419e6":
        raise AramiCourseError("Lesson 1 audio commit does not match the user-confirmed recording")
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
    """Load and validate the five source-derived Lesson 1 practice/assessment items."""
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
        if len(questions) != 5:
            raise AramiCourseError(f"Lesson 1 {mode} must contain the five source exercise topics")
        section_ids = [item.get("section_id") for item in questions]
        if set(section_ids) != LESSON_1_SECTIONS:
            raise AramiCourseError(f"Lesson 1 {mode} must cover each of the four verified source sections")
        if section_ids.count("lesson1_short_i") != 2 or any(
            section_ids.count(section) != 1
            for section in LESSON_1_SECTIONS - {"lesson1_short_i"}
        ):
            raise AramiCourseError(f"Lesson 1 {mode} must contain exactly five source-derived items")
        if any(not isinstance(item.get("source_evidence"), str) or not item["source_evidence"].strip() for item in questions):
            raise AramiCourseError(f"Lesson 1 {mode} questions require source evidence")
        expected_answers = {
            "lesson1_alphabet_count": "٣٤ پیت",
            "lesson1_vowel_count": "٨ بزوێن",
            "lesson1_dual_letters": "(و) و (ی)",
            "lesson1_short_i": None,
        }
        for item in questions:
            expected = expected_answers[item["section_id"]]
            if expected is not None and item["options"][item["answer_index"]] != expected:
                raise AramiCourseError(f"Lesson 1 {mode} answer mismatch for {item['section_id']}")
        short_i = [item for item in questions if item["section_id"] == "lesson1_short_i"]
        if len(short_i) != 2:
            raise AramiCourseError(f"Lesson 1 {mode} must test both short-i facts")
        marker = next((item for item in short_i if item["type"] == "recognize" and "i" in item["options"]), None)
        special_letter = next((item for item in short_i if "پیتێکی تایبەت" in item["prompt"]), None)
        if marker is None or marker["options"][marker["answer_index"]] != "i":
            raise AramiCourseError(f"Lesson 1 {mode} must identify the short-i marker")
        if special_letter is None or special_letter["options"][special_letter["answer_index"]] not in {"نەخێر"}:
            raise AramiCourseError(f"Lesson 1 {mode} must preserve the no-special-letter fact")
    return bank


def load_arami_lesson1_content(base_dir):
    """Load the source-faithful lesson text separately from interaction data."""
    root = Path(base_dir).resolve()
    path = root / "course_data" / "arami_course1_lesson_01_content.json"
    try:
        content = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AramiCourseError("Arami Lesson 1 source text could not be loaded") from exc
    if content.get("course_id") != COURSE_ID or content.get("lesson_id") != LESSON_1_ID:
        raise AramiCourseError("lesson text belongs to a different course or lesson")
    sections = content.get("sections")
    if not isinstance(sections, list) or len(sections) != 8:
        raise AramiCourseError("Arami Lesson 1 must contain its eight original sections")
    if not isinstance(content.get("objectives"), list) or not content["objectives"]:
        raise AramiCourseError("Arami Lesson 1 objectives are missing")
    if not isinstance(content.get("conclusion"), str) or not content["conclusion"].strip():
        raise AramiCourseError("Arami Lesson 1 conclusion is missing")
    for section in sections:
        if not isinstance(section, dict) or not isinstance(section.get("title"), str):
            raise AramiCourseError("invalid Arami Lesson 1 source section")
        if not any(key in section for key in ("body", "table", "questions")):
            raise AramiCourseError("empty Arami Lesson 1 source section")
    return content
