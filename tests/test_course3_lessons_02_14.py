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
        self.assertIn("گواڵو", content)

    def test_lessons_5_to_10_restore_source_examples_from_pages_9_to_16(self):
        expected = {
            5: ("ڕاو", "شەوبۆ", "ئومێد", "ئووبا", "کەرکووک", "توو"),
            6: ("ئینجا", "ماسیگر", "قەیسەری", "سییی", "نووسییان"),
            7: ("سەوزاییی دارستان", "پەککەوتەییم", "خۆجێیییەکان"),
            8: ("چەمچەماڵی", "میراوایی"),
            10: ("نوێن", "دوێت", "بیستۊن", "خوەێان → خوەیان"),
        }
        for number, markers in expected.items():
            with self.subTest(lesson=number):
                lesson = self.lessons[number - 1]
                content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
                for marker in markers:
                    self.assertIn(marker, content)

    def test_lesson_13_distinguishes_adverbial_and_adjectival_reduplication(self):
        lesson = self.lessons[12]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        self.assertIn("سوور سوور", content)
        self.assertIn("بااڵبەرز", content)
        self.assertIn("دەمارەشانە", content)
        for marker in ("مارماسی", "مانگەشەو", "دەربەدەر", "هێلکەوڕۆن", "مێرگەسوور", "لرفەلرف", "ماڵەوماڵ", "وێنەگرتن", "گوڵوموڵ", "هەزارپێ"):
            self.assertIn(marker, content)

    def test_lesson_14_covers_ordinal_and_compound_number_rules(self):
        lesson = self.lessons[13]
        content = " ".join(lesson["key_points"] + [v for pair in lesson["examples"] for v in pair])
        for marker in ("بیست و یەک", "یەکسەد", "دووشەممە", "سێیەم"):
            self.assertIn(marker, content)


if __name__ == "__main__":
    unittest.main()
