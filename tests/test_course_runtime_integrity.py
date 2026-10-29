import unittest

import bot


class CourseRuntimeIntegrityTests(unittest.TestCase):
    def test_manifest_lessons_are_loaded_once_in_declared_course_order(self):
        all_ids = []
        for course in bot.COURSES:
            course_id = course["id"]
            declared = course.get("lesson_ids", [])
            runtime = bot.COURSE_LESSON_ORDER.get(course_id, [])
            with self.subTest(course=course_id):
                self.assertEqual(runtime, declared)
                self.assertTrue(all(lesson_id in bot.LESSON_DATA for lesson_id in runtime))
                self.assertEqual(len(runtime), len(set(runtime)))
                all_ids.extend(runtime)

        self.assertEqual(len(all_ids), len(set(all_ids)))
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["orthography_basic"]), 22)
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["daily_conversation"]), 48)
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["unified_orthography"]), 12)
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], [])

    def test_every_runtime_lesson_has_title_and_content(self):
        for lesson_id, lesson in bot.LESSON_DATA.items():
            with self.subTest(lesson=lesson_id):
                self.assertTrue(lesson.get("title", "").strip())
                self.assertTrue(lesson.get("content", "").strip())
                self.assertIn(lesson_id, bot.LESSON_COURSE)

    def test_all_loaded_quiz_items_have_valid_unique_options_and_answer(self):
        for lesson_id in bot.LESSON_DATA:
            questions = bot.QUIZ_DATA.get(lesson_id, [])
            with self.subTest(lesson=lesson_id):
                for index, question in enumerate(questions):
                    options = question.get("options", [])
                    self.assertTrue(question.get("question", "").strip(), (lesson_id, index))
                    self.assertGreaterEqual(len(options), 2, (lesson_id, index))
                    self.assertTrue(all(isinstance(option, str) and option.strip() for option in options))
                    self.assertEqual(len(options), len(set(options)), (lesson_id, index))
                    self.assertIn(question.get("answer"), options, (lesson_id, index))

    def test_course_successors_never_cross_course_boundaries(self):
        for course_id, lesson_ids in bot.COURSE_LESSON_ORDER.items():
            for index, lesson_id in enumerate(lesson_ids):
                expected = lesson_ids[index + 1] if index + 1 < len(lesson_ids) else None
                with self.subTest(course=course_id, lesson=lesson_id):
                    self.assertEqual(bot.next_course_lesson(lesson_id), expected)


if __name__ == "__main__":
    unittest.main()
