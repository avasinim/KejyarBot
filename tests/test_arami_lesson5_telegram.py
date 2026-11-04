import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from arami_lesson5_telegram import callback, menu_keyboard


def make_update(action, message_id=10):
    message = SimpleNamespace(
        message_id=message_id,
        reply_text=AsyncMock(return_value=SimpleNamespace(message_id=message_id + 1)),
        reply_voice=AsyncMock(),
    )
    query = SimpleNamespace(
        data=f"arami5:{action}",
        message=message,
        from_user=SimpleNamespace(id=123),
        answer=AsyncMock(),
        edit_message_reply_markup=AsyncMock(),
        edit_message_text=AsyncMock(),
    )
    return SimpleNamespace(callback_query=query), query


def sample_bank():
    return {
        "practice": [
            {
                "id": f"p{i}",
                "section_id": "lesson5_source_exercises",
                "type": "recognize",
                "prompt": f"پرسیاری ڕاهێنان {i}",
                "options": ["وەڵامی ڕاست", "وەڵامی هەڵە"],
                "answer_index": 0,
            }
            for i in range(1, 3)
        ],
        "assessment": [
            {
                "id": f"a{i}",
                "section_id": "lesson5_source_exercises",
                "type": "recognize",
                "prompt": f"پرسیاری تاقیکردنەوە {i}",
                "options": ["هەڵبژاردەی هەڵە", "هەڵبژاردەی ڕاست"],
                "answer_index": 1,
            }
            for i in range(1, 3)
        ],
    }


class AramiLesson5TelegramTests(unittest.IsolatedAsyncioTestCase):
    def test_menu_exposes_reading_practice_and_assessment(self):
        keyboard = menu_keyboard()
        callbacks = [
            button.callback_data
            for row in keyboard.inline_keyboard
            for button in row
        ]
        self.assertEqual(callbacks, [
            "arami5:lesson",
            "arami5:practice",
            "arami5:assessment",
            "aramiC:menu",
        ])

    async def test_lesson_callback_reads_its_own_source_and_returns_to_lesson5_menu(self):
        update, query = make_update("lesson")
        manifest = {"lessons": [{"number": 5, "id": "arami_course1_lesson_05"}]}
        with patch(
            "arami_lesson5_telegram.load_arami_lesson5_source",
            return_value="# وانەی ٥\n\nدەقی سەرچاوەی وانەی پێنج.",
        ), patch("arami_lesson5_telegram.load_manifest", return_value=manifest):
            await callback(update, SimpleNamespace(user_data={}), "/unused")
        query.message.reply_voice.assert_not_awaited()
        self.assertGreaterEqual(query.message.reply_text.await_count, 3)
        first_call = query.message.reply_text.await_args_list[0]
        first_text = first_call.args[0]
        self.assertIn("<b>📘 وانەی ٥ — پیتەکان و هاوتای لاتینی</b>", first_text)
        self.assertIn("<code>کەژیار — KejyarBot@</code>", first_text)
        self.assertIn("دەقی سەرچاوەی وانەی پێنج", first_text)
        self.assertEqual(first_call.kwargs.get("parse_mode"), "HTML")
        completion_calls = [
            call for call in query.message.reply_text.await_args_list
            if call.kwargs.get("reply_markup") is not None
            and any(
                button.callback_data == "finish_arami_course1_lesson_05"
                for row in call.kwargs["reply_markup"].inline_keyboard
                for button in row
            )
        ]
        self.assertEqual(len(completion_calls), 1)
        self.assertIn("کۆتایی وانەی ٥", completion_calls[0].args[0])

    async def test_lesson_reader_refuses_locked_lesson5(self):
        update, query = make_update("lesson")
        manifest = {"lessons": [{"number": 5, "id": "arami_course1_lesson_05"}]}
        with patch(
            "arami_lesson5_telegram.load_arami_lesson5_source",
            return_value="# وانەی ٥\n\nدەقی وانە.",
        ), patch("arami_lesson5_telegram.load_manifest", return_value=manifest):
            await callback(update, SimpleNamespace(user_data={}), "/unused", can_open=lambda user_id, lesson_id: False)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("سەرەتا وانەی پێشووتر", query.message.reply_text.await_args.args[0])

    async def test_practice_and_assessment_use_lesson5_scoped_sessions(self):
        bank = sample_bank()
        lesson1_session = {"mode": "lesson1-practice", "sentinel": True}
        context = SimpleNamespace(user_data={"arami_lesson1_session": lesson1_session})

        update, _query = make_update("practice")
        with patch("arami_lesson5_telegram.load_arami_lesson5_interactions", return_value=bank):
            await callback(update, context, "/unused")
        practice = context.user_data["arami_lesson5_session"]
        self.assertEqual(practice["mode"], "practice")
        self.assertEqual(context.user_data["arami_lesson1_session"], lesson1_session)
        self.assertEqual(context.user_data["arami_lesson5_message_id"], 11)

        update, _query = make_update("assessment")
        with patch("arami_lesson5_telegram.load_arami_lesson5_interactions", return_value=bank):
            await callback(update, context, "/unused")
        assessment = context.user_data["arami_lesson5_session"]
        self.assertEqual(assessment["mode"], "assessment")
        self.assertEqual(context.user_data["arami_lesson1_session"], lesson1_session)
        self.assertIsNot(assessment, practice)

    async def test_locked_lesson5_practice_and_assessment_are_not_started(self):
        for action in ("practice", "assessment"):
            update, query = make_update(action)
            context = SimpleNamespace(user_data={})
            with patch("arami_lesson5_telegram.load_manifest", return_value={
                "lessons": [{"number": 5, "id": "arami_course1_lesson_05"}]
            }):
                await callback(update, context, "/unused", can_open=lambda user_id, lesson_id: False)
            query.message.reply_text.assert_awaited_once()
            self.assertIn("ڕاهێنان و تاقیکردنەوە", query.message.reply_text.await_args.args[0])
            self.assertNotIn("arami_lesson5_session", context.user_data)

    async def test_practice_answer_is_submitted_and_progresses_to_next_question(self):
        bank = sample_bank()
        context = SimpleNamespace(user_data={})
        update, _query = make_update("practice")
        with patch("arami_lesson5_telegram.load_arami_lesson5_interactions", return_value=bank):
            await callback(update, context, "/unused")
        first_id = context.user_data["arami_lesson5_message_id"]

        update, pick_query = make_update("pick:0", message_id=first_id)
        await callback(update, context, "/unused")
        pick_query.edit_message_reply_markup.assert_awaited_once()

        update, submit_query = make_update("submit", message_id=first_id)
        await callback(update, context, "/unused")
        self.assertFalse(context.user_data["arami_lesson5_session"]["closed"])
        submit_query.edit_message_text.assert_awaited_once()
        next_markup = submit_query.edit_message_text.await_args.kwargs["reply_markup"]
        self.assertEqual(next_markup.inline_keyboard[0][0].callback_data, "arami5:next")

        update, _next_query = make_update("next", message_id=first_id)
        await callback(update, context, "/unused")
        self.assertEqual(context.user_data["arami_lesson5_session"]["index"], 1)
        self.assertEqual(context.user_data["arami_lesson5_message_id"], first_id + 1)

    async def test_assessment_hides_correct_answers_until_final_score(self):
        bank = sample_bank()
        context = SimpleNamespace(user_data={})
        update, _query = make_update("assessment")
        with patch("arami_lesson5_telegram.load_arami_lesson5_interactions", return_value=bank):
            await callback(update, context, "/unused")
        for index in range(2):
            message_id = context.user_data["arami_lesson5_message_id"]
            update, _pick_query = make_update("pick:0", message_id=message_id)
            await callback(update, context, "/unused")
            update, submit_query = make_update("submit", message_id=message_id)
            await callback(update, context, "/unused")
            shown = submit_query.edit_message_text.await_args.args[0]
            self.assertNotIn("وەڵامی ڕاست", shown)
            if index == 0:
                self.assertIn("وەڵامەکەت وەرگیرا", shown)
                update, _next_query = make_update("next", message_id=message_id)
                await callback(update, context, "/unused")
            else:
                self.assertIn("ئەنجام", shown)
                self.assertNotIn("دووبارەکردنەوەی پرسیارە هەڵەکان", str(submit_query.edit_message_text.await_args.kwargs["reply_markup"]))

    async def test_stale_lesson5_question_message_cannot_change_current_answer(self):
        context = SimpleNamespace(user_data={
            "arami_lesson5_session": {
                "mode": "practice",
                "questions": [{
                    "id": "p1",
                    "section_id": "lesson5_source_exercises",
                    "type": "recognize",
                    "prompt": "پرسیار",
                    "options": ["A", "B"],
                    "answer_index": 0,
                }],
                "index": 0,
                "selected_index": None,
                "answers": [],
                "closed": False,
            },
            "arami_lesson5_message_id": 99,
        })
        update, query = make_update("pick:0", message_id=10)
        await callback(update, context, "/unused")
        self.assertIsNone(context.user_data["arami_lesson5_session"]["selected_index"])
        query.edit_message_reply_markup.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
