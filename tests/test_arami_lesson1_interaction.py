import unittest

from arami_lesson1_interaction import (
    InvalidQuestionBank,
    create_session,
    current_question,
    select_answer,
    submit_answer,
    session_result,
    retry_missed,
    validate_question_bank,
)


BANK = [
    {
        "id": "q1",
        "type": "recognize",
        "prompt": "PROMPT_A",
        "options": ["A", "B", "C"],
        "answer_index": 1,
        "section_id": "section-a",
    },
    {
        "id": "q2",
        "type": "classify",
        "prompt": "PROMPT_B",
        "options": ["X", "Y"],
        "answer_index": 0,
        "section_id": "section-b",
    },
]


class AramiLesson1InteractionTests(unittest.TestCase):
    def test_bank_is_validated_without_rewriting_source_records(self):
        original = [dict(item) for item in BANK]
        self.assertTrue(validate_question_bank(BANK))
        session = create_session(BANK, "practice")
        self.assertEqual(BANK, original)
        self.assertEqual(session["questions"], BANK)

    def test_selection_does_not_submit_or_score(self):
        session = create_session(BANK, "practice")
        select_answer(session, 1)
        self.assertEqual(session["answers"], [])
        self.assertEqual(session["index"], 0)
        self.assertEqual(session["selected_index"], 1)

    def test_submit_records_correctness_and_advances_once(self):
        session = create_session(BANK, "assessment")
        select_answer(session, 1)
        first = submit_answer(session)
        self.assertTrue(first["correct"])
        self.assertEqual(session["index"], 1)
        self.assertEqual(len(session["answers"]), 1)
        self.assertIsNone(session["selected_index"])

    def test_double_submit_is_rejected(self):
        session = create_session(BANK, "assessment")
        select_answer(session, 1)
        submit_answer(session)
        with self.assertRaises(ValueError):
            submit_answer(session)
        self.assertEqual(len(session["answers"]), 1)

    def test_final_result_has_score_percentage_and_section_links(self):
        session = create_session(BANK, "assessment")
        select_answer(session, 0)
        submit_answer(session)
        select_answer(session, 0)
        submit_answer(session)
        self.assertEqual(
            session_result(session),
            {
                "mode": "assessment",
                "total": 2,
                "correct": 1,
                "incorrect": 1,
                "percentage": 50,
                "missed": [{"question_id": "q1", "section_id": "section-a"}],
            },
        )

    def test_retry_missed_creates_separate_practice_session(self):
        session = create_session(BANK, "assessment")
        select_answer(session, 0)
        submit_answer(session)
        select_answer(session, 0)
        submit_answer(session)
        retry = retry_missed(session)
        self.assertEqual(retry["mode"], "practice")
        self.assertEqual([q["id"] for q in retry["questions"]], ["q1"])
        self.assertEqual(session["answers"], retry["answers"])

    def test_perfect_score_has_no_retry_session(self):
        session = create_session(BANK, "practice")
        for answer in (1, 0):
            select_answer(session, answer)
            submit_answer(session)
        self.assertIsNone(retry_missed(session))

    def test_audio_task_requires_explicit_asset_reference(self):
        item = dict(BANK[0], id="listen-1", type="listen")
        with self.assertRaises(InvalidQuestionBank):
            validate_question_bank([item])
        item["audio_asset"] = "verified/lesson-audio.ogg"
        self.assertTrue(validate_question_bank([item]))

    def test_duplicate_ids_and_duplicate_options_are_rejected(self):
        with self.assertRaises(InvalidQuestionBank):
            validate_question_bank([BANK[0], BANK[0]])
        bad = dict(BANK[0], options=["A", "A"])
        with self.assertRaises(InvalidQuestionBank):
            validate_question_bank([bad])

    def test_invalid_indices_and_unfinished_results_are_rejected(self):
        session = create_session(BANK, "practice")
        with self.assertRaises(ValueError):
            select_answer(session, 9)
        with self.assertRaises(ValueError):
            session_result(session)
        with self.assertRaises(ValueError):
            create_session(BANK, "latin")


if __name__ == "__main__":
    unittest.main()
