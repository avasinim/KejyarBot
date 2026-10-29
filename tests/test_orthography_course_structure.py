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
        self.assertEqual(self.course["title"], "کۆرسی ١: ڕێنووسی سەرەتاییی زمانی کوردی")
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
        self.assertTrue(safety["do_not_keep_legacy_ten_lesson_course_as_separate_course"])
        self.assertTrue(safety["do_not_enable_dynamic_speech"])
        self.assertTrue(safety["do_not_change_production_or_main"])

    def test_runtime_preserves_course_one_ids_and_loads_active_courses_two_and_three(self):
        bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")
        manifest_path = ROOT / "courses.json"
        with manifest_path.open(encoding="utf-8") as source:
            manifest = json.load(source)
        courses = {course["id"]: course for course in manifest["courses"]}
        self.assertIn('load_json("course_data/orthography_foundations.json")', bot_source)
        self.assertIn('load_json("course_data/orthography_foundations_quiz_draft.json")', bot_source)
        self.assertIn('for course_lesson in ORTHOGRAPHY_COURSE.get("lessons", [])', bot_source)
        self.assertIn('load_json("course_data/daily_conversation_lessons_01_06.json")', bot_source)
        self.assertIn('load_json("course_data/unified_orthography_lessons_01_66.json")', bot_source)
        self.assertIn('callback_data=f"open_lesson_{lesson}"', bot_source)
        self.assertIn('reply_markup=InlineKeyboardMarkup(keyboard_rows)', bot_source)
        self.assertEqual(courses["orthography_basic"]["status"], "active")
        self.assertEqual(len(courses["orthography_basic"]["lesson_ids"]), 22)
        self.assertEqual(courses["daily_conversation"]["status"], "active")
        self.assertEqual(len(courses["daily_conversation"]["lesson_ids"]), 48)
        self.assertEqual(courses["unified_orthography"]["status"], "active")
        self.assertEqual(len(courses["unified_orthography"]["lesson_ids"]), 55)
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
            # Titles may quote individual Kurdish letters in lesson prose.
            normalize_title = lambda value: value.replace("«", "").replace("»", "").replace("“", "").replace("”", "").replace(chr(34), "").replace(":", "").replace("ـ", "").strip()
            self.assertIn(normalize_title(lesson["title"]), normalize_title(draft), path.name)

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
            self.assertGreaterEqual(
                len(question["options"]),
                3,
                f"Lesson {item['lesson_number']} needs at least three answer options.",
            )
            self.assertEqual(
                len(question["options"]),
                len(set(question["options"])),
                f"Lesson {item['lesson_number']} must not repeat answer options.",
            )
            self.assertGreaterEqual(question["correct_option_index"], 0)
            self.assertLess(question["correct_option_index"], len(question["options"]))
            self.assertTrue(question["question"].strip())
            self.assertTrue(question["explanation"].strip())

    def test_quiz_explanations_are_lesson_specific_not_one_repeated_template(self):
        explanations = [
            item["questions"][0]["explanation"]
            for item in self.quiz["quizzes"]
        ]
        self.assertEqual(len(explanations), 22)
        self.assertEqual(len(set(explanations)), 22)
        self.assertTrue(all(len(explanation) >= 40 for explanation in explanations))
        self.assertIn("فێرخوازانی سەرەتایی", self.quiz["note"])

    def test_draft_status_is_not_misrepresented_as_source_reviewed_or_runtime_ready(self):
        self.assertEqual(self.course["status"], "beginner_course_editorial_pass")
        self.assertEqual(
            self.quiz["status"],
            "beginner_quiz_editorial_pass",
        )
        for lesson in self.course["lessons"]:
            self.assertEqual(
                lesson["content_status"],
                "beginner_draft_needs_clarity_and_examples",
            )
            self.assertEqual(
                lesson["quiz_status"],
                "beginner_quiz_draft_needs_lesson_alignment",
            )


if __name__ == "__main__":
    unittest.main()
