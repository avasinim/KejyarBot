"""Regression checks for Course 3 quiz prompt clarity."""
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class UnifiedOrthographyQuizPromptTests(unittest.TestCase):
    def test_quiz_prompts_are_unique_across_the_66_lessons(self):
        path = ROOT / "course_data" / "unified_orthography_lessons_01_66.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        lessons = payload.get("lessons", [])
        self.assertEqual(len(lessons), 66)
        prompts = [
            question["q"].strip().casefold()
            for lesson in lessons
            for question in lesson.get("quiz", [])
        ]
        self.assertEqual(len(prompts), 202)
        self.assertEqual(len(prompts), len(set(prompts)))

    def test_rewritten_prompts_keep_question_options_and_answer_keys(self):
        path = ROOT / "course_data" / "unified_orthography_lessons_01_66.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        for lesson in payload["lessons"]:
            for question in lesson.get("quiz", []):
                options = question.get("options", [])
                answer = question.get("answer")
                self.assertGreaterEqual(len(options), 2)
                self.assertEqual(len(options), len(set(options)))
                self.assertIsInstance(answer, int)
                self.assertGreaterEqual(answer, 0)
                self.assertLess(answer, len(options))
                self.assertTrue(question.get("explanation", "").strip())


if __name__ == "__main__":
    unittest.main()
