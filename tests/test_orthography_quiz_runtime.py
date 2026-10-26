import copy
import json
import unittest
from pathlib import Path

from course_data.orthography_quiz_adapter import convert_quiz_draft
from course_data.orthography_quiz_runtime import (
    SESSION_KEY,
    apply_answer,
    build_quiz_session,
    clear_course_quiz_session,
    make_answer_callback,
    make_start_callback,
    parse_answer_callback,
    parse_start_callback,
)


class OrthographyQuizRuntimeIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).resolve().parents[1] / "course_data" / "orthography_foundations_quiz_draft.json"
        cls.converted = convert_quiz_draft(json.loads(path.read_text(encoding="utf-8")))

    def test_session_is_namespaced_and_has_independent_state(self):
        legacy = {"quiz": {"lesson": "وانە_1", "score": 1}}
        session = build_quiz_session(self.converted, 1)
        self.assertEqual(SESSION_KEY, "orthography_foundations_quiz")
        self.assertEqual(session["course_id"], "orthography_foundations")
        self.assertEqual(session["lesson_id"], "lesson_01")
        self.assertEqual(session["score"], 0)
        session["score"] += 1
        session["questions"][0]["options"].append("session-only")
        self.assertEqual(legacy["quiz"]["score"], 1)
        self.assertNotIn("session-only", self.converted["lesson_01"][0]["options"])

    def test_all_22_lesson_sessions_start_at_zero(self):
        for number in range(1, 23):
            session = build_quiz_session(self.converted, number)
            self.assertEqual(session["lesson_id"], f"lesson_{number:02d}")
            self.assertEqual(session["index"], 0)
            self.assertGreaterEqual(len(session["questions"]), 1)

    def test_namespaced_callbacks_do_not_overlap_legacy_callbacks(self):
        callback = make_answer_callback(2)
        self.assertEqual(callback, "orthography_quiz_answer_2")
        self.assertEqual(parse_answer_callback(callback), 2)
        self.assertIsNone(parse_answer_callback("answer_2"))
        self.assertIsNone(parse_answer_callback("quiz_2_start"))
        self.assertIsNone(parse_answer_callback("orthography_quiz_answer_x"))

    def test_rejects_invalid_lesson_numbers_and_missing_questions(self):
        for number in (0, 23, True, "1"):
            with self.subTest(number=number), self.assertRaises(ValueError):
                build_quiz_session(self.converted, number)
        with self.assertRaises(ValueError):
            build_quiz_session({}, 1)

    def test_rejects_malformed_question_before_starting_session(self):
        broken = copy.deepcopy(self.converted)
        broken["lesson_01"][0]["answer"] = "not an option"
        with self.assertRaises(ValueError):
            build_quiz_session(broken, 1)



    def test_rejects_duplicate_options_before_starting_session(self):
        broken = copy.deepcopy(self.converted)
        broken["lesson_01"][0]["options"][1] = broken["lesson_01"][0]["options"][0]
        with self.assertRaises(ValueError):
            build_quiz_session(broken, 1)

    def test_rejects_missing_explanation_before_session_starts(self):
        broken = copy.deepcopy(self.converted)
        broken["lesson_01"][0]["explanation"] = " "
        with self.assertRaises(ValueError):
            build_quiz_session(broken, 1)

    def test_answer_progression_scores_and_finishes_without_rewards(self):
        quizzes = {
            "lesson_01": [
                {"question": "Q1", "options": ["A", "B"], "answer": "B", "explanation": "why B"},
                {"question": "Q2", "options": ["C", "D"], "answer": "C", "explanation": "why C"},
            ]
        }
        session = build_quiz_session(quizzes, 1)
        first = apply_answer(session, 1)
        self.assertTrue(first["correct"])
        self.assertFalse(first["completed"])
        self.assertEqual(first["score"], 1)
        second = apply_answer(session, 1)
        self.assertFalse(second["correct"])
        self.assertTrue(second["completed"])
        self.assertEqual(second["score"], 1)
        self.assertNotIn("xp", session)
        self.assertNotIn("rewards", session)
        with self.assertRaises(ValueError):
            apply_answer(session, 0)

    def test_answer_handler_rejects_wrong_session_and_bad_option(self):
        with self.assertRaises(ValueError):
            apply_answer({"course_id": "legacy"}, 0)
        session = build_quiz_session(self.converted, 1)
        with self.assertRaises(ValueError):
            apply_answer(session, 999)


    def test_course_session_cleanup_preserves_legacy_quiz(self):
        user_data = {
            "quiz": {"lesson": "وانە_1", "score": 3},
            SESSION_KEY: {"course_id": "orthography_foundations", "index": 2},
        }
        removed = clear_course_quiz_session(user_data)
        self.assertEqual(removed["index"], 2)
        self.assertNotIn(SESSION_KEY, user_data)
        self.assertEqual(user_data["quiz"], {"lesson": "وانە_1", "score": 3})

    def test_course_session_cleanup_is_safe_when_no_session_exists(self):
        user_data = {"quiz": {"score": 1}}
        self.assertIsNone(clear_course_quiz_session(user_data))
        self.assertEqual(user_data, {"quiz": {"score": 1}})


    def test_course_session_cleanup_rejects_non_mapping(self):
        with self.assertRaises(ValueError):
            clear_course_quiz_session(["not", "a", "mapping"])

    def test_start_callbacks_are_namespaced_and_validated(self):
        for number in range(1, 23):
            callback = make_start_callback(number)
            self.assertLessEqual(len(callback.encode("utf-8")), 64)
            self.assertEqual(parse_start_callback(callback), number)
        for invalid in (0, 23, True, "1"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                make_start_callback(invalid)
        self.assertIsNone(parse_start_callback("quiz_1_start"))
        self.assertIsNone(parse_start_callback("ofquiz_start_00"))
        self.assertIsNone(parse_start_callback("ofquiz_start_23"))
        self.assertIsNone(parse_start_callback("ofquiz_start_1"))

if __name__ == "__main__":
    unittest.main()
