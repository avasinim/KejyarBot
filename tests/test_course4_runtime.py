"""Regression checks for the new owner-supplied Course 4 grammar curriculum."""
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
        self.assertEqual(self.payload["lessons"][0]["title"], "وانەی ١: پێشەکی — ڕێزمان (Grammar)")
        self.assertEqual(self.payload["lessons"][0]["review_status"], "awaiting_owner_supplied_lesson_text")

    def test_old_course4_lesson_ids_are_not_registered(self):
        manifest = json.loads(COURSES_PATH.read_text(encoding="utf-8"))
        course = next(item for item in manifest["courses"] if item["id"] == "grammar")
        self.assertEqual(course["status"], "active")
        self.assertEqual(course["lesson_ids"], ["grammar_01"])
        self.assertEqual(set(self.lessons), {"grammar_01"})
        self.assertEqual(set(self.quizzes), {"grammar_01"})
        self.assertEqual(self.quizzes["grammar_01"], [])

    def test_new_lesson_waits_for_owner_text_without_invented_quiz_content(self):
        lesson = self.payload["lessons"][0]
        for field in ("key_points", "examples", "exercises", "comprehension", "quiz"):
            self.assertEqual(lesson[field], [])


if __name__ == "__main__":
    unittest.main()
