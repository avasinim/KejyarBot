import sqlite3
import tempfile
import unittest
from pathlib import Path

from course_data.orthography_progress_store import (
    COURSE_ID,
    get_course_completed_lessons,
    init_course_progress,
    record_course_quiz_completion,
)


class OrthographyProgressStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test.db"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_completion_is_idempotent_and_course_scoped(self):
        init_course_progress(self.db_path)
        self.assertTrue(record_course_quiz_completion(self.db_path, 7, "lesson_01"))
        self.assertFalse(record_course_quiz_completion(self.db_path, 7, "lesson_01"))
        self.assertTrue(record_course_quiz_completion(self.db_path, 7, "lesson_02"))
        self.assertEqual(get_course_completed_lessons(self.db_path, 7), ["lesson_01", "lesson_02"])
        self.assertEqual(get_course_completed_lessons(self.db_path, 7, course_id="another_course"), [])

    def test_does_not_change_legacy_users_or_completed_quizzes(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY, completed_lessons TEXT, completed_quizzes TEXT, xp INTEGER)")
        conn.execute("INSERT INTO users VALUES (7, 'وانە_1,وانە_2', 'وانە_1', 40)")
        conn.commit()
        conn.close()
        record_course_quiz_completion(self.db_path, 7, "lesson_01")
        conn = sqlite3.connect(self.db_path)
        row = conn.execute("SELECT completed_lessons, completed_quizzes, xp FROM users WHERE user_id=7").fetchone()
        conn.close()
        self.assertEqual(row, ("وانە_1,وانە_2", "وانە_1", 40))

    def test_validates_identifiers(self):
        for user_id, lesson_id in ((True, "lesson_01"), (1, "وانە_1"), (1, ""), (1, "lesson_1"), (1, "lesson_23")):
            with self.subTest(user_id=user_id, lesson_id=lesson_id), self.assertRaises(ValueError):
                record_course_quiz_completion(self.db_path, user_id, lesson_id)


    def test_progress_is_isolated_by_user_and_course(self):
        self.assertTrue(record_course_quiz_completion(self.db_path, 7, "lesson_01", COURSE_ID))
        self.assertTrue(record_course_quiz_completion(self.db_path, 7, "lesson_01", "another_course"))
        self.assertTrue(record_course_quiz_completion(self.db_path, 8, "lesson_01", COURSE_ID))
        self.assertEqual(get_course_completed_lessons(self.db_path, 7, COURSE_ID), ["lesson_01"])
        self.assertEqual(get_course_completed_lessons(self.db_path, 8, COURSE_ID), ["lesson_01"])
        self.assertEqual(get_course_completed_lessons(self.db_path, 7, "another_course"), ["lesson_01"])

    def test_rejects_blank_or_non_string_course_ids(self):
        for course_id in ("", "   ", None, 123, " another_course", "another_course "):
            with self.subTest(course_id=course_id), self.assertRaises(ValueError):
                record_course_quiz_completion(self.db_path, 7, "lesson_01", course_id)
        with self.assertRaises(ValueError):
            get_course_completed_lessons(self.db_path, 7, course_id=" ")


    def test_accepts_each_of_the_22_course_lesson_ids(self):
        for number in range(1, 23):
            lesson_id = f"lesson_{number:02d}"
            with self.subTest(lesson_id=lesson_id):
                self.assertTrue(record_course_quiz_completion(self.db_path, 99, lesson_id))
        self.assertEqual(
            get_course_completed_lessons(self.db_path, 99),
            [f"lesson_{number:02d}" for number in range(1, 23)],
        )

    def test_course_id_constant(self):
        self.assertEqual(COURSE_ID, "orthography_foundations")


if __name__ == "__main__":
    unittest.main()
