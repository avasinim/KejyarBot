import asyncio
import asyncio
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class AramiCourse1ProgressionTests(unittest.TestCase):
    def test_all_21_lessons_form_one_ordered_sequence_with_terminal_lesson(self):
        lesson_ids = bot.ARMI_LESSON_IDS
        self.assertEqual(len(lesson_ids), 21)
        for index, lesson_id in enumerate(lesson_ids[:-1]):
            self.assertEqual(bot.next_course_lesson(lesson_id), lesson_ids[index + 1])
        self.assertIsNone(bot.next_course_lesson(lesson_ids[-1]))

    def test_lesson_unlocking_requires_every_previous_lesson(self):
        lesson_ids = bot.ARMI_LESSON_IDS
        with patch.object(bot, "course_is_active", return_value=True), patch.object(
            bot, "get_completed_lessons", return_value=[]
        ):
            self.assertTrue(bot.can_open(12345, lesson_ids[0]))
            self.assertFalse(bot.can_open(12345, lesson_ids[1]))
            self.assertFalse(bot.can_open(12345, lesson_ids[-1]))

        with patch.object(bot, "course_is_active", return_value=True), patch.object(
            bot, "get_completed_lessons", return_value=[lesson_ids[0]]
        ):
            self.assertTrue(bot.can_open(12345, lesson_ids[1]))
            self.assertFalse(bot.can_open(12345, lesson_ids[2]))

    def test_noncontiguous_saved_progress_does_not_skip_course1_lessons(self):
        lesson_ids = bot.ARMI_LESSON_IDS
        # Even if stale/corrupt progress says lesson 3 is complete, lesson 4
        # remains locked while lesson 2 is missing.
        with patch.object(bot, "course_is_active", return_value=True), patch.object(
            bot, "get_completed_lessons", return_value=[lesson_ids[0], lesson_ids[2]]
        ):
            self.assertFalse(bot.can_open(12345, lesson_ids[3]))
            self.assertFalse(bot.can_open(12345, lesson_ids[4]))

    def test_all_courses_reject_noncontiguous_progress(self):
        course_ids = (
            "arami_orthography_foundations",
            "daily_conversation",
            "unified_orthography",
            "kurmanji_latin_orthography",
            "kurmanji_latin_grammar",
        )
        with patch.object(bot, "course_is_active", return_value=True):
            for course_id in course_ids:
                order = bot.COURSE_LESSON_ORDER[course_id]
                with self.subTest(course_id=course_id):
                    # A stale record for lesson 3 must not unlock lesson 4
                    # while lesson 2 remains incomplete.
                    with patch.object(
                        bot, "get_completed_lessons",
                        return_value=[order[0], order[2]],
                    ):
                        self.assertFalse(bot.can_open(12345, order[3]))
                    with patch.object(
                        bot, "get_completed_lessons",
                        return_value=order[:3],
                    ):
                        self.assertTrue(bot.can_open(12345, order[3]))

    def test_inactive_course_cannot_open_any_lesson(self):
        with patch.object(bot, "course_is_active", return_value=False), patch.object(
            bot, "get_completed_lessons", return_value=[]
        ):
            self.assertFalse(bot.can_open(12345, bot.ARMI_LESSON_IDS[0]))


