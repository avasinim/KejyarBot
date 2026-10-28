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

    async def test_quiz_catalog_uses_readable_lesson_numbers_and_stable_callbacks(self):
        from unittest.mock import patch

        message = SimpleNamespace(
            text="📝 تاقیکردنەوەکان",
            reply_text=AsyncMock(),
        )
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        with patch.object(bot, "get_user", return_value=(12345, 0, 0, "A1.1", 0, None, 0, 0, 0, 0)), patch.object(bot, "get_completed_lessons", return_value=["وانە_1"]):
            await bot.message(update, context)

        message.reply_text.assert_awaited_once()
        kwargs = message.reply_text.await_args.kwargs
        keyboard = kwargs["reply_markup"].inline_keyboard
        self.assertEqual(keyboard[0][0].text, "📝 تاقیکردنەوەی وانەی ١")
        self.assertEqual(keyboard[0][0].callback_data, "quiz_1_start")
        self.assertNotIn("وانە_1", keyboard[0][0].text)

    async def test_learning_path_does_not_show_internal_lesson_ids(self):
        from unittest.mock import patch

        message = SimpleNamespace(
            text="🧭 ڕێگای فێربوون",
            reply_text=AsyncMock(),
        )
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        with patch.object(bot, "get_user", return_value=(12345, 0, 0, "A1.1", 0, None, 0, 0, 0, 0)), patch.object(bot, "get_completed_lessons", return_value=[]), patch.object(bot, "can_open", side_effect=lambda user_id, lesson: lesson == "وانە_1"):
            await bot.message(update, context)

        message.reply_text.assert_awaited_once()
        reply = message.reply_text.await_args.args[0]
        self.assertIn("وانەی ١:", reply)
        self.assertNotIn("وانە_1:", reply)
        self.assertIn("وانەی ٢٢:", reply)


if __name__ == "__main__":
    unittest.main()
