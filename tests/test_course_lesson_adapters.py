import json
import unittest
from pathlib import Path

from course_lesson_adapters import adapt_conversation_lessons, adapt_unified_orthography_lessons

ROOT = Path(__file__).resolve().parents[1]


def load_payload(name):
    with (ROOT / name).open(encoding="utf-8") as handle:
        return json.load(handle)


class ConversationLessonAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payloads = [
            load_payload("course_data/daily_conversation_lessons_01_06.json"),
            load_payload("course_data/daily_conversation_lessons_07_12.json"),
        ]

    def test_loads_twelve_lessons_with_unique_namespaced_keys(self):
        lessons, quizzes = adapt_conversation_lessons("daily_conversation", self.payloads)
        expected = [f"daily_conversation_{i:02d}" for i in range(1, 13)]
        self.assertEqual(list(lessons), expected)
        self.assertEqual(list(quizzes), expected)
        self.assertTrue(all(lessons[key]["content"] for key in expected))
        self.assertTrue(all(lessons[key]["review_status"] == "draft_source_check_required" for key in expected))
        self.assertTrue(all("تێبینیی سەرچاوە" in lessons[key]["content"] for key in expected))

    def test_unified_orthography_adapter_loads_twelve_draft_lessons(self):
        payload = load_payload("course_data/unified_orthography_lessons_01_12.json")
        lessons, quizzes = adapt_unified_orthography_lessons(payload)
        expected = [f"unified_orthography_{i:02d}" for i in range(1, 13)]
        self.assertEqual(list(lessons), expected)
        self.assertEqual(list(quizzes), expected)
        self.assertTrue(all(lessons[key]["content"] for key in expected))
        self.assertTrue(all(lessons[key]["review_status"] == "draft_source_check_required" for key in expected))
        self.assertTrue(all(quizzes[key] for key in expected))

    def test_course_one_legacy_keys_are_not_used(self):
        lessons, _ = adapt_conversation_lessons("daily_conversation", self.payloads)
        self.assertNotIn("وانە_1", lessons)
        self.assertNotIn("وانە_12", lessons)

    def test_invalid_quiz_answer_index_is_rejected(self):
        payload = {"lessons": [{
            "number": 1,
            "title": "Test",
            "quiz": [{"q": "Question?", "options": ["A", "B"], "answer": 2}],
        }]}
        with self.assertRaises(ValueError):
            adapt_conversation_lessons("daily_conversation", [payload])

    def test_duplicate_lesson_number_is_rejected(self):
        payload = {"lessons": [
            {"number": 1, "title": "One", "quiz": []},
            {"number": 1, "title": "Duplicate", "quiz": []},
        ]}
        with self.assertRaises(ValueError):
            adapt_conversation_lessons("daily_conversation", [payload])

    def test_non_contiguous_lesson_number_is_rejected(self):
        payload = {"lessons": [{"number": 2, "title": "Two", "quiz": []}]}
        with self.assertRaises(ValueError):
            adapt_conversation_lessons("daily_conversation", [payload])


if __name__ == "__main__":
    unittest.main()
