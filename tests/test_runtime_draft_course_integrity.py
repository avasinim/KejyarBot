"""Runtime integrity checks for the isolated multi-course candidate.

These tests intentionally verify that draft material is loaded for integration
checks without making it available to learners.
"""
import unittest

import bot


class RuntimeDraftCourseIntegrityTests(unittest.TestCase):
    def test_all_70_manifest_lessons_are_loaded_without_id_collisions(self):
        expected = {
            "orthography_basic": [f"وانە_{n}" for n in range(1, 23)],
            "daily_conversation": [f"daily_conversation_{n:02d}" for n in range(1, 37)],
            "unified_orthography": [f"unified_orthography_{n:02d}" for n in range(1, 13)],
        }
        self.assertEqual(len(bot.LESSON_DATA), 70)
        for course_id, lesson_ids in expected.items():
            with self.subTest(course=course_id):
                self.assertEqual(bot.COURSE_LESSON_ORDER[course_id], lesson_ids)
                self.assertTrue(all(lesson_id in bot.LESSON_DATA for lesson_id in lesson_ids))
        self.assertEqual(len(bot.LESSON_DATA), len(set(bot.LESSON_DATA)))

    def test_draft_course_lessons_and_quizzes_are_loaded_but_review_gated(self):
        for course_id in ("daily_conversation", "unified_orthography"):
            with self.subTest(course=course_id):
                self.assertFalse(bot.course_is_active(course_id))
                for lesson_id in bot.COURSE_LESSON_ORDER[course_id]:
                    self.assertFalse(bot.can_open(12345, lesson_id))
                    self.assertIn("draft_editorial_review", bot.LESSON_DATA[lesson_id]["review_status"])
                    self.assertTrue(bot.LESSON_DATA[lesson_id]["content"].strip())
                    questions = bot.QUIZ_DATA[lesson_id]
                    self.assertTrue(questions)
                    self.assertTrue(all(q.get("question") and q.get("explanation") for q in questions))

    def test_course_four_remains_planned_and_empty(self):
        course = next(course for course in bot.COURSES if course["id"] == "grammar")
        self.assertEqual(course["status"], "planned")
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], [])


if __name__ == "__main__":
    unittest.main()
