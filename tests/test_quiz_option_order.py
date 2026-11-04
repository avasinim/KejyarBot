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


    def test_all_active_course_quiz_banks_keep_their_correct_answers(self):
        import bot

        for lesson_id, questions in bot.QUIZ_DATA.items():
            randomized = randomized_question_copy(questions, rng=ReverseRng())
            self.assertEqual(len(randomized), len(questions), lesson_id)
            for shown, source in zip(randomized, questions):
                self.assertEqual(set(shown["options"]), set(source["options"]), lesson_id)
                if "answer_index" in shown:
                    self.assertEqual(
                        shown["options"][shown["answer_index"]],
                        source["options"][source["answer_index"]],
                        lesson_id,
                    )
                else:
                    self.assertIn(shown["answer"], shown["options"], lesson_id)


    def test_every_arami_course1_practice_and_assessment_bank_is_randomized_safely(self):
        from pathlib import Path

        from arami_course1_telegram import load_question_banks
        from arami_course1_runtime import (
            load_arami_lesson1_interactions,
            load_arami_lesson5_interactions,
        )
        from arami_lesson1_interaction import create_session

        root = Path(__file__).resolve().parents[1]
        banks = load_question_banks(root)
        lesson1 = load_arami_lesson1_interactions(root)
        lesson5 = load_arami_lesson5_interactions(root)
        all_banks = {
            **{number: record for number, record in banks.items()},
            1: lesson1,
            5: lesson5,
        }
        self.assertEqual(set(all_banks), set(range(1, 22)))

        for lesson_number, lesson_banks in all_banks.items():
            for mode in ("practice", "assessment"):
                source = lesson_banks[mode]
                snapshot = [
                    dict(item, options=list(item["options"]))
                    for item in source
                ]
                session = create_session(source, mode)
                self.assertEqual(len(session["questions"]), len(source))
                for shown, original in zip(session["questions"], source):
                    self.assertEqual(set(shown["options"]), set(original["options"]))
                    self.assertEqual(
                        shown["options"][shown["answer_index"]],
                        original["options"][original["answer_index"]],
                        f"Lesson {lesson_number} {mode} {original['id']}",
                    )
                self.assertEqual(source, snapshot, f"source bank mutated: lesson {lesson_number} {mode}")

    def test_invalid_answer_is_rejected(self):
        with self.assertRaises(ValueError):
            randomized_question_copy([{"options": ["A", "B"], "answer": "missing"}])


if __name__ == "__main__":
    unittest.main()
