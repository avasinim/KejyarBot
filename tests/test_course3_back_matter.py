"""Regression checks for the final Course 3 book back matter."""
import json
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "course_data" / "unified_orthography_lessons_01_66.json"


class Course3BackMatterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with PATH.open(encoding="utf-8") as source:
            cls.lessons = json.load(source)["lessons"]

    def test_back_matter_titles_match_the_adapted_book_sequence(self):
        self.assertEqual(
            [lesson["title"] for lesson in self.lessons[62:]],
            ["پاشەکی و ڕوونکردنەوە", "ژێدەر", "دەرەنجام", "سوپاسنامە و تەواو"],
        )

    def test_back_matter_lessons_have_practice_and_keep_draft_status(self):
        for lesson in self.lessons[62:]:
            with self.subTest(lesson=lesson["number"]):
                self.assertEqual(lesson["review_status"], "draft_editorial_review")
                self.assertGreaterEqual(len(lesson["quiz"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 3)
                self.assertGreaterEqual(len(lesson["comprehension"]), 3)
                self.assertTrue(lesson["source"]["pages"])

    def test_appendix_tracks_publication_history_and_dates(self):
        appendix = self.lessons[62]
        content = " ".join(
            appendix["key_points"]
            + [v for pair in appendix["examples"] for v in pair]
        )
        for marker in ("٢٠٠٣/٠٩/٠٦", "٢٠٢١/٠٩/٢٥", "٢٠٢٤/٠٢/٢١", "٢٠٢٤/٠٨/٢٥", "٢٠٢٤/٠٨/٣٠"):
            self.assertIn(marker, content)
        self.assertEqual(appendix["source"]["pages"], "٦٠، ٨٦–٨٨")

    def test_both_distinct_reference_lists_are_present(self):
        references = self.lessons[63]
        content = " ".join(
            references["key_points"]
            + [v for pair in references["examples"] for v in pair]
        )
        self.assertIn("١٧ ژێدەر", content)
        self.assertIn("٥ ژێدەر", content)
        for marker in ("Vuxen svenska", "fritext.se/svmall.html", "Artificial intelligence (AI)", "١٩٨٢", "٢٠٠٥"):
            self.assertIn(marker, content)
        self.assertEqual(references["source"]["pages"], "٦٠، ٨٥")
        self.assertGreaterEqual(len(references["quiz"]), 5)

    def test_conclusion_and_acknowledgements_match_source_pages(self):
        conclusion = self.lessons[64]
        acknowledgements = self.lessons[65]
        conclusion_text = " ".join(conclusion["key_points"])
        acknowledgement_text = " ".join(acknowledgements["key_points"])
        self.assertIn("مەبەست", conclusion_text)
        self.assertIn("ڕێنووسی یەکگرتوو", conclusion_text)
        self.assertIn("حەمەسەعید حەسەن", acknowledgement_text)
        self.assertIn("سوپاسنامە", acknowledgements["title"])
        self.assertEqual(conclusion["source"]["pages"], "٨٤")
        self.assertEqual(acknowledgements["source"]["pages"], "٨٤، ٨٩")


if __name__ == "__main__":
    unittest.main()
