"""Regression tests for owner-activated Courses 2 and 3."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class ActivatedCoursesTests(unittest.IsolatedAsyncioTestCase):
    def make_update(self, callback_data, user_id=12345):
        message = SimpleNamespace(reply_text=AsyncMock(), message_id=77)
        query = SimpleNamespace(
            data=callback_data,
            from_user=SimpleNamespace(id=user_id),
            message=message,
            answer=AsyncMock(),
        )
        return SimpleNamespace(callback_query=query), message, query

    def test_manifest_activates_48_and_12_lessons_without_activating_course_four(self):
        self.assertTrue(bot.course_is_active("daily_conversation"))
        self.assertTrue(bot.course_is_active("unified_orthography"))
        self.assertFalse(bot.course_is_active("grammar"))
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["daily_conversation"]), 48)
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["unified_orthography"]), 55)

    def test_startup_validation_confirms_both_activated_courses_are_complete(self):
        bot.validate_activated_course_runtime()

    def test_course_lesson_ids_are_unique_and_do_not_replace_course_one_ids(self):
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["orthography_basic"]), 22)
        all_ids = [
            lesson
            for course_id in ("orthography_basic", "daily_conversation", "unified_orthography")
            for lesson in bot.COURSE_LESSON_ORDER[course_id]
        ]
        self.assertEqual(len(all_ids), 125)
        self.assertEqual(len(set(all_ids)), 125)
        self.assertEqual(bot.COURSE_LESSON_ORDER["orthography_basic"][0], "وانە_1")

    def test_course_two_and_three_progression_is_independent(self):
        course_two = bot.COURSE_LESSON_ORDER["daily_conversation"]
        course_three = bot.COURSE_LESSON_ORDER["unified_orthography"]
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertTrue(bot.can_open(12345, course_two[0]))
            self.assertFalse(bot.can_open(12345, course_two[1]))
            self.assertTrue(bot.can_open(12345, course_three[0]))
            self.assertFalse(bot.can_open(12345, course_three[1]))
        with patch.object(bot, "get_completed_lessons", return_value=[course_two[0]]):
            self.assertTrue(bot.can_open(12345, course_two[1]))
            self.assertFalse(bot.can_open(12345, course_three[1]))
        with patch.object(bot, "get_completed_lessons", return_value=course_three[:-1]):
            self.assertTrue(bot.can_open(12345, course_three[-1]))

    async def test_open_course_two_shows_all_48_lesson_buttons(self):
        update, message, query = self.make_update("course_daily_conversation")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 48)
        self.assertEqual(
            keyboard[0][0].callback_data,
            "open_lesson_daily_conversation_01",
        )

    async def test_open_course_three_shows_all_12_lesson_buttons(self):
        update, message, query = self.make_update("course_unified_orthography")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 55)
        self.assertEqual(
            keyboard[0][0].callback_data,
            "open_lesson_unified_orthography_01",
        )

    def test_lesson_editorial_review_notes_do_not_deactivate_courses(self):
        self.assertTrue(bot.course_is_active("daily_conversation"))
        self.assertTrue(bot.course_is_active("unified_orthography"))
        for lesson_id in (
            bot.COURSE_LESSON_ORDER["daily_conversation"][0],
            bot.COURSE_LESSON_ORDER["unified_orthography"][0],
        ):
            self.assertEqual(
                bot.LESSON_DATA[lesson_id]["review_status"],
                "draft_editorial_review",
            )


if __name__ == "__main__":
    unittest.main()
