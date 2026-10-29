"""Callback-level tests verify activated courses and course-local lesson locks."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class ActiveCourseCallbackTests(unittest.IsolatedAsyncioTestCase):
    def make_update(self, data, user_id=12345):
        message = SimpleNamespace(reply_text=AsyncMock(), message_id=77)
        query = SimpleNamespace(
            data=data,
            from_user=SimpleNamespace(id=user_id),
            message=message,
            answer=AsyncMock(),
        )
        return SimpleNamespace(callback_query=query), message, query

    async def test_course_two_lists_all_48_lessons_by_default(self):
        update, message, query = self.make_update("course_daily_conversation")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()
        text = message.reply_text.await_args.args[0]
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertIn("٤٨ وانەی وتووێژ", text)
        self.assertEqual(len(keyboard), 48)
        self.assertEqual(keyboard[0][0].callback_data, "open_lesson_daily_conversation_01")

    async def test_course_three_lists_all_12_lessons_by_default(self):
        update, message, query = self.make_update("course_unified_orthography")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 12)
        self.assertEqual(keyboard[0][0].callback_data, "open_lesson_unified_orthography_01")

    async def test_first_course_two_lesson_opens_but_second_stays_locked(self):
        update, message, query = self.make_update("open_lesson_daily_conversation_01")
        with patch.object(bot, "get_completed_lessons", return_value=[]), \
             patch.object(bot, "send_lesson_text", new_callable=AsyncMock) as send_text, \
             patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock):
            await bot.open_selected_lesson(update, SimpleNamespace())
        send_text.assert_awaited_once()
        self.assertIn("daily_conversation_01", str(send_text.await_args))

        update, message, query = self.make_update("open_lesson_daily_conversation_02")
        with patch.object(bot, "get_completed_lessons", return_value=[]), \
             patch.object(bot, "send_lesson_text", new_callable=AsyncMock) as send_text:
            await bot.open_selected_lesson(update, SimpleNamespace())
        message.reply_text.assert_awaited_once()
        self.assertIn("پێشووتر", message.reply_text.await_args.args[0])
        send_text.assert_not_awaited()

    async def test_quiz_still_requires_lesson_completion(self):
        update, message, query = self.make_update("quiz_daily_conversation_01_start")
        context = SimpleNamespace(user_data={})
        with patch.object(bot, "get_completed_lessons", return_value=[]), \
             patch.object(bot, "send_question", new_callable=AsyncMock) as send_question:
            await bot.start_quiz(update, context)
        message.reply_text.assert_awaited_once()
        self.assertIn("سەرەتا خودی ئەم وانەیە تەواو بکە", message.reply_text.await_args.args[0])
        self.assertNotIn("quiz", context.user_data)
        send_question.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
