"""Callback-level tests ensure draft lessons cannot be opened or completed."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class DraftCourseCallbackGateTests(unittest.IsolatedAsyncioTestCase):
    def make_update(self, data, user_id=12345):
        message = SimpleNamespace(
            reply_text=AsyncMock(),
            message_id=77,
        )
        query = SimpleNamespace(
            data=data,
            from_user=SimpleNamespace(id=user_id),
            message=message,
            answer=AsyncMock(),
        )
        return SimpleNamespace(callback_query=query), message, query

    async def test_course_button_does_not_list_draft_lessons(self):
        update, message, query = self.make_update("course_daily_conversation")
        await bot.open_course(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()
        reply = message.reply_text.await_args.args[0]
        self.assertIn("چالاک نەکراون", reply)
        self.assertNotIn("open_lesson_daily_conversation_01", str(message.reply_text.await_args.kwargs))

    async def test_forged_open_lesson_callback_cannot_reveal_draft_content(self):
        update, message, query = self.make_update("open_lesson_daily_conversation_01")
        with patch.object(bot, "send_lesson_text", new_callable=AsyncMock) as send_text, \
             patch.object(bot, "send_lesson_infographic", new_callable=AsyncMock) as send_image:
            await bot.open_selected_lesson(update, SimpleNamespace())
        message.reply_text.assert_awaited_once()
        self.assertIn("🔒", message.reply_text.await_args.args[0])
        send_text.assert_not_awaited()
        send_image.assert_not_awaited()

    async def test_forged_finish_callback_cannot_award_draft_rewards(self):
        update, message, query = self.make_update("finish_daily_conversation_01")
        with patch.object(bot, "complete_lesson_with_rewards") as award:
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))
        message.reply_text.assert_awaited_once()
        self.assertIn("🔒", message.reply_text.await_args.args[0])
        award.assert_not_called()


    async def test_stale_draft_quiz_session_is_cancelled_without_quiz_rewards(self):
        update, message, query = self.make_update("answer_0")
        update.effective_user = query.from_user
        context = SimpleNamespace(user_data={
            "quiz": {
                "lesson": "daily_conversation_01",
                "index": 0,
                "questions": [{
                    "question": "Test?",
                    "options": ["A", "B"],
                    "answer": "A",
                    "explanation": "Test explanation",
                }],
                "score": 0,
                "question_message_id": 77,
            }
        })
        with patch.object(bot, "complete_quiz_with_rewards") as award:
            await bot.quiz_answer(update, context)
        self.assertNotIn("quiz", context.user_data)
        message.reply_text.assert_awaited_once()
        self.assertIn("🔒", message.reply_text.await_args.args[0])
        award.assert_not_called()


if __name__ == "__main__":
    unittest.main()
