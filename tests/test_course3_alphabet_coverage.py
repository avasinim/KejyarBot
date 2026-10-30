"""Regression coverage for the complete Kurdish alphabet lesson in Course 3."""
import json
import unittest
from pathlib import Path


COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3AlphabetCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_lesson_1_contains_all_34_letters_and_both_letter_classes(self):
        lesson = self.lessons[0]
        examples = " ".join(item for pair in lesson["examples"] for item in pair)
        for letter in ("ئـ", "ا", "ب", "پ", "ت", "ج", "چ", "ح", "خ", "د", "ر", "ڕ",
                       "ز", "ژ", "س", "ش", "ع", "غ", "ف", "ڤ", "ق", "ک", "گ", "ل",
                       "ڵ", "م", "ن", "هـ", "ە", "و", "وو", "ۆ", "ی", "ێ"):
            self.assertIn(letter, examples)
        self.assertIn("پیتەلکاوەکان", examples)
        self.assertIn("پیتەنەلکاوەکان", examples)
        self.assertGreaterEqual(len(lesson["quiz"]), 3)


if __name__ == "__main__":
    unittest.main()
