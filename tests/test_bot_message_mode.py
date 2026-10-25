import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class MessageModeTests(unittest.IsolatedAsyncioTestCase):
    def make_update_context(self, text, user_data=None):
        message = SimpleNamespace(
            text=text,
            reply_text=AsyncMock(),
        )
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data=user_data if user_data is not None else {})
        return update, context

    async def test_ordinary_text_stays_in_daily_chat_mode(self):
        update, context = self.make_update_context(
            "دەمەوێت لە بازاڕ گفتوگۆ بکەم",
            {"daily_chat_mode": True, "daily_chat_scenario": "market"},
        )
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "reply_to_daily_message", return_value="وەڵامی گفتوگۆ") as reply,
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock),
        ):
            await bot.message(update, context)

        self.assertTrue(context.user_data["daily_chat_mode"])
        reply.assert_called_once_with(
            "دەمەوێت لە بازاڕ گفتوگۆ بکەم", context.user_data
        )
        update.message.reply_text.assert_awaited_once()

    async def test_lesson_menu_button_exits_daily_chat_mode(self):
        lesson_button = next(iter(bot.LESSON_BUTTONS))
        lesson = bot.LESSON_BUTTONS[lesson_button]
        update, context = self.make_update_context(
            lesson_button,
            {"daily_chat_mode": True, "daily_chat_scenario": "market", "daily_chat_stage": 2},
        )
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock),
            patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock),
        ):
            await bot.message(update, context)

        self.assertFalse(context.user_data["daily_chat_mode"])
        self.assertEqual(context.user_data["daily_chat_scenario"], "market")
        update.message.reply_text.assert_awaited_once()
        self.assertEqual(update.message.reply_text.await_args.args[0], bot.LESSON_DATA[lesson]["content"])


if __name__ == "__main__":
    unittest.main()
