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
