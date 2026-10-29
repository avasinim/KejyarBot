import unittest

from tools.prepare_botkeep_zip import (
    MAX_FILES,
    MAX_UNCOMPRESSED_BYTES,
    ROOT,
    include,
)


class BotkeepPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(
            (path for path in ROOT.rglob("*") if include(path)),
            key=lambda path: path.relative_to(ROOT).as_posix(),
        )
        cls.relative = {
            path.relative_to(ROOT).as_posix()
            for path in cls.files
        }

    def test_all_runtime_entrypoints_and_course_data_are_included(self):
        required = {
            "bot.py",
            "main.py",
            "database.py",
            "voice.py",
            "daily_chat.py",
            "speech.py",
            "course_runtime.py",
            "course_lesson_adapters.py",
            "course_quiz_review.py",
            "courses.json",
            "requirements.txt",
            "course_data/orthography_foundations.json",
            "course_data/orthography_original_lessons.json",
            "course_data/orthography_foundations_quiz_draft.json",
            "course_data/daily_conversation_lessons_01_06.json",
            "course_data/daily_conversation_lessons_07_12.json",
            "course_data/unified_orthography_lessons_01_12.json",
        }
        self.assertTrue(required.issubset(self.relative), sorted(required - self.relative))

    def test_lesson_1_jpg_is_tracked_but_excluded_from_zip(self):
        image_path = ROOT / "photo_2026-10-27_00-13-52.jpg"
        self.assertTrue(image_path.is_file(), "Lesson 1 source infographic must exist in the repository")
        self.assertNotIn(image_path.relative_to(ROOT).as_posix(), self.relative)

    def test_text_svg_infographics_are_included(self):
        self.assertIn("assets/infographics/lesson-01-greetings.svg", self.relative)
        self.assertIn("assets/infographics/lesson-02-letters-sample.svg", self.relative)

    def test_secrets_databases_backups_and_binary_voice_are_excluded(self):
        for path in self.relative:
            self.assertNotIn(".env", path.split("/"))
            self.assertNotIn("voices", path.split("/"))
            self.assertNotIn("tests", path.split("/"))
            self.assertNotIn("docs", path.split("/"))
            self.assertNotIn("tools", path.split("/"))
            self.assertFalse(path.endswith((".mp3", ".wav", ".ogg", ".jpg", ".jpeg", ".png", ".webp", ".db", ".sqlite", ".sqlite3", ".pyc")))
        self.assertNotIn("bot_backup.py", self.relative)
        self.assertNotIn("bot_before_lesson_voice.py", self.relative)

    def test_package_stays_within_botkeep_limits(self):
        uncompressed_bytes = sum(path.stat().st_size for path in self.files)
        self.assertLessEqual(len(self.files), MAX_FILES)
        self.assertLess(uncompressed_bytes, MAX_UNCOMPRESSED_BYTES)


if __name__ == "__main__":
    unittest.main()
