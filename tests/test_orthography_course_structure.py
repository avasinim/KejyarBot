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
            kurdish_digits = str(number).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
            self.assertIn(f"وانەی {kurdish_digits}", draft, path.name)
            # Titles may quote individual Kurdish letters in lesson prose.
            normalize_title = lambda value: value.replace("«", "").replace("»", "").replace("“", "").replace("”", "").replace(chr(34), "").replace(":", "").replace("ـ", "").strip()
            self.assertIn(normalize_title(lesson["title"]), normalize_title(draft), path.name)

    def test_quiz_draft_has_valid_multiple_choice_questions_per_lesson(self):
        self.assertEqual(self.quiz["course_id"], self.course["course_id"])
        self.assertEqual(self.quiz["lesson_quiz_count"], 22)
        quizzes = self.quiz["quizzes"]
        self.assertEqual(len(quizzes), 22)
        self.assertEqual(
            [item["lesson_number"] for item in quizzes],
            list(range(1, 23)),
        )
        total_questions = 0
        question_ids = []
        for item in quizzes:
            self.assertGreaterEqual(len(item["questions"]), 1)
            total_questions += len(item["questions"])
            for question in item["questions"]:
                question_ids.append(question["id"])
                self.assertEqual(question["type"], "multiple_choice")
                self.assertGreaterEqual(len(question["options"]), 2)
                self.assertGreaterEqual(question["correct_option_index"], 0)
                self.assertLess(question["correct_option_index"], len(question["options"]))
                self.assertTrue(question["question"].strip())
                self.assertTrue(question["explanation"].strip())
        self.assertEqual(len(question_ids), len(set(question_ids)))
        self.assertEqual(total_questions, self.quiz["total_question_count"])
        self.assertEqual(total_questions, 51)
        self.assertEqual([len(item["questions"]) for item in quizzes[:12]], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
        self.assertEqual([len(quizzes[index]["questions"]) for index in range(12, 18)], [2, 2, 2, 2, 2, 2])
        self.assertEqual(len(quizzes[18]["questions"]), 1)
        self.assertTrue(all(len(item["questions"]) == 1 for item in quizzes[19:]))

    def test_quiz_explanations_are_lesson_specific_not_one_repeated_template(self):
        explanations = [
            item["questions"][0]["explanation"]
            for item in self.quiz["quizzes"]
        ]
        self.assertEqual(len(explanations), 22)
        self.assertEqual(len(set(explanations)), 22)
        self.assertTrue(all(len(explanation) >= 40 for explanation in explanations))
        self.assertIn(
            "not source-verified",
            self.quiz["note"],
        )

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
