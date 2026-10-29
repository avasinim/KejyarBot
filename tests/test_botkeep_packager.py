import contextlib
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import tools.prepare_botkeep_zip as packager
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
            "course_data/daily_conversation_lessons_07_30.json",
            "course_data/daily_conversation_lessons_31_36.json",
            "course_data/daily_conversation_lessons_37_42.json",
            "course_data/daily_conversation_lessons_43_48.json",
            "course_data/daily_conversation_plan.json",
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

    def test_actual_archive_build_excludes_secrets_and_includes_required_files(self):
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
            "course_data/daily_conversation_lessons_07_30.json",
            "course_data/daily_conversation_lessons_31_36.json",
            "course_data/daily_conversation_lessons_37_42.json",
            "course_data/daily_conversation_lessons_43_48.json",
            "course_data/daily_conversation_plan.json",
            "course_data/unified_orthography_lessons_01_12.json",
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            output = Path(temporary) / "actual-package.zip"
            for relative in required:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("test runtime file", encoding="utf-8")
            for relative, contents in {
                ".env": "TELEGRAM_BOT_TOKEN=must-not-ship",
                "kejyar.db": "fake database",
                "voices/kejyar.mp3": "fake audio",
                "tests/test_secret.py": "test",
                "docs/internal.txt": "internal",
                "tools/internal.py": "internal",
                "bot_backup.py": "old backup",
            }.items():
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(contents, encoding="utf-8")

            with patch.object(packager, "ROOT", root), patch.object(packager, "OUTPUT", output):
                with contextlib.redirect_stdout(io.StringIO()):
                    result = packager.main()

            self.assertEqual(result, 0)
            self.assertTrue(output.is_file())
            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())
            self.assertTrue(required.issubset(names), sorted(required - names))
            for forbidden in (".env", "kejyar.db", "voices/kejyar.mp3",
                              "tests/test_secret.py", "docs/internal.txt",
                              "tools/internal.py", "bot_backup.py"):
                self.assertNotIn(forbidden, names)


if __name__ == "__main__":
    unittest.main()
