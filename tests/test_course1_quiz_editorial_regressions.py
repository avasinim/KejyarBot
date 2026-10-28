import json
import unittest
from pathlib import Path


class CourseOneQuizEditorialRegressionTests(unittest.TestCase):
    def test_lesson_four_question_matches_original_example_spelling(self):
        path = Path(__file__).resolve().parents[1] / "course_data" / "orthography_foundations_quiz_draft.json"
        draft = json.loads(path.read_text(encoding="utf-8"))
        lesson_four = next(item for item in draft["quizzes"] if item["lesson_id"] == "lesson_04")
        question = next(item for item in lesson_four["questions"] if item["id"] == "l4_q3")

        self.assertIn("«ایمان»", question["question"])
        self.assertNotIn("«اِیمان»", question["question"])
        self.assertIn("ئـ + ی = ئیمان", question["explanation"])
        self.assertEqual(question["options"][question["correct_option_index"]], "ئیمان")


if __name__ == "__main__":
    unittest.main()
