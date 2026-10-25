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


    async def test_quiz_menu_uses_human_readable_lesson_titles(self):
        completed = [bot.ORDER[0], bot.ORDER[1]]
        update, context = self.make_update_context("📝 تاقیکردنەوەکان")
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=completed),
        ):
            await bot.message(update, context)

        args = update.message.reply_text.await_args
        self.assertIn("تاقیکردنەوەی وانە تەواوکراوەکان", args.args[0])
        buttons = [button for row in args.kwargs["reply_markup"].inline_keyboard for button in row]
        self.assertEqual(len(buttons), 2)
        for lesson in completed:
            expected_title = bot.LESSON_DATA[lesson]["title"]
            self.assertTrue(any(expected_title in button.text for button in buttons))
            self.assertTrue(any(button.callback_data == f"quiz_{lesson.split('_')[1]}_start" for button in buttons))

    async def test_lesson_catalog_lists_all_ten_lessons_as_compact_inline_buttons(self):
        update, context = self.make_update_context("📚 پەڕگەی وانەکان")
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "can_open", return_value=False),
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        args = update.message.reply_text.await_args
        self.assertIn("پەڕگەی وانەکان", args.args[0])
        markup = args.kwargs["reply_markup"]
        buttons = [button for row in markup.inline_keyboard for button in row]
        self.assertEqual(len(buttons), 10)
        self.assertEqual(len(markup.inline_keyboard), 5)
        self.assertTrue(all(button.callback_data.startswith("open_lesson_") for button in buttons))
        for lesson in bot.ORDER:
            self.assertTrue(any(bot.LESSON_DATA[lesson]["title"] in button.text for button in buttons))
        self.assertEqual(len(bot.MENU.keyboard), 3, "Persistent menu should use three compact mobile rows.")
        self.assertTrue(all(len(row) == 2 for row in bot.MENU.keyboard))

    async def test_opening_unlocked_lesson_from_inline_catalog(self):
        query_message = SimpleNamespace(reply_text=AsyncMock())
        query = SimpleNamespace(
            data="open_lesson_7",
            from_user=SimpleNamespace(id=12345),
            message=query_message,
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={"daily_chat_mode": True})
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock),
            patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock),
        ):
            await bot.open_lesson_from_catalog(update, context)

        query.answer.assert_awaited_once()
        self.assertFalse(context.user_data["daily_chat_mode"])
        query_message.reply_text.assert_awaited_once()
        self.assertEqual(query_message.reply_text.await_args.args[0], bot.LESSON_DATA["وانە_7"]["content"])

    async def test_locked_catalog_lesson_stays_locked(self):
        query_message = SimpleNamespace(reply_text=AsyncMock())
        query = SimpleNamespace(
            data="open_lesson_7",
            from_user=SimpleNamespace(id=12345),
            message=query_message,
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})
        with patch.object(bot, "can_open", return_value=False):
            await bot.open_lesson_from_catalog(update, context)

        query_message.reply_text.assert_awaited_once_with("🔒 سەرەتا وانەی پێشووتر تەواو بکە.")

if __name__ == "__main__":
    unittest.main()
