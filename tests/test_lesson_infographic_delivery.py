import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class LessonInfographicDeliveryTests(unittest.IsolatedAsyncioTestCase):
    def make_update(self, callback_data):
        query = SimpleNamespace(
            data=callback_data,
            answer=AsyncMock(),
            from_user=SimpleNamespace(id=12345),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        return SimpleNamespace(callback_query=query), query

    async def assert_text_then_infographic(self, callback_data, lesson, handler_name):
        update, query = self.make_update(callback_data)
        calls = []

        async def record_text(*args, **kwargs):
            calls.append("text")

        async def record_image(*args, **kwargs):
            calls.append("image")

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "send_lesson_text", new_callable=AsyncMock, side_effect=record_text) as send_text,
            patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock, side_effect=record_image) as send_image,
        ):
            await getattr(bot, handler_name)(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        send_text.assert_awaited_once_with(
            query.message,
            bot.LESSON_DATA[lesson]["content"],
            bot.lesson_keyboard(lesson),
        )
        send_image.assert_awaited_once_with(query.message, lesson)
        self.assertEqual(calls, ["text", "image"])

    async def test_long_lesson_text_is_chunked_and_keyboard_is_only_on_final_chunk(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        keyboard = object()
        content = ("نمونەی وانە.\n" * 900).strip()

        await bot.send_lesson_text(message, content, keyboard)

        self.assertGreater(message.reply_text.await_count, 1)
        calls = message.reply_text.await_args_list
        self.assertTrue(all(len(call.args[0]) <= 3800 for call in calls))
        self.assertTrue(all(call.kwargs.get("reply_markup") is None for call in calls[:-1]))
        self.assertIs(calls[-1].kwargs.get("reply_markup"), keyboard)
        delivered = "".join(call.args[0] for call in calls).replace("\n", "")
        expected = content.replace("\\n", "")
        self.assertEqual(len(delivered), len(expected))
        self.assertEqual(delivered, expected)

    async def test_opening_lesson_sends_text_then_optional_infographic(self):
        await self.assert_text_then_infographic(
            "open_lesson_وانە_1", "وانە_1", "open_selected_lesson"
        )

    async def test_next_lesson_path_also_attempts_infographic_after_text(self):
        await self.assert_text_then_infographic(
            "next_lesson_وانە_2", "وانە_2", "open_next_lesson"
        )


if __name__ == "__main__":
    unittest.main()
