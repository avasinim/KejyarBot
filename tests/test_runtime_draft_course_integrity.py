"""Runtime integrity checks for the active multi-course candidate."""
import unittest
from unittest.mock import patch

import bot


class RuntimeDraftCourseIntegrityTests(unittest.TestCase):
    def test_all_46_manifest_lessons_are_loaded_without_id_collisions(self):
        expected = {
            "orthography_basic": [f"وانە_{n}" for n in range(1, 23)],
            "daily_conversation": [f"daily_conversation_{n:02d}" for n in range(1, 13)],
            "unified_orthography": [f"unified_orthography_{n:02d}" for n in range(1, 13)],
        }
        self.assertEqual(len(bot.LESSON_DATA), 46)
        for course_id, lesson_ids in expected.items():
            with self.subTest(course=course_id):
                self.assertEqual(bot.COURSE_LESSON_ORDER[course_id], lesson_ids)
                self.assertTrue(all(lesson_id in bot.LESSON_DATA for lesson_id in lesson_ids))
        self.assertEqual(len(bot.LESSON_DATA), len(set(bot.LESSON_DATA)))

    def test_course_one_has_22_original_text_records(self):
        self.assertEqual(set(bot.ORIGINAL_LESSONS_BY_NUMBER), set(range(1, 23)))
        for number in range(1, 23):
            with self.subTest(number=number):
                original = bot.ORIGINAL_LESSONS_BY_NUMBER[number]
                runtime = bot.LESSON_DATA[f"وانە_{number}"]
                self.assertTrue(original["title"].strip())
                self.assertTrue(original["content"].strip())
                self.assertEqual(runtime["title"], original["title"])
                self.assertIn(original["content"].strip(), runtime["content"])
                self.assertNotIn("هێشتا لە فایلەکەدا نییە", runtime["content"])

    def test_every_manifest_lesson_has_usable_content_and_structured_quiz_data(self):
        for course in bot.COURSES:
            if course.get("status") != "active":
                continue
            for lesson_id in course.get("lesson_ids", []):
                with self.subTest(course=course["id"], lesson=lesson_id):
                    lesson = bot.LESSON_DATA[lesson_id]
                    self.assertTrue(lesson.get("title", "").strip())
                    self.assertTrue(lesson.get("content", "").strip())
                    self.assertIn(lesson_id, bot.QUIZ_DATA)
                    questions = bot.QUIZ_DATA[lesson_id]
                    self.assertTrue(questions, "Every active lesson must have quiz data, even if editorial review gates access.")
                    for question in questions:
                        options = question.get("options")
                        self.assertTrue(question.get("question", "").strip())
                        self.assertIsInstance(options, list)
                        self.assertGreaterEqual(len(options), 2)
                        self.assertTrue(all(isinstance(option, str) and option.strip() for option in options))
                        self.assertEqual(len(options), len(set(options)))
                        self.assertIn(question.get("answer"), options)

    def test_active_course_lessons_and_quizzes_are_loaded(self):
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            for course_id in ("daily_conversation", "unified_orthography"):
                with self.subTest(course=course_id):
                    self.assertTrue(bot.course_is_active(course_id))
                    for lesson_id in bot.COURSE_LESSON_ORDER[course_id]:
                        with self.subTest(lesson=lesson_id):
                            self.assertEqual(
                                bot.can_open(12345, lesson_id),
                                lesson_id == bot.COURSE_LESSON_ORDER[course_id][0],
                            )
                            self.assertIn(
                                "draft_editorial_review",
                                bot.LESSON_DATA[lesson_id]["review_status"],
                            )
                            self.assertTrue(bot.LESSON_DATA[lesson_id]["content"].strip())
                            questions = bot.QUIZ_DATA[lesson_id]
                            self.assertTrue(questions)
                            self.assertTrue(
                                all(q.get("question") and q.get("explanation") for q in questions)
                            )

    def test_course_four_remains_planned_and_empty(self):
        course = next(course for course in bot.COURSES if course["id"] == "grammar")
        self.assertEqual(course["status"], "planned")
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], [])


if __name__ == "__main__":
    unittest.main()
