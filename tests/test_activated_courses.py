"""Regression tests for owner-activated Courses 2 and 3."""
import asyncio
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

import bot

# Most callback tests use an isolated/mock learner-progress ledger.
_beta_ledger_test_default = None
_beta_completion_test_default = None

def setUpModule():
    global _beta_ledger_test_default, _beta_completion_test_default
    _beta_ledger_test_default = patch.object(bot, "get_completed_beta_lessons", return_value=[])
    _beta_completion_test_default = patch.object(bot, "complete_beta_lesson", return_value=True)
    _beta_ledger_test_default.start()
    _beta_completion_test_default.start()

def tearDownModule():
    if _beta_completion_test_default is not None:
        _beta_completion_test_default.stop()
    if _beta_ledger_test_default is not None:
        _beta_ledger_test_default.stop()

ROOT = Path(__file__).resolve().parents[1]


class ActivatedCoursesTests(unittest.IsolatedAsyncioTestCase):
    def make_update(self, callback_data, user_id=12345):
        message = SimpleNamespace(reply_text=AsyncMock(), edit_text=AsyncMock(), message_id=77)
        query = SimpleNamespace(
            data=callback_data,
            from_user=SimpleNamespace(id=user_id),
            message=message,
            answer=AsyncMock(),
        )
        return SimpleNamespace(callback_query=query), message, query

    def test_manifest_activates_courses_two_and_three_and_retires_legacy_course_one(self):
        self.assertTrue(bot.course_is_active("arami_orthography_foundations"))
        self.assertFalse(bot.course_is_active("orthography_basic"))
        self.assertEqual(bot.COURSE_LESSON_ORDER["orthography_basic"], [])
        self.assertEqual(len(next(c for c in bot.COURSES if c["id"] == "arami_orthography_foundations")["lesson_ids"]), 21)
        arami_course = next(c for c in bot.COURSES if c["id"] == "arami_orthography_foundations")
        self.assertEqual(arami_course["title"], "کۆرسی ١: ڕێنووسی سەرەتاییی کوردی")
        self.assertFalse(any(key.startswith("وانە_") for key in bot.LESSON_DATA))
        self.assertFalse(any(key.startswith("وانە_") for key in bot.QUIZ_DATA))
        self.assertTrue(bot.course_is_active("daily_conversation"))
        self.assertTrue(bot.course_is_active("unified_orthography"))
        self.assertTrue(bot.course_is_active("grammar"))
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["daily_conversation"]), 42)
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["unified_orthography"]), 66)

    async def test_retired_22_lesson_course_is_not_shown_in_course_menu(self):
        message = SimpleNamespace(reply_text=AsyncMock(), text="📘 کۆرسەکان")
        update = SimpleNamespace(
            message=message,
            effective_user=SimpleNamespace(id=12345),
        )
        with patch.object(bot, "get_user"), patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.message(update, SimpleNamespace(user_data={}))
        self.assertEqual(message.reply_text.await_count, 1)
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        callbacks = [button.callback_data for row in keyboard for button in row]
        self.assertNotIn("course_orthography_basic", callbacks)
        self.assertIn("course_arami_orthography_foundations", callbacks)

    async def test_open_arami_course_from_generic_course_menu(self):
        update, message, query = self.make_update("course_arami_orthography_foundations")
        with patch.object(bot, "get_completed_lessons", return_value=[]), patch.object(
            bot, "can_open", return_value=True
        ):
            await bot.open_course(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()
        keyboard = message.reply_text.await_args.kwargs["reply_markup"]
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        reads = [button for button in buttons if button.callback_data.startswith("aramiC:select:")]
        practices = [button for button in buttons if ":practice" in button.callback_data]
        assessments = [button for button in buttons if ":assessment" in button.callback_data]
        self.assertEqual(len(reads), 21)
        self.assertEqual(len(practices), 0)
        self.assertEqual(len(assessments), 0)
        self.assertEqual(len(reads), 21)
        self.assertEqual([len(row) for row in keyboard.inline_keyboard[:-1]], [2] * 10 + [1])

    def test_arami_assessment_does_not_award_xp_before_explicit_approval(self):
        with patch.object(bot, "complete_quiz_with_rewards") as reward:
            self.assertFalse(bot.award_arami_assessment(12345, "arami_course1_lesson_01"))
        reward.assert_not_called()

    def test_startup_validation_confirms_both_activated_courses_are_complete(self):
        bot.validate_activated_course_runtime()

    def test_all_active_courses_have_globally_unique_lesson_ids_and_exact_reverse_mapping(self):
        active_orders = {
            course_id: lessons
            for course_id, lessons in bot.COURSE_LESSON_ORDER.items()
            if bot.course_is_active(course_id)
        }
        flattened = [
            (course_id, lesson_id)
            for course_id, lessons in active_orders.items()
            for lesson_id in lessons
        ]
        lesson_ids = [lesson_id for _, lesson_id in flattened]

        self.assertTrue(lesson_ids)
        self.assertEqual(
            len(lesson_ids),
            len(set(lesson_ids)),
            "A lesson ID must belong to exactly one active course",
        )
        for course_id, lesson_id in flattened:
            self.assertEqual(bot.LESSON_COURSE.get(lesson_id), course_id)

        self.assertEqual(set(bot.LESSON_COURSE), set(lesson_ids))

    def test_course_lesson_ids_are_unique_and_do_not_replace_course_one_ids(self):
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["orthography_basic"]), 0)
        all_ids = [
            lesson
            for course_id in ("daily_conversation", "unified_orthography")
            for lesson in bot.COURSE_LESSON_ORDER[course_id]
        ]
        self.assertEqual(len(all_ids), 108)
        self.assertEqual(len(set(all_ids)), 108)
        self.assertEqual(bot.COURSE_LESSON_ORDER["orthography_basic"], [])

    def test_arami_course_progression_uses_all_21_manifest_lesson_ids(self):
        order = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"]
        self.assertEqual(len(order), 21)
        self.assertEqual(order[0], "arami_course1_lesson_01")
        self.assertEqual(order[-1], "arami_course1_lesson_21")
        with (
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "get_completed_beta_lessons", return_value=[]),
        ):
            self.assertTrue(bot.can_open(12345, order[0]))
            self.assertFalse(bot.can_open(12345, order[1]))
        with patch.object(bot, "get_completed_lessons", return_value=[order[0]]):
            self.assertTrue(bot.can_open(12345, order[1]))
            self.assertFalse(bot.can_open(12345, order[2]))

    def test_approved_course4_lesson_does_not_reuse_stale_beta_completion(self):
        order = bot.COURSE_LESSON_ORDER["grammar"]
        lesson_32 = order[31]
        lesson_33 = order[32]
        official_prefix = order[:28]
        beta_prefix = order[28:31]
        approved_record = {
            **bot.LESSON_DATA[lesson_32],
            "review_status": "scientific_review_complete_with_qualified_notes",
        }

        with (
            patch.object(bot, "get_completed_lessons", return_value=official_prefix),
            patch.object(bot, "get_completed_beta_lessons", return_value=[*beta_prefix, lesson_32]),
            patch.dict(bot.LESSON_DATA, {lesson_32: approved_record}),
        ):
            # The old Beta record must not stand in for official completion
            # after the lesson has left the pending-review state.
            self.assertFalse(bot.can_open(12345, lesson_33))

        with (
            patch.object(bot, "get_completed_lessons", return_value=official_prefix),
            patch.object(bot, "get_completed_beta_lessons", return_value=[*beta_prefix, lesson_32]),
        ):
            # While lesson 32 is still an eligible Beta draft, its separate
            # Beta completion may continue the Beta review sequence.
            self.assertTrue(bot.can_open(12345, lesson_33))

    def test_course_two_and_three_progression_is_independent(self):
        course_two = bot.COURSE_LESSON_ORDER["daily_conversation"]
        course_three = bot.COURSE_LESSON_ORDER["unified_orthography"]
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertTrue(bot.can_open(12345, course_two[0]))
            self.assertFalse(bot.can_open(12345, course_two[1]))
            self.assertTrue(bot.can_open(12345, course_three[0]))
            self.assertFalse(bot.can_open(12345, course_three[1]))
        with patch.object(bot, "get_completed_lessons", return_value=[course_two[0]]):
            self.assertTrue(bot.can_open(12345, course_two[1]))
            self.assertFalse(bot.can_open(12345, course_three[1]))
        with patch.object(bot, "get_completed_lessons", return_value=course_three[:-1]):
            self.assertTrue(bot.can_open(12345, course_three[-1]))

    def test_all_course_types_unlock_only_a_contiguous_prefix(self):
        course_ids = (
            "arami_orthography_foundations",
            "daily_conversation",
            "unified_orthography",
            "kurmanji_latin_orthography",
            "kurmanji_latin_grammar",
        )
        for course_id in course_ids:
            order = bot.COURSE_LESSON_ORDER[course_id]
            with self.subTest(course_id=course_id), patch.object(
                bot, "get_completed_lessons", return_value=[order[0], order[2]]
            ):
                self.assertFalse(bot.can_open(12345, order[3]))

    async def test_finishing_arami_lesson_one_records_progress_and_unlocks_lesson_two(self):
        lesson_id = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"][0]
        update, message, query = self.make_update(f"finish_{lesson_id}")
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "complete_beta_lesson", return_value=True) as complete,
            patch.object(bot, "check_badges"),
        ):
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        complete.assert_called_once_with(12345, lesson_id)
        self.assertEqual(message.reply_text.await_count, 1)
        self.assertIn("وانەی دواتر ئامادەیە", message.reply_text.await_args.args[0])
        keyboard = message.reply_text.await_args.kwargs["reply_markup"]
        self.assertEqual(
            keyboard.inline_keyboard[0][0].callback_data,
            "aramiC:lesson:2",
        )

    async def test_finishing_arami_final_review_only_lesson_stays_beta_without_assessment(self):
        lesson_id = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"][-1]
        update, message, query = self.make_update(f"finish_{lesson_id}")
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "complete_beta_lesson", return_value=True) as complete,
            patch.object(bot, "complete_lesson_with_rewards") as official_complete,
            patch.object(bot, "check_badges") as badges,
            patch.object(bot, "get_user_level") as level,
        ):
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        complete.assert_called_once_with(12345, lesson_id)
        official_complete.assert_not_called()
        badges.assert_not_called()
        level.assert_not_called()
        message.reply_text.assert_awaited_once()
        reply = message.reply_text.await_args
        self.assertIn("پێشچوونی Beta", reply.args[0])
        self.assertIn("ڕێڕەوی تاقیکاریی Beta تەواو بوو", reply.args[0])
        self.assertNotIn("کۆرسی ١ تەواو بوو", reply.args[0])
        self.assertNotIn("وانەی دواتر ئامادەیە", reply.args[0])
        self.assertNotIn("reply_markup", reply.kwargs)

    async def test_uncompleted_previous_lesson_blocks_arami_reward_claim(self):
        lesson_id = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"][1]
        update, message, query = self.make_update(f"finish_{lesson_id}")
        with (
            patch.object(bot, "can_open", return_value=False),
            patch.object(bot, "complete_lesson_with_rewards") as complete,
        ):
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        complete.assert_not_called()
        message.reply_text.assert_awaited_once()
        self.assertIn("سەرەتا وانەی پێشووتر تەواو بکە", message.reply_text.await_args.args[0])

    async def test_repeated_arami_completion_does_not_grant_rewards_again(self):
        lesson_id = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"][0]
        update, message, query = self.make_update(f"finish_{lesson_id}")
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "complete_beta_lesson", return_value=False) as complete,
            patch.object(bot, "check_badges") as badges,
        ):
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        complete.assert_called_once_with(12345, lesson_id)
        badges.assert_not_called()
        message.reply_text.assert_awaited_once()
        self.assertIn("پێشتر بۆ پێشچوونی Beta تۆمار کراوە", message.reply_text.await_args.args[0])

    async def test_open_course_two_shows_first_12_of_42_lesson_buttons(self):
        update, message, query = self.make_update("course_daily_conversation")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 7)
        self.assertEqual(keyboard[-1][0].callback_data, "coursepage:daily_conversation:1")
        self.assertEqual(
            keyboard[0][0].callback_data,
            "open_lesson_daily_conversation_01",
        )

    async def test_open_course_three_shows_all_66_lesson_buttons(self):
        update, message, query = self.make_update("course_unified_orthography")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 7)
        self.assertEqual(keyboard[-1][0].callback_data, "coursepage:unified_orthography:1")
        self.assertEqual(
            keyboard[0][0].callback_data,
            "open_lesson_unified_orthography_01",
        )

    async def test_course_menu_descriptions_use_real_line_breaks(self):
        update, message, query = self.make_update("course_daily_conversation")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        rendered = message.reply_text.await_args.args[0]
        self.assertIn("\n", rendered)
        self.assertNotIn("\\n", rendered)

    async def test_arami_course_menu_description_uses_real_line_break(self):
        update, message, query = self.make_update("course_arami_orthography_foundations")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        rendered = message.reply_text.await_args.args[0]
        self.assertIn("\n", rendered)
        self.assertNotIn("\\n", rendered)

    async def test_course_menu_pagination_opens_the_requested_next_page(self):
        update, message, query = self.make_update("coursepage:daily_conversation:1")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course_page(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.reply_text.assert_not_awaited()
        message.edit_text.assert_awaited_once()
        rendered = message.edit_text.await_args.args[0]
        self.assertIn("کۆرسی ٢: وتووێژ", rendered)
        self.assertIn("13 تا 24 لە 42", rendered)
        self.assertIn("لاپەڕەی 2/4", rendered)
        keyboard = message.edit_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 7)
        self.assertEqual(
            keyboard[0][0].callback_data,
            "open_lesson_daily_conversation_13",
        )
        self.assertEqual(keyboard[-1][0].callback_data, "coursepage:daily_conversation:0")

    async def test_course_two_last_page_keeps_lessons_37_to_42_and_edits_same_message(self):
        update, message, query = self.make_update("coursepage:daily_conversation:3")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course_page(update, SimpleNamespace())
        message.reply_text.assert_not_awaited()
        message.edit_text.assert_awaited_once()
        rendered = message.edit_text.await_args.args[0]
        self.assertEqual(rendered.count("کۆرسی ٢: وتووێژ"), 1)
        self.assertEqual(rendered.count("٤٢ وانەی وتووێژ"), 1)
        self.assertIn("37 تا 42 لە 42", rendered)
        self.assertIn("لاپەڕەی 4/4", rendered)
        keyboard = message.edit_text.await_args.kwargs["reply_markup"].inline_keyboard
        lesson_buttons = [button.callback_data for row in keyboard for button in row if button.callback_data.startswith("open_lesson_")]
        self.assertEqual(lesson_buttons, [
            "open_lesson_daily_conversation_37",
            "open_lesson_daily_conversation_38",
            "open_lesson_daily_conversation_39",
            "open_lesson_daily_conversation_40",
            "open_lesson_daily_conversation_41",
            "open_lesson_daily_conversation_42",
        ])
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["daily_conversation"]), 42)

    def test_global_quiz_menus_are_paginated_for_all_completed_courses(self):
        all_lessons = [
            lesson_id
            for course_id, lesson_ids in bot.COURSE_LESSON_ORDER.items()
            if bot.course_is_active(course_id)
            for lesson_id in lesson_ids
        ]
        with (
            patch.object(bot, "get_completed_lessons", return_value=all_lessons),
            patch.object(bot, "can_open", return_value=True),
        ):
            for mode in ("practice", "assessment"):
                items = bot.quiz_menu_items(12345, mode)
                self.assertGreater(len(items), bot.QUIZ_MENU_PAGE_SIZE)
                keyboard, page_count = bot.quiz_menu_keyboard(items, 0, mode)
                self.assertLessEqual(len(keyboard.inline_keyboard), bot.QUIZ_MENU_PAGE_SIZE + 1)
                self.assertEqual(keyboard.inline_keyboard[-1][0].callback_data, f"quizmenu:{mode}:1")
                last_page, _ = bot.quiz_menu_keyboard(items, page_count - 1, mode)
                self.assertLessEqual(len(last_page.inline_keyboard), bot.QUIZ_MENU_PAGE_SIZE + 1)

    async def test_quiz_menu_page_callback_renders_requested_page(self):
        update, message, query = self.make_update("quizmenu:assessment:1")
        items = [(f"Lesson {i}", f"quiz_lesson_{i}_start") for i in range(25)]
        with patch.object(bot, "quiz_menu_items", return_value=items):
            await bot.open_quiz_menu_page(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.edit_text.assert_awaited_once()
        message.reply_text.assert_not_awaited()
        keyboard = message.edit_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(keyboard[0][0].callback_data, "quiz_lesson_12_start")
        self.assertEqual(keyboard[-1][0].callback_data, "quizmenu:assessment:0")

    def test_arami_review_lessons_are_excluded_from_official_assessment_menu(self):
        arami = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"]
        with (
            patch.object(bot, "get_completed_lessons", return_value=arami),
            patch.object(bot, "can_open", return_value=True),
        ):
            practice_items = bot.quiz_menu_items(12345, "practice")
            assessment_items = bot.quiz_menu_items(12345, "assessment")

        arami_prefixes = ("arami1:", "arami5:", "aramiC:")
        self.assertTrue(any(callback.startswith(arami_prefixes) for _, callback in practice_items))
        self.assertFalse(any(callback.startswith(arami_prefixes) for _, callback in assessment_items))

    def test_arami_review_assessment_cannot_grant_official_rewards(self):
        arami = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"]
        review_lesson_id = arami[1]
        with patch.object(bot, "complete_quiz_with_rewards") as award:
            result = bot.award_arami_assessment(12345, review_lesson_id)

        self.assertFalse(result)
        self.assertFalse(bot.award_arami_assessment(12345, "unregistered_arami_lesson"))
        self.assertFalse(bot.award_arami_assessment(12345, "grammar_13"))
        award.assert_not_called()

    def test_every_active_course_uses_explicit_fail_closed_academic_approval(self):
        active_course_ids = {
            course["id"] for course in bot.COURSES if course.get("status") == "active"
        }
        self.assertEqual(active_course_ids, set(bot.ACADEMIC_REVIEW_REQUIRED_COURSE_IDS))

        # Lesson 13 remains review-only until its source mapping is fully reconciled.
        self.assertEqual(
            bot.LESSON_DATA["grammar_13"]["review_status"],
            "internal_cross_lesson_synthesis_no_external_source_mapping",
        )
        self.assertTrue(bot.lesson_is_pending_review("grammar_13"))
        self.assertTrue(bot.lesson_is_beta_review("grammar_13"))
        self.assertFalse(bot.lesson_quiz_is_available("grammar_13"))

        # Review-state distribution is a release gate, not inferred from runtime activation.
        course4 = [
            bot.LESSON_DATA[lesson_id]
            for lesson_id in bot.COURSE_LESSON_ORDER["grammar"]
        ]
        self.assertEqual(sum(x.get("review_status") == "scientific_review_complete_with_qualified_notes" for x in course4), 27)
        self.assertEqual(sum(x.get("review_status") == "independent_academic_research_owner_requested_lesson" for x in course4), 3)
        self.assertEqual(sum(x.get("review_status") == "internal_cross_lesson_synthesis_no_external_source_mapping" for x in course4), 1)
        self.assertEqual(sum(x.get("review_status") == "owner_review_pending_expanded_draft" for x in course4), 19)
        for lesson_id in ("grammar_29", "grammar_30", "grammar_31"):
            self.assertTrue(bot.lesson_is_pending_review(lesson_id))
            self.assertTrue(bot.lesson_is_beta_review(lesson_id))
            self.assertFalse(bot.lesson_quiz_is_available(lesson_id))

        # Unknown and missing statuses must never silently become official.
        approved_record = dict(bot.LESSON_DATA["grammar_13"])
        for status in ("future_unrecognized_status", "draft_editorial_review", None):
            with self.subTest(status=status):
                record = dict(approved_record)
                if status is None:
                    record.pop("review_status", None)
                else:
                    record["review_status"] = status
                with patch.dict(bot.LESSON_DATA, {"grammar_13": record}):
                    self.assertTrue(bot.lesson_is_pending_review("grammar_13"))
                    self.assertTrue(bot.lesson_is_beta_review("grammar_13"))

    def test_progress_badges_use_only_completed_lessons_from_active_courses(self):
        arami = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"]
        daily = bot.COURSE_LESSON_ORDER["daily_conversation"]
        unified = bot.COURSE_LESSON_ORDER["unified_orthography"]
        completed = [arami[0], daily[0], unified[-1]]
        with (
            patch.object(bot, "get_completed_lessons", return_value=completed),
            patch.object(
                bot,
                "course_is_active",
                side_effect=lambda course_id: course_id in {
                    "arami_orthography_foundations",
                    "daily_conversation",
                    "unified_orthography",
                },
            ),
        ):
            badges = bot.current_progress_badges(12345)

        self.assertEqual(len(badges), 0, "Unapproved Arami and draft editorial lessons cannot earn official badges")
        self.assertFalse(any("کۆرسی ٣" in badge for badge in badges))
        self.assertFalse(any("Diyako" in badge for badge in badges))

    def test_progress_badges_hide_stale_later_completions(self):
        daily = bot.COURSE_LESSON_ORDER["daily_conversation"]
        with patch.object(bot, "get_completed_lessons", return_value=[daily[0], daily[2]]):
            badges = bot.current_progress_badges(12345)
        self.assertEqual(badges, [], "Draft editorial progress must stay outside official badges")
        self.assertFalse(any("کۆرسی ٢: وتووێژ — وانەی 3" in badge for badge in badges))

    def test_lesson_editorial_review_notes_do_not_deactivate_courses(self):
        self.assertTrue(bot.course_is_active("daily_conversation"))
        self.assertTrue(bot.course_is_active("unified_orthography"))
        for lesson_id in (
            bot.COURSE_LESSON_ORDER["daily_conversation"][0],
            bot.COURSE_LESSON_ORDER["unified_orthography"][0],
        ):
            self.assertEqual(
                bot.LESSON_DATA[lesson_id]["review_status"],
                "draft_editorial_review",
            )

    def test_main_registers_startup_log_after_telegram_initialization(self):
        builder = Mock()
        application = Mock()
        builder.token.return_value = builder
        builder.post_init.return_value = builder
        builder.build.return_value = application
        with (
            patch.object(bot, "validate_activated_course_runtime"),
            patch.object(bot, "init_db"),
            patch.object(bot.Application, "builder", return_value=builder),
            patch.dict("os.environ", {"TELEGRAM_BOT_TOKEN": "safe-test-token"}),
        ):
            bot.main()

        callback = builder.post_init.call_args.args[0]
        self.assertTrue(asyncio.iscoroutinefunction(callback))
        with patch.object(bot.logger, "info") as log_info:
            asyncio.run(callback(application))
        log_info.assert_called_once_with(
            "KejyarBot Telegram initialization succeeded; polling is starting"
        )
        application.run_polling.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()


class Course4TelegramPresentationReadinessTests(unittest.IsolatedAsyncioTestCase):
    def test_course4_catalog_is_paginated_and_all_50_callbacks_are_reachable(self):
        expected = [f"grammar_{number:02d}" for number in range(1, 51)]
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], expected)
        with (
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "get_completed_beta_lessons", return_value=[]),
        ):
            pages = [
                bot.course_menu_keyboard("grammar", 12345, page)
                for page in range(5)
            ]
        for _, page_count in pages:
            self.assertEqual(page_count, 5)
        page_ids = [
            [button.callback_data for row in keyboard.inline_keyboard for button in row
             if button.callback_data.startswith("open_lesson_")]
            for keyboard, _ in pages
        ]
        for page, ids in enumerate(page_ids):
            self.assertEqual(ids, [f"open_lesson_{item}" for item in expected[page * 12:(page + 1) * 12]])
        self.assertEqual(pages[1][0].inline_keyboard[-1][0].callback_data, "coursepage:grammar:0")
        self.assertEqual(pages[2][0].inline_keyboard[-1][0].callback_data, "coursepage:grammar:1")
        self.assertEqual(pages[3][0].inline_keyboard[-1][0].callback_data, "coursepage:grammar:2")
        self.assertEqual(pages[4][0].inline_keyboard[-1][0].callback_data, "coursepage:grammar:3")

    async def test_every_course4_lesson_renders_as_telegram_safe_branded_chunks(self):
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["grammar"]), 50)
        for lesson_id in bot.COURSE_LESSON_ORDER["grammar"]:
            with self.subTest(lesson=lesson_id):
                lesson = bot.LESSON_DATA[lesson_id]
                message = SimpleNamespace(reply_text=AsyncMock())
                markup = bot.lesson_keyboard(lesson_id)
                await bot.send_lesson_text(message, lesson["content"], markup)
                self.assertGreater(message.reply_text.await_count, 0)
                chunks = [call.args[0] for call in message.reply_text.await_args_list]
                self.assertTrue(all(len(chunk) <= 3500 for chunk in chunks))
                rendered = "\\n".join(chunks)
                self.assertIn(lesson["title"], rendered)
                self.assertIn("کەژیار — KejyarBot@", rendered)
                self.assertTrue(all(call.kwargs.get("parse_mode") == "HTML" for call in message.reply_text.await_args_list))
                self.assertEqual(message.reply_text.await_args_list[-1].kwargs.get("reply_markup"), markup)
                for call in message.reply_text.await_args_list[:-1]:
                    self.assertIsNone(call.kwargs.get("reply_markup"))

    def test_course4_assessments_are_loaded_and_use_standard_quiz_flow(self):
        for lesson_id in bot.COURSE_LESSON_ORDER["grammar"][:31]:
            with self.subTest(lesson=lesson_id):
                self.assertEqual(len(bot.QUIZ_DATA[lesson_id]), 8)
                self.assertTrue(bot.quiz_is_available(lesson_id))
                self.assertFalse(bot.quiz_requires_submission(lesson_id))
                for question in bot.QUIZ_DATA[lesson_id]:
                    self.assertTrue(question["question"].strip())
                    self.assertTrue(question["explanation"].strip())
                    self.assertIn(question["answer"], question["options"])
        for lesson_id in bot.COURSE_LESSON_ORDER["grammar"][31:]:
            with self.subTest(review_lesson=lesson_id):
                self.assertEqual(bot.QUIZ_DATA[lesson_id], [])
                self.assertTrue(bot.LESSON_DATA[lesson_id]["review_status"].startswith("owner_review_pending"))
                self.assertTrue(bot.LESSON_DATA[lesson_id]["content"].strip())


class Course4Lesson18VoiceTests(unittest.TestCase):
    def test_active_passive_lesson_is_complete_and_source_qualified(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_18")
        self.assertEqual(lesson["number"], 18)
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["key_points"]), 8)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertNotIn("Active and Passive", " ".join(lesson["appendix"]))
        self.assertIn("هیچ کتێب یان فایلێکی دەرەکی", " ".join(lesson["appendix"]))
        self.assertNotIn("١١٢–١٢٤", " ".join(lesson["appendix"]))
        self.assertIn("بابەتێکی جیاوازە", " ".join(lesson["appendix"]))
