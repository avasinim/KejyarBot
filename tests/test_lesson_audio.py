"""Regression guard: course readers do not resolve or send lesson audio."""
import unittest

import arami_course1_telegram


class TextOnlyLessonReaderTests(unittest.TestCase):
    def test_course1_reader_exposes_no_audio_delivery_api(self):
        self.assertFalse(hasattr(arami_course1_telegram, "send_lesson_audio"))
        self.assertFalse(hasattr(arami_course1_telegram, "load_lesson_audio_files"))

    def test_repository_contains_no_prerecorded_audio_files(self):
        from pathlib import Path

        root = Path(__file__).resolve().parents[1]
        audio_extensions = {
            ".mp3", ".wav", ".ogg", ".oga", ".m4a", ".aac",
            ".flac", ".opus", ".wma", ".aiff", ".aif", ".amr",
            ".mid", ".midi",
        }
        audio_files = [
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file()
            and ".git" not in path.parts
            and path.suffix.lower() in audio_extensions
        ]
        self.assertEqual(audio_files, [], f"Unexpected audio files: {audio_files}")


if __name__ == "__main__":
    unittest.main()
