"""Regression tests for the owner-supplied replacement Course 4 grammar lesson."""
import json
import unittest
from pathlib import Path

import bot


ROOT = Path(__file__).resolve().parents[1]


class Course4GrammarRuntimeTests(unittest.TestCase):
    def test_course4_is_active_with_only_owner_supplied_lesson_one(self):
        self.assertTrue(bot.course_is_active("grammar"))
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], ["grammar_01"])
        self.assertIn("grammar_01", bot.LESSON_DATA)
        self.assertEqual(bot.QUIZ_DATA["grammar_01"], [])
        self.assertEqual(bot.LESSON_DATA["grammar_01"]["review_status"],
                         "owner_review_pending_scientific_term_clarification")

    def test_source_preserves_owner_content_and_does_not_invent_quiz(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        self.assertEqual(source["course_id"], "grammar")
        self.assertEqual([lesson["id"] for lesson in source["lessons"]], ["grammar_01"])
        lesson = source["lessons"][0]
        self.assertEqual(len(lesson["exercises"]), 4)
        self.assertEqual(len(lesson["comprehension"]) - 1, 8)
        self.assertEqual(lesson["quiz"], [])
        self.assertIn("کەژیار", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("فێزیۆلۆژی", bot.LESSON_DATA["grammar_01"]["content"])

    def test_other_active_courses_keep_their_existing_lesson_counts(self):
        expected = {
            "arami_orthography_foundations": 21,
            "daily_conversation": 42,
            "unified_orthography": 66,
            "kurmanji_latin_orthography": 12,
            "kurmanji_latin_grammar": 12,
        }
        for course_id, count in expected.items():
            with self.subTest(course_id=course_id):
                self.assertTrue(bot.course_is_active(course_id))
                self.assertEqual(len(bot.COURSE_LESSON_ORDER[course_id]), count)

    def test_course4_runtime_validation_accepts_pending_owner_review_lesson(self):
        bot.validate_activated_course_runtime()


if __name__ == "__main__":
    unittest.main()
