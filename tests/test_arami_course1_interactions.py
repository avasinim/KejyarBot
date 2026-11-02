"""Source-grounding and schema tests for Arami Course 1 Lesson 1 interactions."""
import json
from pathlib import Path

from arami_lesson1_interaction import (
    create_session, current_question, select_answer, submit_answer,
    session_result, validate_question_bank,
)

BANK_PATH = Path(__file__).resolve().parents[1] / "course_data" / "arami_course1_lesson_01_interactions.json"


def load_bank():
    return json.loads(BANK_PATH.read_text(encoding="utf-8"))


def test_lesson1_practice_and_assessment_banks_are_valid():
    bank = load_bank()
    assert bank["course_id"] == "arami_orthography_foundations"
    assert bank["lesson_id"] == "arami_course1_lesson_01"
    assert validate_question_bank(bank["practice"])
    assert validate_question_bank(bank["assessment"])


def test_each_question_has_verified_lesson_evidence():
    bank = load_bank()
    for mode in ("practice", "assessment"):
        for question in bank[mode]:
            assert question["section_id"] in {
                "lesson1_alphabet_count", "lesson1_vowel_count",
                "lesson1_dual_letters", "lesson1_short_i",
            }
            assert question["source_evidence"]
            assert 0 <= question["answer_index"] < len(question["options"])


def test_only_five_pdf_exercise_topics_are_tested():
    bank = load_bank()
    for mode in ("practice", "assessment"):
        assert len(bank[mode]) == 5
        answers = {q["section_id"]: q["options"][q["answer_index"]] for q in bank[mode]}
        assert answers["lesson1_alphabet_count"] == "٣٤ پیت"
        assert answers["lesson1_vowel_count"] == "٨ بزوێن"
        assert answers["lesson1_dual_letters"] == "(و) و (ی)"
        assert sum(q["section_id"] == "lesson1_short_i" for q in bank[mode]) == 2
        assert all(q["source_evidence"] for q in bank[mode])
    assert bank["source_correction"]["lesson_1_vowel_count"] == 8



def test_selection_does_not_count_as_an_answer_until_submission():
    bank = load_bank()["practice"]
    session = create_session(bank, "practice")

    select_answer(session, 0)

    assert session["answers"] == []
    assert session["index"] == 0
    assert current_question(session)["id"] == bank[0]["id"]


def test_submitted_question_cannot_be_submitted_twice():
    bank = load_bank()["practice"]
    session = create_session(bank[:1], "practice")
    select_answer(session, bank[0]["answer_index"])

    recorded = submit_answer(session)

    assert recorded["correct"] is True
    assert len(session["answers"]) == 1
    assert session["closed"] is True
    try:
        submit_answer(session)
    except ValueError:
        pass
    else:
        raise AssertionError("a completed question must not be recorded twice")
    assert len(session["answers"]) == 1
    assert session_result(session)["correct"] == 1


def test_retry_attempt_is_a_new_session_and_does_not_change_original_answers():
    bank = load_bank()["practice"]
    session = create_session(bank[:2], "practice")
    select_answer(session, (bank[0]["answer_index"] + 1) % len(bank[0]["options"]))
    submit_answer(session)
    select_answer(session, bank[1]["answer_index"])
    submit_answer(session)

    original_answers = list(session["answers"])
    assert session_result(session)["incorrect"] == 1
    from arami_lesson1_interaction import retry_missed
    retry = retry_missed(session)

    assert retry is not None
    assert retry["mode"] == "practice"
    assert len(retry["questions"]) == 1
    assert session["answers"] == original_answers
    assert retry["answers"] == []
