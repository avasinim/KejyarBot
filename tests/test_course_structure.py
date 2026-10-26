import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CourseStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lessons = json.loads((ROOT / "lessons.json").read_text(encoding="utf-8"))
        cls.courses = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        cls.quizzes = json.loads((ROOT / "quiz.json").read_text(encoding="utf-8"))
        cls.bot = (ROOT / "bot.py").read_text(encoding="utf-8")

    def test_course_one_uses_user_supplied_lesson_one(self):
        lesson = self.lessons["وانە_1"]
        self.assertEqual(lesson["title"], "پیتەکان و دەنگەکان")
        self.assertIn("(٣٧) دەنگی هەیە", lesson["content"])
        self.assertIn("٣٤", lesson["content"])
        self.assertIn("وانە_1", self.courses["orthography_basic"]["lesson_ids"])

    def test_course_one_includes_user_supplied_vowels_lesson(self):
        lesson = self.lessons["وانە_2"]
        self.assertEqual(lesson["title"], "بزوێنەکان")
        self.assertIn("(٨) دەنگن", lesson["content"])
        self.assertIn("(ا، ە، و، ۆ، وو، ی، ێ)", lesson["content"])
        self.assertIn("وانە_2", self.courses["orthography_basic"]["lesson_ids"])
        self.assertGreaterEqual(len(self.quizzes["وانە_2"]), 3)
        for question in self.quizzes["وانە_2"]:
            self.assertIn(question["answer"], question["options"])

    def test_daily_conversation_has_separate_lesson_id(self):
        lesson = self.lessons["وتوێژ_1"]
        self.assertEqual(lesson["title"], "سڵاو و ناساندنی خۆ")
        self.assertIn("وتوێژ_1", self.courses["daily_conversation"]["lesson_ids"])
        self.assertNotIn("وتوێژ_1", [*self.courses["orthography_basic"]["lesson_ids"]])

    def test_planned_courses_have_no_fabricated_lessons(self):
        for course_id in ("unified_orthography", "grammar"):
            self.assertEqual(self.courses[course_id]["status"], "planned")
            self.assertEqual(self.courses[course_id]["lesson_ids"], [])

    def test_lesson_one_quiz_answers_exist_in_options(self):
        questions = self.quizzes["وانە_1"]
        self.assertGreaterEqual(len(questions), 2)
        for question in questions:
            self.assertIn(question["answer"], question["options"])

    def test_course_navigation_handlers_are_registered(self):
        self.assertIn("async def open_course(", self.bot)
        self.assertIn("async def open_course_lesson(", self.bot)
        self.assertIn("pattern=\"^course_lesson_\"", self.bot)

    def test_duplicate_lesson_completion_is_guarded(self):
        self.assertIn("if lesson in get_completed_lessons(uid):", self.bot)
        self.assertIn("خەڵاتەکە پێشتر هەژمار کراوە", self.bot)

    def test_quiz_xp_is_awarded_only_for_first_completion(self):
        self.assertIn("already_completed = lesson in get_completed_lessons(uid)", self.bot)
        self.assertIn("if not already_completed:", self.bot)
        self.assertIn("XP دووبارە زیاد نەکرا", self.bot)


if __name__ == "__main__":
    unittest.main()
