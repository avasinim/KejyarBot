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
            assert question["section_id"] in {"lesson1_vowel_count", "lesson1_chart_categories"}
            assert question["source_evidence"]
            assert 0 <= question["answer_index"] < len(question["options"])


def test_only_verified_lesson_facts_and_chart_color_are_tested():
    bank = load_bank()
    allowed_prompts = {
        "ژمارەی بزوێنەکانی وانەی ١ چەندە؟",
        "بەپێی فێرکاریی وانەی ١، چەند بزوێن هەن؟",
        "لە خشتەی وانەکەدا بزوێنەکان بە کام ڕەنگە دیاریکراون؟",
        "کام ڕەنگ لە خشتەکەدا بۆ نیشاندانی بزوێنەکان بەکارهاتووە؟",
    }
    for mode in ("practice", "assessment"):
        assert all(q["prompt"] in allowed_prompts for q in bank[mode])
    assert bank["source_correction"]["lesson_1_vowel_count"] == 8
    vowel_questions = [q for mode in ("practice", "assessment") for q in bank[mode] if q["section_id"] == "lesson1_vowel_count"]
    assert len(vowel_questions) == 2
    assert all(q["options"][q["answer_index"]] == "٨ بزوێن" for q in vowel_questions)
    assert all("٦ بزوێن" not in q["options"] for q in vowel_questions)
    assert bank["not_yet_authored"][:3] == [
        "sound-to-letter listening items",
        "letter-sequence completion",
        "letter-name matching",
    ]
