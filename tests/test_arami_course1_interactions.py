"""Source-grounding and schema tests for Arami Course 1 Lesson 1 interactions."""
import json
from pathlib import Path

from arami_lesson1_interaction import validate_question_bank

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
