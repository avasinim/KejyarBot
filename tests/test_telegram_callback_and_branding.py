"""Regression guards for Telegram callback payload limits and Kejyar branding."""
import json
import unittest
from pathlib import Path

import bot

ROOT = Path(__file__).resolve().parents[1]


class TelegramCallbackAndBrandingTests(unittest.TestCase):
    def test_all_course_and_lesson_callback_payloads_fit_telegram_limit(self):
        callbacks = []
        for course in bot.COURSES:
            callbacks.append(f"course_{course['id']}")
            for lesson in course.get("lesson_ids", []):
                callbacks.extend(
                    (
                        f"open_lesson_{lesson}",
                        f"finish_{lesson}",
                        f"next_lesson_{lesson}",
                    )
                )
                quiz_id = lesson.removeprefix("وانە_") if lesson.startswith("وانە_") else lesson
                callbacks.append(f"quiz_{quiz_id}_start")

        # Telegram's callback_data is limited to 1–64 bytes, not 64 characters.
        too_long = [(value, len(value.encode("utf-8"))) for value in callbacks
                    if not 1 <= len(value.encode("utf-8")) <= 64]
        self.assertEqual(too_long, [])

    def test_course_catalog_callback_ids_are_unique(self):
        callbacks = [f"course_{course['id']}" for course in bot.COURSES]
        self.assertEqual(len(callbacks), len(set(callbacks)))

    def test_lesson_header_and_infographic_caption_use_kejyars_correct_name(self):
        source = (ROOT / "bot.py").read_text(encoding="utf-8")
        self.assertIn('caption="🌿 کەژیار | وانەی ١: پیتەکان و دەنگەکان"', source)
        self.assertNotIn("کەویار", source)
        self.assertNotIn("╭━━━━━━━━━━━━━━━━━━╮", source)
        self.assertNotIn('"content": f"📚 {ORTHOGRAPHY_COURSE[', source)


if __name__ == "__main__":
    unittest.main()
