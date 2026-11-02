import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

from arami_course1_telegram import (
    AramiCourseTelegramError,
    _plain_markdown,
    course_menu_keyboard,
    load_lesson_source,
    load_manifest,
    load_question_banks,
)


ROOT = Path(__file__).resolve().parents[1]


class AramiCourseTelegramTests(unittest.TestCase):
    def test_manifest_has_exactly_20_numbered_lessons(self):
        manifest = load_manifest(ROOT)
        self.assertEqual(len(manifest["lessons"]), 20)
        self.assertEqual(
            [item["number"] for item in sorted(manifest["lessons"], key=lambda item: item["number"])],
            list(range(1, 21)),
        )

    def test_course_menu_exposes_all_20_lessons(self):
        keyboard = course_menu_keyboard(load_manifest(ROOT))
        buttons = [button for row in keyboard.inline_keyboard for button in row]
        callbacks = {button.callback_data for button in buttons}
        read_callbacks = {item for item in callbacks if item.endswith(":lesson") or item.startswith("aramiC:lesson:")}
        self.assertEqual(len(read_callbacks), 20)
        self.assertEqual(
            read_callbacks,
            {("arami1:lesson" if number == 1 else ("arami5:lesson" if number == 5 else f"aramiC:lesson:{number}")) for number in range(1, 21)},
        )

    def test_source_question_banks_match_their_own_lessons_and_preserve_source_counts(self):
        banks = load_question_banks(ROOT)
        self.assertEqual(set(banks), {2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20})
        self.assertEqual({number: len(bank["practice"]) for number, bank in banks.items()}, {2: 4, 3: 4, 4: 5, 6: 5, 7: 4, 8: 8, 9: 5, 10: 5, 11: 5, 12: 4, 13: 4, 14: 5, 15: 4, 16: 3, 17: 4, 18: 4, 19: 4, 20: 4})
        seen_ids = set()
        for number, bank in banks.items():
            self.assertEqual(len(bank["practice"]), len(bank["assessment"]))
            self.assertTrue(all(item["source_evidence"] for item in bank["practice"] + bank["assessment"]))
            for mode in ("practice", "assessment"):
                prefix = "p" if mode == "practice" else "a"
                for index, item in enumerate(bank[mode], start=1):
                    self.assertEqual(item["id"], f"{number}{prefix}{index}")
                    self.assertEqual(item["section_id"], f"lesson{number}_source_exercises")
                    self.assertNotIn(item["id"], seen_ids)
                    seen_ids.add(item["id"])

    def test_menu_exposes_practice_and_assessment_only_for_verified_question_banks(self):
        banks = load_question_banks(ROOT)
        keyboard = course_menu_keyboard(load_manifest(ROOT), banks)
        callbacks = [button.callback_data for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len([item for item in callbacks if item.endswith(":lesson") or item.startswith("aramiC:lesson:")]), 20)
        self.assertEqual(len([item for item in callbacks if item.startswith("aramiC:practice:")]), 18)
        self.assertEqual(len([item for item in callbacks if item.startswith("aramiC:assessment:")]), 18)
        self.assertIn("aramiC:practice:11", callbacks)
        self.assertIn("aramiC:practice:14", callbacks)
        self.assertIn("aramiC:practice:20", callbacks)
        self.assertIn("aramiC:assessment:20", callbacks)
        self.assertIn("aramiC:assessment:11", callbacks)
        self.assertIn("aramiC:assessment:14", callbacks)
        self.assertIn("aramiC:practice:15", callbacks)
        self.assertIn("aramiC:assessment:15", callbacks)
        self.assertIn("arami1:practice", callbacks)
        self.assertIn("arami1:assessment", callbacks)
        self.assertIn("arami5:practice", callbacks)
        self.assertIn("arami5:assessment", callbacks)

    def test_manifest_maps_audio_to_the_correct_lesson_sources(self):
        manifest = load_manifest(ROOT)
        lessons = {item["number"]: item for item in manifest["lessons"]}
        self.assertEqual(lessons[13]["content_file"], "course_data/arami_course1_lesson_13_w_source.md")
        self.assertEqual(lessons[14]["content_file"], "course_data/arami_course1_lesson_14_bizroke_hishu_source.md")
        self.assertEqual(lessons[15]["content_file"], "course_data/arami_course1_lesson_15_l_ll_source.md")
        self.assertEqual(lessons[16]["content_file"], "course_data/arami_course1_lesson_16_v_source.md")
        self.assertEqual([item["file"] for item in lessons[14]["audio_files"]], ["بزرۆکە.ogg", "بزرۆکەی ٢.ogg", "بزرۆکەی ٣.ogg"])
        self.assertEqual([item["file"] for item in lessons[15]["audio_files"]], ["دەنگی ل.ogg", "دەنگی ڵ.ogg"])
        self.assertEqual([item["file"] for item in lessons[16]["audio_files"]], ["دەنگ ڤ.ogg"])
        self.assertEqual([item["file"] for item in lessons[20]["audio_files"]], ["بڕگە.ogg"])
        self.assertEqual([item["file"] for item in lessons[1]["audio_files"]], ["بزوێنی ی.ogg"])
        self.assertEqual(lessons[12]["content_file"], "course_data/arami_course1_lesson_11_y_source.md")
        self.assertEqual([item["file"] for item in lessons[12]["audio_files"]], ["ی.ogg", "پیتی دەنگی ٢.ogg"])
        self.assertEqual(len(lessons[11]["audio_files"]), 4)
        self.assertEqual(len(lessons[13]["audio_files"]), 2)

    def test_lesson14_preserves_the_supplied_hidden_vowel_examples_and_audio(self):
        manifest = load_manifest(ROOT)
        lesson = next(item for item in manifest["lessons"] if item["number"] == 14)
        _, source = load_lesson_source(ROOT, 14)
        for example in ("min", "çil", "dill", "mirdim", "xistin", "kirdin", "birdin"):
            self.assertIn(example, source)
        self.assertIn("I i", source)
        self.assertIn("6639c30ca85bdae4f64134e1368617b2e507fb6c", lesson["audio_commits"])
        self.assertIn("بزرۆکە.ogg", [item["file"] for item in lesson["audio_files"]])
        self.assertNotIn("6639c30ca85bdae4f64134e1368617b2e507fb6c", source)

    def test_every_manifest_audio_file_exists_and_stays_inside_project(self):
        from arami_course1_telegram import load_lesson_audio_files
        manifest = load_manifest(ROOT)
        for lesson in manifest["lessons"]:
            with self.subTest(lesson=lesson["number"]):
                assets = load_lesson_audio_files(ROOT, lesson)
                for path, label in assets:
                    self.assertTrue(path.is_file())
                    self.assertTrue(label)

    async def test_lesson_audio_delivery_sends_each_mapped_recording(self):
        from arami_course1_telegram import send_lesson_audio
        message = SimpleNamespace(reply_voice=AsyncMock(), reply_text=AsyncMock())
        lesson14 = next(item for item in load_manifest(ROOT)["lessons"] if item["number"] == 14)
        sent = await send_lesson_audio(message, ROOT, lesson14)
        self.assertTrue(sent)
        self.assertEqual(message.reply_voice.await_count, 3)
        message.reply_text.assert_not_awaited()

    def test_a_recording_is_never_reused_across_different_lessons(self):
        manifest = load_manifest(ROOT)
        owners = {}
        for lesson in manifest["lessons"]:
            for asset in lesson.get("audio_files", []):
                filename = asset["file"]
                self.assertNotIn(filename, owners, f"{filename} reused by Lessons {owners.get(filename)} and {lesson['number']}")
                owners[filename] = lesson["number"]

    def test_every_registered_source_is_read_from_its_manifest_path(self):
        manifest = load_manifest(ROOT)
        for lesson in manifest["lessons"]:
            with self.subTest(lesson=lesson["number"]):
                loaded, source = load_lesson_source(ROOT, lesson["number"])
                self.assertEqual(loaded["id"], lesson["id"])
                self.assertTrue(source.strip())

    def test_final_lesson_20_source_is_loaded_from_its_own_manifest_path(self):
        lesson, source = load_lesson_source(ROOT, 20)
        self.assertEqual(lesson["id"], "arami_course1_lesson_20")
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
        for value in (0, 21, True, "5"):
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
            data=f"aramiC:{action}", message=message, answer=AsyncMock(),
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
        self.assertIn("وەڵامەکەت تۆمار کرا", assessment_query.edit_message_text.await_args.args[0])
        self.assertNotIn("وەڵامی ڕاست:", assessment_query.edit_message_text.await_args.args[0])


if __name__ == "__main__":
    unittest.main()
