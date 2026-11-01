"""Isolated runtime adapter for Arami Course 1; never touches Latin course data."""
import json
from pathlib import Path

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
