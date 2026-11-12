import os
import tempfile
import unittest
from unittest.mock import patch

import bot
import database
from course_runtime import is_beta_review_lesson


class Course4BetaReviewPolicyTests(unittest.TestCase):
    def test_lesson13_internal_status_is_not_in_the_explicit_32_to_50_beta_range(self):
        self.assertFalse(is_beta_review_lesson(
            "grammar", "grammar_13",
            {"source_number": 13, "review_status": "internal_cross_lesson_synthesis_no_external_source_mapping"},
        ))
        self.assertFalse(is_beta_review_lesson(
            "grammar", "grammar_13",
            {"source_number": 13, "review_status": "scientific_review_complete_with_qualified_notes"},
        ))

    def test_lesson_32_is_beta_progression_eligible(self):
        self.assertTrue(is_beta_review_lesson(
            "grammar", "grammar_32",
            {"source_number": 32, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_lesson_46_is_beta_progression_eligible(self):
        self.assertTrue(is_beta_review_lesson(
            "grammar", "grammar_46",
            {"source_number": 46, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_lesson_50_is_beta_progression_eligible(self):
        self.assertTrue(is_beta_review_lesson(
            "grammar", "grammar_50",
            {"source_number": 50, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_lessons_47_to_50_are_beta_progression_eligible(self):
        for number in range(47, 51):
            with self.subTest(number=number):
                self.assertTrue(is_beta_review_lesson(
                    "grammar", f"grammar_{number:02d}",
                    {"source_number": number, "review_status": "owner_review_pending_expanded_draft"},
                ))

    def test_lessons_outside_32_to_50_are_not_eligible(self):
        for number in (31, 51, 0, -1):
            with self.subTest(number=number):
                self.assertFalse(is_beta_review_lesson(
                    "grammar", f"grammar_{number:02d}",
                    {"source_number": number, "review_status": "owner_review_pending_expanded_draft"},
                ))

    def test_other_courses_are_not_eligible(self):
        self.assertFalse(is_beta_review_lesson(
            "unified_orthography", "unified_orthography_32",
            {"source_number": 32, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_approved_or_other_review_states_are_not_beta_drafts(self):
        for status in ("approved", "scientific_review_complete_with_qualified_notes", "draft"):
            with self.subTest(status=status):
                self.assertFalse(is_beta_review_lesson(
                    "grammar", "grammar_32",
                    {"source_number": 32, "review_status": status},
                ))

    def test_id_and_source_number_must_match(self):
        self.assertFalse(is_beta_review_lesson(
            "grammar", "grammar_33",
            {"source_number": 32, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_boolean_is_not_accepted_as_a_lesson_number(self):
        self.assertFalse(is_beta_review_lesson(
            "grammar", "grammar_01",
            {"source_number": True, "review_status": "owner_review_pending_expanded_draft"},
        ))


class Course4BetaProgressLedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_db_name = database.DB_NAME
        database.DB_NAME = os.path.join(self.temp_dir.name, "test_kejy_ar.db")
        database.init_db()

    def tearDown(self):
        database.DB_NAME = self.original_db_name
        self.temp_dir.cleanup()

    def test_beta_completion_is_idempotent_and_separate_from_official_completion(self):
        user_id = 987654321
        self.assertTrue(database.complete_beta_lesson(user_id, "grammar_32"))
        self.assertFalse(database.complete_beta_lesson(user_id, "grammar_32"))
        self.assertEqual(database.get_completed_beta_lessons(user_id), ["grammar_32"])
        self.assertEqual(database.get_completed_lessons(user_id), [])
        row = database.get_user(user_id)
        self.assertEqual(row[1], 0)  # score
        self.assertEqual(row[2], 0)  # XP
        self.assertEqual(row[8], 0)  # coins
        self.assertEqual(row[9], 0)  # chests

    def test_existing_progress_survives_beta_column_migration(self):
        import sqlite3

        database.DB_NAME = os.path.join(self.temp_dir.name, "legacy_kejy_ar.db")
        conn = sqlite3.connect(database.DB_NAME)
        conn.execute("""
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                score INTEGER DEFAULT 0,
                xp INTEGER DEFAULT 0,
                level TEXT DEFAULT 'A1.1 🌱',
                correct_answers INTEGER DEFAULT 0,
                completed_lessons TEXT DEFAULT '',
                badges TEXT DEFAULT '',
                tests INTEGER DEFAULT 0,
                coins INTEGER DEFAULT 0,
                chests INTEGER DEFAULT 0
            )
        """)
        conn.execute(
            "INSERT INTO users(user_id, completed_lessons) VALUES(?, ?)",
            (123456789, "grammar_01,grammar_02"),
        )
        conn.commit()
        conn.close()

        database.init_db()
        self.assertEqual(
            database.get_completed_lessons(123456789),
            ["grammar_01", "grammar_02"],
        )
        self.assertEqual(database.get_completed_beta_lessons(123456789), [])
        conn = sqlite3.connect(database.DB_NAME)
        columns = {row[1] for row in conn.execute("PRAGMA table_info(users)")}
        conn.close()
        self.assertIn("beta_completed_lessons", columns)
        self.assertIn("completed_quizzes", columns)


class AcademicApprovalScopeRegressionTests(unittest.TestCase):
    def test_editorial_metadata_does_not_disable_other_active_courses(self):
        lesson_courses = {
            "daily_conversation_01": "daily_conversation",
            "unified_orthography_01": "unified_orthography",
            "kurmanji_latin_orthography_01": "kurmanji_latin_orthography",
            "kurmanji_latin_grammar_01": "kurmanji_latin_grammar",
        }
        lesson_data = {
            "daily_conversation_01": {"review_status": "draft_editorial_review"},
            "unified_orthography_01": {"review_status": "draft_editorial_review"},
            "kurmanji_latin_orthography_01": {"title": "Latin orthography"},
            "kurmanji_latin_grammar_01": {"title": "Latin grammar"},
        }
        with patch.multiple(
            bot,
            LESSON_COURSE=lesson_courses,
            LESSON_DATA=lesson_data,
            quiz_is_available=lambda _lesson: True,
        ):
            for lesson_id in lesson_courses:
                with self.subTest(lesson=lesson_id):
                    self.assertFalse(bot._lesson_requires_academic_approval(lesson_id))
                    self.assertFalse(bot.lesson_is_beta_review(lesson_id))
                    self.assertTrue(bot.lesson_quiz_is_available(lesson_id))

    def test_course4_unapproved_lessons_remain_fail_closed(self):
        lesson_courses = {
            "grammar_01": "grammar",
            "grammar_32": "grammar",
        }
        lesson_data = {
            "grammar_01": {
                "source_number": 1,
                "review_status": "scientific_review_complete_with_qualified_notes",
            },
            "grammar_32": {
                "source_number": 32,
                "review_status": "owner_review_pending_expanded_draft",
            },
        }
        with patch.multiple(
            bot,
            LESSON_COURSE=lesson_courses,
            LESSON_DATA=lesson_data,
            quiz_is_available=lambda _lesson: True,
        ):
            self.assertFalse(bot.lesson_is_beta_review("grammar_01"))
            self.assertTrue(bot.lesson_quiz_is_available("grammar_01"))
            self.assertTrue(bot.lesson_is_beta_review("grammar_32"))
            self.assertFalse(bot.lesson_quiz_is_available("grammar_32"))


if __name__ == "__main__":
    unittest.main()
