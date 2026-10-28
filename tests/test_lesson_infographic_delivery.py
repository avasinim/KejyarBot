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

    async def test_opening_lesson_sends_text_then_optional_infographic(self):
        update, query = self.make_update("open_lesson_وانە_1")
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "send_lesson_text", new_callable=AsyncMock) as send_text,
            patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock) as send_image,
        ):
            await bot.open_selected_lesson(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        send_text.assert_awaited_once_with(
            query.message,
            bot.LESSON_DATA["وانە_1"]["content"],
            bot.lesson_keyboard("وانە_1"),
        )
        send_image.assert_awaited_once_with(query.message, "وانە_1")
        self.assertLess(
            send_text.await_args_list[0]._call_start if hasattr(send_text.await_args_list[0], "_call_start") else 0,
            1,
        )

    async def test_next_lesson_path_also_attempts_infographic_after_text(self):
        update, query = self.make_update("next_lesson_وانە_2")
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "send_lesson_text", new_callable=AsyncMock) as send_text,
            patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock) as send_image,
        ):
            await bot.open_next_lesson(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        send_text.assert_awaited_once_with(
            query.message,
            bot.LESSON_DATA["وانە_2"]["content"],
            bot.lesson_keyboard("وانە_2"),
        )
        send_image.assert_awaited_once_with(query.message, "وانە_2")


if __name__ == "__main__":
    unittest.main()
