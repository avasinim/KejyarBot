import json
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


class FutureCurriculumDraftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (BASE_DIR / "curriculum" / "future_courses_draft.json").open(encoding="utf-8") as handle:
            cls.data = json.load(handle)

    def test_future_courses_are_placeholders_waiting_for_user_content(self):
        courses = {course["course_id"]: course for course in self.data["courses"]}
        self.assertEqual(set(courses), {"unified_orthography", "grammar"})
        for course in courses.values():
            with self.subTest(course=course["course_id"]):
                self.assertEqual(course["status"], "awaiting_user_content")
                self.assertEqual(course["lessons"], [])

    def test_placeholder_does_not_invent_lesson_titles_or_examples(self):
        for course in self.data["courses"]:
            self.assertEqual(course["lessons"], [])
        self.assertIn("ناونیشان", self.data["note"])
        self.assertIn("خاوەن پڕۆژە", self.data["note"])


if __name__ == "__main__":
    unittest.main()
