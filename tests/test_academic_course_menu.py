import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class AcademicCourseMenuTests(unittest.TestCase):
    def test_course_catalogue_uses_two_columns_and_preserves_lesson_callbacks(self):
        lesson_ids = ["sample_01", "sample_02", "sample_03"]
        lesson_data = {
            lesson_id: {"title": f"ناونیشانی وانەی {index}"}
            for index, lesson_id in enumerate(lesson_ids, 1)
        }
        with patch.multiple(
            bot,
            COURSE_LESSON_ORDER={"sample": lesson_ids},
            LESSON_DATA=lesson_data,
            get_completed_lessons=lambda _user_id: ["sample_01"],
            get_completed_beta_lessons=lambda _user_id: [],
            can_open=lambda _user_id, lesson_id: lesson_id == "sample_01",
            lesson_is_beta_review=lambda _lesson_id: False,
            lesson_is_pending_review=lambda _lesson_id: False,
        ):
            keyboard, page_count = bot.course_menu_keyboard("sample", 123, 0)

        self.assertEqual(page_count, 1)
        self.assertEqual([len(row) for row in keyboard.inline_keyboard], [2, 1])
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(
            [button.callback_data for button in buttons],
            [f"open_lesson_{lesson_id}" for lesson_id in lesson_ids],
        )
        self.assertIn("01", buttons[0].text)
        self.assertIn("02", buttons[1].text)
        self.assertTrue(buttons[0].text.startswith("✅"))
        self.assertTrue(buttons[1].text.startswith("🔒"))
        self.assertTrue(buttons[2].text.startswith("🔒"))

    def test_course_catalogue_keeps_page_navigation(self):
        lesson_ids = [f"sample_{index:02d}" for index in range(1, 14)]
        lesson_data = {
            lesson_id: {"title": f"وانەی {index}"}
            for index, lesson_id in enumerate(lesson_ids, 1)
        }
        with patch.multiple(
            bot,
            COURSE_LESSON_ORDER={"sample": lesson_ids},
            LESSON_DATA=lesson_data,
            get_completed_lessons=lambda _user_id: [],
            get_completed_beta_lessons=lambda _user_id: [],
            can_open=lambda _user_id, _lesson_id: True,
            lesson_is_beta_review=lambda _lesson_id: False,
            lesson_is_pending_review=lambda _lesson_id: False,
        ):
            first_page, page_count = bot.course_menu_keyboard("sample", 123, 0)
            second_page, second_page_count = bot.course_menu_keyboard("sample", 123, 1)

        self.assertEqual(page_count, 2)
        self.assertEqual(second_page_count, 2)
        self.assertEqual([len(row) for row in first_page.inline_keyboard], [2, 2, 2, 2, 2, 2, 1])
        self.assertEqual([len(row) for row in second_page.inline_keyboard], [1, 1])
        self.assertEqual(
            first_page.inline_keyboard[-1][0].callback_data,
            "coursepage:sample:1",
        )
        self.assertEqual(
            second_page.inline_keyboard[-1][0].callback_data,
            "coursepage:sample:0",
        )


    def test_locked_state_takes_precedence_over_beta_review_and_stale_completion(self):
        lesson_ids = ["beta_01", "pending_02", "stale_03", "open_04"]
        lesson_data = {
            "beta_01": {"title": "وانەی Beta"},
            "pending_02": {"title": "وانەی پێداچوونەوە"},
            "stale_03": {"title": "وانەی پێشتر تەواوکراو"},
            "open_04": {"title": "وانەی کراوە"},
        }
        with patch.multiple(
            bot,
            COURSE_LESSON_ORDER={"sample": lesson_ids},
            LESSON_DATA=lesson_data,
            get_completed_lessons=lambda _user_id: ["stale_03"],
            get_completed_beta_lessons=lambda _user_id: [],
            can_open=lambda _user_id, lesson_id: lesson_id == "open_04",
            lesson_is_beta_review=lambda lesson_id: lesson_id == "beta_01",
            lesson_is_pending_review=lambda lesson_id: lesson_id == "pending_02",
        ):
            keyboard, page_count = bot.course_menu_keyboard("sample", 123, 0)

        self.assertEqual(page_count, 1)
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        self.assertTrue(buttons[0].text.startswith("🔒 🧪"))
        self.assertTrue(buttons[1].text.startswith("🔒 📝"))
        self.assertTrue(buttons[2].text.startswith("🔒"))
        self.assertTrue(buttons[3].text.startswith("🔓"))


