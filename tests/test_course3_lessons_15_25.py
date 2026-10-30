"""Regression tests for source-aligned Course 3 lessons 15–25."""
import json
import unittest
from pathlib import Path

COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3Lessons15To25Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_lessons_15_to_25_have_complete_practice_sets(self):
        for number in range(15, 26):
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)
                for question in lesson["quiz"]:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    self.assertTrue(question["explanation"])

    def test_compound_verb_lessons_distinguish_infinitive_and_conjugated_forms(self):
        for number, terms in {
            16: ("فێرکردن", "فێر دەکەم"),
            17: ("چاوداگرتن", "چاو دادەگرم"),
            18: ("دەستپێکردن", "دەست پێ دەکات"),
            19: ("دەستپێڕاگەیشتن", "دەستی لێ هەڵدەگرم"),
            20: ("نامەکەم پێ دا", "دەستی لێ دا"),
            21: ("لەدایکبوون", "لەدایک دەبم"),
        }.items():
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
                for term in terms:
                    self.assertIn(term, content)

    def test_lesson_25_preserves_root_d_before_postposition_da(self):
        lesson = self.lessons[24]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("لەبن بەرددا", content)
        self.assertIn("ئەحمەد", content)
        self.assertIn("قادر", content)


if __name__ == "__main__":
    unittest.main()
