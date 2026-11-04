import unittest

from quiz_option_order import randomized_question_copy


class ReverseRng:
    @staticmethod
    def shuffle(items):
        items.reverse()


class QuizOptionOrderTests(unittest.TestCase):
    def test_answer_text_remains_correct_after_option_shuffle(self):
        source = [{"question": "Q", "options": ["wrong-a", "correct", "wrong-b"], "answer": "correct"}]
        result = randomized_question_copy(source, rng=ReverseRng())
        self.assertEqual(result[0]["options"], ["wrong-b", "correct", "wrong-a"])
        self.assertEqual(result[0]["answer"], "correct")
        self.assertEqual(source[0]["options"], ["wrong-a", "correct", "wrong-b"])

    def test_answer_index_is_rebased_after_option_shuffle(self):
        source = [{"prompt": "Q", "options": ["A", "B", "C"], "answer_index": 1}]
        result = randomized_question_copy(source, rng=ReverseRng())
        self.assertEqual(result[0]["options"], ["C", "B", "A"])
        self.assertEqual(result[0]["answer_index"], 1)
        self.assertEqual(source[0]["answer_index"], 1)
        self.assertEqual(source[0]["options"], ["A", "B", "C"])

    def test_integer_answer_index_is_converted_to_correct_answer_text(self):
        source = [{"question": "Q", "options": ["A", "B", "C"], "answer": 0}]
        result = randomized_question_copy(source, rng=ReverseRng())
        self.assertEqual(result[0]["options"], ["C", "B", "A"])
        self.assertEqual(result[0]["answer"], "A")
        self.assertEqual(source[0]["answer"], 0)

    def test_each_attempt_gets_an_independent_copy(self):
        source = [{"question": "Q", "options": ["A", "B"], "answer": "A"}]
        first = randomized_question_copy(source, rng=ReverseRng())
        second = randomized_question_copy(source, rng=ReverseRng())
        self.assertIsNot(first, second)
        self.assertIsNot(first[0]["options"], second[0]["options"])
        self.assertEqual(source[0]["options"], ["A", "B"])

    def test_invalid_answer_is_rejected(self):
        with self.assertRaises(ValueError):
            randomized_question_copy([{"options": ["A", "B"], "answer": "missing"}])


if __name__ == "__main__":
    unittest.main()
