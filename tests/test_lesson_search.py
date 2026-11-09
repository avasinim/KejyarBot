"""Regression tests for academic lesson-title search."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class LessonSearchTests(unittest.IsolatedAsyncioTestCase):
    def make_update(self, text, user_data=None):
        message = SimpleNamespace(text=text, reply_text=AsyncMock())
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=24680),
        )
        context = SimpleNamespace(user_data=user_data if user_data is not None else {})
        return update, context

    async def test_search_button_enters_search_mode_and_exits_daily_chat(self):
        update, context = self.make_update(
            "🔎 گەڕانی وانە",
            {"daily_chat_mode": True, "daily_chat_scenario": "market"},
        )
        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        self.assertTrue(context.user_data["lesson_search_mode"])
        self.assertFalse(context.user_data["daily_chat_mode"])
        self.assertNotIn("daily_chat_scenario", context.user_data)
        update.message.reply_text.assert_awaited_once()
        self.assertEqual(
            update.message.reply_text.await_args.kwargs["parse_mode"],
            "HTML",
        )

    async def test_search_finds_course_one_and_other_active_course_titles(self):
        update, context = self.make_update(
            "پیت",
            {"lesson_search_mode": True},
        )
        courses = [
            {"id": "arami_orthography_foundations"},
            {"id": "grammar"},
            {"id": "inactive_course"},
        ]
        arami_manifest = {
            "lessons": [
                {"number": 1, "title": "پیتەکان و دەنگەکان"},
                {"number": 5, "title": "پیتەکان و هاوتای لاتینی"},
                {"number": 2, "title": "ڕێنووس"},
            ]
        }
        course_lessons = {
            "grammar": ["grammar_01", "grammar_02"],
            "inactive_course": ["inactive_01"],
        }
        lesson_data = {
            "grammar_01": {"title": "پیت و دەنگ لە ڕێزماندا"},
            "grammar_02": {"title": "مۆرفۆلۆجی"},
            "inactive_01": {"title": "پیتەکانی ئەلفوبێ"},
        }
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "COURSES", courses),
            patch.object(bot, "course_is_active", side_effect=lambda course_id: course_id != "inactive_course"),
            patch.object(bot, "load_arami_course1_manifest", return_value=arami_manifest),
            patch.object(bot, "COURSE_LESSON_ORDER", course_lessons),
            patch.object(bot, "LESSON_DATA", lesson_data),
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        rendered = update.message.reply_text.await_args.args[0]
        self.assertIn("3 وانە دۆزرایەوە", rendered)
        keyboard = update.message.reply_text.await_args.kwargs["reply_markup"]
        callbacks = [
            button.callback_data
            for row in keyboard.inline_keyboard
            for button in row
        ]
        self.assertEqual(
            callbacks,
            [
                "arami1:lesson",
                "arami5:lesson",
                "open_lesson_grammar_01",
            ],
        )
        self.assertNotIn("open_lesson_inactive_01", callbacks)
        self.assertNotIn("lesson_search_mode", context.user_data)

    async def test_search_normalizes_case_and_whitespace_in_titles(self):
        update, context = self.make_update(
            "  مۆرفۆلۆجی   ",
            {"lesson_search_mode": True},
        )
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "COURSES", [{"id": "grammar"}]),
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "COURSE_LESSON_ORDER", {"grammar": ["grammar_01"]}),
            patch.object(bot, "LESSON_DATA", {
                "grammar_01": {"title": "  مۆرفۆلۆجی   زمانی کوردی  "},
            }),
        ):
            await bot.message(update, context)

        keyboard = update.message.reply_text.await_args.kwargs["reply_markup"]
        self.assertEqual(
            keyboard.inline_keyboard[0][0].callback_data,
            "open_lesson_grammar_01",
        )

    async def test_search_reports_no_match_without_exposing_lesson_actions(self):
        update, context = self.make_update(
            "پیت",
            {"lesson_search_mode": True},
        )
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "COURSES", [{"id": "grammar"}]),
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "COURSE_LESSON_ORDER", {"grammar": ["grammar_01"]}),
            patch.object(bot, "LESSON_DATA", {
                "grammar_01": {"title": "مۆرفۆلۆجی"},
            }),
        ):
            await bot.message(update, context)

        update.message.reply_text.assert_awaited_once()
        self.assertIn(
            "هیچ وانەیەک بەو وشەیە نەدۆزرایەوە",
            update.message.reply_text.await_args.args[0],
        )
        self.assertIs(update.message.reply_text.await_args.kwargs["reply_markup"], bot.MENU)


    async def test_search_results_are_paginated_without_dropping_matches(self):
        results = [(f"Lesson {i}", f"open_lesson_grammar_{i:02d}") for i in range(1, 26)]
        keyboard, page, page_count, first, last = bot.lesson_search_keyboard(results, 0)
        self.assertEqual((page, page_count, first, last), (0, 3, 1, 12))
        callbacks = [button.callback_data for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len(callbacks), 13)
        self.assertEqual(callbacks[-1], "lessonsearch:1")

        second, page, page_count, first, last = bot.lesson_search_keyboard(results, 1)
        callbacks = [button.callback_data for row in second.inline_keyboard for button in row]
        self.assertEqual((page, page_count, first, last), (1, 3, 13, 24))
        self.assertEqual(callbacks[-1], "lessonsearch:2")
        self.assertEqual(callbacks[-2], "lessonsearch:0")

        third, page, page_count, first, last = bot.lesson_search_keyboard(results, 2)
        callbacks = [button.callback_data for row in third.inline_keyboard for button in row]
        self.assertEqual((page, page_count, first, last), (2, 3, 25, 25))
        self.assertEqual(callbacks[-1], "lessonsearch:1")

    async def test_search_page_callback_edits_existing_result_message(self):
        message = SimpleNamespace(reply_text=AsyncMock(), edit_text=AsyncMock())
        query = SimpleNamespace(
            data="lessonsearch:1",
            message=message,
            answer=AsyncMock(),
            edit_message_text=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        results = [(f"Lesson {i}", f"open_lesson_grammar_{i:02d}") for i in range(1, 15)]
        context = SimpleNamespace(user_data={"lesson_search_results": results})

        await bot.open_lesson_search_page(update, context)

        query.answer.assert_awaited_once()
        query.edit_message_text.assert_awaited_once()
        rendered = query.edit_message_text.await_args.args[0]
        self.assertIn("13–14", rendered)
        keyboard = query.edit_message_text.await_args.kwargs["reply_markup"]
        callbacks = [button.callback_data for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(callbacks[-1], "lessonsearch:0")
        self.assertFalse(any(item.startswith("lessonsearch:2") for item in callbacks))


if __name__ == "__main__":
    unittest.main()
