"""Course-scoped infographic asset lookup.

Course 3 images must be explicitly namespaced so its lesson 1 can never
accidentally pick up the daily-conversation lesson-01 SVG.
"""
from pathlib import Path

COURSE3_ID = "unified_orthography"


def course_infographic_path(lesson_id, lesson, base_dir):
    """Return an existing PNG for a reviewed, namespaced course lesson.

    SVG is intentionally not returned because Telegram's send_photo expects a
    raster image. Missing artwork is a normal state while visuals are being
    authored and must not prevent the lesson text from being delivered.
    """
    if not isinstance(lesson, dict) or lesson.get("course_id") != COURSE3_ID:
        return None
    number = lesson.get("source_number")
    if not isinstance(number, int) or isinstance(number, bool) or not 1 <= number <= 66:
        return None
    path = Path(base_dir) / "assets" / "infographics" / f"course3-lesson-{number:02d}.png"
    return path if path.is_file() else None
