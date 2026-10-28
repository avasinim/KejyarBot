import unittest

from course_quiz_review import (
    COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED,
    quiz_is_available,
)


class CourseOneQuizReviewGateTests(unittest.TestCase):
    def test_flagged_lessons_are_not_quiz_available(self):
        expected = {
            "وانە_2", "وانە_4", "وانە_8", "وانە_13", "وانە_14",
            "وانە_16", "وانە_18", "وانە_19", "وانە_21",
        }
        self.assertEqual(COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED, expected)
        for lesson in expected:
            with self.subTest(lesson=lesson):
                self.assertFalse(quiz_is_available(lesson))

    def test_unflagged_course_one_lessons_remain_quiz_available(self):
        for number in (1, 3, 5, 6, 7, 9, 10, 11, 12, 15, 17, 20, 22):
            with self.subTest(number=number):
                self.assertTrue(quiz_is_available(f"وانە_{number}"))

    def test_namespaced_courses_are_not_blocked_by_course_one_gate(self):
        self.assertTrue(quiz_is_available("daily_conversation_01"))
        self.assertTrue(quiz_is_available("unified_orthography_01"))


if __name__ == "__main__":
    unittest.main()
