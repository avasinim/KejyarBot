"""Regression tests for the replacement of legacy Course 1 by Arami's 20 lessons."""
import json
import unittest
from pathlib import Path

import bot
from arami_course1_telegram import load_manifest, load_question_banks, course_menu_keyboard


ROOT = Path(__file__).resolve().parents[1]


class OrthographyCourseStructureTests(unittest.TestCase):
    def test_legacy_22_lesson_course_is_retired_from_runtime(self):
        with (ROOT / "courses.json").open(encoding="utf-8") as source:
            manifest = json.load(source)
        courses = {item["id"]: item for item in manifest["courses"]}
        legacy = courses["orthography_basic"]
        self.assertEqual(legacy["status"], "retired_replaced_by_arami_course1")
        self.assertEqual(legacy["lesson_ids"], [])
        self.assertFalse(bot.course_is_active("orthography_basic"))
        self.assertEqual(bot.COURSE_LESSON_ORDER["orthography_basic"], [])
        self.assertEqual(bot.ORDER, [])

    def test_arami_course_one_is_the_only_active_course_one_with_20_lessons(self):
        manifest = load_manifest(ROOT)
        banks = load_question_banks(ROOT)
        self.assertEqual(manifest["course_total_lessons"], 20)
        self.assertEqual([x["number"] for x in manifest["lessons"]], list(range(1, 21)))
        self.assertEqual(len(banks), 18)
        keyboard = course_menu_keyboard(manifest, banks)
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        read = [b for b in buttons if b.callback_data.endswith(":lesson") or b.callback_data.startswith("aramiC:lesson:")]
        self.assertEqual(len(read), 20)

    def test_course_two_three_and_latin_courses_are_unchanged_and_active(self):
        self.assertTrue(bot.course_is_active("daily_conversation"))
        self.assertTrue(bot.course_is_active("unified_orthography"))
        self.assertTrue(bot.course_is_active("kurmanji_latin_orthography"))
        self.assertTrue(bot.course_is_active("kurmanji_latin_grammar"))
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["daily_conversation"]), 48)
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["unified_orthography"]), 66)
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["kurmanji_latin_orthography"]), 12)
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"]), 12)

    def test_dynamic_speech_remains_disabled_by_default(self):
        self.assertEqual(__import__("os").environ.get("KEJYAR_ENABLE_DYNAMIC_SPEECH", "false").lower(), "false")


if __name__ == "__main__":
    unittest.main()
