"""Source-fidelity regression checks for Course 3."""
import json
import unittest
from pathlib import Path


COURSE_PATH = (
    Path(__file__).resolve().parents[1]
    / "course_data"
    / "unified_orthography_lessons_01_66.json"
)


class CourseThreeSourceFidelityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def lesson(self, number):
        return self.lessons[number - 1]

    def test_lesson_10_preserves_the_books_dialect_examples_and_qualification(self):
        lesson = self.lesson(10)
        examples = {pair[0] for pair in lesson["examples"]}
        self.assertIn("بیستوین (بێستوون)، چوی (چۆن)، دوێت (کچ)", examples)
        self.assertIn("سویر (سوور، شایی)، دویر (دوور)، ژویر (ژوور)، نویسەر (نووسەر)", examples)
        self.assertIn("بیستۊن، دۊر، سۊر", examples)
        self.assertTrue(any("زۆربەی زمانەوانان" in point for point in lesson["key_points"]))

    def test_lesson_38_keeps_irregular_verb_paradigms_from_pages_45_to_47(self):
        lesson = self.lesson(38)
        examples = {pair[0] for pair in lesson["examples"]}
        self.assertTrue(any("ژیام، ژیایت، ژیا" in example for example in examples))
        self.assertTrue(any("گریام، گریایت، گریا" in example for example in examples))
        self.assertTrue(any("شیام، شیایت، شیا" in example for example in examples))
        self.assertTrue(any("دەژی/دەژێت" in example for example in examples))
        self.assertIn("٤٥–٤٧", lesson["source"]["pages"])

    def test_lesson_50_retains_examples_from_book_page_58_and_59(self):
        lesson = self.lesson(50)
        examples = {pair[0] for pair in lesson["examples"]}
        self.assertIn("پێم وا نییە، پێم وا بوو", examples)
        self.assertIn("تەمەندرێژ بیت", examples)
        self.assertIn("دڵناسک", examples)
        self.assertIn("ئەوان چوونە ژوورەوە", examples)
        self.assertIn("هاتوچۆ، دەستوبرد", examples)
        self.assertIn("نییە", examples)
        self.assertIn("٥٨", lesson["source"]["pages"])
        self.assertIn("٥٩", lesson["source"]["pages"])

    def test_lesson_59_distinguishes_dialogue_marker_from_sentence_dash(self):
        lesson = self.lesson(59)
        examples = {pair[0] for pair in lesson["examples"]}
        # The book uses U+0640 at the start of dialogue turns, but ASCII
        # hyphens for parenthetical interruptions and numeric ranges.
        self.assertIn("ـ ئاکۆ، گوێت لە سەربازەکانە؟", examples)
        self.assertIn(
            "پیرەمێرد - حاجی تۆفیق - لە وەرگێڕانی هۆنراوەدا دەستی بااڵی هەبوو.",
            examples,
        )
        self.assertIn(
            "کوردستان - نیشتمانی ئێمە - جوانترین شوێنە.",
            examples,
        )
        self.assertIn("٧٨", lesson["source"]["pages"])


if __name__ == "__main__":
    unittest.main()
