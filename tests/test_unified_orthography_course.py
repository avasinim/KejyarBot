"""Structural safeguards for the draft unified-orthography course.

These tests validate data shape only; they do not certify linguistic rules or examples.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(relative_path):
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


class UnifiedOrthographyCourseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = read_json("courses.json")
        cls.data = read_json("course_data/unified_orthography_lessons_01_12.json")
        cls.course = next(
            item for item in cls.manifest["courses"]
            if item["id"] == "unified_orthography"
        )

    def test_course_remains_planned_until_editorial_and_runtime_review(self):
        self.assertEqual(self.course["status"], "draft_for_review")
        self.assertEqual(self.course["lesson_ids"], [f"unified_orthography_{n:02d}" for n in range(1, 13)])

    def test_course_has_twelve_ordered_drafts(self):
        lessons = self.data["lessons"]
        self.assertEqual(len(lessons), 12)
        self.assertEqual([lesson["number"] for lesson in lessons], list(range(1, 13)))

    def test_each_lesson_has_core_teaching_fields(self):
        for lesson in self.data["lessons"]:
            with self.subTest(lesson=lesson["number"]):
                self.assertTrue(lesson.get("title", "").strip())
                self.assertTrue(lesson.get("objective", "").strip())
                self.assertTrue(lesson.get("key_points"))
                self.assertTrue(lesson.get("examples"))
                self.assertTrue(lesson.get("exercises"))
                self.assertTrue(lesson.get("comprehension"))
                self.assertEqual(len(lesson["comprehension"]), 2)
                self.assertTrue(lesson.get("role_play"))
                self.assertEqual(lesson.get("review_status"), "draft_editorial_review")

    def test_quiz_answer_indexes_are_valid(self):
        for lesson in self.data["lessons"]:
            for quiz in lesson.get("quiz", []):
                with self.subTest(lesson=lesson["number"], question=quiz.get("q")):
                    self.assertTrue(quiz.get("options"))
                    self.assertIsInstance(quiz.get("answer"), int)
                    self.assertGreaterEqual(quiz["answer"], 0)
                    self.assertLess(quiz["answer"], len(quiz["options"]))



if __name__ == "__main__":
    unittest.main()
