"""Regression tests for presentation-only Course 4 grammar lesson pagination."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class Course4LessonPaginationTests(unittest.IsolatedAsyncioTestCase):
    def test_lesson_pages_preserve_all_rendered_blocks_and_respect_page_limit(self):
        source = "\\n\\n".join(
            f"بەشی {number}: ئەم دەقە تەنها بۆ تاقیکردنەوەی دابەشکردنی پێشکەشکردنە."
            for number in range(1, 121)
        )
        blocks = bot.render_lesson_html_blocks(source)
        pages = bot.split_lesson_html(blocks, limit=2200)

        self.assertGreater(len(pages), 1)
        self.assertTrue(all(len(page) <= 2200 for page in pages))
        rendered = "\\n".join(pages)
        for number in (1, 2, 40, 80, 120):
            self.assertIn(f"بەشی {number}:", rendered)

    def test_navigation_buttons_show_previous_and_next_and_finish_only_on_last_page(self):
        completion = bot.InlineKeyboardMarkup([[
            bot.InlineKeyboardButton("finish", callback_data="finish_grammar_01")
        ]])

        first = bot.lesson_page_keyboard("grammar_01", 0, 3, completion)
        middle = bot.lesson_page_keyboard("grammar_01", 1, 3, completion)
        last = bot.lesson_page_keyboard("grammar_01", 2, 3, completion)

        first_callbacks = [button.callback_data for row in first.inline_keyboard for button in row]
        middle_callbacks = [button.callback_data for row in middle.inline_keyboard for button in row]
        last_callbacks = [button.callback_data for row in last.inline_keyboard for button in row]

        self.assertIn("lessonpage:grammar_01:1", first_callbacks)
        self.assertNotIn("finish_grammar_01", first_callbacks)
        self.assertIn("lessonpage:grammar_01:0", middle_callbacks)
        self.assertIn("lessonpage:grammar_01:2", middle_callbacks)
        self.assertNotIn("finish_grammar_01", middle_callbacks)
        self.assertIn("lessonpage:grammar_01:1", last_callbacks)
        self.assertIn("finish_grammar_01", last_callbacks)

    async def test_grammar_lesson_opens_one_page_with_navigation(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        content = "وانەی تاقیکاری\\n\\n" + "\\n\\n".join(
            f"خاڵی فێرکاری {number}: " + ("دەقی فێرکاریی پارێزراو. " * 12)
            for number in range(1, 90)
        )

        await bot.send_lesson_text(
            message,
            content,
            bot.lesson_keyboard("grammar_01"),
            lesson_id="grammar_01",
            page=0,
        )

        message.reply_text.assert_awaited_once()
        args, kwargs = message.reply_text.await_args
        self.assertIn("بەشی 1 لە", args[0])
        self.assertIn("وانەی ١", args[0])
        self.assertIsNotNone(kwargs["reply_markup"])
        callbacks = [
            button.callback_data
            for row in kwargs["reply_markup"].inline_keyboard
            for button in row
        ]
        self.assertTrue(any(value.startswith("lessonpage:grammar_01:") for value in callbacks))
        self.assertNotIn("finish_grammar_01", callbacks)

    async def test_page_callback_reopens_only_requested_grammar_page_without_resending_image(self):
        query = SimpleNamespace(
            answer=AsyncMock(),
            data="lessonpage:grammar_01:1",
            from_user=SimpleNamespace(id=12345),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        with patch.object(bot, "can_open", return_value=True), patch.object(
            bot, "send_shared_lesson_image", new=AsyncMock()
        ) as send_image:
            await bot.open_lesson_page(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("بەشی 2 لە", query.message.reply_text.await_args.args[0])
        send_image.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
