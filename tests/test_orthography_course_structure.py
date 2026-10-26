import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "course_data" / "orthography_foundations.json"
QUIZ_PATH = ROOT / "course_data" / "orthography_foundations_quiz_draft.json"
DRAFT_DIR = ROOT / "course_data"


class OrthographyCourseStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.course = json.load(source)
        with QUIZ_PATH.open(encoding="utf-8") as source:
            cls.quiz = json.load(source)

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

    def test_runtime_menu_lists_new_course_separately(self):
        bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")
        self.assertIn('["ڕێنووسی زمانی کوردی"]', bot_source)
        self.assertIn('if text == "ڕێنووسی زمانی کوردی":', bot_source)
        self.assertIn('load_json("course_data/orthography_foundations.json")', bot_source)
        self.assertIn("course['title']", bot_source)
        self.assertIn('course.get("lessons", [])', bot_source)
        # The separate course must not become lesson 23 of the older course.
        self.assertIn('"do_not_modify_existing_ten_lesson_course": true',
                      COURSE_PATH.read_text(encoding="utf-8"))

    def test_all_22_draft_files_exist_and_match_catalog_numbers_and_titles(self):
        for lesson in self.course["lessons"]:
            number = lesson["number"]
            path = DRAFT_DIR / f"orthography_lesson_{number:02d}_draft.md"
            self.assertTrue(path.is_file(), f"Missing draft: {path.name}")
            draft = path.read_text(encoding="utf-8")
            self.assertIn(f"وانەی {number}", draft, path.name)
            self.assertIn(lesson["title"], draft, path.name)

    def test_quiz_draft_has_one_valid_multiple_choice_question_per_lesson(self):
        self.assertEqual(self.quiz["course_id"], self.course["course_id"])
        self.assertEqual(self.quiz["lesson_quiz_count"], 22)
        quizzes = self.quiz["quizzes"]
        self.assertEqual(len(quizzes), 22)
        self.assertEqual(
            [item["lesson_number"] for item in quizzes],
            list(range(1, 23)),
        )
        for item in quizzes:
            self.assertEqual(len(item["questions"]), 1)
            question = item["questions"][0]
            self.assertEqual(question["type"], "multiple_choice")
            self.assertGreaterEqual(len(question["options"]), 2)
            self.assertGreaterEqual(question["correct_option_index"], 0)
            self.assertLess(question["correct_option_index"], len(question["options"]))
            self.assertTrue(question["question"].strip())

    def test_draft_status_is_not_misrepresented_as_source_reviewed_or_runtime_ready(self):
        self.assertEqual(self.course["status"], "curriculum_structure")
        self.assertEqual(
            self.quiz["status"],
            "draft_needs_editorial_and_source_review",
        )
        for lesson in self.course["lessons"]:
            self.assertEqual(
                lesson["content_status"],
                "needs_source_review_and_editorial_entry",
            )
            self.assertEqual(
                lesson["quiz_status"],
                "draft_needs_editorial_and_source_review",
            )


if __name__ == "__main__":
    unittest.main()