class InactiveAramiCourseCallbackTests(unittest.IsolatedAsyncioTestCase):
    async def test_stale_course_button_does_not_open_inactive_arami_catalogue(self):
        query = SimpleNamespace(
            data="course_arami_orthography_foundations",
            from_user=SimpleNamespace(id=123),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace()

        with patch.object(bot, "course_is_active", return_value=False):
            with patch.object(bot, "load_arami_course1_manifest") as load_manifest:
                with patch.object(bot, "load_arami_course1_question_banks") as load_banks:
                    await bot.open_course(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("چالاک نییە", query.message.reply_text.await_args.args[0])
        load_manifest.assert_not_called()
        load_banks.assert_not_called()



class BetaProgressDisplayTests(unittest.IsolatedAsyncioTestCase):
    async def test_course_page_counts_only_current_beta_review_lessons(self):
        message = SimpleNamespace(reply_text=AsyncMock(), edit_text=AsyncMock())
        course = {
            "id": "grammar",
            "title": "کۆرسی ٤: ڕێزمان",
            "description": "٤٦ وانە",
        }
        order = ["grammar_32"]
        with patch.object(bot, "COURSES", [course]), \
             patch.object(bot, "course_is_active", return_value=True), \
             patch.object(bot, "COURSE_LESSON_ORDER", {"grammar": order}), \
             patch.object(bot, "course_menu_keyboard", return_value=("keyboard", 1)), \
             patch.object(bot, "get_completed_lessons", return_value=[]), \
             patch.object(
                 bot,
                 "get_completed_beta_lessons",
                 return_value=["grammar_32", "grammar_99", "daily_conversation_01"],
             ), \
             patch.object(bot, "lesson_is_beta_review", side_effect=lambda lesson: lesson == "grammar_32"):
            await bot.send_course_page(message, "grammar", 123)

        message.reply_text.assert_awaited_once()
        page_text = message.reply_text.await_args.args[0]
        self.assertIn("Beta: 1/1", page_text)
        self.assertNotIn("Beta: 3/1", page_text)


class CoursePageRenderingTests(unittest.IsolatedAsyncioTestCase):
    async def test_course_title_and_description_are_html_escaped(self):
        message = SimpleNamespace(reply_text=AsyncMock(), edit_text=AsyncMock())
        course = {"id": "sample", "title": "<Test & Course>", "description": "desc <tag> & details"}
        with (
            patch.object(bot, "COURSES", [course]),
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "course_menu_keyboard", return_value=("keyboard", 1)),
            patch.object(bot, "COURSE_LESSON_ORDER", {"sample": ["sample_01"]}),
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "get_completed_beta_lessons", return_value=[]),
            patch.object(bot, "lesson_is_beta_review", return_value=False),
        ):
            await bot.send_course_page(message, "sample", 123)

        rendered = message.reply_text.await_args.args[0]
        self.assertIn("<b>&lt;Test &amp; Course&gt;</b>", rendered)
        self.assertIn("desc &lt;tag&gt; &amp; details", rendered)
        self.assertEqual(message.reply_text.await_args.kwargs["parse_mode"], "HTML")


    async def test_course_page_rejects_non_decimal_unicode_digits(self):
        message = SimpleNamespace(reply_text=AsyncMock(), edit_text=AsyncMock())
        query = SimpleNamespace(
            data="coursepage:sample:²",
            from_user=SimpleNamespace(id=123),
            answer=AsyncMock(),
            message=message,
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace()
        await bot.open_course_page(update, context)

        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()
        self.assertIn("نادروستە", message.reply_text.await_args.args[0])
        message.edit_text.assert_not_awaited()


class QuizMenuPaginationTests(unittest.IsolatedAsyncioTestCase):
    async def test_quiz_menu_page_edits_existing_message(self):
        message = SimpleNamespace(reply_text=AsyncMock(), edit_text=AsyncMock())
        query = SimpleNamespace(
            data="quizmenu:practice:1",
            message=message,
            from_user=SimpleNamespace(id=123),
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        items = [(f"ڕاهێنان {i}", f"quiz_{i}_start") for i in range(1, 15)]
        with patch.object(bot, "quiz_menu_items", return_value=items):
            await bot.open_quiz_menu_page(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        message.edit_text.assert_awaited_once()
        message.reply_text.assert_not_awaited()
        self.assertIn("13–14", message.edit_text.await_args.args[0])
        keyboard = message.edit_text.await_args.kwargs["reply_markup"]
        callbacks = [button.callback_data for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(callbacks, ["quiz_13_start", "quiz_14_start", "quizmenu:practice:0"])

    async def test_empty_quiz_menu_page_replaces_stale_menu_message(self):
        message = SimpleNamespace(reply_text=AsyncMock(), edit_text=AsyncMock())
        with patch.object(bot, "quiz_menu_items", return_value=[]):
            await bot.send_quiz_menu(message, 123, "practice", edit=True)
        message.edit_text.assert_awaited_once()
        message.reply_text.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
