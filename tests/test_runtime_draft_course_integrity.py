"""Runtime integrity checks for the isolated multi-course candidate.

These tests intentionally verify that draft material is loaded for integration
checks without making it available to learners.
"""
import unittest
from unittest.mock import patch

import bot


class RuntimeDraftCourseIntegrityTests(unittest.TestCase):
    def test_all_82_manifest_lessons_are_loaded_without_id_collisions(self):
        expected = {
            "orthography_basic": [f"وانە_{n}" for n in range(1, 23)],
            "daily_conversation": [f"daily_conversation_{n:02d}" for n in range(1, 49)],
            "unified_orthography": [f"unified_orthography_{n:02d}" for n in range(1, 13)],
        }
        self.assertEqual(len(bot.LESSON_DATA), 82)
        for course_id, lesson_ids in expected.items():
            with self.subTest(course=course_id):
                self.assertEqual(bot.COURSE_LESSON_ORDER[course_id], lesson_ids)
                self.assertTrue(all(lesson_id in bot.LESSON_DATA for lesson_id in lesson_ids))
        self.assertEqual(len(bot.LESSON_DATA), len(set(bot.LESSON_DATA)))

    def test_original_lesson_content_does_not_repeat_course_or_decorative_headers(self):
        for lesson_id in bot.COURSE_LESSON_ORDER["orthography_basic"]:
            with self.subTest(lesson=lesson_id):
                content = bot.LESSON_DATA[lesson_id]["content"]
                self.assertNotIn("📚 کۆرسی ١:", content)
                self.assertNotIn("╭━━━━━━━━━━━━━━━━━━╮", content)
                self.assertNotIn("کەویار", content)
        lesson = bot.LESSON_DATA["وانە_1"]
        self.assertIn("ئەلفبێی زمانی کوردی", lesson["content"])
        self.assertIn("تەواوکردنی وانە", lesson["content"])

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

    def test_all_48_conversation_lessons_stay_locked_even_with_fake_completion(self):
        # A stale database row or a crafted callback must not bypass the
        # course-level activation gate, even if every draft lesson appears done.
        all_draft_ids = bot.COURSE_LESSON_ORDER["daily_conversation"]
        self.assertEqual(len(all_draft_ids), 48)
        with patch.object(bot, "get_completed_lessons", return_value=all_draft_ids):
            for lesson_id in all_draft_ids:
                with self.subTest(lesson=lesson_id):
                    self.assertFalse(bot.can_open(12345, lesson_id))

    def test_progress_and_quiz_catalog_lessons_are_scoped_to_active_courses(self):
        active_lessons = bot.active_course_lessons()
        self.assertEqual(active_lessons, bot.COURSE_LESSON_ORDER["orthography_basic"])
        self.assertTrue(all(lesson.startswith("وانە_") for lesson in active_lessons))
        for course_id in ("daily_conversation", "unified_orthography"):
            self.assertTrue(
                set(bot.COURSE_LESSON_ORDER[course_id]).isdisjoint(active_lessons)
            )

    def test_active_course_lessons_include_namespaced_lessons_when_course_activates(self):
        with patch.object(
            bot, "course_is_active",
            side_effect=lambda course_id: course_id == "daily_conversation",
        ):
            active_lessons = bot.active_course_lessons()
        self.assertEqual(active_lessons, bot.COURSE_LESSON_ORDER["daily_conversation"])
        self.assertEqual(len(active_lessons), 48)
        self.assertTrue(all(lesson.startswith("daily_conversation_") for lesson in active_lessons))

    def test_draft_course_completions_never_grant_legacy_badges(self):
        draft_ids = (
            bot.COURSE_LESSON_ORDER["daily_conversation"]
            + bot.COURSE_LESSON_ORDER["unified_orthography"]
        )
        with patch.object(bot, "get_completed_lessons", return_value=draft_ids), \
             patch.object(bot, "add_badge") as add_badge:
            bot.check_badges(12345)
        add_badge.assert_not_called()

    def test_next_lesson_never_crosses_course_boundaries(self):
        for course_id in ("daily_conversation", "unified_orthography"):
            lesson_ids = bot.COURSE_LESSON_ORDER[course_id]
            with self.subTest(course=course_id):
                for current, following in zip(lesson_ids, lesson_ids[1:]):
                    self.assertEqual(bot.next_course_lesson(current), following)
                self.assertIsNone(bot.next_course_lesson(lesson_ids[-1]))

    def test_badges_use_course_local_numbers_and_skip_inactive_courses(self):
        recorded = []
        course_title = next(
            course["title"] for course in bot.COURSES
            if course["id"] == "daily_conversation"
        )
        with (
            patch.object(
                bot, "get_completed_lessons",
                return_value=["وانە_1", "daily_conversation_02", "unified_orthography_01"],
            ),
            patch.object(
                bot, "course_is_active",
                side_effect=lambda course_id: course_id in {"orthography_basic", "daily_conversation"},
            ),
            patch.object(bot, "add_badge", side_effect=lambda user_id, badge: recorded.append(badge)),
        ):
            bot.check_badges(12345)
        self.assertIn("🏅 کۆرسی ڕێنووسی — وانەی 1", recorded)
        self.assertIn(f"🏅 {course_title} — وانەی 2", recorded)
        self.assertEqual(len(recorded), 2)
        self.assertFalse(any("unified_orthography" in badge for badge in recorded))

    def test_course_one_progression_does_not_spill_into_course_two(self):
        legacy_ids = bot.COURSE_LESSON_ORDER["orthography_basic"]
        conversation_ids = bot.COURSE_LESSON_ORDER["daily_conversation"]
        self.assertEqual(legacy_ids, [f"وانە_{n}" for n in range(1, 23)])
        self.assertEqual(bot.next_course_lesson(legacy_ids[-1]), None)
        self.assertNotIn(legacy_ids[-1], conversation_ids)
        self.assertEqual(conversation_ids[0], "daily_conversation_01")

    def test_every_loaded_lesson_belongs_to_exactly_one_manifest_course(self):
        manifest_ids = [
            lesson_id
            for course in bot.COURSES
            for lesson_id in course.get("lesson_ids", [])
        ]
        self.assertEqual(len(manifest_ids), len(set(manifest_ids)))
        self.assertEqual(set(manifest_ids), set(bot.LESSON_DATA))
        self.assertEqual(set(bot.LESSON_COURSE), set(bot.LESSON_DATA))
        for course in bot.COURSES:
            expected = [lesson for lesson in course.get("lesson_ids", []) if lesson in bot.LESSON_DATA]
            self.assertEqual(bot.COURSE_LESSON_ORDER[course["id"]], expected)
            for lesson_id in expected:
                self.assertEqual(bot.LESSON_COURSE[lesson_id], course["id"])

    def test_course_four_remains_planned_and_empty(self):
        course = next(course for course in bot.COURSES if course["id"] == "grammar")
        self.assertEqual(course["status"], "planned")
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], [])


if __name__ == "__main__":
    unittest.main()
