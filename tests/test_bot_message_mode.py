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

    async def test_unexpected_update_error_is_logged_and_user_gets_retry_message(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        update = SimpleNamespace(effective_message=message, callback_query=None)
        context = SimpleNamespace(error=RuntimeError("internal database detail"))

        with patch.object(bot.logger, "error") as log_error:
            await bot.handle_unexpected_error(update, context)

        message.reply_text.assert_awaited_once()
        self.assertIn("دووبارە هەوڵ بدەرەوە", message.reply_text.await_args.args[0])
        self.assertNotIn(
            "internal database detail", message.reply_text.await_args.args[0]
        )
        log_error.assert_called_once()

    async def test_unexpected_callback_error_uses_callback_message_fallback(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        query = SimpleNamespace(message=message)
        update = SimpleNamespace(effective_message=None, callback_query=query)
        context = SimpleNamespace(error=RuntimeError("callback failure"))

        with patch.object(bot.logger, "error"):
            await bot.handle_unexpected_error(update, context)

        message.reply_text.assert_awaited_once()
        self.assertIn("کێشەیەکی کاتی", message.reply_text.await_args.args[0])

    async def test_unexpected_error_does_not_raise_if_retry_notice_fails(self):
        message = SimpleNamespace(
            reply_text=AsyncMock(side_effect=RuntimeError("telegram unavailable"))
        )
        update = SimpleNamespace(effective_message=message, callback_query=None)
        context = SimpleNamespace(error=RuntimeError("handler failure"))

        with (
            patch.object(bot.logger, "error"),
            patch.object(bot.logger, "exception") as log_exception,
        ):
            await bot.handle_unexpected_error(update, context)

        message.reply_text.assert_awaited_once()
        log_exception.assert_called_once()

    async def test_lesson_completion_confirmation_survives_badge_database_error(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        query = SimpleNamespace(
            answer=AsyncMock(),
            from_user=SimpleNamespace(id=12345),
            data="finish_وانە_1",
            message=message,
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
            patch.object(bot, "complete_lesson_with_rewards", return_value=True) as complete,
            patch.object(bot, "check_badges", side_effect=RuntimeError("badge db unavailable")),
            patch.object(bot, "next_course_lesson", return_value=None),
            patch.object(bot, "QUIZ_DATA", {}),
            patch.object(bot.logger, "exception") as log_exception,
        ):
            await bot.finish_lesson(update, context)

        complete.assert_called_once_with(12345, "وانە_1")
        message.reply_text.assert_awaited_once()
        self.assertIn("وانەکە تەواو بوو", message.reply_text.await_args.args[0])
        self.assertIn("+10 XP", message.reply_text.await_args.args[0])
        log_exception.assert_called_once()

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

    async def test_goodbye_exits_daily_chat_mode_in_bot_handler(self):
        update, context = self.make_update_context(
            "خواحافیز",
            {"daily_chat_mode": True, "daily_chat_scenario": "market", "daily_chat_stage": 2},
        )
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock),
        ):
            await bot.message(update, context)

        self.assertFalse(context.user_data["daily_chat_mode"])
        self.assertNotIn("daily_chat_scenario", context.user_data)
        self.assertNotIn("daily_chat_stage", context.user_data)
        update.message.reply_text.assert_awaited_once()
        self.assertIn("خواحافیز", update.message.reply_text.await_args.args[0])

    async def test_chest_without_inventory_gives_clear_message_and_no_voice_reward(self):
        update, context = self.make_update_context("🎁 سەنوقی خەڵات")
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "open_chest", return_value=0),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock) as voice,
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        self.assertIn("سەنوقێکت نیە", update.message.reply_text.await_args.args[0])
        voice.assert_not_awaited()

    async def test_chest_database_failure_returns_retry_message_without_voice(self):
        update, context = self.make_update_context("🎁 سەنوقی خەڵات")
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "open_chest", side_effect=RuntimeError("database unavailable")),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock) as voice,
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        self.assertIn("دووبارە هەوڵ بدەرەوە", update.message.reply_text.await_args.args[0])
        voice.assert_not_awaited()

    async def test_opened_chest_reports_reward_and_uses_configured_voice_path(self):
        update, context = self.make_update_context("🎁 سەنوقی خەڵات")
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "open_chest", return_value=20),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock) as voice,
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        self.assertIn("20 Coin", update.message.reply_text.await_args.args[0])
        voice.assert_awaited_once()
        self.assertIn("20 کۆین", voice.await_args.args[1])

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


    async def test_lesson_catalog_shows_four_distinct_courses(self):
        update, context = self.make_update_context("📚 وانەکان")
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        call = update.message.reply_text.await_args
        keyboard = call.kwargs["reply_markup"]
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len(buttons), 4)
        self.assertEqual(len(bot.COURSES), 4)
        for course, button in zip(bot.COURSES, buttons):
            with self.subTest(course=course["id"]):
                self.assertIn(course["title"], button.text)
                self.assertEqual(button.callback_data, f"course_{course['id']}")

    async def test_course_one_opens_22_lesson_buttons(self):
        query = SimpleNamespace(
            data="course_orthography_basic",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})
        with (
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "can_open", return_value=False),
        ):
            await bot.open_course(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        keyboard = query.message.reply_text.await_args.kwargs["reply_markup"]
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len(buttons), 22)
        for number, button in enumerate(buttons, start=1):
            self.assertEqual(button.callback_data, f"open_lesson_وانە_{number}")
            self.assertTrue(button.text.startswith("🔒"))

    async def test_active_unified_orthography_course_lists_12_lessons(self):
        query = SimpleNamespace(
            data="course_unified_orthography",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        keyboard = query.message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 12)
        self.assertEqual(keyboard[0][0].callback_data, "open_lesson_unified_orthography_01")


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


    async def test_stale_next_lesson_callback_cannot_bypass_unlock_gate(self):
        query = SimpleNamespace(
            data="next_lesson_daily_conversation_02",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=False),
            patch.object(bot, "send_lesson_text", new_callable=AsyncMock) as send_lesson,
            patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock) as send_image,
        ):
            await bot.open_next_lesson(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("تەواو بکە", query.message.reply_text.await_args.args[0])
        send_lesson.assert_not_awaited()
        send_image.assert_not_awaited()

    async def test_stale_finish_callback_cannot_award_rewards_for_locked_lesson(self):
        query = SimpleNamespace(
            data="finish_daily_conversation_02",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=False),
            patch.object(bot, "complete_lesson_with_rewards") as complete,
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock) as voice,
        ):
            await bot.finish_lesson(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("تەواو بکە", query.message.reply_text.await_args.args[0])
        complete.assert_not_called()
        voice.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
