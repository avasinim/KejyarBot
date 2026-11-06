"""Regression checks for the owner-review Course 4 runtime data."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import database

from course_lesson_adapters import adapt_unified_orthography_lessons
from course_runtime import can_open_lesson
from quiz_option_order import randomized_question_copy


ROOT = Path(__file__).resolve().parents[1]
COURSE4_PATH = ROOT / "course_data" / "grammar_course4_lessons_01_08.json"
COURSES_PATH = ROOT / "courses.json"


class Course4RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(COURSE4_PATH.read_text(encoding="utf-8"))
        cls.lessons, cls.quizzes = adapt_unified_orthography_lessons(cls.payload)

    def test_course_boundary_and_eight_contiguous_lessons(self):
        self.assertEqual(self.payload["course_id"], "grammar")
        self.assertEqual(self.payload["source_page_limit"], 342)
        self.assertEqual([item["number"] for item in self.payload["lessons"]], list(range(1, 9)))
        self.assertEqual(list(self.lessons), [f"grammar_{number:02d}" for number in range(1, 9)])

    def test_course4_is_registered_active_with_exact_lesson_ids(self):
        manifest = json.loads(COURSES_PATH.read_text(encoding="utf-8"))
        course = next(item for item in manifest["courses"] if item["id"] == "grammar")
        self.assertEqual(course["status"], "active")
        self.assertEqual(course["lesson_ids"], [f"grammar_{number:02d}" for number in range(1, 9)])

    def test_course4_quizzes_are_not_blocked_by_editorial_gate(self):
        from course_quiz_review import quiz_is_available
        for number in range(1, 9):
            self.assertTrue(quiz_is_available(f"grammar_{number:02d}"))

    def test_source_page_ranges_are_contiguous_from_11_through_342(self):
        import re
        ranges = []
        for item in self.payload["lessons"]:
            match = re.search(r"(\d+)\s*[–-]\s*(\d+)", item["title"])
            self.assertIsNotNone(match, item["title"])
            ranges.append((int(match.group(1)), int(match.group(2))))
        self.assertEqual(ranges[0][0], 11)
        for previous, current in zip(ranges, ranges[1:]):
            self.assertEqual(current[0], previous[1] + 1)
        self.assertEqual(ranges[-1][1], 342)

    def test_each_lesson_has_the_expected_teaching_sections(self):
        for item in self.payload["lessons"]:
            with self.subTest(lesson=item["number"]):
                for field in ("objective", "key_points", "examples", "exercises", "comprehension"):
                    self.assertTrue(item.get(field))

    def test_every_lesson_has_nonempty_content_and_owner_review_marker(self):
        for lesson_id, lesson in self.lessons.items():
            with self.subTest(lesson=lesson_id):
                self.assertTrue(lesson["title"].strip())
                self.assertTrue(lesson["content"].strip())
                self.assertTrue(lesson["review_status"].startswith("owner_review"))
                self.assertIn("تێبینی پێداچوونەوە", lesson["content"])
                self.assertIn("پەسەندی کۆتایی", lesson["content"])

    def test_every_lesson_has_two_valid_provisional_quiz_questions(self):
        for lesson_id, questions in self.quizzes.items():
            with self.subTest(lesson=lesson_id):
                self.assertEqual(len(questions), 2)
                for question in questions:
                    self.assertTrue(question["question"].strip())
                    self.assertGreaterEqual(len(question["options"]), 2)
                    self.assertEqual(len(question["options"]), len(set(question["options"])))
                    self.assertIn(question["answer"], question["options"])
                    self.assertTrue(question["explanation"].strip())

    def test_course4_quiz_option_randomization_preserves_answers_and_source(self):
        for lesson_id, questions in self.quizzes.items():
            with self.subTest(lesson=lesson_id):
                original = json.loads(json.dumps(questions, ensure_ascii=False))
                shuffled = randomized_question_copy(questions, rng=type("Reverse", (), {"shuffle": staticmethod(list.reverse)})())
                self.assertEqual(questions, original)
                self.assertEqual(len(shuffled), len(original))
                for before, after in zip(original, shuffled):
                    self.assertEqual(set(before["options"]), set(after["options"]))
                    self.assertEqual(before["answer"], after["answer"])
                    self.assertEqual(after["options"], list(reversed(before["options"])))
    def test_course4_lessons_unlock_in_sequence_only(self):
        lesson_ids = [f"grammar_{number:02d}" for number in range(1, 9)]
        completed = set()
        self.assertTrue(can_open_lesson(lesson_ids, completed, "grammar_01"))
        self.assertFalse(can_open_lesson(lesson_ids, completed, "grammar_02"))
        completed.add("grammar_01")
        self.assertTrue(can_open_lesson(lesson_ids, completed, "grammar_02"))
        self.assertFalse(can_open_lesson(lesson_ids, completed, "grammar_03"))
        completed.update(lesson_ids[:-1])
        self.assertTrue(can_open_lesson(lesson_ids, completed, "grammar_08"))
        self.assertFalse(can_open_lesson(lesson_ids, completed, "grammar_09"))
    def test_course4_lesson_rewards_are_granted_once(self):
        with tempfile.TemporaryDirectory() as directory:
            db_path = Path(directory) / "course4-test.db"
            with patch.object(database, "DB_NAME", str(db_path)):
                database.init_db()
                self.assertTrue(database.complete_lesson_with_rewards(900001, "grammar_01"))
                self.assertFalse(database.complete_lesson_with_rewards(900001, "grammar_01"))
                user = database.get_user(900001)
                self.assertEqual(user[1], 10)  # score
                self.assertEqual(user[2], 10)  # XP
                self.assertEqual(user[8], 5)   # coins
                self.assertEqual(user[9], 1)   # reward chests

    def test_course4_quiz_rewards_are_granted_once_without_lesson_coins(self):
        with tempfile.TemporaryDirectory() as directory:
            db_path = Path(directory) / "course4-test.db"
            with patch.object(database, "DB_NAME", str(db_path)):
                database.init_db()
                self.assertTrue(database.complete_quiz_with_rewards(900002, "grammar_01"))
                self.assertFalse(database.complete_quiz_with_rewards(900002, "grammar_01"))
                user = database.get_user(900002)
                self.assertEqual(user[1], 20)  # score
                self.assertEqual(user[2], 20)  # XP
                self.assertEqual(user[7], 1)   # completed quiz count
                self.assertEqual(user[8], 0)   # quizzes do not repeat lesson coins
                self.assertEqual(user[9], 0)   # quizzes do not repeat lesson chests
    def test_quizzes_are_not_silently_omitted_by_adapter(self):
        self.assertEqual(set(self.quizzes), set(self.lessons))
        self.assertTrue(all(self.quizzes[key] for key in self.lessons))


if __name__ == "__main__":
    unittest.main()
