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

    def test_course_title_and_22_sequential_lessons(self):
        lessons = self.course["lessons"]
        self.assertEqual(self.course["title"], "دەورەی ١: ڕێنووسی زمانی کوردی")
        self.assertEqual(self.course["lesson_count"], 22)
        self.assertEqual(len(lessons), 22)
        self.assertEqual([lesson["number"] for lesson in lessons], list(range(1, 23)))
        self.assertEqual(len({lesson["id"] for lesson in lessons}), 22)

    def test_course_ends_after_lesson_22_without_a_duplicate_course_button(self):
        behavior = self.course["completion_behavior"]
        self.assertEqual(behavior["after_lesson"], 22)
        self.assertFalse(behavior["show_separate_menu_button"])
        self.assertIsNone(behavior["button_text"])
        self.assertFalse(behavior["treat_button_as_lesson_23"])

    def test_existing_course_and_production_are_protected_by_design(self):
        safety = self.course["safety"]
        self.assertTrue(safety["do_not_modify_existing_ten_lesson_course"])
        self.assertTrue(safety["do_not_enable_dynamic_speech"])
        self.assertTrue(safety["do_not_change_production_or_main"])

    def test_runtime_menu_has_course_title_and_lists_course_lessons(self):
        bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")
        self.assertIn('["ڕێنووسی زمانی کوردی"]', bot_source)
        self.assertIn('if text == "ڕێنووسی زمانی کوردی":', bot_source)
        self.assertIn('load_json("course_data/orthography_foundations.json")', bot_source)
        self.assertIn("course['title']", bot_source)
        self.assertIn("course.get(\"lessons\", [])", bot_source)
        # The new course is a separate menu entry, not lesson 23 in the old course.
        self.assertIn('"do_not_modify_existing_ten_lesson_course": true', (ROOT / "course_data" / "orthography_foundations.json").read_text(encoding="utf-8"))

    def test_lessons_are_not_misrepresented_as_source_reviewed(self):
        for lesson in self.course["lessons"]:
            self.assertEqual(
                lesson["content_status"],
                "needs_source_review_and_editorial_entry",
            )
            self.assertEqual(lesson["quiz_status"], "not_created")


if __name__ == "__main__":
    unittest.main()
