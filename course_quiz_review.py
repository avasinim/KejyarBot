"""Editorial availability rules for quizzes awaiting source review.

This module deliberately does not disable lessons or change course activation.
"""
COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED = frozenset({
    "وانە_2",
    "وانە_4",
    "وانە_8",
    "وانە_12",
    "وانە_13",
    "وانە_14",
    "وانە_16",
    "وانە_18",
    "وانە_19",
    "وانە_20",
    "وانە_21",
})


def quiz_is_available(lesson_key: str) -> bool:
    """Return False for Course 1 quizzes flagged for source/content review."""
    return lesson_key not in COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED
