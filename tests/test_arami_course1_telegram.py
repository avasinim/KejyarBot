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
    def test_manifest_has_exactly_21_numbered_lessons(self):
        manifest = load_manifest(ROOT)
        self.assertEqual(len(manifest["lessons"]), 21)
        self.assertEqual(
            [item["number"] for item in sorted(manifest["lessons"], key=lambda item: item["number"])],
            list(range(1, 22)),
        )

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

    def test_source_question_banks_match_their_own_lessons_and_preserve_source_counts(self):
        banks = load_question_banks(ROOT)
        self.assertEqual(set(banks), {2, 3, 4, 6, 7, 8, 9, 10, 13})
        self.assertEqual({number: len(bank["practice"]) for number, bank in banks.items()}, {2: 4, 3: 4, 4: 5, 6: 5, 7: 4, 8: 8, 9: 5, 10: 5, 13: 5})
        for number, bank in banks.items():
            self.assertEqual(len(bank["practice"]), len(bank["assessment"]))
            self.assertTrue(all(item["source_evidence"] for item in bank["practice"] + bank["assessment"]))

    def test_menu_exposes_practice_and_assessment_only_for_verified_question_banks(self):
        banks = load_question_banks(ROOT)
        keyboard = course_menu_keyboard(load_manifest(ROOT), banks)
        callbacks = [button.callback_data for row in keyboard.inline_keyboard for button in row]
        self.assertEqual(len([item for item in callbacks if item.endswith(":lesson") or item.startswith("aramiC:lesson:")]), 21)
        self.assertEqual(len([item for item in callbacks if item.startswith("aramiC:practice:")]), 9)
        self.assertEqual(len([item for item in callbacks if item.startswith("aramiC:assessment:")]), 9)
        self.assertNotIn("aramiC:practice:15", callbacks)
        self.assertIn("arami1:practice", callbacks)
        self.assertIn("arami1:assessment", callbacks)
        self.assertIn("arami5:practice", callbacks)
        self.assertIn("arami5:assessment", callbacks)

    def test_every_registered_source_is_read_from_its_manifest_path(self):
        manifest = load_manifest(ROOT)
        for lesson in manifest["lessons"]:
            if lesson["number"] == 15:
                continue
            with self.subTest(lesson=lesson["number"]):
                loaded, source = load_lesson_source(ROOT, lesson["number"])
                self.assertEqual(loaded["id"], lesson["id"])
                self.assertTrue(source.strip())

    def test_missing_lesson_15_source_is_never_replaced_with_another_lesson(self):
        with self.assertRaises(AramiCourseTelegramError):
            load_lesson_source(ROOT, 15)

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
            data=f"aramiC:{action}", message=message, answer=AsyncMock(),
            edit_message_reply_markup=AsyncMock(), edit_message_text=AsyncMock(),
        )
        return SimpleNamespace(callback_query=query), query

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
