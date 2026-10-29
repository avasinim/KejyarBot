import unittest

import bot

from course_quiz_review import (
    COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED,
    quiz_is_available,
)


class CourseOneQuizReviewTests(unittest.TestCase):
    def test_all_flagged_lessons_are_unavailable(self):
        for lesson_key in COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED:
            with self.subTest(lesson_key=lesson_key):
                self.assertFalse(quiz_is_available(lesson_key))

    def test_lesson_20_is_flagged_for_source_review(self):
        self.assertIn("وانە_20", COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
        self.assertFalse(quiz_is_available("وانە_20"))

    def test_duplicate_title_lesson_12_is_flagged_for_review(self):
        self.assertIn("وانە_12", COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
        self.assertFalse(quiz_is_available("وانە_12"))

    def test_repetitive_quiz_sets_are_flagged_for_review(self):
        for lesson_key in ("وانە_5", "وانە_7"):
            with self.subTest(lesson_key=lesson_key):
                self.assertIn(lesson_key, COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
                self.assertFalse(quiz_is_available(lesson_key))

    def test_repetitive_question_patterns_are_flagged(self):
        for lesson_key in ("وانە_4", "وانە_6", "وانە_9", "وانە_10", "وانە_11", "وانە_17"):
            with self.subTest(lesson_key=lesson_key):
                self.assertIn(lesson_key, COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED)
                self.assertFalse(quiz_is_available(lesson_key))

    def test_review_flags_reference_existing_course_one_quizzes(self):
        course_one_keys = {f"وانە_{number}" for number in range(1, 23)}
        self.assertTrue(COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED <= course_one_keys)
        self.assertTrue(COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED <= set(bot.QUIZ_DATA))
        self.assertTrue(all(bot.QUIZ_DATA[key] for key in COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED))

    def test_unflagged_lesson_remains_available(self):
        self.assertTrue(quiz_is_available("وانە_1"))
        self.assertTrue(quiz_is_available("وانە_22"))

    def test_review_gate_does_not_match_partial_lesson_keys(self):
        self.assertTrue(quiz_is_available("وانە_200"))
        self.assertTrue(quiz_is_available("daily_conversation_20"))


    def test_runtime_rejects_start_callbacks_for_every_flagged_lesson(self):
        from types import SimpleNamespace
        from unittest.mock import AsyncMock, patch
        import asyncio

        async def check_flagged_start(lesson_key):
            number = lesson_key.removeprefix("وانە_")
            query = SimpleNamespace(
                data=f"quiz_{number}_start",
                from_user=SimpleNamespace(id=12345),
                message=SimpleNamespace(reply_text=AsyncMock()),
                answer=AsyncMock(),
            )
            update = SimpleNamespace(
                callback_query=query,
                effective_user=SimpleNamespace(id=12345),
            )
            context = SimpleNamespace(user_data={})

            with (
                patch.object(bot, "course_is_active", return_value=True),
                patch.object(bot, "get_completed_lessons", return_value=[lesson_key]),
            ):
                await bot.start_quiz(update, context)

            query.answer.assert_awaited_once()
            query.message.reply_text.assert_awaited_once()
            self.assertIn("پێداچوونەوە", query.message.reply_text.await_args.args[0])
            self.assertNotIn("quiz", context.user_data)

        for lesson_key in sorted(COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED):
            with self.subTest(lesson=lesson_key):
                asyncio.run(check_flagged_start(lesson_key))

    def test_runtime_rejects_answer_callbacks_for_every_flagged_lesson(self):
        from types import SimpleNamespace
        from unittest.mock import AsyncMock, patch

        async def check_flagged_lesson(lesson_key):
            query = SimpleNamespace(
                data="answer_0",
                message=SimpleNamespace(
                    message_id=77,
                    reply_text=AsyncMock(),
                ),
                answer=AsyncMock(),
                edit_message_reply_markup=AsyncMock(),
            )
            update = SimpleNamespace(
                callback_query=query,
                effective_user=SimpleNamespace(id=12345),
            )
            context = SimpleNamespace(user_data={
                "quiz": {
                    "index": 0,
                    "lesson": lesson_key,
                    "questions": [{
                        "question": "پرسیار",
                        "options": ["وەڵامی ١", "وەڵامی ٢"],
                        "answer": "وەڵامی ١",
                    }],
                    "score": 0,
                    "question_message_id": 77,
                }
            })

            with (
                patch.object(bot, "get_completed_lessons", return_value=[lesson_key]),
                patch.object(bot, "course_is_active", return_value=True),
            ):
                await bot.quiz_answer(update, context)

            self.assertNotIn("quiz", context.user_data)
            query.answer.assert_awaited_once()
            query.edit_message_reply_markup.assert_not_awaited()
            query.message.reply_text.assert_awaited_once()
            self.assertIn("پێداچوونەوە", query.message.reply_text.await_args.args[0])

        import asyncio

        for lesson_key in sorted(COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED):
            with self.subTest(lesson=lesson_key):
                asyncio.run(check_flagged_lesson(lesson_key))


if __name__ == "__main__":
    unittest.main()
