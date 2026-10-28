import unittest

from course_quiz_review import (
    COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED,
    quiz_is_available,
)


class CourseOneQuizReviewGateTests(unittest.TestCase):
    def test_flagged_lessons_are_not_quiz_available(self):
        # Keep this explicit release gate aligned with the current source audit.
        # Do not make a quiz available merely to satisfy an older test expectation.
        expected = {
            "وانە_2", "وانە_4", "وانە_5", "وانە_6", "وانە_7",
            "وانە_8", "وانە_9", "وانە_10", "وانە_11", "وانە_12",
            "وانە_13", "وانە_14", "وانە_16", "وانە_17", "وانە_18",
            "وانە_19", "وانە_20", "وانە_21",
        }
        self.assertEqual(COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED, expected)
        for lesson in expected:
            with self.subTest(lesson=lesson):
                self.assertFalse(quiz_is_available(lesson))

    def test_only_unflagged_course_one_lessons_pass_this_gate(self):
        for number in (1, 3, 15, 22):
            with self.subTest(number=number):
                self.assertTrue(quiz_is_available(f"وانە_{number}"))

    def test_namespaced_courses_are_not_blocked_by_course_one_gate(self):
        self.assertTrue(quiz_is_available("daily_conversation_01"))
        self.assertTrue(quiz_is_available("unified_orthography_01"))


if __name__ == "__main__":
    unittest.main()
