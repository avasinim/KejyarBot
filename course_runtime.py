"""Pure helpers for keeping lesson identity and unlocking scoped to one course.

The legacy Course 1 keys are intentionally preserved. New courses use namespaced
keys, e.g. conversation_01 and unified_01, to avoid collisions in SQLite progress.
"""
import re


LEGACY_COURSE_ID = "orthography_basic"
LEGACY_LESSON_PREFIX = "وانە_"


def lesson_key(course_id, number):
    """Return a stable key; never rename existing Course 1 progress keys."""
    if not isinstance(number, int) or isinstance(number, bool) or number < 1:
        raise ValueError("lesson number must be a positive integer")
    if course_id == LEGACY_COURSE_ID:
        return f"{LEGACY_LESSON_PREFIX}{number}"
    slug = re.sub(r"[^a-z0-9]+", "_", str(course_id).lower()).strip("_")
    if not slug:
        raise ValueError("course id must contain a usable identifier")
    return f"{slug}_{number:02d}"


def can_open_lesson(lesson_ids, completed_ids, lesson_id):
    """Unlock only the first lesson or a lesson whose predecessor is complete."""
    ordered = list(lesson_ids)
    if lesson_id not in ordered:
        return False
    index = ordered.index(lesson_id)
    if index == 0:
        return True
    return ordered[index - 1] in set(completed_ids)


def visible_course_lessons(course, lesson_data):
    """Return only manifest lessons actually loaded by the runtime."""
    return [
        lesson_id for lesson_id in course.get("lesson_ids", [])
        if lesson_id in lesson_data
    ]
