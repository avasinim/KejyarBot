"""Regression tests for Course 3 punctuation lessons 51–61."""
import json
import unittest
from pathlib import Path

COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3PunctuationLessonsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_all_punctuation_lessons_have_complete_practice(self):
        for number in range(51, 63):
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)
                for question in lesson["quiz"]:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    self.assertTrue(question["explanation"])

    def test_period_colon_comma_and_semicolon_rules(self):
        period = " ".join(self.lessons[50]["key_points"] + [v for pair in self.lessons[50]["examples"] for v in pair])
        colon = " ".join(self.lessons[51]["key_points"] + [v for pair in self.lessons[51]["examples"] for v in pair])
        comma = " ".join(self.lessons[52]["key_points"] + [v for pair in self.lessons[52]["examples"] for v in pair])
        semicolon = " ".join(self.lessons[53]["key_points"] + [v for pair in self.lessons[53]["examples"] for v in pair])
        self.assertIn("د. سۆران", period)
        self.assertIn("ی.ن.ک.", period)
        self.assertIn("١٢:٢٧:١٢", colon)
        self.assertIn("بەزەیی، پێویست نییە", comma)
        self.assertIn("بەڵام", semicolon)

    def test_question_and_exclamation_scope(self):
        question = " ".join(self.lessons[54]["key_points"] + [v for pair in self.lessons[54]["examples"] for v in pair])
        exclamation = " ".join(self.lessons[55]["key_points"] + [v for pair in self.lessons[55]["examples"] for v in pair])
        self.assertIn("پرسیاری ناڕاستەوخۆ", question)
        self.assertIn("پرسیاری ڕیتۆریکی", question)
        self.assertIn("سوپاسگوزاری", exclamation)
        self.assertIn("بە کەمی", exclamation)

    def test_quote_and_parenthesis_usage(self):
        quotes = " ".join(self.lessons[56]["key_points"] + [v for pair in self.lessons[56]["examples"] for v in pair])
        parentheses = " ".join(self.lessons[57]["key_points"] + [v for pair in self.lessons[57]["examples"] for v in pair])
        self.assertIn("دەقگێڕانەوەی یەکەم", quotes)
        self.assertIn("firewall", parentheses)
        self.assertIn("١٧٨٣", parentheses)

    def test_dash_ellipsis_and_spaces(self):
        dash = " ".join(self.lessons[58]["key_points"] + [v for pair in self.lessons[58]["examples"] for v in pair])
        ellipsis = " ".join(self.lessons[59]["key_points"] + [v for pair in self.lessons[59]["examples"] for v in pair])
        spaces = " ".join(self.lessons[60]["key_points"] + [v for pair in self.lessons[60]["examples"] for v in pair])
        self.assertIn("٩–١٢", dash)
        self.assertIn("تەنیا سێ", ellipsis)
        self.assertIn("کرێکار", spaces)
        self.assertIn("باس دەکرێت", spaces)
        self.assertIn("کە ماڵت بێ", spaces)

    def test_sources_remain_book_aligned(self):
        for number in range(51, 63):
            with self.subTest(lesson=number):
                source = self.lessons[number - 1]["source"]
                self.assertEqual(source["book"], "پوختەی ڕێنووس و خاڵبەندی")
                self.assertEqual(source["author"], "دیاکۆ هاشمی")
                self.assertEqual(source["edition"], 4)


if __name__ == "__main__":
    unittest.main()
