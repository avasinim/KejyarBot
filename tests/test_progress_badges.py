import unittest
from unittest.mock import patch

import bot


class OfficialProgressBadgeBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.course = {
            "id": "grammar",
            "title": "Course 4",
            "description": "Grammar",
            "status": "active",
        }
        self.lesson_ids = ["grammar_01", "grammar_02", "grammar_03", "grammar_04"]
        self.completed = ["grammar_01", "grammar_02", "grammar_04"]

    def _patch_progress(self):
        return (
            patch.object(bot, "COURSES", [self.course]),
            patch.object(bot, "COURSE_LESSON_ORDER", {"grammar": self.lesson_ids}),
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(
                bot,
                "lesson_is_beta_review",
                side_effect=lambda lesson: lesson == "grammar_03",
            ),
        )

    def test_visible_badges_stop_at_beta_lesson_and_ignore_later_completion(self):
        with (
            patch.object(bot, "get_completed_lessons", return_value=self.completed),
            *self._patch_progress(),
        ):
            badges = bot.current_progress_badges(12345)

        self.assertEqual(len(badges), 2)
        self.assertTrue(badges[0].endswith("وانەی 1"))
        self.assertTrue(badges[1].endswith("وانەی 2"))
        self.assertFalse(any("وانەی 3" in badge or "وانەی 4" in badge for badge in badges))

    def test_badge_ledger_does_not_award_beta_or_out_of_sequence_lessons(self):
        with (
            patch.object(bot, "get_completed_lessons", return_value=self.completed),
            patch.object(bot, "add_badge") as add_badge,
            *self._patch_progress(),
        ):
            bot.check_badges(12345)

        awarded = [call.args[1] for call in add_badge.call_args_list]
        self.assertEqual(len(awarded), 2)
        self.assertTrue(awarded[0].endswith("وانەی 1"))
        self.assertTrue(awarded[1].endswith("وانەی 2"))

    def test_beta_only_progress_does_not_create_official_badges(self):
        with (
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "get_completed_beta_lessons", return_value=self.lesson_ids),
            patch.object(bot, "add_badge") as add_badge,
            *self._patch_progress(),
        ):
            self.assertEqual(bot.current_progress_badges(12345), [])
            bot.check_badges(12345)

        add_badge.assert_not_called()


if __name__ == "__main__":
    unittest.main()
