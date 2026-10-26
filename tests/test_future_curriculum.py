import json
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


class FutureCurriculumDraftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (BASE_DIR / "curriculum" / "future_courses_draft.json").open(encoding="utf-8") as handle:
            cls.data = json.load(handle)

    def test_two_future_courses_have_eight_draft_lessons_each(self):
        courses = {course["course_id"]: course for course in self.data["courses"]}
        self.assertEqual(set(courses), {"unified_orthography", "grammar"})
        self.assertEqual(len(courses["unified_orthography"]["lessons"]), 8)
        self.assertEqual(len(courses["grammar"]["lessons"]), 8)
        self.assertEqual(courses["unified_orthography"]["status"], "draft")
        self.assertEqual(courses["grammar"]["status"], "draft")

    def test_draft_lesson_ids_and_titles_are_unique_and_complete(self):
        lessons = [lesson for course in self.data["courses"] for lesson in course["lessons"]]
        ids = [lesson["id"] for lesson in lessons]
        titles = [lesson["title"] for lesson in lessons]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(titles), len(set(titles)))
        self.assertEqual(len(lessons), 16)

    def test_every_draft_lesson_has_objectives_examples_exercise_and_source_gate(self):
        for course in self.data["courses"]:
            for lesson in course["lessons"]:
                with self.subTest(lesson=lesson["id"]):
                    self.assertTrue(lesson["objectives"])
                    self.assertTrue(lesson["examples"])
                    self.assertTrue(lesson["exercise"].strip())
                    self.assertTrue(lesson["source_requirement"].strip())


if __name__ == "__main__":
    unittest.main()
