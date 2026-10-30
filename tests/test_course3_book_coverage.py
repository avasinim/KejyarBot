"""Regression checks for complete Course 3 punctuation coverage from the source book."""
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3BookCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.course = json.load(source)
        cls.lessons = cls.course["lessons"]

    def test_course3_keeps_66_lessons_in_order_and_source_review_state(self):
        self.assertEqual(len(self.lessons), 66)
        self.assertEqual([lesson["number"] for lesson in self.lessons], list(range(1, 67)))
        self.assertTrue(all(
            lesson["review_status"] == "draft_editorial_review"
            for lesson in self.lessons
        ))

    def test_final_punctuation_lesson_covers_book_subsections_12_through_19(self):
        lesson = self.lessons[61]
        content = " ".join(
            [lesson["title"], lesson["objective"]]
            + lesson["key_points"]
            + [value for pair in lesson["examples"] for value in pair]
            + lesson["exercises"]
            + lesson["comprehension"]
        )
        for marker in ("/", "ر", "[]", "#", "*", "=", "&", "_", "{}"):
            self.assertIn(marker, content)
        self.assertEqual(lesson["source"]["book"], "پوختەی ڕێنووس و خاڵبەندی")
        self.assertEqual(lesson["source"]["author"], "دیاکۆ هاشمی")
        self.assertEqual(lesson["source"]["edition"], 4)
        self.assertEqual(lesson["source"]["pages"], "٨٣–٨٤")
        self.assertIn("پەڕە ٨٣–٨٤", lesson["source"]["source_policy"])
        self.assertGreaterEqual(len(lesson["quiz"]), 3)

    def test_appendix_and_book_back_matter_remain_separate_lessons(self):
        self.assertEqual(
            [lesson["title"] for lesson in self.lessons[62:]],
            ["پاشەکی و ڕوونکردنەوە", "ژێدەر", "دەرەنجام", "سوپاسنامە و تەواو"],
        )


if __name__ == "__main__":
    unittest.main()
