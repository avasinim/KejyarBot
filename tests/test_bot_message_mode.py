import html
import re
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
        ):
            await bot.message(update, context)

        self.assertTrue(context.user_data["daily_chat_mode"])
        reply.assert_called_once_with(
            "دەمەوێت لە بازاڕ گفتوگۆ بکەم", context.user_data
        )
        update.message.reply_text.assert_awaited_once()

    async def test_course_menu_button_exits_daily_chat_mode(self):
        update, context = self.make_update_context(
            "📘 کۆرسەکان",
            {"daily_chat_mode": True, "daily_chat_scenario": "market", "daily_chat_stage": 2},
        )
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        self.assertFalse(context.user_data["daily_chat_mode"])
        self.assertNotIn("daily_chat_scenario", context.user_data)
        self.assertNotIn("daily_chat_stage", context.user_data)
        update.message.reply_text.assert_awaited_once()
        keyboard = update.message.reply_text.await_args.kwargs["reply_markup"]
        callbacks = [button.callback_data for row in keyboard.inline_keyboard for button in row]
        self.assertIn("course_arami_orthography_foundations", callbacks)
        self.assertNotIn("course_orthography_basic", callbacks)


    async def test_arami_menu_opens_all_21_lessons_with_practice_and_assessment(self):
        update, context = self.make_update_context("📕 ڕێنووسی سەرەتاییی کوردی")
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "can_open", return_value=True),
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        call = update.message.reply_text.await_args
        self.assertIn("٢١ وانە", call.args[0])
        keyboard = call.kwargs["reply_markup"]
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        reads = [button.callback_data for button in buttons if button.callback_data.endswith(":lesson") or button.callback_data.startswith("aramiC:lesson:")]
        practices = [button.callback_data for button in buttons if ":practice" in button.callback_data]
        assessments = [button.callback_data for button in buttons if ":assessment" in button.callback_data]
        self.assertEqual(len(reads), 21)
        self.assertEqual(len(practices), 21)
        self.assertEqual(len(assessments), 21)
        self.assertIn("arami1:practice", practices)
        self.assertIn("arami5:practice", practices)
        self.assertIn("aramiC:practice:21", practices)

    async def test_learning_path_reports_all_21_arami_lessons_and_progress(self):
        update, context = self.make_update_context("🧭 ڕێگای فێربوون")
        completed = ["arami_course1_lesson_01", "arami_course1_lesson_02"]
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=completed),
            patch.object(bot, "can_open", side_effect=lambda user_id, lesson_id: lesson_id == "arami_course1_lesson_03"),
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        output = update.message.reply_text.await_args.args[0]
        self.assertIn("پێشکەوتن: 2/21 وانە", output)
        self.assertIn("✅ تەواو کراوە — وانەی 1:", output)
        self.assertIn("🔓 ئامادەیە — وانەی 3:", output)
        self.assertIn("🔒 داخراوە — وانەی 4:", output)
        self.assertEqual(sum(" — وانەی " in line for line in output.splitlines()), 21)

    async def test_latin_menu_key_groups_both_active_latin_courses(self):
        label = "ڕێنووسی لاتینی کوردیی"
        self.assertIn(label, [button.text for row in bot.MENU.keyboard for button in row])
        update, context = self.make_update_context(label)
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        self.assertIn("دوو کۆرسە", update.message.reply_text.await_args.args[0])
        keyboard = update.message.reply_text.await_args.kwargs["reply_markup"]
        callbacks = [row[0].callback_data for row in keyboard.inline_keyboard]
        self.assertEqual(callbacks, [
            "course_kurmanji_latin_orthography",
            "course_kurmanji_latin_grammar",
        ])

    async def test_generic_course_list_does_not_duplicate_latin_courses(self):
        update, context = self.make_update_context("📘 کۆرسەکان")
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        keyboard = update.message.reply_text.await_args.kwargs["reply_markup"]
        callbacks = [row[0].callback_data for row in keyboard.inline_keyboard]
        self.assertNotIn("course_kurmanji_latin_orthography", callbacks)
        self.assertNotIn("course_kurmanji_latin_grammar", callbacks)

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
        self.assertEqual(len(bot.ORDER), 0)
        read_buttons = [
            button for button in buttons
            if button.callback_data.endswith(":lesson") or button.callback_data.startswith("aramiC:lesson:")
        ]
        self.assertEqual(len(read_buttons), 21)
        self.assertIn("ڕێنووسی سەرەتاییی کوردی", call.args[0])


    async def test_quiz_selection_menu_shows_readable_lesson_titles(self):
        update, context = self.make_update_context("📝 تاقیکردنەوەکان")
        completed = list(bot.ORDER)
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=completed),
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        call = update.message.reply_text.await_args
        self.assertNotIn("reply_markup", call.kwargs)
        self.assertIn("سەرەتا وانەیەک بکەرەوە", call.args[0])
        self.assertEqual(bot.ORDER, [])

    async def test_clickable_practice_menu_lists_only_lesson_three_and_both_latin_courses(self):
        update, context = self.make_update_context("🎯 ڕاهێنانی کرتەیی")
        completed = [
            *bot.ORDER,
            *bot.COURSE_LESSON_ORDER["kurmanji_latin_orthography"],
            *bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"],
        ]
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=completed),
        ):
            await bot.message(update, context)

        self.assertIn("ڕاهێنانی کرتەیی", update.message.reply_text.await_args.args[0])
        keyboard = update.message.reply_text.await_args.kwargs["reply_markup"]
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        expected = [
            *bot.COURSE_LESSON_ORDER["kurmanji_latin_orthography"],
            *bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"],
        ]
        lesson_callbacks = [
            button.callback_data for button in buttons
            if button.callback_data.startswith("quiz_")
        ]
        self.assertEqual(
            lesson_callbacks,
            [bot.lesson_practice_callback(lesson) for lesson in expected[:bot.QUIZ_MENU_PAGE_SIZE]],
        )
        self.assertEqual(buttons[-1].callback_data, "quizmenu:practice:1")

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
        self.assertEqual("".join(html.unescape(re.sub(r"<[^>]+>", "", chunk)) for chunk in chunks), bot.add_kejyar_brand_signature(content))
        self.assertTrue(all(call.kwargs.get("parse_mode") == "HTML" for call in calls))

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
        self.assertIn("نەناسراوە", query.message.reply_text.await_args.args[0])
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


    async def test_dictionary_section_has_clean_single_heading_and_real_line_breaks(self):
        update, context = self.make_update_context("📖 وشەنامەی کوردی")
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        output = update.message.reply_text.await_args_list[0].args[0]
        self.assertIn("╭━━━━━━━━━━━━━━━━━━━━╮\n", output)
        self.assertNotIn(r"\n", output)
        self.assertEqual(output.count("📚 <b>کتێبخانەی وشەنامەی کوردی</b>"), 1)
        self.assertNotIn("📖 <b>وشەنامەی کوردی</b>", output)

    async def test_keyboard_section_has_clean_single_heading_and_real_line_breaks(self):
        update, context = self.make_update_context("⌨️ تەختەکلیلی کوردی")
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        output = update.message.reply_text.await_args_list[0].args[0]
        self.assertIn("╭━━━━━━━━━━━━━━━━━━━━╮\n", output)
        self.assertNotIn(r"\n", output)
        self.assertEqual(output.count("⌨️ <b>ناوەندی تەختەکلیلی کوردی</b>"), 1)
        self.assertNotIn("⌨️ <b>تەختەکلیلی کوردی</b>", output)

    async def test_kurmanji_months_callback_preserves_bold_html_tags(self):
        query = SimpleNamespace(
            data="months:kurmanji",
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        await bot.open_kurdish_months(update, SimpleNamespace(user_data={}))

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        output = query.message.reply_text.await_args
        self.assertIn("<b>مانگەکانی کورمانجی</b>", output.args[0])
        self.assertNotIn("&lt;b&gt;", output.args[0])
        self.assertNotIn("&lt;/b&gt;", output.args[0])
        self.assertEqual(output.kwargs["parse_mode"], "HTML")
        self.assertIsNotNone(output.kwargs["reply_markup"])

    async def test_months_menu_heading_uses_real_line_breaks(self):
        update, context = self.make_update_context("🗓️ مانگەکانی ساڵ لەناو کورداندا")
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        output = update.message.reply_text.await_args.args[0]
        self.assertIn("╭━━━━━━━━━━━━━━━━━━━━╮\n", output)
        self.assertNotIn(r"\n", output)


if __name__ == "__main__":
    unittest.main()
