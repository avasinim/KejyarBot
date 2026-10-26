import copy
import json
import unittest
from pathlib import Path

from course_data.orthography_quiz_adapter import convert_quiz_draft
from course_data.orthography_quiz_runtime import (
    SESSION_KEY,
    build_quiz_session,
    make_answer_callback,
    parse_answer_callback,
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


if __name__ == "__main__":
    unittest.main()
