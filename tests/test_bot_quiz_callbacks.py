import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot
from course_quiz_review import COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED


class QuizCallbackValidationTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # Quiz callbacks revalidate persisted lesson completion. Keep these unit
        # tests independent of a real SQLite file and isolate each test user.
        patcher = patch.object(
            bot, "get_completed_lessons", return_value=["وانە_1", "وانە_2"]
        )
        patcher.start()
        self.addCleanup(patcher.stop)

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

    async def test_stale_quiz_for_source_review_lesson_is_stopped(self):
        update, context, query = self.make_context("answer_0")
        context.user_data["quiz"]["lesson"] = "وانە_2"
        query.message.reply_text = AsyncMock()

        await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.answer.assert_awaited_once()
        query.edit_message_reply_markup.assert_not_awaited()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("لە پێداچوونەوەدایە", query.message.reply_text.await_args.args[0])

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

    async def test_namespaced_course_quiz_completion_rewards_keep_course_identity(self):
        lesson = "daily_conversation_01"
        update, context, query = self.make_context("answer_0")
        context.user_data["quiz"]["lesson"] = lesson
        context.user_data["quiz"]["questions"] = [{
            "question": "پرسیاری وتووێژ",
            "options": ["وەڵامی دروست", "وەڵامی هەڵە"],
            "answer": "وەڵامی دروست",
        }]
        query.message.reply_text = AsyncMock()

        with (
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "quiz_is_available", return_value=True),
            patch.object(bot, "complete_quiz_with_rewards", return_value=True) as reward,
        ):
            await bot.quiz_answer(update, context)

        reward.assert_called_once_with(12345, lesson)
        self.assertNotIn("quiz", context.user_data)
        result_text = query.message.reply_text.await_args_list[-1].args[0]
        self.assertIn("+20 XP", result_text)

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


    async def test_source_review_quiz_cannot_start_even_via_direct_callback(self):
        query = SimpleNamespace(
            data="quiz_2_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        await bot.start_quiz(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێداچوونەوەی سەرچاوەدایە", query.message.reply_text.await_args.args[0])

    async def test_all_source_review_quizzes_reject_direct_start_callbacks(self):
        # Derive callback coverage from the actual gate, so adding a newly
        # flagged lesson cannot silently leave its direct callback untested.
        gated_lessons = sorted(
            int(lesson_key.removeprefix("وانە_"))
            for lesson_key in COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED
        )
        for number in gated_lessons:
            with self.subTest(lesson=number):
                query = SimpleNamespace(
                    data=f"quiz_{number}_start",
                    from_user=SimpleNamespace(id=12345),
                    answer=AsyncMock(),
                    message=SimpleNamespace(reply_text=AsyncMock()),
                )
                update = SimpleNamespace(
                    callback_query=query,
                    effective_user=SimpleNamespace(id=12345),
                )
                context = SimpleNamespace(user_data={})

                await bot.start_quiz(update, context)

                self.assertNotIn("quiz", context.user_data)
                query.answer.assert_awaited_once()
                query.message.reply_text.assert_awaited_once()
                self.assertIn(
                    "پێداچوونەوەی سەرچاوەدایە",
                    query.message.reply_text.await_args.args[0],
                )

    async def test_namespaced_course_quiz_callback_preserves_full_lesson_key(self):
        lesson = "daily_conversation_01"
        query = SimpleNamespace(
            data=f"quiz_{lesson}_start",
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

        with (
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            await bot.start_quiz(update, context)

        self.assertEqual(context.user_data["quiz"]["lesson"], lesson)
        self.assertEqual(context.user_data["quiz"]["questions"], bot.QUIZ_DATA[lesson])
        query.answer.assert_awaited_once()

    async def test_unified_orthography_quiz_callback_preserves_full_lesson_key(self):
        lesson = "unified_orthography_01"
        query = SimpleNamespace(
            data=f"quiz_{lesson}_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(
                reply_text=AsyncMock(return_value=SimpleNamespace(message_id=89))
            ),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            await bot.start_quiz(update, context)

        self.assertEqual(context.user_data["quiz"]["lesson"], lesson)
        self.assertEqual(context.user_data["quiz"]["questions"], bot.QUIZ_DATA[lesson])
        query.answer.assert_awaited_once()

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

    async def test_locked_lesson_completion_callback_cannot_grant_rewards(self):
        lesson = "daily_conversation_02"
        query = SimpleNamespace(
            data=f"finish_{lesson}",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=False),
            patch.object(bot, "complete_lesson_with_rewards") as complete,
            patch.object(bot, "get_user_level") as level,
            patch.object(bot, "check_badges") as badges,
            patch.object(bot, "send_conversation_voice", new_callable=AsyncMock) as voice,
        ):
            await bot.finish_lesson(update, context)

        complete.assert_not_called()
        level.assert_not_called()
        badges.assert_not_called()
        voice.assert_not_awaited()
        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێشووتر", query.message.reply_text.await_args.args[0])

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


    async def test_namespaced_course_lesson_completion_offers_same_course_next_lesson(self):
        lesson = "daily_conversation_01"
        query = SimpleNamespace(
            data=f"finish_{lesson}",
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

        complete.assert_called_once_with(12345, lesson)
        reply = query.message.reply_text.await_args
        button = reply.kwargs["reply_markup"].inline_keyboard[0][0]
        self.assertEqual(button.callback_data, "next_lesson_daily_conversation_02")
        self.assertIn("دەستپێکردنی", button.text)

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


    async def test_final_lesson_completion_uses_namespaced_quiz_callback_for_each_new_course(self):
        for course_id in ("daily_conversation", "unified_orthography"):
            final_lesson = bot.COURSE_LESSON_ORDER[course_id][-1]
            with self.subTest(course=course_id):
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
                    patch.object(bot, "get_user_level", side_effect=["A1.1 🌱", "A1.1 🌱"]),
                    patch.object(bot, "complete_lesson_with_rewards", return_value=True) as complete,
                    patch.object(bot, "check_badges"),
                    patch.object(bot, "quiz_is_available", return_value=True),
                    patch.object(bot, "send_conversation_voice", new_callable=AsyncMock),
                ):
                    await bot.finish_lesson(update, context)

                complete.assert_called_once_with(12345, final_lesson)
                query.answer.assert_awaited_once()
                reply = query.message.reply_text.await_args
                self.assertEqual(
                    reply.kwargs["reply_markup"].inline_keyboard[0][0].callback_data,
                    f"quiz_{final_lesson}_start",
                )
                self.assertIn("تاقیکردنەوە", reply.args[0])

    async def test_explanation_uses_real_line_breaks(self):
        update, context, query = self.make_context("answer_0")
        context.user_data["quiz"]["questions"][0]["explanation"] = "ئەمە ڕوونکردنەوەیە."
        query.message.reply_text = AsyncMock()
        with patch.object(bot, "complete_quiz_with_rewards", return_value=True):
            await bot.quiz_answer(update, context)

        feedback = query.message.reply_text.await_args_list[0].args[0]
        self.assertIn("\n\n📘 ڕوونکردنەوە:", feedback)
        self.assertNotIn("\\n", feedback)


if __name__ == "__main__":
    unittest.main()
