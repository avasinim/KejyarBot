import json
import unittest
from pathlib import Path

from course_lesson_adapters import adapt_unified_orthography_lessons


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "course_data" / "unified_orthography_lessons_01_66.json"
CANDIDATE_PATH = (
    ROOT
    / "course_data"
    / "appendices"
    / "unified_orthography_lessons_01_68_candidate_2026-11-10.json"
)
MANIFEST_PATH = (
    ROOT
    / "course_data"
    / "appendices"
    / "course3_68_lesson_manifest_candidate_2026-11-10.json"
)
RUNTIME_MANIFEST_PATH = ROOT / "courses.json"
BOT_PATH = ROOT / "bot.py"


class Course3Lessons67And68IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
        cls.candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.runtime_manifest = json.loads(RUNTIME_MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.bot_source = BOT_PATH.read_text(encoding="utf-8")

    def test_original_66_lessons_are_preserved_byte_for_data(self):
        self.assertEqual(self.candidate["lessons"][:66], self.source["lessons"])

    def test_candidate_has_68_contiguous_lessons(self):
        lessons = self.candidate["lessons"]
        self.assertEqual(len(lessons), 68)
        self.assertEqual([item["number"] for item in lessons], list(range(1, 69)))
        self.assertEqual(
            len({item["id"] for item in lessons[66:]}),
            2,
        )

    def test_candidate_manifest_matches_all_68_runtime_keys(self):
        expected_ids = [
            f"unified_orthography_{number:02d}"
            for number in range(1, 69)
        ]
        course = self.manifest["course"]
        self.assertEqual(course["id"], "unified_orthography")
        self.assertEqual(course["lesson_ids"], expected_ids)

    def test_runtime_manifest_and_loader_are_wired_for_68_lessons(self):
        course = next(
            item
            for item in self.runtime_manifest["courses"]
            if item["id"] == "unified_orthography"
        )
        expected_ids = [
            f"unified_orthography_{number:02d}"
            for number in range(1, 69)
        ]
        self.assertEqual(course["status"], "active")
        self.assertEqual(course["lesson_ids"], expected_ids)
        self.assertIn(
            "course_data/appendices/unified_orthography_lessons_01_68_candidate_2026-11-10.json",
            self.bot_source,
        )
        self.assertIn('"unified_orthography": 68', self.bot_source)
        self.assertIn("include_extended_sections=True", self.bot_source)

    def test_adapter_renders_structured_activities_as_readable_text(self):
        lessons, quizzes = adapt_unified_orthography_lessons(
            self.candidate,
            include_extended_sections=True,
        )
        for number in (67, 68):
            key = f"unified_orthography_{number:02d}"
            raw = self.candidate["lessons"][number - 1]
            self.assertIn(key, lessons)
            self.assertEqual(len(quizzes[key]), 12)
            content = lessons[key]["content"]
            self.assertIn("🎯 چالاکییەکان", content)
            for activity in raw["activities"]:
                self.assertIn(activity["title"], content)
                self.assertIn(activity["instruction"], content)
            self.assertNotIn("{'title':", content)

    def test_quiz_answers_are_valid_and_source_metadata_is_present(self):
        _, quizzes = adapt_unified_orthography_lessons(
            self.candidate,
            include_extended_sections=True,
        )
        for number in (67, 68):
            raw = self.candidate["lessons"][number - 1]
            self.assertTrue(raw.get("source", {}).get("book"))
            key = f"unified_orthography_{number:02d}"
            self.assertEqual(len(quizzes[key]), 12)
            for item in quizzes[key]:
                self.assertIn(item["answer"], item["options"])
                self.assertTrue(item["question"].strip())


if __name__ == "__main__":
    unittest.main()