class QuizCallbackValidationTests(unittest.IsolatedAsyncioTestCase):
    def make_context(self, callback_data, message_id=77):
        query = SimpleNamespace(
            data=callback_data,
            message=SimpleNamespace(message_id=message_id),
            from_user=SimpleNamespace(id=12345),
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

    async def test_telegram_acknowledgement_failure_releases_answer_claim(self):
        update, context, query = self.make_context("answer_0")
        query.message.reply_text = AsyncMock()
        query.answer = AsyncMock(side_effect=RuntimeError("Telegram acknowledgement failed"))

        with self.assertRaisesRegex(RuntimeError, "acknowledgement failed"):
            await bot.quiz_answer(update, context)

        quiz = context.user_data["quiz"]
        self.assertFalse(quiz["answer_in_progress"])
        self.assertEqual(quiz["question_message_id"], 77)
        self.assertEqual(quiz["index"], 0)
        self.assertEqual(quiz["score"], 0)
        query.edit_message_reply_markup.assert_not_awaited()
        query.message.reply_text.assert_not_awaited()

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


    async def test_duplicate_callback_during_answer_processing_is_ignored(self):
        update, context, query = self.make_context("answer_0")
        context.user_data["quiz"]["answer_in_progress"] = True

        await bot.quiz_answer(update, context)

        self.assertEqual(context.user_data["quiz"]["index"], 0)
        self.assertEqual(context.user_data["quiz"]["score"], 0)
        self.assertEqual(context.user_data["quiz"]["question_message_id"], 77)
        query.answer.assert_awaited_once()
        query.edit_message_reply_markup.assert_not_awaited()

    async def test_concurrent_course3_submit_callbacks_claim_one_answer_and_one_reward(self):
        lesson = bot.COURSE_LESSON_ORDER["unified_orthography"][0]
        update, context, first_query = self.make_context("submit_answer")
        context.user_data["quiz"].update({
            "lesson": lesson,
            "selected_answer_index": 0,
            "answer_in_progress": False,
        })
        reply_text = AsyncMock()
        first_query.message.reply_text = reply_text

        second_query = SimpleNamespace(
            data="submit_answer",
            message=SimpleNamespace(message_id=77, reply_text=reply_text),
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            edit_message_reply_markup=AsyncMock(),
        )
        second_update = SimpleNamespace(
            callback_query=second_query,
            effective_user=SimpleNamespace(id=12345),
        )
        acknowledgement_gate = asyncio.Event()

        async def delayed_acknowledgement():
            await acknowledgement_gate.wait()

        first_query.answer = AsyncMock(side_effect=delayed_acknowledgement)
        with patch.object(bot, "complete_quiz_with_rewards", return_value=True) as reward:
            first = asyncio.create_task(bot.quiz_answer(
                update, context, selected_index=0
            ))
            await asyncio.sleep(0)

            # The first callback must claim the question before its first await.
            self.assertTrue(context.user_data["quiz"]["answer_in_progress"])
            await bot.quiz_answer(second_update, context, selected_index=0)

            second_query.answer.assert_awaited_once()
            second_query.edit_message_reply_markup.assert_not_awaited()
            reward.assert_not_called()

            acknowledgement_gate.set()
            await first

        reward.assert_called_once_with(12345, lesson)
        self.assertNotIn("quiz", context.user_data)
        first_query.edit_message_reply_markup.assert_awaited_once_with(
            reply_markup=None
        )
        self.assertEqual(reply_text.await_count, 2)

    async def test_feedback_delivery_failure_clears_uncommitted_quiz(self):
        update, context, query = self.make_context("answer_0")
        query.message.reply_text = AsyncMock(
            side_effect=RuntimeError("Telegram feedback delivery failed")
        )
        with patch.object(bot, "complete_quiz_with_rewards") as reward:
            with self.assertRaisesRegex(RuntimeError, "feedback delivery failed"):
                await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        reward.assert_not_called()

    async def test_next_question_delivery_failure_clears_quiz(self):
        update, context, query = self.make_context("answer_0")
        context.user_data["quiz"]["questions"].append({
            "question": "پرسیاری دووەم",
            "options": ["وەڵامی A", "وەڵامی B"],
            "answer": "وەڵامی A",
        })
        query.message.reply_text = AsyncMock(
            side_effect=[None, RuntimeError("Telegram next question delivery failed")]
        )

        with self.assertRaisesRegex(RuntimeError, "next question delivery failed"):
            await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        self.assertEqual(query.message.reply_text.await_count, 2)

    async def test_reward_persistence_failure_clears_exhausted_quiz(self):
        update, context, query = self.make_context("answer_0")
        query.message.reply_text = AsyncMock()
        with patch.object(
            bot,
            "complete_quiz_with_rewards",
            side_effect=RuntimeError("quiz reward database failure"),
        ) as reward:
            with self.assertRaisesRegex(RuntimeError, "quiz reward database failure"):
                await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        reward.assert_called_once_with(12345, "وانە_1")
        self.assertEqual(query.message.reply_text.await_count, 1)

    async def test_final_result_delivery_failure_clears_already_rewarded_quiz(self):
        update, context, query = self.make_context("answer_0")
        query.message.reply_text = AsyncMock(
            side_effect=[None, RuntimeError("Telegram final result delivery failed")]
        )
        with patch.object(bot, "complete_quiz_with_rewards", return_value=True) as reward:
            with self.assertRaisesRegex(RuntimeError, "final result delivery failed"):
                await bot.quiz_answer(update, context)

        self.assertNotIn("quiz", context.user_data)
        reward.assert_called_once_with(12345, "وانە_1")
        self.assertEqual(query.message.reply_text.await_count, 2)

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


    async def test_invalid_lesson_completion_acknowledges_callback(self):
        query = SimpleNamespace(
            data="finish_unknown_lesson",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once_with("❌ ئەم وانەیە نەناسراوە.")

    async def test_successful_lesson_completion_acknowledges_callback(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_orthography"][0]
        next_lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_orthography"][1]
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
            patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
            patch.object(bot, "complete_lesson_with_rewards", return_value=True),
            patch.object(bot, "check_badges"),
            patch.object(bot, "quiz_requires_submission", return_value=False),
            patch.object(bot, "next_course_lesson", return_value=next_lesson),
        ):
            await bot.finish_lesson(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()

    async def test_latin_lesson_completion_offers_next_lesson_in_same_course(self):
        for course_id in ("kurmanji_latin_orthography", "kurmanji_latin_grammar"):
            with self.subTest(course_id=course_id):
                first, second = bot.COURSE_LESSON_ORDER[course_id][:2]
                query = SimpleNamespace(
                    data=f"finish_{first}",
                    from_user=SimpleNamespace(id=12345),
                    answer=AsyncMock(),
                    message=SimpleNamespace(reply_text=AsyncMock()),
                )
                update = SimpleNamespace(callback_query=query)
                context = SimpleNamespace(user_data={})
                with (
                    patch.object(bot, "can_open", return_value=True),
                    patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
                    patch.object(bot, "complete_lesson_with_rewards", return_value=True),
                    patch.object(bot, "check_badges"),
                ):
                    await bot.finish_lesson(update, context)

                keyboard = query.message.reply_text.await_args.kwargs["reply_markup"]
                self.assertEqual(
                    keyboard.inline_keyboard[0][0].callback_data,
                    f"next_lesson_{second}",
                )

    async def test_final_lesson_of_each_latin_course_offers_its_own_quiz(self):
        for course_id in ("kurmanji_latin_orthography", "kurmanji_latin_grammar"):
            with self.subTest(course_id=course_id):
                final_lesson = bot.COURSE_LESSON_ORDER[course_id][-1]
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
                    patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
                    patch.object(bot, "complete_lesson_with_rewards", return_value=True),
                    patch.object(bot, "check_badges"),
                    patch.object(bot, "quiz_is_available", return_value=True),
                ):
                    await bot.finish_lesson(update, context)

                keyboard = query.message.reply_text.await_args.kwargs["reply_markup"]
                self.assertEqual(
                    keyboard.inline_keyboard[0][0].callback_data,
                    f"quiz_{final_lesson}_start",
                )

    async def test_both_latin_course_quizzes_start_with_namespaced_lesson_ids(self):
        for course_id in ("kurmanji_latin_orthography", "kurmanji_latin_grammar"):
            with self.subTest(course_id=course_id):
                lesson = bot.COURSE_LESSON_ORDER[course_id][0]
                query = SimpleNamespace(
                    data=f"quiz_{lesson}_start",
                    from_user=SimpleNamespace(id=12345),
                    answer=AsyncMock(),
                    message=SimpleNamespace(
                        reply_text=AsyncMock(return_value=SimpleNamespace(message_id=880))
                    ),
                )
                update = SimpleNamespace(
                    callback_query=query,
                    effective_user=SimpleNamespace(id=12345),
                )
                context = SimpleNamespace(user_data={})
                source_snapshot = [dict(item, options=list(item["options"])) for item in bot.QUIZ_DATA[lesson]]
                with (
                    patch.object(bot, "get_completed_lessons", return_value=[lesson]),
                    patch.object(bot, "quiz_is_available", return_value=True),
                ):
                    await bot.start_quiz(update, context)

                quiz = context.user_data["quiz"]
                expected = bot.QUIZ_DATA[lesson][0]
                self.assertEqual(quiz["lesson"], lesson)
                self.assertEqual(len(quiz["questions"]), len(bot.QUIZ_DATA[lesson]))
                for randomized, source in zip(quiz["questions"], bot.QUIZ_DATA[lesson]):
                    self.assertEqual(set(randomized["options"]), set(source["options"]))
                    self.assertEqual(randomized["options"][randomized["options"].index(source["answer"])], source["answer"])
                self.assertEqual(bot.QUIZ_DATA[lesson], source_snapshot)
                self.assertEqual(quiz["question_message_id"], 880)
                self.assertEqual(query.message.reply_text.await_args.args[0], "🎯 ڕاهێنان " + expected["question"])
                markup = query.message.reply_text.await_args.kwargs["reply_markup"]
                self.assertEqual(
                    [row[0].callback_data for row in markup.inline_keyboard],
                    [f"select_answer_{i}" for i in range(len(expected["options"]))],
                )

    async def test_stale_completed_latin_lesson_cannot_bypass_course_sequence(self):
        course = bot.COURSE_LESSON_ORDER["kurmanji_latin_orthography"]
        lesson = course[1]
        query = SimpleNamespace(
            data=f"quiz_{lesson}_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})
        with (
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "quiz_is_available", return_value=True),
            patch.object(bot, "can_open", return_value=False),
        ):
            await bot.start_quiz(update, context)
        self.assertNotIn("quiz", context.user_data)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("وانەکانی پێشوو", query.message.reply_text.await_args.args[0])

    async def test_quiz_start_acknowledgement_failure_clears_launch_claim(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0]
        query = SimpleNamespace(
            data=f"quiz_{lesson}_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(side_effect=RuntimeError("Telegram start acknowledgement failed")),
            message=SimpleNamespace(message_id=501, reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query, effective_user=SimpleNamespace(id=12345))
        context = SimpleNamespace(user_data={})
        with (
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            with self.assertRaisesRegex(RuntimeError, "start acknowledgement failed"):
                await bot.start_quiz(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.message.reply_text.assert_not_awaited()

    async def test_first_quiz_question_delivery_failure_clears_launch_state(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0]
        query = SimpleNamespace(
            data=f"quiz_{lesson}_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(
                message_id=502,
                reply_text=AsyncMock(side_effect=RuntimeError("Telegram first question delivery failed")),
            ),
        )
        update = SimpleNamespace(callback_query=query, effective_user=SimpleNamespace(id=12345))
        context = SimpleNamespace(user_data={})
        with (
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            with self.assertRaisesRegex(RuntimeError, "first question delivery failed"):
                await bot.start_quiz(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertNotIn("quiz", context.user_data)

    async def test_duplicate_quiz_start_callback_does_not_replace_inflight_quiz(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0]
        query = SimpleNamespace(
            data=f"quiz_{lesson}_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(
                message_id=500,
                reply_text=AsyncMock(return_value=SimpleNamespace(message_id=880)),
            ),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})
        acknowledgement_gate = asyncio.Event()

        async def delayed_acknowledgement():
            await acknowledgement_gate.wait()

        query.answer = AsyncMock(side_effect=delayed_acknowledgement)
        with (
            patch.object(bot, "course_is_active", return_value=True),
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            first = asyncio.create_task(bot.start_quiz(update, context))
            await asyncio.sleep(0)
            first_quiz = context.user_data["quiz"]
            first_questions = first_quiz["questions"]

            query.answer = AsyncMock()
            await bot.start_quiz(update, context)

            self.assertIs(context.user_data["quiz"], first_quiz)
            self.assertIs(context.user_data["quiz"]["questions"], first_questions)
            query.message.reply_text.assert_not_awaited()

            acknowledgement_gate.set()
            await first

        query.message.reply_text.assert_awaited_once()
        self.assertEqual(context.user_data["quiz"]["question_message_id"], 880)

    async def test_latin_quiz_answer_requires_selection_then_submit(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0]
        question = bot.QUIZ_DATA[lesson][0]
        correct_index = question["options"].index(question["answer"])
        update, context, query = self.make_context(f"select_answer_{correct_index}")
        context.user_data["quiz"].update({
            "lesson": lesson,
            "questions": [question],
            "score": 0,
        })
        query.message.reply_text = AsyncMock()
        with patch.object(bot, "complete_quiz_with_rewards", return_value=True) as reward:
            await bot.select_quiz_answer(update, context)
            self.assertEqual(context.user_data["quiz"]["selected_answer_index"], correct_index)
            self.assertEqual(context.user_data["quiz"]["score"], 0)
            selected_markup = query.edit_message_reply_markup.await_args.kwargs["reply_markup"]
            self.assertEqual(selected_markup.inline_keyboard[-1][0].callback_data, "submit_answer")
            reward.assert_not_called()

            query.data = "submit_answer"
            await bot.submit_quiz_answer(update, context)

        reward.assert_called_once_with(12345, lesson)
        self.assertNotIn("quiz", context.user_data)
        self.assertTrue(any("1/1" in call.args[0] for call in query.message.reply_text.await_args_list))

    async def test_selection_acknowledgement_failure_clears_pending_selection(self):
        lesson = bot.COURSE_LESSON_ORDER["unified_orthography"][0]
        update, context, query = self.make_context("select_answer_0")
        context.user_data["quiz"].update({
            "lesson": lesson,
            "selected_answer_index": None,
        })
        query.answer = AsyncMock(side_effect=RuntimeError("selection acknowledgement failed"))

        with self.assertRaisesRegex(RuntimeError, "selection acknowledgement failed"):
            await bot.select_quiz_answer(update, context)

        self.assertIsNone(context.user_data["quiz"]["selected_answer_index"])
        query.edit_message_reply_markup.assert_not_awaited()

    async def test_selection_keyboard_edit_failure_clears_unsubmittable_selection(self):
        lesson = bot.COURSE_LESSON_ORDER["unified_orthography"][0]
        update, context, query = self.make_context("select_answer_1")
        context.user_data["quiz"].update({
            "lesson": lesson,
            "selected_answer_index": None,
        })
        query.edit_message_reply_markup = AsyncMock(
            side_effect=RuntimeError("selection keyboard edit failed")
        )

        with self.assertRaisesRegex(RuntimeError, "selection keyboard edit failed"):
            await bot.select_quiz_answer(update, context)

        self.assertIsNone(context.user_data["quiz"]["selected_answer_index"])
        query.answer.assert_awaited_once()
        query.edit_message_reply_markup.assert_awaited_once()

    async def test_selection_is_recorded_before_callback_acknowledgement(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0]
        question = bot.QUIZ_DATA[lesson][0]
        correct_index = question["options"].index(question["answer"])
        update, context, query = self.make_context(f"select_answer_{correct_index}")
        context.user_data["quiz"].update({
            "lesson": lesson,
            "questions": [question],
            "score": 0,
        })
        acknowledgement_gate = asyncio.Event()

        async def delayed_acknowledgement():
            await acknowledgement_gate.wait()

        query.answer = AsyncMock(side_effect=delayed_acknowledgement)
        task = asyncio.create_task(bot.select_quiz_answer(update, context))
        await asyncio.sleep(0)

        self.assertEqual(
            context.user_data["quiz"]["selected_answer_index"], correct_index
        )
        acknowledgement_gate.set()
        await task
        query.edit_message_reply_markup.assert_awaited_once()

    async def test_wrong_submitted_answer_shows_incorrect_and_reveals_correct_answer(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0]
        question = bot.QUIZ_DATA[lesson][0]
        wrong_index = next(
            index for index, option in enumerate(question["options"])
            if option != question["answer"]
        )
        update, context, query = self.make_context(f"select_answer_{wrong_index}")
        context.user_data["quiz"].update({
            "lesson": lesson,
            "questions": [question],
            "score": 0,
        })
        query.message.reply_text = AsyncMock()

        await bot.select_quiz_answer(update, context)
        query.data = "submit_answer"
        with patch.object(bot, "complete_quiz_with_rewards", return_value=True):
            await bot.submit_quiz_answer(update, context)

        feedback = [call.args[0] for call in query.message.reply_text.await_args_list]
        self.assertTrue(any("❌" in item and question["answer"] in item for item in feedback))
        self.assertNotIn("quiz", context.user_data)

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
    async def test_lesson_completion_offers_clickable_practice_for_exact_target_lessons(self):
        targets = [
            "وانە_3",
            bot.COURSE_LESSON_ORDER["kurmanji_latin_orthography"][0],
            bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0],
        ]
        for lesson in targets:
            with self.subTest(lesson=lesson):
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
                    patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
                    patch.object(bot, "complete_lesson_with_rewards", return_value=True),
                    patch.object(bot, "check_badges"),
                    patch.object(bot, "quiz_is_available", return_value=True),
                ):
                    await bot.finish_lesson(update, context)

                keyboard = query.message.reply_text.await_args.kwargs["reply_markup"]
                callbacks = [
                    button.callback_data
                    for row in keyboard.inline_keyboard
                    for button in row
                ]
                self.assertIn(bot.lesson_practice_callback(lesson), callbacks)

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
    async def test_course_one_lesson_two_does_not_offer_clickable_practice(self):
        lesson = "وانە_2"
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
            patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
            patch.object(bot, "complete_lesson_with_rewards", return_value=True),
            patch.object(bot, "check_badges"),
        ):
            await bot.finish_lesson(update, context)

        keyboard = query.message.reply_text.await_args.kwargs["reply_markup"]
        callbacks = [
            button.callback_data
            for row in keyboard.inline_keyboard
            for button in row
        ]
        self.assertFalse(any(callback.startswith("quiz_") for callback in callbacks))

    def test_submission_mode_is_limited_to_course_one_lesson_three_and_both_latin_courses(self):
        self.assertFalse(bot.quiz_requires_submission("وانە_2"))
        self.assertTrue(bot.quiz_requires_submission("وانە_3"))
        self.assertFalse(bot.quiz_requires_submission("وانە_4"))
        for course_id in ("kurmanji_latin_orthography", "kurmanji_latin_grammar"):
            self.assertTrue(bot.quiz_requires_submission(bot.COURSE_LESSON_ORDER[course_id][0]))

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
    async def test_course_one_lesson_three_uses_select_then_submit_buttons(self):
        lesson = "وانە_3"
        query = SimpleNamespace(
            data="quiz_3_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(
                reply_text=AsyncMock(return_value=SimpleNamespace(message_id=883))
            ),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})
        with (
            patch.object(bot, "get_completed_lessons", return_value=[lesson]),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            await bot.start_quiz(update, context)

        markup = query.message.reply_text.await_args.kwargs["reply_markup"]
        self.assertTrue(all(
            row[0].callback_data.startswith("select_answer_")
            for row in markup.inline_keyboard
        ))

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
    async def test_course_one_lesson_two_keeps_immediate_answer_buttons(self):
        query = SimpleNamespace(
            data="quiz_2_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(
                reply_text=AsyncMock(return_value=SimpleNamespace(message_id=882))
            ),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})
        with (
            patch.object(bot, "get_completed_lessons", return_value=["وانە_2"]),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            await bot.start_quiz(update, context)

        markup = query.message.reply_text.await_args.kwargs["reply_markup"]
        self.assertTrue(all(
            row[0].callback_data.startswith("answer_")
            for row in markup.inline_keyboard
        ))

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
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

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
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


    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
    def test_lesson_lock_requires_previous_lesson_completion(self):
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertTrue(bot.can_open(12345, "وانە_1"))
            self.assertFalse(bot.can_open(12345, "وانە_2"))
            self.assertFalse(bot.can_open(12345, "وانە_22"))
            self.assertFalse(bot.can_open(12345, "not-a-lesson"))

        with patch.object(bot, "get_completed_lessons", return_value=["وانە_1"]):
            self.assertTrue(bot.can_open(12345, "وانە_2"))
            self.assertFalse(bot.can_open(12345, "وانە_3"))

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
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

    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
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
        ):
            await bot.finish_lesson(update, context)

        complete.assert_called_once_with(12345, "وانە_1")
        badges.assert_not_called()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێشتر تەواو کراوە", query.message.reply_text.await_args.args[0])


    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
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
        ):
            await bot.finish_lesson(update, context)

        complete.assert_called_once_with(12345, final_lesson)
        reply = query.message.reply_text.await_args
        button = reply.kwargs["reply_markup"].inline_keyboard[0][0]
        self.assertEqual(button.callback_data, "quiz_22_start")
        self.assertIn("تاقیکردنەوە", button.text)


    @unittest.skip("Legacy 22-lesson Course 1 retired; Arami 21-lesson interaction tests cover the replacement.")
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

    async def test_retired_legacy_lesson_22_quiz_cannot_be_started(self):
        update, context, query = self.make_context("quiz_22_start", message_id=77)
        context.user_data.clear()
        query.message.reply_text = AsyncMock()

        with patch.object(bot, "get_completed_lessons", return_value=["وانە_22"]):
            await bot.start_quiz(update, context)

        self.assertNotIn("quiz", context.user_data)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("لە ڕێڕەوی فێربووندا نیە", query.message.reply_text.await_args.args[0])


