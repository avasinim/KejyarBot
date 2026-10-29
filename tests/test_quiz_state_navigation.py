import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class QuizStateNavigationTests(unittest.IsolatedAsyncioTestCase):
    async def test_entering_daily_chat_clears_active_quiz(self):
        update = SimpleNamespace(
            message=SimpleNamespace(
                text="💬 گفتوگۆی ڕۆژانە",
                reply_text=AsyncMock(),
            ),
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={
            "quiz": {"lesson": "وانە_1", "question_message_id": 77},
            "daily_chat_mode": False,
        })

        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        self.assertNotIn("quiz", context.user_data)
        self.assertTrue(context.user_data["daily_chat_mode"])
        update.message.reply_text.assert_awaited_once()

    async def test_inline_course_navigation_clears_active_quiz(self):
        query = SimpleNamespace(
            data="course_grammar",
            answer=AsyncMock(),
            from_user=SimpleNamespace(id=12345),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={
            "quiz": {"lesson": "daily_conversation_01", "question_message_id": 77}
        })

        await bot.open_course(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
