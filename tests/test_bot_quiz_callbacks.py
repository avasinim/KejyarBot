import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock

import bot


class QuizCallbackValidationTests(unittest.IsolatedAsyncioTestCase):
    def make_context(self, callback_data, message_id=77):
        query = SimpleNamespace(
            data=callback_data,
            message=SimpleNamespace(message_id=message_id),
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
                "lesson": "وانە_1",
                "questions": [{
                    "question": "پرسیار",
                    "options": ["وەڵامی ١", "وەڵامی ٢"],
                    "answer": "وەڵامی ١",
                }],
                "score": 0,
                "question_message_id": 77,
            }
        })
        return update, context, query

    async def test_malformed_answer_does_not_strand_active_question(self):
        update, context, query = self.make_context("answer_nope")

        await bot.quiz_answer(update, context)

        self.assertEqual(context.user_data["quiz"]["index"], 0)
        self.assertEqual(context.user_data["quiz"]["question_message_id"], 77)
        self.assertEqual(context.user_data["quiz"]["score"], 0)
        query.answer.assert_awaited_once()
        query.edit_message_reply_markup.assert_not_awaited()

    async def test_out_of_range_answer_does_not_strand_active_question(self):
        update, context, query = self.make_context("answer_9")

        await bot.quiz_answer(update, context)

        self.assertEqual(context.user_data["quiz"]["index"], 0)
        self.assertEqual(context.user_data["quiz"]["question_message_id"], 77)
        self.assertEqual(context.user_data["quiz"]["score"], 0)
        query.answer.assert_awaited_once()
        query.edit_message_reply_markup.assert_not_awaited()

    async def test_stale_question_callback_is_ignored(self):
        update, context, query = self.make_context("answer_0", message_id=76)

        await bot.quiz_answer(update, context)

        self.assertEqual(context.user_data["quiz"]["index"], 0)
        self.assertEqual(context.user_data["quiz"]["question_message_id"], 77)
        self.assertEqual(context.user_data["quiz"]["score"], 0)
        query.answer.assert_awaited_once()
        query.edit_message_reply_markup.assert_not_awaited()


    async def test_valid_final_answer_completes_quiz_and_claims_reward_once(self):
        from unittest.mock import patch

        update, context, query = self.make_context("answer_0")
        query.message.reply_text = AsyncMock()
        with patch.object(bot, "complete_quiz_with_rewards", return_value=True) as reward:
            await bot.quiz_answer(update, context)

            self.assertNotIn("quiz", context.user_data)
            query.answer.assert_awaited_once()
            query.edit_message_reply_markup.assert_awaited_once_with(reply_markup=None)
            reward.assert_called_once_with(12345, "وانە_1")
            self.assertEqual(query.message.reply_text.await_count, 2)

            # A repeat click after completion cannot claim the reward again.
            await bot.quiz_answer(update, context)
            reward.assert_called_once_with(12345, "وانە_1")

    async def test_correct_answer_on_nonfinal_question_advances_once(self):
        update, context, query = self.make_context("answer_0")
        context.user_data["quiz"]["questions"].append({
            "question": "پرسیاری دووەم",
            "options": ["وەڵامی A", "وەڵامی B"],
            "answer": "وەڵامی A",
        })
        query.message.reply_text = AsyncMock(
            return_value=SimpleNamespace(message_id=78)
        )

        await bot.quiz_answer(update, context)

        self.assertEqual(context.user_data["quiz"]["index"], 1)
        self.assertEqual(context.user_data["quiz"]["score"], 1)
        self.assertEqual(context.user_data["quiz"]["question_message_id"], 78)
        query.edit_message_reply_markup.assert_awaited_once_with(reply_markup=None)
        self.assertEqual(query.message.reply_text.await_count, 2)


if __name__ == "__main__":
    unittest.main()