class AramiCourse1CompletionNavigationTests(unittest.IsolatedAsyncioTestCase):
    async def test_duplicate_completion_keeps_next_lesson_navigation_without_rewards(self):
        lesson = bot.ARMI_LESSON_IDS[0]
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
            patch.object(bot, "complete_lesson_with_rewards", return_value=False) as complete,
            patch.object(bot, "get_user_level") as level,
            patch.object(bot, "check_badges") as badges,
        ):
            await bot.finish_lesson(update, context)

        complete.assert_called_once_with(12345, lesson)
        level.assert_called_once_with(12345)
        badges.assert_not_called()
        query.message.reply_text.assert_awaited_once()
        reply = query.message.reply_text.await_args
        self.assertIn("پێشتر تەواو کراوە", reply.args[0])
        self.assertNotIn("+10 XP", reply.args[0])
        buttons = [
            button.callback_data
            for row in reply.kwargs["reply_markup"].inline_keyboard
            for button in row
        ]
        self.assertEqual(buttons, ["aramiC:lesson:2"])

    async def test_final_course1_lesson_offers_its_dedicated_assessment(self):
        lesson = bot.ARMI_LESSON_IDS[-1]
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
            patch.object(bot, "complete_lesson_with_rewards", return_value=True),
            patch.object(bot, "get_user_level", side_effect=["A1.1", "A1.1"]),
            patch.object(bot, "check_badges"),
        ):
            await bot.finish_lesson(update, context)

        reply = query.message.reply_text.await_args
        buttons = [
            button.callback_data
            for row in reply.kwargs["reply_markup"].inline_keyboard
            for button in row
        ]
        self.assertEqual(buttons, ["aramiC:assessment:21"])
        self.assertIn("کۆرسی ١ تەواو بوو", reply.args[0])

    async def test_completion_of_lesson_four_routes_to_dedicated_lesson_five_reader(self):
        lesson = bot.ARMI_LESSON_IDS[3]
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
            patch.object(bot, "complete_lesson_with_rewards", return_value=True),
            patch.object(bot, "get_user_level", side_effect=["A1.1", "A1.1"]),
            patch.object(bot, "check_badges"),
        ):
            await bot.finish_lesson(update, context)

        reply = query.message.reply_text.await_args
        buttons = [
            button.callback_data
            for row in reply.kwargs["reply_markup"].inline_keyboard
            for button in row
        ]
        self.assertEqual(buttons, ["arami5:lesson"])


