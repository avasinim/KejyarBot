"""Regression coverage for complete source subsections in Course 3 lessons 40 and 43."""
import json
import unittest
from pathlib import Path


COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3SourceCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_lesson_40_covers_all_topics_on_book_page_48(self):
        lesson = self.lessons[39]
        content = " ".join(
            [lesson["title"], lesson["objective"]]
            + lesson["key_points"]
            + [item for pair in lesson["examples"] for item in pair]
            + lesson["exercises"]
        )
        for term in ("یەکشەممە", "دارمۆز", "بە پێی", "بەپێی"):
            self.assertIn(term, content)
        self.assertGreaterEqual(len(lesson["quiz"]), 3)

    def test_lesson_43_covers_it_decisions_and_abbreviation_rules(self):
        lesson = self.lessons[42]
        content = " ".join(
            [lesson["title"], lesson["objective"]]
            + lesson["key_points"]
            + [item for pair in lesson["examples"] for item in pair]
            + lesson["exercises"]
        )
        for term in ("U+200C", "سەهۆڵفرۆش", "پ.د.ک", "PDF", "هەڵەچن"):
            self.assertIn(term, content)
        self.assertGreaterEqual(len(lesson["quiz"]), 3)


if __name__ == "__main__":
    unittest.main()
