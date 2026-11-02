import unittest

from arami_lesson1_interaction import create_session, select_answer, submit_answer
from arami_lesson1_presentation import (
    answer_feedback,
    lesson_action_payload,
    question_view,
    result_view,
)


BANK = [
    {
        "id": "vowel-count",
        "type": "recognize",
        "section_id": "lesson1_vowel_count",
        "prompt": "ژمارەی بزوێنەکانی وانەی ١ چەندە؟",
        "options": ["٨ بزوێن", "٦ بزوێن"],
        "answer_index": 0,
    },
    {
        "id": "color-key",
        "type": "classify",
        "section_id": "lesson1_chart_categories",
        "prompt": "بزوێنەکان بە کام ڕەنگ نیشان دراون؟",
        "options": ["سوور", "سەوز"],
        "answer_index": 0,
    },
]


class AramiLesson1PresentationTests(unittest.TestCase):
    def test_action_callbacks_are_namespaced_and_allowlisted(self):
        self.assertEqual(lesson_action_payload("practice"), "arami1:practice")
        self.assertEqual(lesson_action_payload("assessment"), "arami1:assessment")
        for unsafe in ("latin", "finish_1", "delete", ""):
            with self.assertRaises(ValueError):
                lesson_action_payload(unsafe)

    def test_question_view_does_not_expose_correct_answer(self):
        session = create_session(BANK, "practice")
        view = question_view(session)
        self.assertEqual(view["prompt"], BANK[0]["prompt"])
        self.assertEqual(view["options"], BANK[0]["options"])
        self.assertNotIn("answer_index", view)
        self.assertFalse(view["submitted"])

    def test_feedback_requires_matching_submitted_record(self):
        session = create_session(BANK, "practice")
        question = BANK[0]
        select_answer(session, 0)
        record = submit_answer(session)
        feedback = answer_feedback(question, record)
        self.assertTrue(feedback["correct"])
        self.assertEqual(feedback["correct_index"], 0)
        with self.assertRaises(ValueError):
            answer_feedback(BANK[1], record)

    def test_result_view_reports_score_and_missed_section(self):
        session = create_session(BANK, "assessment")
        select_answer(session, 1)
        submit_answer(session)
        select_answer(session, 0)
        submit_answer(session)
        view = result_view(session)
        self.assertEqual(view["score"], "1/2")
        self.assertEqual(view["percentage"], 50)
        self.assertTrue(view["can_retry_missed"])
        self.assertEqual(view["missed"], [{"question_id": "vowel-count", "section_id": "lesson1_vowel_count"}])


if __name__ == "__main__":
    unittest.main()
