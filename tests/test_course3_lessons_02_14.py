"""Regression tests for source-aligned Course 3 lessons 2–14."""
import json
import unittest
from pathlib import Path

COURSE_PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3Lessons02To14Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with COURSE_PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_lessons_2_to_14_have_three_quiz_questions_and_practice(self):
        for number in range(2, 15):
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)
                for question in lesson["quiz"]:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    self.assertTrue(question["explanation"])

    def test_lesson_2_preserves_the_book_examples_where_hamza_is_retained(self):
        lesson = self.lessons[1]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("لێوئاڵ", content)
        self.assertIn("قورئان", content)
        self.assertIn("نەء", content)
        self.assertIn("إقرأ", content)
        self.assertIn("گواڵو", content)
        self.assertIn("گۆشتاو، گواڵو، ماستاو، ڕۆژاوا، مااڵوایی", content)
        self.assertIn("گۆشتئاو، گوڵئاو، ماستئاو، ڕۆژئاوا، ماڵئاوایی", content)

    def test_lessons_3_and_4_preserve_unicode_letter_contrasts(self):
        lesson3 = self.lessons[2]
        lesson4 = self.lessons[3]
        text3 = " ".join(lesson3["key_points"] + [v for pair in lesson3["examples"] for v in pair])
        text4 = " ".join(lesson4["key_points"] + [v for pair in lesson4["examples"] for v in pair])
        self.assertIn("ڕاز / راز", text3)
        self.assertIn("چاک، چاك", text4)
        self.assertIn("یونیکۆد", text3)

    def test_lesson_6_covers_long_i_and_consonantal_y_source_examples(self):
        lesson = self.lessons[5]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("ئینجا", "فڕین", "مەستی", "هێشوویی", "سییی", "یۆنجە", "کۆیە", "سێیەک"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lesson_7_preserves_all_yiii_source_patterns(self):
        lesson = self.lessons[6]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("خۆجێیییەکان", "سەوزاییی دارستان", "پەککەوتەییم", "پەککەوتەییت", "پەککەوتەییی", "ییی"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lesson_8_covers_all_nisbat_patterns_from_the_book(self):
        lesson = self.lessons[7]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("چەمچەماڵی", "میراوایی", "ئەمریکا + یی = ئەمریکایی", "ئەفریقا + یی = ئەفریقایی", "فەرەنسا + یی = فەرەنسایی"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lesson_9_preserves_the_books_keyboard_mapping(self):
        lesson = self.lessons[8]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("M + Shift + H → هـ", content)
        self.assertIn("E → ە", content)
        self.assertIn("Shift + M", content)
        self.assertIn("پەڕەی ١٥", content)

    def test_lessons_18_and_19_preserve_pe_te_le_syntax(self):
        content = " ".join(
            self.lessons[17]["key_points"] + [v for pair in self.lessons[17]["examples"] for v in pair]
            + self.lessons[18]["key_points"] + [v for pair in self.lessons[18]["examples"] for v in pair]
        )
        for marker in ("دەستپێکردن", "کارتێکردن", "دەستیان تێ نەخستبوو", "دەستلێهەڵگرتن", "خۆ تێ هەڵقورتاندن", "دەستم پێ ڕادەگات"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lessons_16_and_17_preserve_compound_verb_patterns(self):
        content = " ".join(
            self.lessons[15]["key_points"] + [v for pair in self.lessons[15]["examples"] for v in pair]
            + self.lessons[16]["key_points"] + [v for pair in self.lessons[16]["examples"] for v in pair]
        )
        for marker in ("نەماندەنووسی", "فێر مەکەن", "فێرتان نەکردبوو", "چاوداگرتن", "پارەوەرگرتن", "ئااڵ هەڵناکەین", "دەستیان هەڵنەگرتبوو"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lesson_20_preserves_independent_particles_and_compound_infinitives(self):
        lesson = self.lessons[19]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("پارە وەردەگرێت", "پشتلێهەڵکردن", "تەماتەسوورکردنەوە", "نامەکەم پێ دا", "پارەم پێنەما", "نامەکەی تێ خست", "دەستی لێ دا", "دەستی لێدا"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lesson_15_distinguishes_simple_and_complex_preverbs(self):
        lesson = self.lessons[14]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("هەڵدەکەیت", "ڕایان نەهێناوە", "هەڵمگرت", "پێکهێنان", "تێکدان", "پێداهێنان", "پێک دەهێنم", "پێکم هێنا"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lessons_13_and_14_cover_final_table_rows_and_number_examples(self):
        lesson13 = self.lessons[12]
        lesson14 = self.lessons[13]
        text13 = " ".join(lesson13["key_points"] + [v for pair in lesson13["examples"] for v in pair])
        text14 = " ".join(lesson14["key_points"] + [v for pair in lesson14["examples"] for v in pair])
        self.assertIn("بڕوبیانوو", text13)
        self.assertIn("جرتوفرت", text13)
        self.assertIn("حەڤدە، هەژدە، نۆزدە", text14)
        self.assertIn("نۆسەد", text14)
        self.assertIn("١٬٨٥٢٬٣٤٤", text14)

    def test_lesson_13_preserves_scientific_compounds_and_source_table(self):
        lesson = self.lessons[12]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("ناوەندەدەمار، هەستەدەمار", "دڕکەپەرچەکردار", "شاهەنگ", "مانگەشەو", "هێلکەوڕۆن", "لرفەلرف", "تەلەفۆنکردن", "کوڵوکۆ", "یەکشاخ، چوارچرا، هەزارپێ"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lessons_12_and_13_preserve_pages_18_and_19_compounds(self):
        content = " ".join(
            self.lessons[11]["key_points"] + [v for pair in self.lessons[11]["examples"] for v in pair]
            + self.lessons[12]["key_points"] + [v for pair in self.lessons[12]["examples"] for v in pair]
        )
        for marker in ("ئەم جارە؛ نەک ئەمجارە", "ئەم ڕۆژی ساڵی تازەیە", "ڕەشماڵ؛ نەک ڕەش ماڵ", "گوڵەگەنم", "هێشوو هێشوو", "تێکسمڕاو", "شانەی دەماری = دەمارەشانە"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lessons_10_to_12_preserve_pages_16_and_17_examples(self):
        content = " ".join(
            self.lessons[9]["key_points"] + [v for pair in self.lessons[9]["examples"] for v in pair]
            + self.lessons[10]["key_points"] + [v for pair in self.lessons[10]["examples"] for v in pair]
            + self.lessons[11]["key_points"] + [v for pair in self.lessons[11]["examples"] for v in pair]
        )
        for marker in ("جوێن", "بیستوین", "بیستۊن", "دەێ (deê)", "خوەی (xwey)", "دەسەسڕ", "دەنووسێت", "ئەمجار سەختترەن", "ئیمشەو هەم دیسان"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_lesson_13_distinguishes_adverbial_and_adjectival_reduplication(self):
        lesson = self.lessons[12]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("سوور سوور", content)
        self.assertIn("بااڵبەرز", content)
        self.assertIn("دەمارەشانە", content)

    def test_lesson_14_covers_all_number_categories_and_source_examples(self):
        lesson = self.lessons[13]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in (
            "بیست و یەک", "یەکسەد", "دووشەممە", "سێیەم",
            "پێنج میلیۆن و سێ سەد و چل و شەش هەزار و چوار سەد و بیست و نۆ",
            "یەک بە یەک", "٠٫٧", "ڕۆژهەڵات", "باشوور", "۴ ۵ ۶", "سێهەم",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)
        self.assertIn("٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩", content)
        self.assertIn("٠ ١ ٢ ٣ ۴ ۵ ۶ ٧ ٨ ٩", content)


if __name__ == "__main__":
    unittest.main()
