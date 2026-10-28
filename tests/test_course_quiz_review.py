import unittest

from course_quiz_review import (
    COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED,
    quiz_is_available,
)


class CourseOneQuizReviewTests(unittest.TestCase):
    def test_all_flagged_lessons_are_unavailable(self):
        for lesson_key in COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED:
            with self.subTest(lesson_key=lesson_key):
                self.assertFalse(quiz_is_available(lesson_key))

    def test_lesson_20_is_flagged_for_source_review(self):
        self.assertIn("وانە_20", COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
        self.assertFalse(quiz_is_available("وانە_20"))

    def test_duplicate_title_lesson_12_is_flagged_for_review(self):
        self.assertIn("وانە_12", COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
        self.assertFalse(quiz_is_available("وانە_12"))

    def test_repetitive_quiz_sets_are_flagged_for_review(self):
        for lesson_key in ("وانە_5", "وانە_7"):
            with self.subTest(lesson_key=lesson_key):
                self.assertIn(lesson_key, COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
                self.assertFalse(quiz_is_available(lesson_key))

    def test_repetitive_question_patterns_are_flagged(self):
        for lesson_key in ("وانە_4", "وانە_6", "وانە_9", "وانە_10", "وانە_11", "وانە_17"):
            with self.subTest(lesson_key=lesson_key):
                self.assertIn(lesson_key, COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
                self.assertFalse(quiz_is_available(lesson_key))

    def test_unflagged_lesson_remains_available(self):
        self.assertTrue(quiz_is_available("وانە_1"))
        self.assertTrue(quiz_is_available("وانە_22"))

    def test_review_gate_does_not_match_partial_lesson_keys(self):
        self.assertTrue(quiz_is_available("وانە_200"))
        self.assertTrue(quiz_is_available("daily_conversation_20"))


if __name__ == "__main__":
    unittest.main()
