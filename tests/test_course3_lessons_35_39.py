"""Regression tests for source-aligned Course 3 lessons 35–39."""
import json
import unittest
from pathlib import Path

COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3Lessons35To39Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_lessons_35_to_39_have_complete_practice_sets(self):
        for number in range(35, 40):
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)
                for question in lesson["quiz"]:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    self.assertTrue(question["explanation"])

    def test_lesson_35_mentions_the_zero_width_non_joiner_decision(self):
        lesson = self.lessons[34]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("U+200C", content)
        self.assertIn("سەهۆڵفرۆش", content)

    def test_lesson_36_preserves_long_uu(self):
        lesson = self.lessons[35]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("خانووەکەم", content)
        self.assertIn("جوانووەکەم", content)

    def test_lesson_38_covers_singular_and_plural_clitics(self):
        lesson = self.lessons[37]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("نووسیی", content)
        self.assertIn("نووسییان", content)

    def test_lesson_39_preserves_vav_as_a_distinct_letter(self):
        lesson = self.lessons[38]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("ڤ", "ف", "و", "ئەرشیڤ"):
            self.assertIn(marker, content)


if __name__ == "__main__":
    unittest.main()
