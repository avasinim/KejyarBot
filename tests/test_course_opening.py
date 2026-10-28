import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class CourseOpeningTests(unittest.IsolatedAsyncioTestCase):
    async def test_active_conversation_course_shows_its_own_lessons(self):
        query = SimpleNamespace(
            data="course_daily_conversation",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)

        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        args, kwargs = query.message.reply_text.await_args
        message = args[0]
        self.assertNotIn("بۆ خوێندکاران چالاک نەکراون", message)
        self.assertIsNotNone(kwargs.get("reply_markup"))
        buttons = [button for row in kwargs["reply_markup"].inline_keyboard for button in row]
        self.assertEqual(len(buttons), 12)
        self.assertEqual(buttons[0].callback_data, "open_lesson_daily_conversation_01")

    def test_active_courses_open_only_their_first_lesson_initially(self):
        self.assertTrue(bot.course_is_active("daily_conversation"))
        self.assertTrue(bot.course_is_active("unified_orthography"))
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertTrue(bot.can_open(12345, "daily_conversation_01"))
            self.assertTrue(bot.can_open(12345, "unified_orthography_01"))

    async def test_active_course_lists_only_its_catalog_lessons(self):
        query = SimpleNamespace(
            data="course_orthography_basic",
            answer=AsyncMock(),
            from_user=SimpleNamespace(id=12345),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)

        from unittest.mock import patch
        with patch.object(bot, "get_completed_lessons", return_value=[]), patch.object(bot, "can_open", return_value=True):
            await bot.open_course(update, SimpleNamespace())

        query.message.reply_text.assert_awaited_once()
        _, kwargs = query.message.reply_text.await_args
        keyboard = kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 22)
        callback_ids = [row[0].callback_data for row in keyboard]
        self.assertEqual(callback_ids, [f"open_lesson_وانە_{n}" for n in range(1, 23)])


if __name__ == "__main__":
    unittest.main()
