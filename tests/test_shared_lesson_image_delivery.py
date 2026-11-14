import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

from lesson_image_delivery import (
    SHARED_LESSON_IMAGE_ROUTES,
    send_shared_lesson_image,
    shared_lesson_image_path,
)


class SharedLessonImageDeliveryTests(unittest.IsolatedAsyncioTestCase):
    def test_only_the_two_approved_exact_course_lesson_pairs_are_routed(self):
        self.assertEqual(len(SHARED_LESSON_IMAGE_ROUTES), 2)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            image = root / "assets" / "lessons" / "kejyar_lesson5_kurdish_letters_v2.png"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"test-image")

            self.assertEqual(
                shared_lesson_image_path(
                    root,
                    "arami_orthography_foundations",
                    "arami_course1_lesson_05",
                ),
                image,
            )
            self.assertEqual(
                shared_lesson_image_path(
                    root,
                    "kurmanji_latin_orthography",
                    "kurmanji_latin_orthography_01",
                ),
                image,
            )
            self.assertIsNone(shared_lesson_image_path(
                root, "kurmanji_latin_grammar", "kurmanji_latin_orthography_01"
            ))
            self.assertIsNone(shared_lesson_image_path(
                root, "arami_orthography_foundations", "arami_course1_lesson_06"
            ))
            self.assertIsNone(shared_lesson_image_path(
                root, "another_course", "another_course_lesson_05"
            ))

    def test_missing_shared_image_fails_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.assertIsNone(shared_lesson_image_path(
                temporary,
                "arami_orthography_foundations",
                "arami_course1_lesson_05",
            ))

    async def test_sender_sends_only_the_approved_image_and_keeps_errors_nonfatal(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            image = root / "assets" / "lessons" / "kejyar_lesson5_kurdish_letters_v2.png"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"test-image")
            message = SimpleNamespace(reply_photo=AsyncMock())

            sent = await send_shared_lesson_image(
                message,
                "kurmanji_latin_orthography",
                "kurmanji_latin_orthography_01",
                base_dir=root,
            )
            self.assertTrue(sent)
            message.reply_photo.assert_awaited_once()

            message.reply_photo.reset_mock()
            not_sent = await send_shared_lesson_image(
                message,
                "kurmanji_latin_grammar",
                "kurmanji_latin_orthography_01",
                base_dir=root,
            )
            self.assertFalse(not_sent)
            message.reply_photo.assert_not_awaited()

    async def test_telegram_photo_errors_do_not_break_lesson_delivery(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            image = root / "assets" / "lessons" / "kejyar_lesson5_kurdish_letters_v2.png"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"test-image")
            message = SimpleNamespace(
                reply_photo=AsyncMock(side_effect=RuntimeError("Telegram unavailable"))
            )
            self.assertFalse(await send_shared_lesson_image(
                message,
                "arami_orthography_foundations",
                "arami_course1_lesson_05",
                base_dir=root,
            ))


if __name__ == "__main__":
    unittest.main()
