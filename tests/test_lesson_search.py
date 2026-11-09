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


if __name__ == "__main__":
    unittest.main()
