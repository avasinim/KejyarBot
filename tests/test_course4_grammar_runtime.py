"""Regression tests for the owner-supplied replacement Course 4 grammar lesson."""
import json
import unittest
from pathlib import Path

import bot


ROOT = Path(__file__).resolve().parents[1]


class Course4GrammarRuntimeTests(unittest.TestCase):
    def test_course4_is_active_with_five_owner_supplied_lessons(self):
        self.assertTrue(bot.course_is_active("grammar"))
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], ["grammar_01", "grammar_02", "grammar_03", "grammar_04", "grammar_05"])
        self.assertIn("grammar_01", bot.LESSON_DATA)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_01"]), 7)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_02"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_03"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_04"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_05"]), 8)
        self.assertEqual(bot.LESSON_DATA["grammar_01"]["review_status"],
                         "owner_review_pending_term_clarification")
        self.assertEqual(bot.LESSON_DATA["grammar_02"]["review_status"],
                         "owner_review_pending_sorani_corpus_validation")
        expected_review_status = {
            "grammar_03": "owner_review_pending_sorani_corpus_validation",
            "grammar_04": "owner_review_pending_sorani_plural_and_gender_validation",
            "grammar_05": "owner_review_pending_sorani_morphology_corpus_validation",
        }
        for lesson_id, expected_status in expected_review_status.items():
            self.assertEqual(bot.LESSON_DATA[lesson_id]["review_status"], expected_status)

    def test_source_preserves_course4_content_and_reviewable_quiz(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        self.assertEqual(source["course_id"], "grammar")
        self.assertEqual([lesson["id"] for lesson in source["lessons"]], ["grammar_01", "grammar_02", "grammar_03", "grammar_04", "grammar_05"])
        lesson = source["lessons"][0]
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]) - 2, 8)
        self.assertEqual(len(lesson["examples"]), 3)
        self.assertEqual(len(lesson["appendix"]), 4)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["quiz"]), 7)
        lesson2 = source["lessons"][1]
        self.assertEqual(len(lesson2["exercises"]), 5)
        self.assertEqual(len(lesson2["activities"]), 3)
        self.assertEqual(len(lesson2["appendix"]), 4)
        self.assertEqual(len(lesson2["comprehension"]) - 2, 8)
        self.assertEqual(len(lesson2["quiz"]), 8)
        self.assertIn("کەژیار", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("پاشکۆ", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("چالاکییەکان", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("فێزیۆلۆژی", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("پاشکۆ", bot.LESSON_DATA["grammar_02"]["content"])
        self.assertIn("چالاکییەکان", bot.LESSON_DATA["grammar_02"]["content"])
        expected_appendix_counts = {"grammar_03": 4, "grammar_04": 5, "grammar_05": 7}
        for lesson_id, appendix_count in expected_appendix_counts.items():
            lesson = next(item for item in source["lessons"] if item["id"] == lesson_id)
            self.assertEqual(len(lesson["appendix"]), appendix_count)
            self.assertEqual(len(lesson["activities"]), 3)
            self.assertEqual(len(lesson["exercises"]), 5)
            self.assertEqual(len(lesson["quiz"]), 8)
            self.assertEqual(len(lesson["comprehension"]) - 2, 8)
            self.assertIn("کەژیار", bot.LESSON_DATA[lesson_id]["content"])
            self.assertIn("پاشکۆ", bot.LESSON_DATA[lesson_id]["content"])
            self.assertIn("چالاکییەکان", bot.LESSON_DATA[lesson_id]["content"])
        lesson4 = next(item for item in source["lessons"] if item["id"] == "grammar_04")
        lesson5 = next(item for item in source["lessons"] if item["id"] == "grammar_05")
        self.assertIn("ئەو ئەسپانە", " ".join(lesson4["key_points"]))
        self.assertIn("ئەو ئەسپانە", " ".join(lesson5["key_points"]))
        self.assertIn("جوان + ـی ← جوانی", str(lesson5["examples"]))
        self.assertIn("دەست + نوێژ ← دەستنوێژ", str(lesson5["examples"]))

    def test_all_course4_lesson_quizzes_and_learning_components_are_well_formed(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        for lesson in source["lessons"]:
            with self.subTest(lesson=lesson["id"]):
                self.assertTrue(lesson["objective"].strip())
                self.assertTrue(lesson["key_points"])
                self.assertTrue(lesson["examples"])
                self.assertEqual(len(lesson["activities"]), 3)
                self.assertEqual(len(lesson["exercises"]), 5)
                self.assertEqual(len(lesson["quiz"]), 7 if lesson["id"] == "grammar_01" else 8)
                self.assertTrue(lesson["appendix"])
                self.assertTrue(lesson["comprehension"])
                self.assertIn("کەژیار", json.dumps(lesson, ensure_ascii=False))
                for question in lesson["quiz"]:
                    self.assertTrue(question["q"].strip())
                    self.assertGreaterEqual(len(question["options"]), 2)
                    self.assertGreaterEqual(question["answer"], 0)
                    self.assertLess(question["answer"], len(question["options"]))
                    self.assertTrue(question["explanation"].strip())

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
