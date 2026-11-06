"""Regression checks for the owner-supplied Course 4 grammar curriculum."""
import json
import unittest
from pathlib import Path

from course_lesson_adapters import adapt_unified_orthography_lessons

ROOT = Path(__file__).resolve().parents[1]
COURSE4_PATH = ROOT / "course_data" / "grammar_course4_lessons.json"
COURSES_PATH = ROOT / "courses.json"


class Course4RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(COURSE4_PATH.read_text(encoding="utf-8"))
        cls.lessons, cls.quizzes = adapt_unified_orthography_lessons(cls.payload)

    def test_course4_contains_only_the_new_first_grammar_lesson(self):
        self.assertEqual(self.payload["course_id"], "grammar")
        self.assertEqual([item["number"] for item in self.payload["lessons"]], [1])
        self.assertEqual(list(self.lessons), ["grammar_01"])
        lesson = self.payload["lessons"][0]
        self.assertEqual(lesson["title"], "وانەی ١: پێشەکی — ڕێزمان (Grammar)")
        self.assertEqual(lesson["review_status"], "owner_review_pending_scientific_term_clarification")
        self.assertTrue(lesson["objective"])
        self.assertEqual(len(lesson["key_points"]), 9)
        self.assertEqual(len(lesson["exercises"]), 4)
        self.assertEqual(len(lesson["comprehension"]), 10)

    def test_old_course4_lesson_ids_are_not_registered(self):
        manifest = json.loads(COURSES_PATH.read_text(encoding="utf-8"))
        course = next(item for item in manifest["courses"] if item["id"] == "grammar")
        self.assertEqual(course["status"], "active")
        self.assertEqual(course["lesson_ids"], ["grammar_01"])
        self.assertEqual(set(self.lessons), {"grammar_01"})
        self.assertEqual(set(self.quizzes), {"grammar_01"})
        self.assertEqual(self.quizzes["grammar_01"], [])

    def test_owner_supplied_lesson_has_no_invented_multiple_choice_quiz(self):
        lesson = self.payload["lessons"][0]
        self.assertTrue(lesson["key_points"])
        self.assertTrue(lesson["exercises"])
        self.assertTrue(lesson["comprehension"])
        self.assertEqual(lesson["quiz"], [])
        self.assertIn("فێزیۆلۆژی", " ".join(lesson["key_points"]))


if __name__ == "__main__":
    unittest.main()
