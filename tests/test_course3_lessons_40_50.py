"""Regression tests for source-aligned Course 3 lessons 40–50."""
import json
import unittest
from pathlib import Path

COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3Lessons40To50Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_lessons_40_to_50_have_complete_practice_sets(self):
        for number in range(40, 51):
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)
                for question in lesson["quiz"]:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    self.assertTrue(question["explanation"])

    def test_weekday_and_fruit_tree_compounds(self):
        lesson = self.lessons[39]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for term in ("یەکشەممە", "یەک شەممەی تر", "دارهەنار", "بە پێی", "بەپێی"):
            self.assertIn(term, content)

    def test_interfix_w_and_adjective_noun_distinction(self):
        lesson41 = " ".join(self.lessons[40]["key_points"] + [v for pair in self.lessons[40]["examples"] for v in pair])
        lesson42 = " ".join(self.lessons[41]["key_points"] + [v for pair in self.lessons[41]["examples"] for v in pair])
        self.assertIn("هەمووان", lesson41)
        self.assertIn("هاتوچۆ", lesson41)
        self.assertIn("گوڵەگەنم", lesson42)
        self.assertIn("کچە جوانەکە", lesson42)

    def test_passive_and_shortened_phrases_are_separated(self):
        passive = " ".join(self.lessons[44]["key_points"] + [v for pair in self.lessons[44]["examples"] for v in pair])
        phrases = " ".join(self.lessons[45]["key_points"] + [v for pair in self.lessons[45]["examples"] for v in pair])
        self.assertIn("دەنووسرێت", passive)
        self.assertIn("وانەکە وترایەوە", passive)
        self.assertIn("شەو شاد", phrases)
        self.assertIn("شەوشادیم لێ کرد", phrases)

    def test_common_error_and_typology_examples(self):
        errors = " ".join(self.lessons[46]["key_points"] + [v for pair in self.lessons[46]["examples"] for v in pair])
        typology = " ".join(self.lessons[47]["key_points"] + [v for pair in self.lessons[47]["examples"] for v in pair])
        self.assertIn("بەرانبەر", errors)
        self.assertIn("سەرپەرشت", errors)
        self.assertIn("زانکۆی پزیشکیی هەولێر", typology)

    def test_ish_rule_and_review_lesson(self):
        ish = " ".join(self.lessons[48]["key_points"] + [v for pair in self.lessons[48]["examples"] for v in pair])
        review = " ".join(self.lessons[49]["key_points"] + [v for pair in self.lessons[49]["examples"] for v in pair])
        self.assertIn("سلێمانییش", ish)
        self.assertIn("پاوەییش", ish)
        self.assertIn("خۆراوا", review)
        self.assertIn("کردبێت", review)


if __name__ == "__main__":
    unittest.main()
