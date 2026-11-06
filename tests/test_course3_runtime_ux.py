"""Regression tests for Course 3 quiz UX and sequential access in text-only mode."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class CourseThreeRuntimeUxTests(unittest.IsolatedAsyncioTestCase):
    def test_course3_quizzes_use_select_then_submit_controls(self):
        lesson = bot.COURSE_LESSON_ORDER["unified_orthography"][0]
        self.assertTrue(bot.quiz_requires_submission(lesson))
        self.assertEqual(len(bot.QUIZ_DATA[lesson]), 3)

    def test_course3_requires_every_prior_lesson_before_unlocking_a_later_one(self):
        lessons = bot.COURSE_LESSON_ORDER["unified_orthography"]
        with patch.object(bot, "get_completed_lessons", return_value=[lessons[0], lessons[2]]):
            self.assertFalse(bot.can_open(90003, lessons[3]))
            self.assertFalse(bot.can_open(90003, lessons[2]))
            self.assertTrue(bot.can_open(90003, lessons[1]))
        with patch.object(bot, "get_completed_lessons", return_value=lessons[:3]):
            self.assertTrue(bot.can_open(90003, lessons[3]))

    async def test_opening_course3_lesson_uses_text_and_never_voice(self):
        lesson = bot.COURSE_LESSON_ORDER["unified_orthography"][0]
        message = SimpleNamespace(reply_text=AsyncMock())
        query = SimpleNamespace(
            data=f"open_lesson_{lesson}",
            from_user=SimpleNamespace(id=90001),
            message=message,
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        with patch.object(bot, "can_open", return_value=True), \
             patch.object(bot, "send_lesson_text", new=AsyncMock()) as send_text, \
             patch.object(bot, "send_lesson_infographic", new=AsyncMock()):
            await bot.open_selected_lesson(update, SimpleNamespace())
        send_text.assert_awaited_once()

    async def test_course3_completion_delivers_next_lesson_automatically_without_voice(self):
        lesson_ids = bot.COURSE_LESSON_ORDER["unified_orthography"]
        lesson, next_lesson = lesson_ids[0], lesson_ids[1]
        message = SimpleNamespace(reply_text=AsyncMock(), message_id=77)
        query = SimpleNamespace(
            data=f"finish_{lesson}",
            from_user=SimpleNamespace(id=90002),
            message=message,
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        with patch.object(bot, "can_open", return_value=True), \
             patch.object(bot, "get_user_level", return_value=1), \
             patch.object(bot, "complete_lesson_with_rewards", return_value=True), \
             patch.object(bot, "check_badges"), \
             patch.object(bot, "next_course_lesson", return_value=next_lesson), \
             patch.object(bot, "quiz_is_available", return_value=True), \
             patch.object(bot, "send_lesson_text", new=AsyncMock()) as send_text:
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))
        self.assertEqual(send_text.await_count, 1)
        self.assertEqual(send_text.await_args.args[1], bot.LESSON_DATA[next_lesson]["content"])

    async def test_course3_retry_after_auto_delivery_failure_offers_manual_resume(self):
        lesson_ids = bot.COURSE_LESSON_ORDER["unified_orthography"]
        lesson, next_lesson = lesson_ids[0], lesson_ids[1]
        message = SimpleNamespace(reply_text=AsyncMock(), message_id=78)
        query = SimpleNamespace(
            data=f"finish_{lesson}",
            from_user=SimpleNamespace(id=90004),
            message=message,
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "get_user_level", side_effect=[1, 1, 1]),
            patch.object(bot, "complete_lesson_with_rewards", side_effect=[True, False]) as complete,
            patch.object(bot, "check_badges"),
            patch.object(bot, "next_course_lesson", return_value=next_lesson),
            patch.object(bot, "quiz_is_available", return_value=True),
            patch.object(
                bot, "send_lesson_text",
                new=AsyncMock(side_effect=RuntimeError("Telegram lesson delivery failed")),
            ) as send_text,
        ):
            with self.assertRaisesRegex(RuntimeError, "Telegram lesson delivery failed"):
                await bot.finish_lesson(update, SimpleNamespace(user_data={}))
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        self.assertEqual(complete.call_count, 2)
        self.assertEqual(complete.call_args_list[0].args, (90004, lesson))
        self.assertEqual(complete.call_args_list[1].args, (90004, lesson))
        self.assertEqual(send_text.await_count, 1)
        self.assertEqual(message.reply_text.await_count, 2)
        self.assertIn("پێشتر تەواو کراوە", message.reply_text.await_args.args[0])
        keyboard = message.reply_text.await_args.kwargs["reply_markup"]
        self.assertEqual(
            keyboard.inline_keyboard[0][0].callback_data,
            f"next_lesson_{next_lesson}",
        )

    def test_bot_module_exposes_no_voice_api(self):
        self.assertFalse(hasattr(bot, "send_voice"))
        self.assertFalse(hasattr(bot, "send_conversation_voice"))
        self.assertFalse(hasattr(bot, "send_kejyar_course_cue"))


if __name__ == "__main__":
    unittest.main()
