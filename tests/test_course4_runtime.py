"""Regression checks for the owner-review Course 4 runtime data."""
import json
import unittest
from pathlib import Path

from course_lesson_adapters import adapt_unified_orthography_lessons


ROOT = Path(__file__).resolve().parents[1]
COURSE4_PATH = ROOT / "course_data" / "grammar_course4_lessons_01_08.json"


class Course4RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(COURSE4_PATH.read_text(encoding="utf-8"))
        cls.lessons, cls.quizzes = adapt_unified_orthography_lessons(cls.payload)

    def test_course_boundary_and_eight_contiguous_lessons(self):
        self.assertEqual(self.payload["course_id"], "grammar")
        self.assertEqual(self.payload["source_page_limit"], 342)
        self.assertEqual([item["number"] for item in self.payload["lessons"]], list(range(1, 9)))
        self.assertEqual(list(self.lessons), [f"grammar_{number:02d}" for number in range(1, 9)])

    def test_every_lesson_has_nonempty_content_and_owner_review_marker(self):
        for lesson_id, lesson in self.lessons.items():
            with self.subTest(lesson=lesson_id):
                self.assertTrue(lesson["title"].strip())
                self.assertTrue(lesson["content"].strip())
                self.assertTrue(lesson["review_status"].startswith("owner_review"))

    def test_every_lesson_has_two_valid_provisional_quiz_questions(self):
        for lesson_id, questions in self.quizzes.items():
            with self.subTest(lesson=lesson_id):
                self.assertEqual(len(questions), 2)
                for question in questions:
                    self.assertTrue(question["question"].strip())
                    self.assertGreaterEqual(len(question["options"]), 2)
                    self.assertEqual(len(question["options"]), len(set(question["options"])))
                    self.assertIn(question["answer"], question["options"])
                    self.assertTrue(question["explanation"].strip())

    def test_quizzes_are_not_silently_omitted_by_adapter(self):
        self.assertEqual(set(self.quizzes), set(self.lessons))
        self.assertTrue(all(self.quizzes[key] for key in self.lessons))


if __name__ == "__main__":
    unittest.main()
