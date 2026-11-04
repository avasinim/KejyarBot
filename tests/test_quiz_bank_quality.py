import json
import unittest
from pathlib import Path

from arami_course1_runtime import (
    load_arami_lesson1_interactions,
    load_arami_lesson5_interactions,
)
from arami_course1_telegram import load_manifest, load_question_banks


ROOT = Path(__file__).resolve().parents[1]


def _normalized_prompt(value):
    return " ".join(str(value).split()).casefold()


class QuizBankQualityTests(unittest.TestCase):
    def test_course1_practice_and_assessment_prompts_are_not_reused_between_lessons(self):
        banks = load_question_banks(ROOT)
        banks[1] = load_arami_lesson1_interactions(ROOT)
        banks[5] = load_arami_lesson5_interactions(ROOT)
        manifest = load_manifest(ROOT)
        self.assertEqual(len(manifest["lessons"]), 21)
        self.assertEqual(set(banks), set(range(1, 22)))

        for mode in ("practice", "assessment"):
            seen = {}
            for lesson_number in range(1, 22):
                for question in banks[lesson_number][mode]:
                    prompt = _normalized_prompt(question.get("prompt", question.get("question", "")))
                    self.assertTrue(prompt, f"Lesson {lesson_number} {mode}: empty prompt")
                    previous = seen.get(prompt)
                    self.assertIsNone(
                        previous,
                        f"Repeated {mode} prompt in lessons {previous} and {lesson_number}: {prompt}",
                    )
                    seen[prompt] = lesson_number
                    options = question["options"]
                    self.assertGreaterEqual(len(options), 2)
                    self.assertEqual(len(options), len(set(options)))
                    answer_index = question["answer_index"]
                    self.assertIsInstance(answer_index, int)
                    self.assertGreaterEqual(answer_index, 0)
                    self.assertLess(answer_index, len(options))

    def test_course1_lessons_4_and_6_practice_keys_match_their_source_facts(self):
        banks = load_question_banks(ROOT)
        lesson4 = banks[4]["practice"]
        lesson6 = banks[6]["practice"]

        expected_lesson4 = [
            (["ب", "ۆ", "وو"], 0),
            (["w", "u", "i"], 1),
            (["î", "y", "i"], 1),
            (["پیتێکی تایبەتی هەیە", "دەنگی کورت (i) ـ بزرۆکەیە و پیتێکی تایبەتی بۆی دانەنراوە", "دەنگی نەبزوێنەیە"], 1),
            (["٣٤", "٣٦", "٣٧"], 2),
        ]
        expected_lesson6 = [
            (["بزوێن", "نەبزوێن", "نیشانەی خاڵبەندی"], 1),
            (["نەبزوێن", "بزوێن", "پیتی بێدەنگ"], 1),
            (["بزوێن", "نەبزوێن", "نیشانەی خاڵبەندی"], 1),
            (["پیتێکی تایبەتی بۆ دانراوە", "بە پیتی (و) دەنووسرێت", "هیچ پیتێکی تایبەتی بۆ دانەنراوە"], 2),
            (["دوو دەنگ", "سێ دەنگ", "چوار دەنگ"], 2),
        ]
        self.assertEqual([(q["options"], q["answer_index"]) for q in lesson4], expected_lesson4)
        self.assertEqual([(q["options"], q["answer_index"]) for q in lesson6], expected_lesson6)

    def test_active_daily_and_unified_orthography_quizzes_have_valid_distinct_options(self):
        daily_paths = (
            "daily_conversation_lessons_01_06.json",
            "daily_conversation_lessons_07_30.json",
            "daily_conversation_lessons_31_36.json",
            "daily_conversation_lessons_37_42.json",
        )
        datasets = []
        for filename in daily_paths:
            payload = json.loads((ROOT / "course_data" / filename).read_text(encoding="utf-8"))
            datasets.extend((lesson["number"], question) for lesson in payload["lessons"] for question in lesson.get("quiz", []))

        orthography = json.loads(
            (ROOT / "course_data" / "unified_orthography_lessons_01_66.json").read_text(encoding="utf-8")
        )
        datasets.extend(
            (lesson["number"], question)
            for lesson in orthography["lessons"]
            for question in lesson.get("quiz", [])
        )

        for lesson_number, question in datasets:
            with self.subTest(lesson=lesson_number, prompt=question.get("q")):
                options = question["options"]
                self.assertGreaterEqual(len(options), 2)
                # Case is meaningful in orthography questions (e.g. PDF vs pdf).
                self.assertEqual(len(options), len(set(options)))
                answer = question["answer"]
                self.assertIsInstance(answer, int)
                self.assertGreaterEqual(answer, 0)
                self.assertLess(answer, len(options))
                self.assertTrue(str(question.get("explanation", "")).strip())


if __name__ == "__main__":
    unittest.main()
