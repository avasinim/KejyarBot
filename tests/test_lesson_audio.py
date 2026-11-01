import tempfile
import unittest
from pathlib import Path

from lesson_audio import LessonAudioError, resolve_lesson_audio_path


class LessonAudioTests(unittest.TestCase):
    def test_resolves_existing_dedicated_ogg(self):
        with tempfile.TemporaryDirectory() as directory:
            audio = Path(directory) / "lesson-01.ogg"
            audio.write_bytes(b"OGG")
            self.assertEqual(
                resolve_lesson_audio_path(directory, {"lesson_audio_asset": "lesson-01.ogg"}),
                audio.resolve(),
            )

    def test_each_lesson_must_declare_its_own_audio(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(LessonAudioError):
                resolve_lesson_audio_path(directory, {"title": "Lesson 1"})

    def test_rejects_path_traversal(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(LessonAudioError):
                resolve_lesson_audio_path(directory, {"lesson_audio_asset": "../outside.ogg"})

    def test_rejects_missing_or_unsupported_audio(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(LessonAudioError):
                resolve_lesson_audio_path(directory, {"lesson_audio_asset": "missing.ogg"})
            bad = Path(directory) / "audio.wav"
            bad.write_bytes(b"WAV")
            with self.assertRaises(LessonAudioError):
                resolve_lesson_audio_path(directory, {"lesson_audio_asset": "audio.wav"})


if __name__ == "__main__":
    unittest.main()
