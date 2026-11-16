"""Exact course-and-lesson image routes shared by Telegram lesson readers."""
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

SHARED_LESSON_IMAGE_ROUTES = {
    (
        "arami_orthography_foundations",
        "arami_course1_lesson_05",
    ): "assets/lessons/kejyar_lesson5_kurdish_letters_v2.png",
    (
        "kurmanji_latin_orthography",
        "kurmanji_latin_orthography_01",
    ): "assets/lessons/kejyar_lesson5_kurdish_letters_v2.png",
}


def shared_lesson_image_path(base_dir, course_id, lesson_id):
    """Resolve an approved shared image only for an exact course/lesson pair."""
    relative_path = SHARED_LESSON_IMAGE_ROUTES.get((course_id, lesson_id))
    if relative_path is None:
        return None
    root = Path(base_dir).resolve()
    path = (root / relative_path).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        return None
    return path if path.is_file() else None


async def send_shared_lesson_image(message, course_id, lesson_id, base_dir=None):
    """Send an exact-route image; missing files or Telegram errors stay nonfatal."""
    root = Path(base_dir).resolve() if base_dir is not None else Path(__file__).resolve().parent
    path = shared_lesson_image_path(root, course_id, lesson_id)
    if path is None:
        return False
    try:
        with path.open("rb") as image:
            await message.reply_photo(
                photo=image,
                caption="🖼️ وێنەی فێرکاری",
            )
    except Exception:
        logger.exception(
            "Could not send shared lesson image for course=%s lesson=%s",
            course_id,
            lesson_id,
        )
        return False
    return True
