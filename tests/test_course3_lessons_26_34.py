"""Regression tests for source-aligned Course 3 lessons 26–34."""
import json
import unittest
from pathlib import Path

COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3Lessons26To34Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_lessons_26_to_34_have_complete_practice_sets(self):
        for number in range(26, 35):
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)
                for question in lesson["quiz"]:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    self.assertTrue(question["explanation"])

    def test_preposition_and_postposition_rules_are_distinguished(self):
        preposition = self.lessons[25]
        postposition = self.lessons[26]
        preposition_text = " ".join(preposition["key_points"] + [v for pair in preposition["examples"] for v in pair])
        postposition_text = " ".join(postposition["key_points"] + [v for pair in postposition["examples"] for v in pair])
        self.assertIn("بە هێز", preposition_text)
        self.assertIn("بەهێز", preposition_text)
        self.assertIn("لە کوردستاندا", postposition_text)

    def test_foreign_word_lesson_covers_kurdish_spelling_and_tashdid(self):
        lesson = self.lessons[32]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("ڤیکتۆر", "گواڵو", "ئینشاڵاڵ", "نەججاڕ"):
            self.assertIn(marker, content)

    def test_lesson_34_keeps_kelhur_note_scoped_to_that_variety(self):
        lesson = self.lessons[33]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("کەلهوڕی", content)
        self.assertIn("دەخۆم", content)
        self.assertIn("چم", content)


if __name__ == "__main__":
    unittest.main()