class AramiCourse1GlobalQuizMenuTests(unittest.IsolatedAsyncioTestCase):
    async def _open_global_menu(self, menu_text, completed):
        message = SimpleNamespace(text=menu_text, reply_text=AsyncMock())
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=24680),
        )
        with (
            patch.object(bot, "get_user"),
            patch.object(bot, "get_completed_lessons", return_value=completed),
            patch.object(bot, "active_course_lessons", return_value=[]),
            patch.object(bot, "course_is_active", return_value=True),
        ):
            await bot.message(update, SimpleNamespace(user_data={}))
        message.reply_text.assert_awaited_once()
        markup = message.reply_text.await_args.kwargs.get("reply_markup")
        if markup is None:
            return set()
        return {
            button.callback_data
            for row in markup.inline_keyboard
            for button in row
        }

    async def test_global_assessment_menu_includes_completed_arami_lessons(self):
        completed = [
            bot.ARMI_LESSON_IDS[0],
            bot.ARMI_LESSON_IDS[1],
            bot.ARMI_LESSON_IDS[4],
        ]
        callbacks = await self._open_global_menu("📝 تاقیکردنەوەکان", completed)
        self.assertEqual(
            callbacks,
            {"arami1:assessment", "aramiC:assessment:2"},
        )

    async def test_global_practice_menu_includes_completed_arami_lessons(self):
        completed = [
            bot.ARMI_LESSON_IDS[0],
            bot.ARMI_LESSON_IDS[1],
            bot.ARMI_LESSON_IDS[4],
        ]
        callbacks = await self._open_global_menu("🎯 ڕاهێنانی کرتەیی", completed)
        self.assertEqual(
            callbacks,
            {"arami1:practice", "aramiC:practice:2"},
        )

    async def test_global_quiz_menu_does_not_list_uncompleted_arami_lessons(self):
        callbacks = await self._open_global_menu("📝 تاقیکردنەوەکان", [])
        self.assertEqual(callbacks, set())



class LessonCompletionFormattingTests(unittest.IsolatedAsyncioTestCase):
    async def test_lesson_completion_rewards_use_real_line_breaks(self):
        lesson = bot.COURSE_LESSON_ORDER["kurmanji_latin_grammar"][0]
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
            patch.object(bot, "complete_lesson_with_rewards", return_value=True),
            patch.object(bot, "get_user_level", return_value="A1.1 🌱"),
            patch.object(bot, "check_badges"),
            patch.object(bot, "quiz_is_available", return_value=True),
        ):
            await bot.finish_lesson(update, context)

        message = query.message.reply_text.await_args.args[0]
        self.assertIn("\n", message)
        self.assertNotIn("\\n", message)


if __name__ == "__main__":
    unittest.main()
