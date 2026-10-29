import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class CourseOpeningTests(unittest.IsolatedAsyncioTestCase):
    async def test_draft_conversation_course_stays_locked(self):
        query = SimpleNamespace(
            data="course_daily_conversation",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)

        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        args, kwargs = query.message.reply_text.await_args
        message = args[0]
        self.assertIn("بۆ خوێندکاران چالاک نەکراون", message)
        self.assertIsNone(kwargs.get("reply_markup"))

    def test_active_course_catalog_matches_runtime_lesson_data(self):
        for course in bot.COURSES:
            if course.get("status") != "active":
                continue
            for lesson_id in course.get("lesson_ids", []):
                with self.subTest(course=course["id"], lesson=lesson_id):
                    self.assertIn(lesson_id, bot.LESSON_DATA)
                    self.assertEqual(bot.LESSON_COURSE.get(lesson_id), course["id"])
                    self.assertIn(lesson_id, bot.COURSE_LESSON_ORDER.get(course["id"], []))

    def test_course_and_lesson_callback_payloads_fit_telegram_limit(self):
        # Telegram limits callback_data to 1–64 UTF-8 bytes, not characters.
        payloads = []
        for course in bot.COURSES:
            payloads.append(f"course_{course['id']}")
        for lesson in bot.LESSON_COURSE:
            payloads.extend([
                f"open_lesson_{lesson}",
                f"finish_{lesson}",
                f"next_lesson_{lesson}",
            ])
            # Match the exact callback format used by bot.py for every course.
            payloads.append(f"quiz_{lesson}_start")

        oversized = [(payload, len(payload.encode("utf-8"))) for payload in payloads
                     if not 1 <= len(payload.encode("utf-8")) <= 64]
        self.assertEqual(oversized, [])

    def test_draft_courses_cannot_open_lessons_before_review(self):
        self.assertFalse(bot.course_is_active("daily_conversation"))
        self.assertFalse(bot.course_is_active("unified_orthography"))
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertFalse(bot.can_open(12345, "daily_conversation_01"))
            self.assertFalse(bot.can_open(12345, "unified_orthography_01"))

    async def test_active_course_lists_only_its_catalog_lessons(self):
        query = SimpleNamespace(
            data="course_orthography_basic",
            answer=AsyncMock(),
            from_user=SimpleNamespace(id=12345),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)

        from unittest.mock import patch
        with patch.object(bot, "get_completed_lessons", return_value=[]), patch.object(bot, "can_open", return_value=True):
            await bot.open_course(update, SimpleNamespace())

        query.message.reply_text.assert_awaited_once()
        _, kwargs = query.message.reply_text.await_args
        keyboard = kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 22)
        callback_ids = [row[0].callback_data for row in keyboard]
        self.assertEqual(callback_ids, [f"open_lesson_وانە_{n}" for n in range(1, 23)])


    async def test_course_menu_summary_matches_manifest_statuses(self):
        message = SimpleNamespace(
            text="📚 وانەکان",
            reply_text=AsyncMock(),
        )
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        with patch.object(bot, "get_user"):
            await bot.message(update, context)

        message.reply_text.assert_awaited_once()
        text = message.reply_text.await_args.args[0]
        self.assertIn("1 کۆرسی چالاک هەیە", text)
        self.assertIn("پلاندانراو", text)
        self.assertIn("ڕێزمان", text)
        self.assertIn("پێداچوونەوەی ناوەڕۆکیان هێشتا تەواو نییە", text)


    def test_completion_in_one_course_never_unlocks_another_courses_next_lesson(self):
        # Unlock checks must use the target course's ordered lesson list.
        cases = [
            ("daily_conversation_02", ["وانە_1"]),
            ("unified_orthography_02", ["daily_conversation_01"]),
            ("وانە_2", ["unified_orthography_01"]),
        ]
        for target_lesson, completed_lessons in cases:
            with self.subTest(target_lesson=target_lesson, completed=completed_lessons):
                with patch.object(bot, "get_completed_lessons", return_value=completed_lessons):
                    self.assertFalse(bot.can_open(12345, target_lesson))


if __name__ == "__main__":
    unittest.main()
