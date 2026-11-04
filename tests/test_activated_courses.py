"""Regression tests for owner-activated Courses 2 and 3."""
import asyncio
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

import bot


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
        self.assertFalse(bot.course_is_active("grammar"))
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["daily_conversation"]), 48)
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
        reads = [button for button in buttons if button.callback_data.endswith(":lesson") or button.callback_data.startswith("aramiC:lesson:")]
        practices = [button for button in buttons if ":practice" in button.callback_data]
        assessments = [button for button in buttons if ":assessment" in button.callback_data]
        self.assertEqual(len(reads), 21)
        self.assertEqual(len(practices), 21)
        self.assertEqual(len(assessments), 21)
        self.assertIn("arami1:practice", [button.callback_data for button in practices])
        self.assertIn("arami5:practice", [button.callback_data for button in practices])

    def test_arami_assessment_reward_uses_unique_lesson_key_and_twenty_xp(self):
        with patch.object(bot, "complete_quiz_with_rewards", side_effect=[True, False]) as reward:
            self.assertTrue(bot.award_arami_assessment(12345, "arami_course1_lesson_01"))
            self.assertFalse(bot.award_arami_assessment(12345, "arami_course1_lesson_01"))
        self.assertEqual(reward.call_count, 2)
        self.assertEqual(reward.call_args_list[0].args, (12345, "arami_assessment:arami_course1_lesson_01"))
        self.assertEqual(reward.call_args_list[0].kwargs, {"points": 20})

    def test_startup_validation_confirms_both_activated_courses_are_complete(self):
        bot.validate_activated_course_runtime()

    def test_course_lesson_ids_are_unique_and_do_not_replace_course_one_ids(self):
        self.assertEqual(len(bot.COURSE_LESSON_ORDER["orthography_basic"]), 0)
        all_ids = [
            lesson
            for course_id in ("daily_conversation", "unified_orthography")
            for lesson in bot.COURSE_LESSON_ORDER[course_id]
        ]
        self.assertEqual(len(all_ids), 114)
        self.assertEqual(len(set(all_ids)), 114)
        self.assertEqual(bot.COURSE_LESSON_ORDER["orthography_basic"], [])

    def test_arami_course_progression_uses_all_21_manifest_lesson_ids(self):
        order = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"]
        self.assertEqual(len(order), 21)
        self.assertEqual(order[0], "arami_course1_lesson_01")
        self.assertEqual(order[-1], "arami_course1_lesson_21")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertTrue(bot.can_open(12345, order[0]))
            self.assertFalse(bot.can_open(12345, order[1]))
        with patch.object(bot, "get_completed_lessons", return_value=[order[0]]):
            self.assertTrue(bot.can_open(12345, order[1]))
            self.assertFalse(bot.can_open(12345, order[2]))

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
            patch.object(bot, "complete_lesson_with_rewards", return_value=True) as complete,
            patch.object(bot, "get_user_level", side_effect=[1, 1]),
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

    async def test_finishing_arami_course_final_lesson_shows_course_completion(self):
        lesson_id = bot.COURSE_LESSON_ORDER["arami_orthography_foundations"][-1]
        update, message, query = self.make_update(f"finish_{lesson_id}")
        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "complete_lesson_with_rewards", return_value=True) as complete,
            patch.object(bot, "get_user_level", side_effect=[1, 1]),
            patch.object(bot, "check_badges"),
            patch.dict(bot.QUIZ_DATA, {lesson_id: []}),
        ):
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        complete.assert_called_once_with(12345, lesson_id)
        message.reply_text.assert_awaited_once()
        self.assertIn("کۆرسی ١ تەواو بوو", message.reply_text.await_args.args[0])
        self.assertNotIn("وانەی دواتر ئامادەیە", message.reply_text.await_args.args[0])
        keyboard = message.reply_text.await_args.kwargs["reply_markup"]
        self.assertEqual(
            keyboard.inline_keyboard[0][0].callback_data,
            "aramiC:assessment:21",
        )

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
            patch.object(bot, "complete_lesson_with_rewards", return_value=False) as complete,
            patch.object(bot, "get_user_level", return_value=1),
            patch.object(bot, "check_badges") as badges,
        ):
            await bot.finish_lesson(update, SimpleNamespace(user_data={}))

        complete.assert_called_once_with(12345, lesson_id)
        badges.assert_not_called()
        message.reply_text.assert_awaited_once()
        self.assertIn("پێشتر تەواو کراوە", message.reply_text.await_args.args[0])

    async def test_open_course_two_shows_all_48_lesson_buttons(self):
        update, message, query = self.make_update("course_daily_conversation")
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            await bot.open_course(update, SimpleNamespace())
        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 13)
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
        self.assertEqual(len(keyboard), 13)
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
        self.assertIn("وانەکانی 13–24 لە کۆی 48 — لاپەڕەی 2/4", rendered)
        keyboard = message.edit_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(len(keyboard), 13)
        self.assertEqual(
            keyboard[0][0].callback_data,
            "open_lesson_daily_conversation_13",
        )
        self.assertEqual(keyboard[-1][0].callback_data, "coursepage:daily_conversation:0")

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
        keyboard = message.reply_text.await_args.kwargs["reply_markup"].inline_keyboard
        self.assertEqual(keyboard[0][0].callback_data, "quiz_lesson_12_start")
        self.assertEqual(keyboard[-1][0].callback_data, "quizmenu:assessment:0")

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

        self.assertEqual(len(badges), 2)
        self.assertIn("کۆرسی ١: ڕێنووسی سەرەتاییی کوردی — وانەی 1", badges[0])
        self.assertIn("کۆرسی ٢: وتووێژ — وانەی 1", badges[1])
        self.assertFalse(any("کۆرسی ٣" in badge for badge in badges))
        self.assertFalse(any("Diyako" in badge for badge in badges))

    def test_progress_badges_hide_stale_later_completions(self):
        daily = bot.COURSE_LESSON_ORDER["daily_conversation"]
        with patch.object(bot, "get_completed_lessons", return_value=[daily[0], daily[2]]):
            badges = bot.current_progress_badges(12345)
        self.assertEqual(
            badges.count("🏅 کۆرسی ٢: وتووێژ — وانەی 1"),
            1,
        )
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
