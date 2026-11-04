"""Regression guard: course readers do not resolve or send lesson audio."""
import unittest

import arami_course1_telegram


class TextOnlyLessonReaderTests(unittest.TestCase):
    def test_course1_reader_exposes_no_audio_delivery_api(self):
        self.assertFalse(hasattr(arami_course1_telegram, "send_lesson_audio"))
        self.assertFalse(hasattr(arami_course1_telegram, "load_lesson_audio_files"))


if __name__ == "__main__":
    unittest.main()
