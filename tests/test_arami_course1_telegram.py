import unittest
from pathlib import Path

from arami_course1_telegram import (
    AramiCourseTelegramError,
    _plain_markdown,
    course_menu_keyboard,
    load_lesson_source,
    load_manifest,
)


ROOT = Path(__file__).resolve().parents[1]


class AramiCourseTelegramTests(unittest.TestCase):
    def test_manifest_has_exactly_21_numbered_lessons(self):
        manifest = load_manifest(ROOT)
        self.assertEqual(len(manifest["lessons"]), 21)
        self.assertEqual(
            [item["number"] for item in sorted(manifest["lessons"], key=lambda item: item["number"])],
            list(range(1, 22)),
        )

    def test_course_menu_exposes_all_21_lessons(self):
        keyboard = course_menu_keyboard(load_manifest(ROOT))
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len(buttons), 21)
        self.assertEqual(
            {button.callback_data for button in buttons},
            {f"aramiC:lesson:{number}" for number in range(1, 22)},
        )

    def test_every_registered_source_is_read_from_its_manifest_path(self):
        manifest = load_manifest(ROOT)
        for lesson in manifest["lessons"]:
            if lesson["number"] == 15:
                continue
            with self.subTest(lesson=lesson["number"]):
                loaded, source = load_lesson_source(ROOT, lesson["number"])
                self.assertEqual(loaded["id"], lesson["id"])
                self.assertTrue(source.strip())

    def test_missing_lesson_15_source_is_never_replaced_with_another_lesson(self):
        with self.assertRaises(AramiCourseTelegramError):
            load_lesson_source(ROOT, 15)

    def test_markdown_renderer_preserves_words_and_table_values(self):
        rendered = _plain_markdown(
            "# سەردێڕ\n\n| پیت | هاوتا |\n|---|---|\n| چ | ç |\n"
        )
        self.assertIn("سەردێڕ", rendered)
        self.assertIn("چ • ç", rendered)
        self.assertNotIn("|---|", rendered)

    def test_invalid_lesson_numbers_are_rejected(self):
        for value in (0, 22, True, "5"):
            with self.subTest(value=value):
                with self.assertRaises(AramiCourseTelegramError):
                    load_lesson_source(ROOT, value)


if __name__ == "__main__":
    unittest.main()
