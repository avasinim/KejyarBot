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


    def test_lessons_36_and_37_match_book_page_44(self):
        lesson36 = self.lesson(36)
        ex36 = {pair[0] for pair in lesson36["examples"]}
        self.assertIn("خانووەکەم کڕی", ex36)
        self.assertIn("خانۆکەم کڕی", ex36)
        self.assertIn("جوانووەکەم ئاو دا", ex36)
        self.assertIn("جوانۆکەم ئاو دا", ex36)

        lesson37 = self.lesson(37)
        ex37 = {pair[0] for pair in lesson37["examples"]}
        self.assertIn("یەک پیاو", ex37)
        self.assertIn("پیاوێک", ex37)
        self.assertIn("گرمەیەک", ex37)
        self.assertIn("گرمەیێک", ex37)
        self.assertIn("سویدی + یەک = سویدییەک / سویدی + یێک = سویدییێک", ex37)
        for n in (36, 37):
            self.assertIn("هیچ سەرچاوەی دەرەکی", self.lesson(n)["source"]["source_policy"])

    def test_lesson_38_keeps_irregular_verb_paradigms_from_pages_45_to_47(self):
        lesson = self.lesson(38)
        examples = {pair[0] for pair in lesson["examples"]}
        self.assertTrue(any("ژیام، ژیایت، ژیا" in example for example in examples))
        self.assertTrue(any("گریام، گریایت، گریا" in example for example in examples))
        self.assertTrue(any("شیام، شیایت، شیا" in example for example in examples))
        self.assertTrue(any("دەژی/دەژێت" in example for example in examples))
        self.assertIn("٤٥–٤٧", lesson["source"]["pages"])


    def test_lessons_39_to_43_match_book_pages_48_to_51(self):
        lesson39 = self.lesson(39)
        ex39 = {pair[0] for pair in lesson39["examples"]}
        self.assertIn("ڤیکتۆر هۆگۆ", ex39)
        self.assertIn("ڤیدیۆ", ex39)
        self.assertIn("ئەرشیڤ، ئارشیڤ", ex39)
        self.assertIn("ئێڤا", ex39)

        lesson40 = self.lesson(40)
        ex40 = {pair[0] for pair in lesson40["examples"]}
        self.assertIn("یەکشەممە، دووشەممە", ex40)
        self.assertIn("یەک دووشەممەی تر", ex40)
        self.assertIn("دارهەنار، دارمۆز، دارگوێز، دارمێو، گەاڵمێو", ex40)
        self.assertIn("بە پێی خۆی چوو بۆ الی دوکتۆر", ex40)
        self.assertIn("بەپێی بڕیارەکە جێبەجێی بکە", ex40)

        lesson41 = self.lesson(41)
        ex41 = {pair[0] for pair in lesson41["examples"]}
        self.assertIn("هەموو + ان = هەمووان", ex41)
        self.assertIn("هێلکەوڕون، مشتومڕ، هاتوچۆ، دەستوبرد", ex41)
        self.assertIn("هاتوچۆ / هاتووچۆ", ex41)
        self.assertIn("پێم وا نییە، پێم وا بوو، وا نەبوو، وا دیارە", ex41)
        self.assertIn("وایە", ex41)

        lesson42 = self.lesson(42)
        ex42 = {pair[0] for pair in lesson42["examples"]}
        self.assertIn("گوڵەگەنم، مانگەشەو", ex42)
        self.assertIn("منداڵە بزێوە جوانە چاوشینەکە", ex42)
        self.assertIn("ناوەندەدەمارەکۆئەندام", ex42)

        lesson43 = self.lesson(43)
        ex43 = {pair[0] for pair in lesson43["examples"]}
        self.assertIn("U+200C", ex43)
        self.assertIn("پ.د.ف، پ.د.ک", ex43)
        self.assertIn("PDF", ex43)
        for n in range(39, 44):
            self.assertIn("هیچ سەرچاوەی دەرەکی", self.lesson(n)["source"]["source_policy"])

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
        self.assertIn("نەورۆز یەکەم مانگی کوردییە.", examples)
        self.assertIn("ی. ن. ک.", examples)
        self.assertIn("د. خ.", examples)
        self.assertNotIn("ی.ن.ک.", examples)
        self.assertIn("تەنیا بەرامبەر بەشی خاڵبەندی", self.lesson(51)["source"]["source_policy"])
        self.assertIn("هیچ سەرچاوەیەکی دەرەکی", self.lesson(51)["source"]["source_policy"])
        self.assertNotIn("نەورۆز جەژنێکی کوردییە.", examples)


    def test_lessons_28_to_35_match_the_book_pages_39_to_43(self):
        lesson28 = self.lesson(28)
        ex28 = {pair[0] for pair in lesson28["examples"]}
        self.assertIn("من و تۆ", ex28)
        self.assertIn("هەوڵ بدە تا بگەیتە ئامانج", ex28)
        self.assertIn("یا بڕۆ یا دانیشە", ex28)

        lesson29 = self.lesson(29)
        ex29 = {pair[0] for pair in lesson29["examples"]}
        self.assertIn("بێتۆیی دەمکوژێت", ex29)
        self.assertIn("بێ تۆ ناچم", ex29)
        self.assertIn("بێ ئازادی ژیان ئەستەمە", ex29)

        lesson30 = self.lesson(30)
        ex30 = {pair[0] for pair in lesson30["examples"]}
        self.assertIn("بەهێواشی، بەهێمنی، بەئەسپایی، بەپەلە", ex30)
        self.assertIn("ئەمشەو دەچم بۆ میوانی", ex30)
        self.assertIn("ئەو جوانی دەدوێت / ئەو بەجوانی دەدوێت", ex30)

        lesson31 = self.lesson(31)
        ex31 = {pair[0] for pair in lesson31["examples"]}
        self.assertIn("جوان، جوانتر، جوانترین", ex31)
        self.assertIn("ڕۆژێکی تر (ڕۆژێکی دیکە)", ex31)
        self.assertIn("کەسێکی تر (کەسێکی دیکە)", ex31)

        lesson32 = self.lesson(32)
        ex32 = {pair[0] for pair in lesson32["examples"]}
        self.assertIn("بشتەوێ ناتدەمێ", ex32)
        self.assertIn("نەشخۆی، نەشهات، نەشمانگرت، بشمانبەن", ex32)

        lesson33 = self.lesson(33)
        ex33 = {pair[0] for pair in lesson33["examples"]}
        self.assertIn("گوڵئاو → گواڵو", ex33)
        self.assertIn("ئینشائەڵاڵ → ئینشاڵاڵ", ex33)
        self.assertIn("موحەممەد، نەججاڕ، بەننا", ex33)

        lesson34 = self.lesson(34)
        ex34 = {pair[0] for pair in lesson34["examples"]}
        self.assertIn("گەر دەپرسی من لەبەر چی کەم دەخۆم", ex34)
        self.assertIn("چم، خوەم، قسە کەم", ex34)

        lesson35 = self.lesson(35)
        ex35 = {pair[0] for pair in lesson35["examples"]}
        self.assertIn("ڕەشماڵ، سەهۆڵفرۆش", ex35)
        self.assertIn("لێرەدا، لە کوردستاندا", ex35)
        self.assertIn("U+200C", ex35)
        for n in range(28, 36):
            self.assertIn("هیچ سەرچاوەی دەرەکی", self.lesson(n)["source"]["source_policy"])

    def test_lesson_52_colon_example_preserves_the_book_list(self):
        lesson = self.lesson(52)
        examples = " ".join(pair[0] for pair in lesson["examples"])
        self.assertIn(
            "میرنشینە کوردییەکان بریتی بوون لە: ئەردەڵان، سۆران، بادینان، بابان، هەکاری و بۆتان.",
            examples,
        )
        self.assertTrue(sum("نموونەی فێرکاریی زیادکراو" in pair[1] for pair in self.lesson(52)["examples"]) >= 3)

    def test_lesson_54_preserves_the_books_two_trip_examples(self):
        lesson = self.lesson(54)
        examples = {pair[0] for pair in lesson["examples"]}
        self.assertIn("لە گەشتەکەمدا سەردانی ئەم شارانەم کرد: پاریس، فەرەنسا؛ ڕۆما، ئیتاڵیا؛ بەرلین، ئەڵمانیا.", examples)
        self.assertIn("لە گەشتەکەمدا سەردانی ئەم شوێنانەم کرد: هەولێر، پایتەختی هەرێم؛ سلێمانی، شاری ڕۆشنبیری؛ دهۆک، دەروازەی کوردستان.", examples)
        self.assertTrue(any("نموونەی فێرکاریی زیادکراو" in pair[1] for pair in lesson["examples"]))

    def test_lesson_53_preserves_book_comma_rules_and_examples(self):
        lesson = self.lesson(53)
        examples = {pair[0] for pair in lesson["examples"]}
        self.assertIn("مەستوورەی کوردستانی، هونەر و مێژوونووس، لە ڕۆژهەڵاتی کوردستاندا دەژیا.", examples)
        self.assertIn("کچینە، هەوڵ بدەن، بە هەوڵدان دەگەنە ئامانج.", examples)
        self.assertIn("خوێ، ڕۆن، پیاز و برنج", examples)
        self.assertIn("بەڵێ، نامەکەم نارد.", examples)
        self.assertIn("نە، لەو کاتەدا ناتوانم بەشدار بم.", examples)
        self.assertTrue(any("پەڕەی ٦٧" in pair[1] or "پەڕەی ٦٨" in pair[1] for pair in lesson["examples"]))

    def test_lesson_54_semicolons_separate_labeled_complex_groups(self):
        lesson = self.lesson(54)
        examples = " ".join(pair[0] for pair in lesson["examples"])
        self.assertIn("گرووپی یەکەم: هەولێر، سلێمانی؛ گرووپی دووەم: دهۆک، کەرکووک.", examples)
        self.assertIn("گرووپی یەکەم: زمان، ئەدەب؛ گرووپی دووەم: مێژوو، کولتوور.", examples)
        self.assertIn("ئێمە هەموو بەرپرسیارین بۆ پاراستنی ژینگە؛ هەر یەک لە ئێمە دەتوانێت ڕۆڵی خۆی هەبێت.", examples)

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

    def test_lesson_58_avoids_disputed_historical_date_example(self):
        lesson = self.lesson(58)
        examples = " ".join(pair[0] for pair in lesson["examples"])
        self.assertIn("وەشانی ٤ی کتێب (٢٠٢٤/٠٨/٢٥)", examples)
        self.assertNotIn("حەمە پاشا (١٧٨٣–١٨٤٦)", examples)

    def test_lesson_59_distinguishes_dialogue_marker_from_sentence_dash(self):
        lesson = self.lesson(59)
        examples = {pair[0] for pair in lesson["examples"]}
        # The book uses U+0640 at the start of dialogue turns, but ASCII
        # hyphens for parenthetical interruptions and numeric ranges.
        self.assertIn("ـ ئاکۆ، گوێت لە سەربازەکانە؟", examples)
        self.assertIn(
            "پیرەمێرد - حاجی تۆفیق - لە وەرگێڕانی هۆنراوەدا دەستێکی بااڵی هەبوو.",
            examples,
        )
        self.assertIn(
            "کوردستان - نیشتمانی ئێمە - جوانترین شوێنە.",
            examples,
        )
        self.assertIn("٧٨", lesson["source"]["pages"])


if __name__ == "__main__":
    unittest.main()
