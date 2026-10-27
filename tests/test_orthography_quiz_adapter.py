import copy
import json
import unittest
from pathlib import Path

from course_data.orthography_quiz_adapter import convert_quiz_draft


class OrthographyQuizAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).resolve().parents[1] / "course_data" / "orthography_foundations_quiz_draft.json"
        cls.data = json.loads(path.read_text(encoding="utf-8"))

    def test_converts_all_22_lessons_and_indexed_answers(self):
        converted = convert_quiz_draft(self.data)
        self.assertEqual(len(converted), 22)
        self.assertEqual(set(converted), {f"lesson_{n:02d}" for n in range(1, 23)})
        for group in self.data["quizzes"]:
            n = group["lesson_number"]
            targets = converted[f"lesson_{n:02d}"]
            self.assertEqual(len(targets), len(group["questions"]))
            for source, target in zip(group["questions"], targets):
                self.assertEqual(
                    set(target), {"question", "options", "answer", "explanation"}
                )
                self.assertEqual(target["question"], source["question"])
                self.assertEqual(target["answer"], source["options"][source["correct_option_index"]])
                self.assertEqual(target["options"], source["options"])
                self.assertEqual(target["explanation"], source["explanation"])

    def test_rejects_wrong_course(self):
        data = copy.deepcopy(self.data)
        data["course_id"] = "legacy"
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)


    def test_rejects_lesson_id_number_mismatch(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][0]["lesson_id"] = "lesson_02"
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_duplicate_lesson_number(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][1]["lesson_number"] = 1
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_duplicate_options_and_boolean_answer_index(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["options"][1] = data["quizzes"][0]["questions"][0]["options"][0]
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["correct_option_index"] = True
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_missing_question_text_and_empty_explanation(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["question"] = "   "
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["explanation"] = ""
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_non_object_draft_group_and_question(self):
        with self.assertRaises(ValueError):
            convert_quiz_draft(None)

        data = copy.deepcopy(self.data)
        data["quizzes"][0] = None
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0] = None
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)


    def test_rejects_duplicate_question_ids(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][1]["questions"][0]["id"] = data["quizzes"][0]["questions"][0]["id"]
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_whitespace_padded_question_and_explanation(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["question"] = " padded question "
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["explanation"] = " padded explanation "
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_whitespace_padded_option(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["options"][0] = " padded option "
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_whitespace_padded_question_id(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["id"] = " l1_q1 "
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_missing_question_id_and_unsupported_type(self):
        data = copy.deepcopy(self.data)
        del data["quizzes"][0]["questions"][0]["id"]
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["type"] = "true_false"
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)

    def test_rejects_invalid_correct_option_index(self):
        data = copy.deepcopy(self.data)
        data["quizzes"][0]["questions"][0]["correct_option_index"] = 99
        with self.assertRaises(ValueError):
            convert_quiz_draft(data)


if __name__ == "__main__":
    unittest.main()
