"""Cross-course launch readiness and fail-closed academic review gates."""
import unittest

import bot
from arami_course1_telegram import load_manifest as load_arami_manifest


class LaunchReadinessMatrixTests(unittest.TestCase):
    def test_all_six_active_courses_have_203_registered_lessons(self):
        active = [
            course for course in bot.COURSES
            if course.get("status") == "active"
        ]
        self.assertEqual(len(active), 6)
        self.assertEqual(
            sum(len(bot.COURSE_LESSON_ORDER[course["id"]]) for course in active),
            203,
        )
        self.assertEqual(
            sum(len(bot.COURSE_LESSON_ORDER[course["id"]]) for course in active),
            len(set(
                lesson_id
                for course in active
                for lesson_id in bot.COURSE_LESSON_ORDER[course["id"]]
            )),
        )

    def test_exactly_thirty_lessons_are_academically_approved(self):
        active_ids = [
            lesson_id
            for course in bot.COURSES
            if course.get("status") == "active"
            for lesson_id in bot.COURSE_LESSON_ORDER[course["id"]]
        ]
        approved = [lesson_id for lesson_id in active_ids if not bot.lesson_is_beta_review(lesson_id)]
        review_only = [lesson_id for lesson_id in active_ids if bot.lesson_is_beta_review(lesson_id)]

        self.assertEqual(len(active_ids), 203)
        self.assertEqual(len(approved), 30)
        self.assertEqual(len(review_only), 173)
        self.assertEqual(
            sum(not bot.lesson_is_beta_review(lesson_id)
                for lesson_id in bot.COURSE_LESSON_ORDER["grammar"]),
            30,
        )

    def test_course4_lesson13_remains_review_only_and_quiz_locked(self):
        lesson_id = "grammar_13"
        self.assertIn(lesson_id, bot.COURSE_LESSON_ORDER["grammar"])
        self.assertTrue(bot.lesson_is_pending_review(lesson_id))
        self.assertTrue(bot.lesson_is_beta_review(lesson_id))
        self.assertFalse(bot.lesson_quiz_is_available(lesson_id))

    def test_no_review_only_lesson_can_start_an_official_quiz(self):
        review_only = [
            lesson_id
            for course in bot.COURSES
            if course.get("status") == "active"
            for lesson_id in bot.COURSE_LESSON_ORDER[course["id"]]
            if bot.lesson_is_beta_review(lesson_id)
        ]
        self.assertEqual(len(review_only), 173)
        for lesson_id in review_only:
            with self.subTest(lesson_id=lesson_id):
                self.assertFalse(bot.lesson_quiz_is_available(lesson_id))

    def test_arami_manifest_has_no_implicit_academic_approval(self):
        manifest = load_arami_manifest(bot.BASE_DIR)
        self.assertEqual(len(manifest["lessons"]), 21)
        self.assertFalse(any(
            item.get("status") in {
                "scientific_review_complete",
                "scientific_review_complete_with_qualified_notes",
                "approved",
            }
            for item in manifest["lessons"]
        ))


if __name__ == "__main__":
    unittest.main()
