"""Structural quality guards for the active multi-course quiz banks.

These checks catch malformed or repetitive quiz data; they do not replace
human review of Kurdish language, pedagogy, or factual answer correctness.
"""
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_FILES = {
    "daily_conversation": [
        "course_data/daily_conversation_lessons_01_06.json",
        "course_data/daily_conversation_lessons_07_30.json",
        "course_data/daily_conversation_lessons_31_36.json",
        "course_data/daily_conversation_lessons_37_42.json",
        "course_data/daily_conversation_lessons_43_48.json",
    ],
    "unified_orthography": [
        "course_data/unified_orthography_lessons_01_12.json",
    ],
}


def load_lessons(paths):
    lessons = []
    for relative_path in paths:
        with (ROOT / relative_path).open(encoding="utf-8") as handle:
            lessons.extend(json.load(handle).get("lessons", []))
    return lessons


class CourseQuizContentQualityTests(unittest.TestCase):
    def test_quiz_questions_have_valid_options_answers_and_explanations(self):
        for course_id, paths in COURSE_FILES.items():
            seen_questions = set()
            lessons = load_lessons(paths)
            with self.subTest(course=course_id):
                self.assertTrue(lessons, "course quiz data must not be empty")
                for lesson in lessons:
                    self.assertTrue(lesson.get("title"), f"lesson {lesson.get('number')} has no title")
                    self.assertTrue(lesson.get("quiz"), f"lesson {lesson.get('number')} has no quiz")
                    for question_number, question in enumerate(lesson["quiz"], start=1):
                        label = f"{course_id} lesson {lesson.get('number')} question {question_number}"
                        prompt = question.get("q", "").strip()
                        options = question.get("options")
                        answer = question.get("answer")
                        explanation = question.get("explanation", "").strip()

                        self.assertTrue(prompt, f"{label}: missing question text")
                        self.assertNotIn(prompt, seen_questions, f"{label}: duplicate question text")
                        seen_questions.add(prompt)
                        self.assertIsInstance(options, list, f"{label}: options must be a list")
                        self.assertGreaterEqual(len(options), 2, f"{label}: needs at least two options")
                        self.assertTrue(all(isinstance(option, str) and option.strip() for option in options),
                                        f"{label}: options must be non-empty strings")
                        self.assertEqual(len(options), len(set(options)), f"{label}: duplicate options")
                        self.assertIsInstance(answer, int, f"{label}: answer must be an option index")
                        self.assertGreaterEqual(answer, 0, f"{label}: answer index cannot be negative")
                        self.assertLess(answer, len(options), f"{label}: answer index is out of range")
                        self.assertTrue(explanation, f"{label}: missing explanation")

    def test_expected_quiz_bank_sizes_are_preserved(self):
        expected = {"daily_conversation": 48, "unified_orthography": 12}
        for course_id, paths in COURSE_FILES.items():
            with self.subTest(course=course_id):
                lessons = load_lessons(paths)
                self.assertEqual(len(lessons), expected[course_id])
                numbers = [lesson.get("number") for lesson in lessons]
                self.assertEqual(numbers, list(range(1, expected[course_id] + 1)))


if __name__ == "__main__":
    unittest.main()
