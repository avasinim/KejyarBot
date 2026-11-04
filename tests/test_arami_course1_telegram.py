import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

from arami_course1_telegram import (
    AramiCourseTelegramError,
    _plain_markdown,
    _render_source_html,
    _send_source,
    lesson_infographic_path,
    send_lesson_infographic,
    callback as arami_course1_callback,
    build_lesson_infographic_svg,
    _split_source_html,
    course_menu_keyboard,
    load_lesson_source,
    load_manifest,
    load_question_banks,
)


ROOT = Path(__file__).resolve().parents[1]


class AramiCourseTelegramTests(unittest.IsolatedAsyncioTestCase):
    async def test_only_the_six_approved_course1_lessons_send_png_infographics(self):
        message = SimpleNamespace(reply_photo=AsyncMock())
        approved = (1, 2, 3, 4, 6, 7)
        for number in approved:
            path = lesson_infographic_path(ROOT, {"number": number})
            self.assertIsNotNone(path, f"Missing infographic for lesson {number}")
            self.assertTrue(path.is_file())
            self.assertTrue(await send_lesson_infographic(
                message, {"number": number}, base_dir=ROOT
            ))
        self.assertIsNone(lesson_infographic_path(ROOT, {"number": 5}))
        self.assertFalse(await send_lesson_infographic(
            message, {"number": 5}, base_dir=ROOT
        ))
        self.assertEqual(message.reply_photo.await_count, 6)
        self.assertFalse((ROOT / "assets" / "course1_infographics" / "lesson_05.png").exists())

    async def test_missing_course1_infographic_does_not_interrupt_lesson_delivery(self):
        with tempfile.TemporaryDirectory() as temporary:
            message = SimpleNamespace(reply_photo=AsyncMock())
            sent = await send_lesson_infographic(
                message, {"number": 1}, base_dir=temporary
            )
        self.assertFalse(sent)
        message.reply_photo.assert_not_awaited()

    def test_infographic_uses_the_current_course_title(self):
        svg = build_lesson_infographic_svg(
            {"number": 1, "title": "پیتەکان و دەنگەکان"},
            "# وانەی ١\n## پیتەکان\n## دەنگەکان",
        ).decode("utf-8")
        self.assertIn("ڕێنووسی سەرەتاییی کوردی", svg)
        self.assertNotIn("ڕێنووسی ئارامی", svg)

    def test_course1_source_formatter_styles_headings_and_plain_pipe_tables(self):
        blocks = _render_source_html(
            "# پیتەکان و دەنگەکان\n"
            "ئامانجەکانی فێربوون\n"
            "ژمارە | پیت/نیشانە | ناو\n"
            "١ | ا | ئەلف\n"
            "٢ | ب | بێ"
        )
        rendered = "\n".join(blocks)
        self.assertIn("<b>📘 پیتەکان و دەنگەکان</b>", rendered)
        self.assertIn("<b>🎯 ئامانجەکانی فێربوون</b>", rendered)
        self.assertIn("<b>ژمارە</b>: ١", rendered)
        self.assertIn("<b>پیت/نیشانە</b>: ا", rendered)
        self.assertIn("<b>ناو</b>: ئەلف", rendered)
        self.assertIn("<b>ژمارە</b>: ٢", rendered)


    def test_reader_uses_a_three_level_classroom_heading_hierarchy(self):
        rendered = "\n".join(_render_source_html(
            "# ناونیشانی وانە\n"
            "## بەشی یەکەم\n"
            "### خاڵی ورد\n"
            "دەقی ڕەسەن"
        ))
        self.assertIn("<b>📘 ناونیشانی وانە</b>", rendered)
        self.assertIn("━━━━━━━━━━━━━━━━━━\n<b>🎓 بەشی یەکەم</b>\n━━━━━━━━━━━━━━━━━━", rendered)
        self.assertIn("<b>▪️ خاڵی ورد</b>", rendered)
        self.assertIn("دەقی ڕەسەن", rendered)


    def test_classroom_callouts_and_sections_have_distinct_visual_treatment(self):
        rendered = "\n".join(_render_source_html(
            "ئامانجەکانی فێربوون\n"
            "١. جیاوازیی پیت و دەنگ\n"
            "نموونە: پیت نیشانەیەکی نووسراوە.\n"
            "تێبینی: ئەم جیاوازییە گرنگە."
        ))
        self.assertIn("<b>🎯 ئامانجەکانی فێربوون</b>", rendered)
        self.assertIn("<b>🔹 ١. جیاوازیی پیت و دەنگ</b>", rendered)
        self.assertIn("<blockquote><b>🧩 نموونە</b>\nپیت نیشانەیەکی نووسراوە.</blockquote>", rendered)
        self.assertIn("<blockquote><b>💡 تێبینی</b>\nئەم جیاوازییە گرنگە.</blockquote>", rendered)

    def test_source_chunks_count_the_actual_blank_line_separator(self):
        blocks = [f"بلاک {index} " + ("دەق " * 12) for index in range(300)]
        chunks = _split_source_html(blocks, limit=3500)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk) <= 3500 for chunk in chunks))
        self.assertEqual(
            [part for chunk in chunks for part in chunk.split("\n\n")],
            blocks,
        )

    def test_all_shared_reader_lessons_render_into_telegram_safe_classroom_chunks(self):
        manifest = load_manifest(ROOT)
        for lesson in manifest["lessons"]:
            if lesson["number"] in {1, 5}:
                continue  # Dedicated structured readers use the same shared renderer.
            _, source = load_lesson_source(ROOT, lesson["number"])
            blocks = _render_source_html(source)
            self.assertTrue(blocks, f"Lesson {lesson['number']} rendered no content")
            chunks = _split_source_html(["<b>📘 وانە</b>", *blocks])
            self.assertTrue(
                all(len(chunk) <= 3500 for chunk in chunks),
                f"Lesson {lesson['number']} exceeds the safe Telegram chunk size",
            )

    def test_course1_source_is_sent_as_formatted_html(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        asyncio.run(_send_source(
            message,
            "وانەی ١ — پیت و دەنگ",
            "# پیت و دەنگ\nئامانجەکانی فێربوون\nئەمە دەقی وانەیە."
        ))
        message.reply_text.assert_awaited_once()
        args, kwargs = message.reply_text.await_args
        self.assertIn("<b>📘 وانەی ١ — پیت و دەنگ</b>", args[0])
        self.assertIn("<code>کەژیار — KejyarBot@</code>", args[0])
        self.assertEqual(kwargs.get("parse_mode"), "HTML")
        self.assertIn("<b>🎯 ئامانجەکانی فێربوون</b>", args[0])

    async def test_returning_to_course_menu_preserves_completed_open_and_locked_states(self):
        manifest = load_manifest(ROOT)
        first_id = manifest["lessons"][0]["id"]
        second_id = manifest["lessons"][1]["id"]
        message = SimpleNamespace(reply_text=AsyncMock())
        query = SimpleNamespace(
            data="aramiC:menu",
            from_user=SimpleNamespace(id=24680),
            message=message,
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        can_open = Mock(side_effect=lambda user_id, lesson_id: lesson_id in {first_id, second_id})
        get_completed = Mock(return_value=[first_id])

        await arami_course1_callback(
            update,
            SimpleNamespace(user_data={}),
            ROOT,
            can_open=can_open,
            get_completed_lessons=get_completed,
        )

        get_completed.assert_called_once_with(24680)
        self.assertTrue(all(call.args[0] == 24680 for call in can_open.call_args_list))
        keyboard = message.reply_text.await_args.kwargs["reply_markup"]
        buttons = {
            button.callback_data: button
            for row in keyboard.inline_keyboard
            for button in row
        }
        self.assertTrue(buttons["arami1:lesson"].text.startswith("✅"))
        self.assertTrue(buttons["aramiC:lesson:2"].text.startswith("🔓"))
        self.assertTrue(buttons["aramiC:lesson:3"].text.startswith("🔒"))
        self.assertIn("aramiC:practice:2", buttons)
        self.assertIn("aramiC:assessment:2", buttons)
        self.assertNotIn("aramiC:practice:3", buttons)
        self.assertNotIn("aramiC:assessment:3", buttons)

    async def test_returning_from_lesson_reader_keeps_the_users_progress_states(self):
        manifest = load_manifest(ROOT)
        first_id = manifest["lessons"][0]["id"]
        second_id = manifest["lessons"][1]["id"]
        message = SimpleNamespace(
            message_id=10,
            reply_text=AsyncMock(return_value=SimpleNamespace(message_id=11)),
            reply_voice=AsyncMock(),
        )
        query = SimpleNamespace(
            data="aramiC:lesson:2",
            from_user=SimpleNamespace(id=24680),
            message=message,
            answer=AsyncMock(),
        )
        update = SimpleNamespace(callback_query=query)
        can_open = Mock(side_effect=lambda user_id, lesson_id: lesson_id in {first_id, second_id})
        get_completed = Mock(return_value=[first_id])

        await arami_course1_callback(
            update,
            SimpleNamespace(user_data={}),
            ROOT,
            can_open=can_open,
            get_completed_lessons=get_completed,
        )

        get_completed.assert_called_once_with(24680)
        menu_call = next(
            call for call in reversed(message.reply_text.await_args_list)
            if call.kwargs.get("reply_markup") is not None
            and any(
                button.callback_data == "aramiC:lesson:3"
                for row in call.kwargs["reply_markup"].inline_keyboard
                for button in row
            )
        )
        buttons = {
            button.callback_data: button
            for row in menu_call.kwargs["reply_markup"].inline_keyboard
            for button in row
        }
        self.assertTrue(buttons["arami1:lesson"].text.startswith("✅"))
        self.assertTrue(buttons["aramiC:lesson:2"].text.startswith("🔓"))
        self.assertTrue(buttons["aramiC:lesson:3"].text.startswith("🔒"))

    def test_manifest_has_exactly_21_numbered_lessons(self):
        manifest = load_manifest(ROOT)
        self.assertEqual(len(manifest["lessons"]), 21)
        self.assertEqual(manifest["course_total_lessons"], 21)
        self.assertEqual(manifest["course_size"], 21)
        self.assertEqual(
            [item["number"] for item in sorted(manifest["lessons"], key=lambda item: item["number"])],
            list(range(1, 22)),
        )

    def test_manifest_rejects_course_size_mismatch(self):
        manifest = json.loads((ROOT / "course_data" / "arami_course1_manifest.json").read_text(encoding="utf-8"))
        manifest["course_size"] = 20
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "course_data").mkdir()
            (root / "course_data" / "arami_course1_manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
            )
            with self.assertRaises(AramiCourseTelegramError):
                load_manifest(root)

    def test_course_menu_exposes_all_21_lessons(self):
        keyboard = course_menu_keyboard(load_manifest(ROOT))
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        callbacks = {button.callback_data for button in buttons}
        read_callbacks = {item for item in callbacks if item.endswith(":lesson") or item.startswith("aramiC:lesson:")}
        self.assertEqual(len(read_callbacks), 21)
        self.assertEqual(
            read_callbacks,
            {("arami1:lesson" if number == 1 else ("arami5:lesson" if number == 5 else f"aramiC:lesson:{number}")) for number in range(1, 22)},
        )

    def test_course_menu_displays_completed_available_and_locked_states(self):
        manifest = load_manifest(ROOT)
        first_id = manifest["lessons"][0]["id"]
        second_id = manifest["lessons"][1]["id"]
        keyboard = course_menu_keyboard(
            manifest,
            completed_lessons={first_id},
            can_open=lambda lesson_id: lesson_id in {first_id, second_id},
        )
        buttons = {
            button.callback_data: button
            for row in keyboard.inline_keyboard
            for button in row
        }
        self.assertTrue(buttons["arami1:lesson"].text.startswith("✅"))
        self.assertTrue(buttons["aramiC:lesson:2"].text.startswith("🔓"))
        self.assertTrue(buttons["aramiC:lesson:3"].text.startswith("🔒"))

    def test_course_menu_marks_all_lessons_available_without_progress_guard(self):
        keyboard = course_menu_keyboard(load_manifest(ROOT))
        buttons = [row[0] for row in keyboard.inline_keyboard]
        self.assertEqual(len(buttons), 21)
        self.assertTrue(all(button.text.startswith("🔓") for button in buttons))

    def test_source_question_banks_match_their_own_lessons_and_preserve_source_counts(self):
        banks = load_question_banks(ROOT)
        self.assertEqual(set(banks), {2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21})
        self.assertEqual({number: len(bank["practice"]) for number, bank in banks.items()}, {2: 4, 3: 4, 4: 5, 6: 5, 7: 4, 8: 8, 9: 5, 10: 5, 11: 5, 12: 5, 13: 4, 14: 5, 15: 10, 16: 6, 17: 3, 18: 4, 19: 4, 20: 4, 21: 4})
        seen_ids = set()
        for number, bank in banks.items():
            self.assertEqual(len(bank["practice"]), len(bank["assessment"]))
            practice_prompts = [item["prompt"].strip().casefold() for item in bank["practice"]]
            assessment_prompts = [item["prompt"].strip().casefold() for item in bank["assessment"]]
            self.assertEqual(len(practice_prompts), len(set(practice_prompts)))
            self.assertEqual(len(assessment_prompts), len(set(assessment_prompts)))
            self.assertFalse(set(practice_prompts) & set(assessment_prompts))
            self.assertTrue(all(item["source_evidence"] for item in bank["practice"] + bank["assessment"]))
            for mode in ("practice", "assessment"):
                prefix = "p" if mode == "practice" else "a"
                for index, item in enumerate(bank[mode], start=1):
                    self.assertEqual(item["id"], f"{number}{prefix}{index}")
                    self.assertTrue(item["section_id"].startswith(f"lesson{number}_"))
                    self.assertNotIn(item["id"], seen_ids)
                    seen_ids.add(item["id"])

    def test_menu_exposes_practice_and_assessment_only_for_verified_question_banks(self):
        banks = load_question_banks(ROOT)
        keyboard = course_menu_keyboard(load_manifest(ROOT), banks)
        callbacks = [button.callback_data for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len([item for item in callbacks if item.endswith(":lesson") or item.startswith("aramiC:lesson:")]), 21)
        self.assertEqual(len([item for item in callbacks if item.startswith("aramiC:practice:")]), 19)
        self.assertEqual(len([item for item in callbacks if item.startswith("aramiC:assessment:")]), 19)
        self.assertIn("aramiC:practice:11", callbacks)
        self.assertIn("aramiC:practice:14", callbacks)
        self.assertIn("aramiC:practice:21", callbacks)
        self.assertIn("aramiC:assessment:21", callbacks)
        self.assertIn("aramiC:assessment:11", callbacks)
        self.assertIn("aramiC:assessment:14", callbacks)
        self.assertIn("aramiC:practice:15", callbacks)
        self.assertIn("aramiC:assessment:15", callbacks)
        self.assertIn("arami1:practice", callbacks)
        self.assertIn("arami1:assessment", callbacks)
        self.assertIn("arami5:practice", callbacks)
        self.assertIn("arami5:assessment", callbacks)

    def test_all_21_lessons_are_enabled_as_text_only_readers(self):
        manifest = load_manifest(ROOT)
        self.assertEqual(len(manifest["lessons"]), 21)
        for lesson in manifest["lessons"]:
            self.assertEqual(lesson["runtime_status"], "enabled_in_arami_course1_catalogue")
            self.assertIn("reader_practice_assessment", lesson["activation_status"])
            self.assertFalse(any("audio" in key.lower() for key in lesson))

    def test_lesson_infographic_is_valid_source_grounded_kurdish_svg(self):
        from arami_course1_telegram import build_lesson_infographic_svg
        lesson, source = load_lesson_source(ROOT, 15)
        svg = build_lesson_infographic_svg(lesson, source).decode("utf-8")
        self.assertIn("<svg", svg)
        self.assertIn("KejyarBot@", svg)
        self.assertIn("پیتی «ل» و «ڵ»", svg)
        self.assertIn("کەژیار", svg)
        self.assertIn("font-size", svg)



    def test_lesson16_source_preserves_the_user_supplied_r_rr_rules_and_examples(self):
        lesson, source = load_lesson_source(ROOT, 16)
        self.assertEqual(lesson["title"], "پیتی «ر» و «ڕ»")
        for example in ("ڕێگا", "ڕێبوار", "ڕامان", "پەڕۆ", "مەڕ", "دڕاو",
                        "دار", "دیوار", "دەرگە", "کورد", "بڕا", "برا",
                        "دڕاو", "دراو", "ئاور", "ئاوڕ", "بڕۆ", "برۆ",
                        "فڕیو", "فریو"):
            self.assertIn(example, source)

    def test_lesson16_r_and_rr_distinction_is_in_both_quiz_modes(self):
        banks = load_question_banks(ROOT)
        for mode in ("practice", "assessment"):
            questions = banks[16][mode]
            self.assertEqual(len(questions), 6)
            self.assertTrue(all("ڕ" in item["source_evidence"] or "ر" in item["source_evidence"] for item in questions))

    def test_lesson15_new_ll_and_l_contrasts_are_in_both_quiz_modes(self):
        banks = load_question_banks(ROOT)
        for mode in ("practice", "assessment"):
            questions = banks[15][mode]
            self.assertEqual(len(questions), 10)
            prompts = [item["prompt"] for item in questions]
            self.assertTrue(any("چڵ" in prompt for prompt in prompts))
            self.assertTrue(any("پەڵە" in prompt for prompt in prompts))
            self.assertTrue(all(item["source_evidence"] for item in questions))

    def test_manifest_keeps_course1_source_paths_without_audio_assignments(self):
        manifest = load_manifest(ROOT)
        lessons = {item["number"]: item for item in manifest["lessons"]}
        self.assertEqual(lessons[13]["content_file"], "course_data/arami_course1_lesson_13_w_source.md")
        self.assertEqual(lessons[14]["content_file"], "course_data/arami_course1_lesson_14_bizroke_hishu_source.md")
        self.assertEqual(lessons[15]["content_file"], "course_data/arami_course1_lesson_15_l_ll_source.md")
        self.assertEqual(lessons[16]["content_file"], "course_data/arami_course1_lesson_16_r_rr_source.md")
        self.assertEqual(lessons[17]["content_file"], "course_data/arami_course1_lesson_16_v_source.md")
        self.assertEqual(lessons[12]["content_file"], "course_data/arami_course1_lesson_12_y_source.md")
        self.assertTrue(all(not any("audio" in key.lower() for key in lesson) for lesson in lessons.values()))

    def test_lesson14_preserves_the_supplied_hidden_vowel_examples(self):
        _, source = load_lesson_source(ROOT, 14)
        for example in ("min", "çil", "dill", "mirdim", "xistin", "kirdin", "birdin"):
            self.assertIn(example, source)
        self.assertIn("I i", source)

    def test_every_registered_source_is_read_from_its_manifest_path(self):
        manifest = load_manifest(ROOT)
        for lesson in manifest["lessons"]:
            with self.subTest(lesson=lesson["number"]):
                loaded, source = load_lesson_source(ROOT, lesson["number"])
                self.assertEqual(loaded["id"], lesson["id"])
                self.assertTrue(source.strip())

    def test_final_lesson_21_source_is_loaded_from_its_own_manifest_path(self):
        lesson, source = load_lesson_source(ROOT, 21)
        self.assertEqual(lesson["id"], "arami_course1_lesson_21")
        self.assertIn("بڕگە و هێشوو", source)
        self.assertIn("## بڕگە (بخش، هجا) چییە؟", source)

    def test_markdown_renderer_preserves_words_and_table_values(self):
        rendered = _plain_markdown(
            "# سەردێڕ\n\n| پیت | هاوتا |\n|---|---|\n| چ | ç |\n"
        )
        self.assertIn("سەردێڕ", rendered)
        self.assertIn("چ • ç", rendered)
        self.assertNotIn("|---|", rendered)

    def test_invalid_lesson_numbers_are_rejected(self):
        for value in (0, 22, True, "5"):
            with self.subTest(value=value):
                with self.assertRaises(AramiCourseTelegramError):
                    load_lesson_source(ROOT, value)


class AramiCourseQuizCallbackTests(unittest.IsolatedAsyncioTestCase):
    def make_update(self, action, message_id=10):
        message = SimpleNamespace(
            message_id=message_id,
            reply_text=AsyncMock(return_value=SimpleNamespace(message_id=message_id + 1)),
        )
        query = SimpleNamespace(
            data=f"aramiC:{action}", message=message, from_user=SimpleNamespace(id=123), answer=AsyncMock(),
            edit_message_reply_markup=AsyncMock(), edit_message_text=AsyncMock(),
        )
        return SimpleNamespace(callback_query=query), query

    async def test_every_registered_lesson_bank_opens_its_own_practice_and_assessment(self):
        from arami_course1_telegram import callback
        banks = load_question_banks(ROOT)
        for number, bank in banks.items():
            for mode in ("practice", "assessment"):
                with self.subTest(lesson=number, mode=mode):
                    context = SimpleNamespace(user_data={})
                    update, _ = self.make_update(f"{mode}:{number}")
                    await callback(update, context, ROOT)
                    session = context.user_data["arami_course1_sessions"][str(number)]
                    self.assertEqual(session["mode"], mode)
                    self.assertEqual(len(session["questions"]), len(bank[mode]))
                    self.assertEqual(context.user_data["arami_course1_active"]["lesson"], number)

    async def test_assessment_completion_awards_once_for_its_lesson(self):
        from arami_course1_telegram import callback
        context = SimpleNamespace(user_data={})
        award = Mock(return_value=True)
        update, _ = self.make_update("assessment:6")
        await callback(update, context, ROOT, award_assessment=award)

        bank = load_question_banks(ROOT)[6]["assessment"]
        for index, question in enumerate(bank):
            message_id = context.user_data["arami_course1_active"]["message_id"]
            update, _ = self.make_update(f"pick:6:{question['answer_index']}", message_id)
            await callback(update, context, ROOT, award_assessment=award)
            update, submit_query = self.make_update(f"submit:6", message_id)
            await callback(update, context, ROOT, award_assessment=award)
            if index < len(bank) - 1:
                update, _ = self.make_update("next:6", message_id)
                await callback(update, context, ROOT, award_assessment=award)

        award.assert_called_once_with(123, "arami_course1_lesson_06")
        self.assertIn("+20 XP", submit_query.edit_message_text.await_args.args[0])

    async def test_lesson6_practice_and_assessment_use_separate_scoped_sessions(self):
        from arami_course1_telegram import callback
        context = SimpleNamespace(user_data={})
        update, _ = self.make_update("practice:6")
        await callback(update, context, ROOT)
        practice = context.user_data["arami_course1_sessions"]["6"]
        self.assertEqual(practice["mode"], "practice")
        question_id = context.user_data["arami_course1_active"]["message_id"]

        update, _ = self.make_update("pick:6:0", message_id=question_id)
        await callback(update, context, ROOT)
        update, submit_query = self.make_update("submit:6", message_id=question_id)
        await callback(update, context, ROOT)
        self.assertIn("وەڵامی ڕاست", submit_query.edit_message_text.await_args.args[0])

        update, _ = self.make_update("assessment:6")
        await callback(update, context, ROOT)
        assessment = context.user_data["arami_course1_sessions"]["6"]
        self.assertEqual(assessment["mode"], "assessment")
        self.assertIsNot(assessment, practice)

        assessment_message_id = context.user_data["arami_course1_active"]["message_id"]
        update, _ = self.make_update("pick:6:0", message_id=assessment_message_id)
        await callback(update, context, ROOT)
        update, assessment_query = self.make_update("submit:6", message_id=assessment_message_id)
        await callback(update, context, ROOT)
        self.assertIn("وەڵامەکەت وەرگیرا", assessment_query.edit_message_text.await_args.args[0])
        self.assertNotIn("وەڵامی ڕاست:", assessment_query.edit_message_text.await_args.args[0])


    async def test_reader_refuses_a_locked_lesson_when_progress_guard_is_supplied(self):
        from arami_course1_telegram import callback
        context = SimpleNamespace(user_data={})
        update, query = self.make_update("lesson:2")
        query.from_user = SimpleNamespace(id=123)
        await callback(update, context, ROOT, can_open=lambda user_id, lesson_id: False)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("سەرەتا وانەی پێشووتر", query.message.reply_text.await_args.args[0])
        self.assertEqual(query.message.reply_text.await_args.kwargs.get("reply_markup"), None)

    async def test_reader_offers_database_completion_callback_for_the_exact_lesson(self):
        from arami_course1_telegram import callback
        context = SimpleNamespace(user_data={})
        update, query = self.make_update("lesson:1")
        query.from_user = SimpleNamespace(id=123)
        query.message.reply_document = AsyncMock()
        query.message.reply_voice = AsyncMock()
        await callback(update, context, ROOT, can_open=lambda user_id, lesson_id: lesson_id == "arami_course1_lesson_01")
        self.assertEqual(query.message.reply_document.await_count, 0)
        self.assertEqual(query.message.reply_voice.await_count, 0)
        self.assertFalse(any("دەنگی وانەکە" in call.args[0] for call in query.message.reply_text.await_args_list))
        completion_messages = [
            call for call in query.message.reply_text.await_args_list
            if call.kwargs.get("reply_markup") is not None
            and any(
                button.callback_data == "finish_arami_course1_lesson_01"
                for row in call.kwargs["reply_markup"].inline_keyboard
                for button in row
            )
        ]
        self.assertEqual(len(completion_messages), 1)

    async def test_locked_lesson_practice_and_assessment_are_not_started(self):
        from arami_course1_telegram import callback
        for action in ("practice:2", "assessment:2"):
            update, query = self.make_update(action)
            query.from_user = SimpleNamespace(id=123)
            context = SimpleNamespace(user_data={})
            await callback(update, context, ROOT, can_open=lambda user_id, lesson_id: False)
            query.message.reply_text.assert_awaited_once()
            self.assertIn("ڕاهێنان و تاقیکردنەوە", query.message.reply_text.await_args.args[0])
            self.assertEqual(context.user_data, {})

if __name__ == "__main__":
    unittest.main()
