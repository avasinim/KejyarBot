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
        self.assertTrue(any("شێوەزار" in point and "شیکاریی فۆنۆلۆژی" in point for point in lesson["key_points"]))

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
        self.assertNotIn("سلێمانییش", examples)  # belongs to lesson 49 / book p.57, not lesson 50 pp.58–59
        self.assertIn("نییە", examples)
        self.assertIn("٥٨", lesson["source"]["pages"])
        self.assertIn("٥٩", lesson["source"]["pages"])

    def test_lesson_51_uses_comma_between_abbreviated_names(self):
        lesson = self.lesson(51)
        examples = " ".join(pair[0] for pair in lesson["examples"])
        self.assertIn("د. سۆران، م. م. بەدرخان", examples)
        self.assertNotIn("د. سۆران؛ م. م. بەدرخان", examples)
        self.assertIn("نەورۆز جەژنێکی کوردییە.", examples)
        self.assertIn("ی. ن. ک.", examples)
        self.assertIn("د. خ.", examples)
        self.assertNotIn("ی.ن.ک.", examples)
        self.assertNotIn("نەورۆز یەکەم مانگی کوردییە.", examples)

    def test_lesson_52_colon_example_preserves_the_book_list(self):
        lesson = self.lesson(52)
        examples = " ".join(pair[0] for pair in lesson["examples"])
        self.assertIn(
            "میرنشینە کوردییەکان بریتی بوون لە: ئەردەڵان، سۆران، بادینان، بابان، هەکاری و بۆتان.",
            examples,
        )

    def test_lesson_54_semicolons_separate_labeled_complex_groups(self):
        lesson = self.lesson(54)
        examples = " ".join(pair[0] for pair in lesson["examples"])
        self.assertIn("گرووپی یەکەم: هەولێر، سلێمانی؛ گرووپی دووەم: دهۆک، کەرکووک.", examples)
        self.assertIn("گرووپی یەکەم: زمان، ئەدەب؛ گرووپی دووەم: مێژوو، کولتوور.", examples)

    def test_lesson_55_covers_uncertainty_and_question_intonation(self):
        lesson = self.lesson(55)
        examples = {pair[0] for pair in lesson["examples"]}
        key_points = " ".join(lesson["key_points"])
        self.assertIn("ئەو لە ساڵی ١٩٨٥ (؟) لەدایک بووە.", examples)
        self.assertIn("دەنگ و ئاوازی پرسیار", key_points)

    def test_lesson_56_uses_the_books_exclamation_mark_purposes(self):
        lesson = self.lesson(56)
        key_points = " ".join(lesson["key_points"])
        self.assertIn("هاندان و دنەدان", key_points)
        self.assertNotIn("پشتیوانی", key_points)
        examples = {pair[0] for pair in lesson["examples"]}
        self.assertIn("ئۆخهی! ئااڵی کورد هەڵکرا.", examples)
        self.assertIn("ئێمە پاڵەوانێتیمان بەدەست هێناوە!", examples)
        self.assertIn("چ خۆش بوو دوێنێ چاوم پێت کەوت!", examples)

    def test_lesson_57_nested_quotation_marks_match_the_book(self):
        lesson = self.lesson(57)
        examples = " ".join(pair[0] for pair in lesson["examples"])
        self.assertIn(
            '"ماسیگرە سەرلێشێواوەکە هاواری کرد \'سەیری ئەو دەیدامە بکەن\' پاشان بێدەنگ بوو"',
            examples,
        )

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
