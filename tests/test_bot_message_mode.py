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

    async def test_start_clears_all_daily_chat_state(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={
            "daily_chat_mode": True,
            "daily_chat_scenario": "market",
            "daily_chat_stage": 2,
            "quiz": {"lesson": "وانە_2", "index": 3},
        })
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "send_voice", new_callable=AsyncMock),
        ):
            await bot.start(update, context)

        self.assertFalse(context.user_data["daily_chat_mode"])
        self.assertNotIn("daily_chat_scenario", context.user_data)
        self.assertNotIn("daily_chat_stage", context.user_data)
        self.assertNotIn("quiz", context.user_data)
        message.reply_text.assert_awaited_once()

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
        self.assertNotIn("daily_chat_scenario", context.user_data)
        self.assertNotIn("daily_chat_stage", context.user_data)
        update.message.reply_text.assert_awaited_once()
        self.assertEqual(update.message.reply_text.await_args.args[0], bot.LESSON_DATA[lesson]["content"])


    async def test_lesson_catalog_renders_all_lessons_as_inline_buttons_even_when_locked(self):
        update, context = self.make_update_context("📚 وانەکان")
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "can_open", return_value=False),
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        call = update.message.reply_text.await_args
        keyboard = call.kwargs["reply_markup"]
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len(buttons), len(bot.ORDER))
        self.assertEqual(len(bot.ORDER), 22)
        self.assertIn(bot.ORTHOGRAPHY_COURSE["title"], call.args[0])
        for lesson, button in zip(bot.ORDER, buttons):
            with self.subTest(lesson=lesson):
                self.assertIn(lesson, button.text)
                self.assertIn(bot.LESSON_DATA[lesson]["title"], button.text)
                self.assertEqual(button.callback_data, f"open_lesson_{lesson}")
                self.assertTrue(button.text.startswith("🔒"))


    async def test_long_lesson_is_chunked_and_completion_keyboard_is_only_on_last_chunk(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        content = "ئ" * 3900 + "\n" + "ب" * 200
        completion_keyboard = object()

        await bot.send_lesson_text(message, content, completion_keyboard)

        calls = message.reply_text.await_args_list
        self.assertGreater(len(calls), 1)
        chunks = [call.args[0] for call in calls]
        self.assertTrue(all(0 < len(chunk) <= 3800 for chunk in chunks))
        self.assertTrue(all(call.kwargs.get("reply_markup") is None for call in calls[:-1]))
        self.assertIs(calls[-1].kwargs["reply_markup"], completion_keyboard)
        self.assertEqual("".join(chunks), content)

    async def test_locked_lesson_callback_does_not_send_lesson_content(self):
        query = SimpleNamespace(
            data="open_lesson_وانە_2",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=False),
            patch.object(bot, "send_lesson_text", new_callable=AsyncMock) as send_lesson,
        ):
            await bot.open_selected_lesson(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("تەواو بکە", query.message.reply_text.await_args.args[0])
        send_lesson.assert_not_awaited()


    async def test_malformed_quiz_index_is_cleared_without_crashing(self):
        query = SimpleNamespace(
            data="answer_0",
            answer=AsyncMock(),
            message=SimpleNamespace(message_id=10, reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query, effective_user=SimpleNamespace(id=12345))
        context = SimpleNamespace(user_data={
            "quiz": {
                "lesson": "وانە_1",
                "index": 4,
                "questions": [{"question": "پرسیار", "options": ["A", "B", "C"], "answer": "A"}],
                "score": 0,
                "question_message_id": 10,
            }
        })

        await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("دۆخی تاقیکردنەوە نادروست", query.message.reply_text.await_args.args[0])

    async def test_malformed_quiz_options_are_cleared_without_scoring(self):
        query = SimpleNamespace(
            data="answer_0",
            answer=AsyncMock(),
            message=SimpleNamespace(message_id=10, reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query, effective_user=SimpleNamespace(id=12345))
        context = SimpleNamespace(user_data={
            "quiz": {
                "lesson": "وانە_1",
                "index": 0,
                "questions": [{"question": "پرسیار", "options": ["A", "A"], "answer": "A"}],
                "score": 0,
                "question_message_id": 10,
            }
        })

        await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پرسیاری تاقیکردنەوە نادروست", query.message.reply_text.await_args.args[0])


    async def test_malformed_quiz_score_is_cleared_without_crashing(self):
        query = SimpleNamespace(
            data="answer_0",
            answer=AsyncMock(),
            message=SimpleNamespace(message_id=10, reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query, effective_user=SimpleNamespace(id=12345))
        context = SimpleNamespace(user_data={
            "quiz": {
                "lesson": "وانە_1",
                "index": 0,
                "questions": [{"question": "پرسیار", "options": ["A", "B", "C"], "answer": "A"}],
                "score": "0",
                "question_message_id": 10,
            }
        })

        await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پرسیاری تاقیکردنەوە نادروست", query.message.reply_text.await_args.args[0])


if __name__ == "__main__":
    unittest.main()
