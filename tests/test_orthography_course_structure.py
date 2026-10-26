import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "course_data" / "orthography_foundations.json"


class OrthographyCourseStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.course = json.load(source)

    def test_course_has_exactly_22_sequential_lessons(self):
        lessons = self.course["lessons"]
        self.assertEqual(self.course["lesson_count"], 22)
        self.assertEqual(len(lessons), 22)
        self.assertEqual([lesson["number"] for lesson in lessons], list(range(1, 23)))
        self.assertEqual(len({lesson["id"] for lesson in lessons}), 22)

    def test_course_ends_with_separate_orthography_menu_key(self):
        behavior = self.course["completion_behavior"]
        self.assertEqual(behavior["after_lesson"], 22)
        self.assertTrue(behavior["show_separate_menu_button"])
        self.assertEqual(behavior["button_text"], "ڕێنووسی زمانی کوردی")
        self.assertFalse(behavior["treat_button_as_lesson_23"])

    def test_existing_course_and_production_are_protected_by_design(self):
        safety = self.course["safety"]
        self.assertTrue(safety["do_not_modify_existing_ten_lesson_course"])
        self.assertTrue(safety["do_not_enable_dynamic_speech"])
        self.assertTrue(safety["do_not_change_production_or_main"])

    def test_lessons_are_not_misrepresented_as_source_reviewed(self):
        for lesson in self.course["lessons"]:
            self.assertEqual(
                lesson["content_status"],
                "needs_source_review_and_editorial_entry",
            )
            self.assertEqual(lesson["quiz_status"], "not_created")


if __name__ == "__main__":
    unittest.main()
