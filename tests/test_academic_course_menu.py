import unittest
from unittest.mock import patch

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
            can_open=lambda _user_id, lesson_id: lesson_id != "sample_03",
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


if __name__ == "__main__":
    unittest.main()
