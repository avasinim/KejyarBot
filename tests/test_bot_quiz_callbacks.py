import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

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


    async def test_quiz_cannot_start_before_lesson_is_completed(self):
        from unittest.mock import patch

        query = SimpleNamespace(
            data="quiz_1_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.start_quiz(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("تەواو بکە", query.message.reply_text.await_args.args[0])

    async def test_completed_lesson_can_start_its_quiz(self):
        from unittest.mock import patch

        query = SimpleNamespace(
            data="quiz_1_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(
                reply_text=AsyncMock(return_value=SimpleNamespace(message_id=88))
            ),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        with patch.object(bot, "get_completed_lessons", return_value=["وانە_1"]):
            await bot.start_quiz(update, context)

        self.assertEqual(context.user_data["quiz"]["lesson"], "وانە_1")
        self.assertEqual(context.user_data["quiz"]["index"], 0)
        self.assertEqual(context.user_data["quiz"]["question_message_id"], 88)
        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()


    def test_lesson_lock_requires_previous_lesson_completion(self):
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertTrue(bot.can_open(12345, "وانە_1"))
            self.assertFalse(bot.can_open(12345, "وانە_2"))
            self.assertFalse(bot.can_open(12345, "وانە_22"))
            self.assertFalse(bot.can_open(12345, "not-a-lesson"))

        with patch.object(bot, "get_completed_lessons", return_value=["وانە_1"]):
            self.assertTrue(bot.can_open(12345, "وانە_2"))
            self.assertFalse(bot.can_open(12345, "وانە_3"))

    async def test_first_lesson_completion_offers_only_the_next_lesson(self):
        query = SimpleNamespace(
            data="finish_وانە_1",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "get_user_level", side_effect=["A1.1 🌱", "A1.1 🌱"]),
            patch.object(bot, "complete_lesson_with_rewards", return_value=True) as complete,
            patch.object(bot, "check_badges"),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock),
        ):
            await bot.finish_lesson(update, context)

        query.answer.assert_awaited_once()
        complete.assert_called_once_with(12345, "وانە_1")
        query.message.reply_text.assert_awaited_once()
        reply = query.message.reply_text.await_args
        self.assertIn("وانەکە تەواو بوو", reply.args[0])
        keyboard = reply.kwargs["reply_markup"]
        button = keyboard.inline_keyboard[0][0]
        self.assertEqual(button.callback_data, "next_lesson_وانە_2")

    async def test_repeated_lesson_completion_does_not_offer_next_lesson_again(self):
        query = SimpleNamespace(
            data="finish_وانە_1",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
            patch.object(bot, "complete_lesson_with_rewards", return_value=False) as complete,
            patch.object(bot, "check_badges") as badges,
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock) as voice,
        ):
            await bot.finish_lesson(update, context)

        complete.assert_called_once_with(12345, "وانە_1")
        badges.assert_not_called()
        voice.assert_not_awaited()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێشتر تەواو کراوە", query.message.reply_text.await_args.args[0])


    async def test_final_lesson_completion_offers_final_lesson_quiz(self):
        final_lesson = bot.ORDER[-1]
        query = SimpleNamespace(
            data=f"finish_{final_lesson}",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "get_user_level", side_effect=["A1.1 🌱", "A1.2 🌿"]),
            patch.object(bot, "complete_lesson_with_rewards", return_value=True) as complete,
            patch.object(bot, "check_badges"),
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock),
        ):
            await bot.finish_lesson(update, context)

        complete.assert_called_once_with(12345, final_lesson)
        reply = query.message.reply_text.await_args
        button = reply.kwargs["reply_markup"].inline_keyboard[0][0]
        self.assertEqual(button.callback_data, "quiz_22_start")
        self.assertIn("تاقیکردنەوە", button.text)


    async def test_lesson_22_quiz_start_maps_to_its_real_draft_question(self):
        query = SimpleNamespace(
            data="quiz_22_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(
                reply_text=AsyncMock(return_value=SimpleNamespace(message_id=228))
            ),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        with patch.object(bot, "get_completed_lessons", return_value=["وانە_22"]):
            await bot.start_quiz(update, context)

        quiz = context.user_data["quiz"]
        expected = bot.QUIZ_DATA["وانە_22"][0]
        self.assertEqual(quiz["lesson"], "وانە_22")
        self.assertEqual(quiz["questions"][0]["question"], expected["question"])
        self.assertEqual(quiz["questions"][0]["answer"], expected["answer"])
        self.assertEqual(quiz["question_message_id"], 228)
        sent_markup = query.message.reply_text.await_args.kwargs["reply_markup"]
        self.assertEqual(
            [row[0].callback_data for row in sent_markup.inline_keyboard],
            [f"answer_{i}" for i in range(len(expected["options"]))],
        )
        query.answer.assert_awaited_once()

    async def test_lesson_22_quiz_answer_records_completion_and_clears_state(self):
        question = bot.QUIZ_DATA["وانە_22"][0]
        update, context, query = self.make_context("answer_0", message_id=77)
        context.user_data["quiz"].update({
            "lesson": "وانە_22",
            "questions": [question],
            "score": 0,
        })
        query.message.reply_text = AsyncMock()

        correct_index = question["options"].index(question["answer"])
        query.data = f"answer_{correct_index}"
        with patch.object(bot, "complete_quiz_with_rewards", return_value=True) as reward:
            await bot.quiz_answer(update, context)

        reward.assert_called_once_with(12345, "وانە_22")
        self.assertNotIn("quiz", context.user_data)
        self.assertTrue(any("تاقیکردنەوە تەواو بوو" in call.args[0]
                            for call in query.message.reply_text.await_args_list))
        self.assertTrue(any("1/1" in call.args[0]
                            for call in query.message.reply_text.await_args_list))


if __name__ == "__main__":
    unittest.main()
