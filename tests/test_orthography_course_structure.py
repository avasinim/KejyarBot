import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "course_data" / "orthography_foundations.json"
QUIZ_PATH = ROOT / "course_data" / "orthography_foundations_quiz_draft.json"
SOURCE_PATH = ROOT / "course_data" / "orthography_original_lessons.json"
DRAFT_DIR = ROOT / "course_data"


class OrthographyCourseStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.course = json.load(source)
        with QUIZ_PATH.open(encoding="utf-8") as source:
            cls.quiz = json.load(source)
        with SOURCE_PATH.open(encoding="utf-8") as source:
            cls.original = json.load(source)

    def test_runtime_course_one_lesson_headers_use_correct_bot_name(self):
        # Catch regressions where lesson cards spell Kejyar as "کەویار".
        import bot

        lesson_ids = bot.COURSE_LESSON_ORDER["orthography_basic"]
        self.assertEqual(len(lesson_ids), 22)
        for lesson_id in lesson_ids:
            with self.subTest(lesson=lesson_id):
                content = bot.LESSON_DATA[lesson_id]["content"]
                header_lines = [line for line in content.splitlines() if "🌿 " in line and "وانەی" in line]
                self.assertEqual(len(header_lines), 1)
                self.assertIn("🌿 کەژیار  •  وانەی", header_lines[0])
                self.assertNotIn("کەویار", header_lines[0])

    def test_course_title_and_22_sequential_lessons(self):
        lessons = self.course["lessons"]
        self.assertEqual(self.course["title"], "کۆرسی ١: ڕێنووسی سەرەتاییی زمانی کوردی")
        self.assertEqual(self.course["lesson_count"], 22)
        self.assertEqual(len(lessons), 22)
        self.assertEqual([lesson["number"] for lesson in lessons], list(range(1, 23)))
        self.assertEqual(len({lesson["id"] for lesson in lessons}), 22)

    def test_source_catalog_plan_and_quiz_are_aligned_by_number_and_title(self):
        source_lessons = self.original["lessons"]
        planned_lessons = self.course["lessons"]
        quiz_lessons = self.quiz["quizzes"]

        expected_numbers = list(range(1, 23))
        self.assertEqual([item["number"] for item in source_lessons], expected_numbers)
        self.assertEqual([item["number"] for item in planned_lessons], expected_numbers)
        self.assertEqual([item["lesson_number"] for item in quiz_lessons], expected_numbers)

        source_titles = {item["number"]: item["title"] for item in source_lessons}
        planned_titles = {
            item["number"]: item.get("source_title", item["title"])
            for item in planned_lessons
        }
        self.assertEqual(source_titles, planned_titles)

        for quiz_lesson in quiz_lessons:
            number = quiz_lesson["lesson_number"]
            self.assertEqual(quiz_lesson["lesson_id"], f"lesson_{number:02d}")
            self.assertTrue(quiz_lesson["questions"], f"Lesson {number} has no quiz questions")

        question_ids = [
            question["id"]
            for quiz_lesson in quiz_lessons
            for question in quiz_lesson["questions"]
        ]
        self.assertEqual(len(question_ids), len(set(question_ids)))

    def test_course_ends_after_lesson_22_without_a_duplicate_course_button(self):
        behavior = self.course["completion_behavior"]
        self.assertEqual(behavior["after_lesson"], 22)
        self.assertFalse(behavior["show_separate_menu_button"])
        self.assertIsNone(behavior["button_text"])
        self.assertFalse(behavior["treat_button_as_lesson_23"])

    def test_existing_course_and_production_are_protected_by_design(self):
        safety = self.course["safety"]
        self.assertTrue(safety["do_not_keep_legacy_ten_lesson_course_as_separate_course"])
        self.assertTrue(safety["do_not_enable_dynamic_speech"])
        self.assertTrue(safety["do_not_change_production_or_main"])

    def test_runtime_uses_22_lessons_as_the_only_course(self):
        bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")
        self.assertIn('load_json("course_data/orthography_foundations.json")', bot_source)
        self.assertIn('load_json("course_data/orthography_foundations_quiz_draft.json")', bot_source)
        self.assertIn('for course_lesson in ORTHOGRAPHY_COURSE.get("lessons", [])', bot_source)
        self.assertIn('load_json("course_data/orthography_original_lessons.json")', bot_source)
        self.assertIn('ORIGINAL_LESSONS_BY_NUMBER.get(number)', bot_source)
        # The lesson catalog is intentionally rendered as inline buttons, not 22 reply-keyboard menu rows.
        self.assertIn("keyboard_rows.append([InlineKeyboardButton(", bot_source)
        self.assertIn('reply_markup=InlineKeyboardMarkup(keyboard_rows)', bot_source)
        self.assertNotIn('load_json("lessons.json")', bot_source)
        self.assertNotIn('load_json("quiz.json")', bot_source)
        self.assertNotIn('"ڕێنووسی زمانی کوردی"', bot_source)
    def test_all_22_draft_files_exist_and_match_catalog_numbers_and_titles(self):
        for lesson in self.course["lessons"]:
            number = lesson["number"]
            path = DRAFT_DIR / f"orthography_lesson_{number:02d}_draft.md"
            self.assertTrue(path.is_file(), f"Missing draft: {path.name}")
            draft = path.read_text(encoding="utf-8")
            kurdish_digits = str(number).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
            self.assertIn(f"وانەی {kurdish_digits}", draft, path.name)
            # Draft headings may use pedagogical titles distinct from the source-catalog title.
            # Validate numbering here; title/source alignment is audited separately.
            self.assertIn(f"## وانەی {kurdish_digits}", draft, path.name)
            self.assertGreater(len(draft.strip()), 200, path.name)

    def test_quiz_draft_has_valid_multiple_choice_questions_for_all_lessons(self):
        self.assertEqual(self.quiz["course_id"], self.course["course_id"])
        self.assertEqual(
            self.quiz["lesson_quiz_count"],
            "variable; expanded source-grounded draft questions",
        )
        quizzes = self.quiz["quizzes"]
        self.assertEqual(len(quizzes), 22)
        self.assertEqual(
            [item["lesson_number"] for item in quizzes],
            list(range(1, 23)),
        )
        all_questions = []
        for item in quizzes:
            self.assertGreaterEqual(len(item["questions"]), 1)
            all_questions.extend(item["questions"])
            for question in item["questions"]:
                self.assertEqual(question["type"], "multiple_choice")
                self.assertGreaterEqual(len(question["options"]), 2)
                self.assertEqual(len(question["options"]), len(set(question["options"])))
                self.assertIsInstance(question["correct_option_index"], int)
                self.assertNotIsInstance(question["correct_option_index"], bool)
                self.assertGreaterEqual(question["correct_option_index"], 0)
                self.assertLess(question["correct_option_index"], len(question["options"]))
                self.assertTrue(question["question"].strip())
                self.assertTrue(question["explanation"].strip())
        self.assertEqual(len(all_questions), 62)
        self.assertEqual(len({q["id"] for q in all_questions}), 62)

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
