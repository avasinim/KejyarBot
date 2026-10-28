import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock

import bot


class CourseOpeningTests(unittest.IsolatedAsyncioTestCase):
    async def test_planned_course_does_not_expose_legacy_lessons(self):
        query = SimpleNamespace(
            data="course_daily_conversation",
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)

        await bot.open_course(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        args, kwargs = query.message.reply_text.await_args
        message = args[0]
        self.assertIn("لە پێداچوونەوەدایە", message)
        self.assertIn("بۆ خوێندکاران چالاک نەکراون", message)
        self.assertIsNone(kwargs.get("reply_markup"))

    def test_draft_courses_cannot_open_lessons_even_by_direct_callback(self):
        self.assertFalse(bot.course_is_active("daily_conversation"))
        self.assertFalse(bot.course_is_active("unified_orthography"))
        self.assertFalse(bot.can_open(12345, "daily_conversation_01"))
        self.assertFalse(bot.can_open(12345, "unified_orthography_01"))

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
        labels = [row[0].text for row in keyboard]
        self.assertEqual(labels[0], "🔓 وانەی ١: ئەلفبێی زمانی کوردی")
        self.assertEqual(labels[-1].split(":")[0], "🔓 وانەی ٢٢")


if __name__ == "__main__":
    unittest.main()
