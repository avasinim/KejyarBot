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


def test_each_question_has_visible_chart_evidence():
    bank = load_bank()
    for mode in ("practice", "assessment"):
        for question in bank[mode]:
            assert question["section_id"].startswith("lesson1_chart_")
            assert question["source_evidence"]
            assert 0 <= question["answer_index"] < len(question["options"])


def test_only_chart_supported_counts_and_color_are_tested():
    bank = load_bank()
    allowed_prompts = {
        "بەپێی خشتەی وانەی یەکەم، ژمارەی گشتیی پیتەکانی ئەلفبێ چەندە؟",
        "لە خشتەکەدا ژمارەی نەبزوێنەکان چەندە؟",
        "بەپێی ڕونکردنەوەی وانەی ١، ژمارەی بزوێنەکان چەندە؟",
        "لە ڕونکردنەوەی وانەی ١دا ژمارەی بزوێنەکان چەندە؟",
        "لە خشتەی وانەکەدا بزوێنەکان بە کام ڕەنگە دیاریکراون؟",
        "ژمارەی گشتیی پیتەکانی ئەلفبێی نیشاندراو لە خشتەکەدا چەندە؟",
        "ژمارەی نەبزوێنەکان لە خشتەکەدا چەندە؟",
        "ژمارەی بزوێنەکان لە خشتەکەدا چەندە؟",
        "کام ڕەنگ لە خشتەکەدا بۆ نیشاندانی بزوێنەکان بەکارهاتووە؟",
    }
    for mode in ("practice", "assessment"):
        assert all(q["prompt"] in allowed_prompts for q in bank[mode])
    assert bank["source_correction"]["lesson_1_vowel_count"] == 8
    assert all("٦ پیت" not in q["options"] for mode in ("practice", "assessment") for q in bank[mode])
    assert bank["not_yet_authored"][:3] == [
        "sound-to-letter listening items",
        "letter-sequence completion",
        "letter-name matching",
    ]
