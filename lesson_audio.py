"""Resolve dedicated prerecorded audio assets for individual lessons."""
from pathlib import Path


class LessonAudioError(ValueError):
    """Lesson audio metadata is absent, unsafe, or unavailable."""


def resolve_lesson_audio_path(base_dir, lesson_data):
    if not isinstance(lesson_data, dict):
        raise LessonAudioError("lesson metadata is missing")
    asset = lesson_data.get("lesson_audio_asset")
    if not isinstance(asset, str) or not asset.strip():
        raise LessonAudioError("lesson-specific audio is required")

    root = Path(base_dir).resolve()
    path = (root / asset).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise LessonAudioError("audio path escapes the project directory") from exc

    if path.suffix.lower() not in {".ogg", ".mp3"}:
        raise LessonAudioError("lesson audio must be an OGG or MP3 file")
    if not path.is_file():
        raise LessonAudioError("lesson audio file does not exist")
    return path
