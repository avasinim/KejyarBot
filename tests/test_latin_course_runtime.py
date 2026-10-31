import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from latin_course_runtime import load_latin_courses
from course_runtime import can_open_lesson


class LatinCourseRuntimeTests(unittest.TestCase):
    def test_loads_exactly_two_separate_courses_and_24_lessons(self):
        lessons, quizzes, courses = load_latin_courses()
        self.assertEqual(len(courses), 2)
        self.assertEqual([len(course["lesson_ids"]) for course in courses], [12, 12])
        self.assertEqual(len(lessons), 24)
        self.assertEqual(len(quizzes), 24)
        self.assertEqual(courses[0]["id"], "kurmanji_latin_orthography")
        self.assertEqual(courses[1]["id"], "kurmanji_latin_grammar")
        self.assertIn("Part I", courses[0]["source_part"])
        self.assertIn("Part II", courses[1]["source_part"])

    def test_each_lesson_keeps_full_markdown_and_five_questions(self):
        lessons, quizzes, _ = load_latin_courses()
        for lesson_id, lesson in lessons.items():
            self.assertTrue(lesson["content"].startswith("## Ders "))
            self.assertIn("###", lesson["content"])
            self.assertEqual(len(quizzes[lesson_id]), 5)
            self.assertTrue(all(len(question["options"]) in (3, 4) for question in quizzes[lesson_id]))

    def test_bot_runtime_loads_both_latin_courses_without_collisions(self):
        import bot

        expected = {
            "kurmanji_latin_orthography": "Part I",
            "kurmanji_latin_grammar": "Part II",
        }
        for course_id, source_part in expected.items():
            self.assertTrue(bot.course_is_active(course_id))
            lesson_ids = bot.COURSE_LESSON_ORDER[course_id]
            self.assertEqual(len(lesson_ids), 12)
            self.assertEqual(len(set(lesson_ids)), 12)
            self.assertTrue(all(bot.LESSON_COURSE[item] == course_id for item in lesson_ids))
            self.assertTrue(all(len(bot.QUIZ_DATA[item]) == 5 for item in lesson_ids))
            self.assertTrue(all(source_part in course["source_part"] for course in bot.COURSES if course["id"] == course_id))
        self.assertEqual(len(bot.COURSES), 6)
        self.assertEqual(len(bot.ORDER), 22)

    def test_bot_routes_course_selection_callbacks_for_both_latin_courses(self):
        bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")
        self.assertIn("kurmanji_latin_orthography|kurmanji_latin_grammar", bot_source)
        self.assertIn('pattern=r"^course_', bot_source)

    def test_course_progress_unlocking_is_isolated_between_the_two_courses(self):
        lessons, _, courses = load_latin_courses()
        first, second = [course["lesson_ids"] for course in courses]
        # Completing the first lesson in Course 1 must not unlock Course 2's
        # second lesson, and vice versa; each course has its own ordered IDs.
        self.assertTrue(can_open_lesson(first, [], first[0]))
        self.assertFalse(can_open_lesson(second, [first[0]], second[1]))
        self.assertTrue(can_open_lesson(second, [], second[0]))
        self.assertFalse(can_open_lesson(first, [second[0]], first[1]))
        self.assertFalse(set(first).intersection(second))

    def test_course_two_lesson_twelve_uses_selected_expanded_lesson(self):
        lessons, quizzes, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_12"]["content"]
        self.assertIn("Şeş cureyên", lesson)
        self.assertIn("jmarnav", lesson)
        self.assertEqual(len(quizzes["kurmanji_latin_grammar_12"]), 5)

    def test_lesson_content_is_not_reformatted_or_truncated(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_orthography_01"]["content"]
        self.assertIn("| Mezin | Biçûk |", lesson)
        self.assertIn("### 6. Testa Kejyar", lesson)
        self.assertIn("### Xulasa", lesson)


if __name__ == "__main__":
    unittest.main()
