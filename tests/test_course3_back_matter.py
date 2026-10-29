"""Regression checks for the final Course 3 book back matter."""
import json
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3BackMatterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_back_matter_titles_match_the_book_sequence(self):
        self.assertEqual(
            [lesson["title"] for lesson in self.lessons[62:]],
            ["پاشەکی", "ژێدەر", "دەرەنجام", "تەواو"],
        )

    def test_back_matter_lessons_have_practice_and_keep_draft_status(self):
        for lesson in self.lessons[62:]:
            with self.subTest(lesson=lesson["number"]):
                self.assertEqual(lesson["review_status"], "draft_editorial_review")
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)

    def test_appendix_and_conclusion_claims_match_source(self):
        appendix = " ".join(self.lessons[62]["key_points"] + [v for pair in self.lessons[62]["examples"] for v in pair])
        references = " ".join(self.lessons[63]["key_points"] + [v for pair in self.lessons[63]["examples"] for v in pair])
        conclusion = " ".join(self.lessons[64]["key_points"] + [v for pair in self.lessons[64]["examples"] for v in pair])
        self.assertIn("٠ و ١", appendix)
        self.assertIn("Svenska skrivregler", references)
        self.assertIn("مەبەست", conclusion)
        self.assertIn("ڕێنووسی یەکگرتوو", conclusion)


if __name__ == "__main__":
    unittest.main()
