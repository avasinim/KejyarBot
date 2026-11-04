import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from arami_lesson1_telegram import callback, menu_keyboard, _lesson_source_markdown


def make_update(action, message_id=10):
    message = SimpleNamespace(
        message_id=message_id,
        reply_text=AsyncMock(return_value=SimpleNamespace(message_id=message_id + 1)),
        reply_voice=AsyncMock(),
    )
    query = SimpleNamespace(
        data=f"arami1:{action}",
        message=message,
        from_user=SimpleNamespace(id=123),
        answer=AsyncMock(),
        edit_message_reply_markup=AsyncMock(),
        edit_message_text=AsyncMock(),
    )
    return SimpleNamespace(callback_query=query), query


class AramiLesson1TelegramTests(unittest.IsolatedAsyncioTestCase):
    def test_lesson1_adapter_preserves_all_structured_source_parts_in_order(self):
        lesson = {
            'title': 'سەردێڕ', 'objectives': ['ئامانج'],
            'sections': [{
                'title': 'بەشی یەک', 'body': 'دەقی ڕەسەن',
                'table': [['پیت', 'ناو'], ['ا', 'ئەلف']],
                'note': 'تێبینیی ڕەسەن',
                'questions': [{'prompt': 'پرسیاری ڕەسەن', 'options': ['هەڵبژاردەی A', 'هەڵبژاردەی B']}],
            }],
        }
        rendered_source = _lesson_source_markdown(lesson)
        expected = ['سەردێڕ', 'ئامانج', 'بەشی یەک', 'دەقی ڕەسەن', 'پیت', 'ئەلف', 'تێبینیی ڕەسەن', 'پرسیاری ڕەسەن', 'A) هەڵبژاردەی A', 'B) هەڵبژاردەی B']
        positions = [rendered_source.index(value) for value in expected]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn('تێبینی: تێبینیی ڕەسەن', rendered_source)

    def test_menu_exposes_only_lesson1_actions(self):
        keyboard = menu_keyboard()
        callbacks = [
            button.callback_data
            for row in keyboard.inline_keyboard
            for button in row
        ]
        self.assertEqual(callbacks, [
            "arami1:lesson",
            "arami1:practice", "arami1:assessment",
            "arami5:menu",
            "aramiC:menu",
        ])

    async def test_lesson1_menu_uses_the_current_course_title(self):
        update, query = make_update("menu")
        await callback(update, SimpleNamespace(user_data={}), "/unused")
        shown = query.message.reply_text.await_args.args[0]
        self.assertIn("کۆرسی ١: ڕێنووسی سەرەتاییی کوردی", shown)
        self.assertNotIn("ڕێنووسی ئارامی", shown)

    async def test_lesson_callback_sends_intro_all_sections_and_conclusion(self):
        lesson = {
            "title": "وانەی ١",
            "objectives": ["ئامانج"],
            "sections": [
                {"title": f"بەشی {i}", "body": f"دەقی {i}"}
                for i in range(1, 9)
            ],
            "conclusion": "پوختە",
        }
        update, query = make_update("lesson")
        manifest = {"lessons": [{"number": 1, "id": "arami_course1_lesson_01"}]}
        with patch("arami_lesson1_telegram.load_arami_lesson1_content", return_value=lesson), patch("arami_lesson1_telegram.load_manifest", return_value=manifest):
            await callback(update, SimpleNamespace(user_data={}), "/unused")
        query.message.reply_voice.assert_not_awaited()
        self.assertEqual(query.message.reply_text.await_count, 4)
        lesson_html = query.message.reply_text.await_args_list[0].args[0]
        self.assertIn("وانەی ١", lesson_html)
        self.assertIn("کەژیار — KejyarBot@", lesson_html)
        self.assertIn("ئامانج", lesson_html)
        self.assertIn("بەشی 8", lesson_html)
        self.assertEqual(query.message.reply_text.await_args_list[0].kwargs["parse_mode"], "HTML")
        self.assertIn("پوختە", query.message.reply_text.await_args_list[1].args[0])
        self.assertEqual(query.message.reply_text.await_args_list[1].kwargs["parse_mode"], "HTML")
        completion_markup = query.message.reply_text.await_args_list[2].kwargs["reply_markup"]
        self.assertEqual(completion_markup.inline_keyboard[0][0].callback_data, "finish_arami_course1_lesson_01")

    async def test_lesson_reader_refuses_locked_lesson1(self):
        update, query = make_update("lesson")
        lesson = {
            "title": "وانەی ١", "objectives": [], "sections": [], "conclusion": "پوختە",
        }
        manifest = {"lessons": [{"number": 1, "id": "arami_course1_lesson_01"}]}
        with patch("arami_lesson1_telegram.load_arami_lesson1_content", return_value=lesson), patch(
            "arami_lesson1_telegram.load_manifest", return_value=manifest
        ):
            await callback(update, SimpleNamespace(user_data={}), "/unused", can_open=lambda user_id, lesson_id: False)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("سەرەتا وانەی پێشووتر", query.message.reply_text.await_args.args[0])

    async def test_legacy_audio_callback_never_sends_voice(self):
        update, query = make_update("audio")
        await callback(update, SimpleNamespace(user_data={}), "/unused")
        query.message.reply_voice.assert_not_awaited()

    async def test_practice_callback_starts_question_session(self):
        bank = {
            "practice": [{
                "id": "q1", "section_id": "lesson1_alphabet_count",
                "type": "recognize", "prompt": "چەند پیت؟",
                "options": ["٣٤", "٣٣"], "answer_index": 0,
            }],
        }
        update, query = make_update("practice")
        context = SimpleNamespace(user_data={})
        with patch("arami_lesson1_telegram.load_arami_lesson1_interactions", return_value=bank):
            await callback(update, context, "/unused")
        self.assertEqual(context.user_data["arami_lesson1_session"]["mode"], "practice")
        self.assertEqual(context.user_data["arami_lesson1_message_id"], 11)
        query.message.reply_text.assert_awaited_once()
        self.assertIn("چەند پیت؟", query.message.reply_text.await_args.args[0])

    async def test_locked_lesson1_practice_and_assessment_are_not_started(self):
        for action in ("practice", "assessment"):
            update, query = make_update(action)
            context = SimpleNamespace(user_data={})
            with patch("arami_lesson1_telegram.load_manifest", return_value={
                "lessons": [{"number": 1, "id": "arami_course1_lesson_01"}]
            }):
                await callback(update, context, "/unused", can_open=lambda user_id, lesson_id: False)
            query.message.reply_text.assert_awaited_once()
            self.assertIn("ڕاهێنان و تاقیکردنەوە", query.message.reply_text.await_args.args[0])
            self.assertNotIn("arami_lesson1_session", context.user_data)

    async def test_stale_question_message_cannot_change_current_answer(self):
        context = SimpleNamespace(user_data={
            "arami_lesson1_session": {
                "mode": "practice",
                "questions": [{
                    "id": "q1", "section_id": "lesson1_alphabet_count",
                    "type": "recognize", "prompt": "چەند پیت؟",
                    "options": ["٣٤", "٣٣"], "answer_index": 0,
                }],
                "index": 0, "selected_index": None, "answers": [], "closed": False,
            },
            "arami_lesson1_message_id": 99,
        })
        update, query = make_update("pick:0", message_id=10)
        await callback(update, context, "/unused")
        self.assertIsNone(context.user_data["arami_lesson1_session"]["selected_index"])
        query.edit_message_reply_markup.assert_not_awaited()



class AramiLesson1TelegramAssessmentTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.bank = {
            "practice": [{
                "id": "q1", "section_id": "lesson1_alphabet_count",
                "type": "recognize", "prompt": "چەند پیت؟",
                "options": ["٣٤", "٣٣"], "answer_index": 0,
            }],
            "assessment": [{
                "id": "a1", "section_id": "lesson1_alphabet_count",
                "type": "recognize", "prompt": "ئەلفبێ چەند پیتە؟",
                "options": ["٣٣", "٣٤"], "answer_index": 1,
            }],
        }

    async def _start_and_answer(self, selected_index):
        update, query = make_update("assessment")
        context = SimpleNamespace(user_data={})
        with patch("arami_lesson1_telegram.load_arami_lesson1_interactions", return_value=self.bank):
            await callback(update, context, "/unused")
        self.assertEqual(context.user_data["arami_lesson1_session"]["mode"], "assessment")
        question_message_id = context.user_data["arami_lesson1_message_id"]
        if selected_index == "correct":
            selected_index = context.user_data["arami_lesson1_session"]["questions"][0]["answer_index"]
        elif selected_index == "wrong":
            question = context.user_data["arami_lesson1_session"]["questions"][0]
            selected_index = (question["answer_index"] + 1) % len(question["options"])

        update, query = make_update(f"pick:{selected_index}", message_id=question_message_id)
        await callback(update, context, "/unused")
        update, query = make_update("submit", message_id=question_message_id)
        await callback(update, context, "/unused")
        return context, query

    async def test_assessment_wrong_answer_offers_retry_and_retry_starts_practice(self):
        context, result_query = await self._start_and_answer("wrong")
        self.assertTrue(context.user_data["arami_lesson1_session"]["closed"])
        result_query.edit_message_text.assert_awaited_once()
        markup = result_query.edit_message_text.await_args.kwargs["reply_markup"]
        callbacks = [
            button.callback_data
            for row in markup.inline_keyboard
            for button in row
        ]
        self.assertIn("arami1:retry", callbacks)

        # The completed result is edited in place, retaining the question message id.
        result_message_id = context.user_data["arami_lesson1_message_id"]
        update, retry_query = make_update("retry", message_id=result_message_id)
        await callback(update, context, "/unused")
        self.assertEqual(context.user_data["arami_lesson1_session"]["mode"], "practice")
        self.assertEqual(context.user_data["arami_lesson1_session"]["questions"][0]["id"], "a1")
        self.assertEqual(context.user_data["arami_lesson1_message_id"], result_message_id + 1)

    async def test_assessment_does_not_reveal_correct_answer_after_each_response(self):
        _context, result_query = await self._start_and_answer("wrong")
        shown = result_query.edit_message_text.await_args.args[0]
        self.assertIn("وەڵامەکەت وەرگیرا", shown)
        self.assertNotIn("وەڵامی ڕاست", shown)

    async def test_perfect_assessment_does_not_offer_retry(self):
        _context, result_query = await self._start_and_answer("correct")
        markup = result_query.edit_message_text.await_args.kwargs["reply_markup"]
        callbacks = [
            button.callback_data
            for row in markup.inline_keyboard
            for button in row
        ]
        self.assertNotIn("arami1:retry", callbacks)
        self.assertIn("arami1:menu", callbacks)



class AramiLesson1TelegramProgressionTests(unittest.IsolatedAsyncioTestCase):
    async def test_practice_requires_submission_then_advances_and_invalidates_old_message(self):
        bank = {
            "practice": [
                {
                    "id": "q1", "section_id": "lesson1_alphabet_count",
                    "type": "recognize", "prompt": "پرسیاری یەکەم",
                    "options": ["٣٤", "٣٣"], "answer_index": 0,
                },
                {
                    "id": "q2", "section_id": "lesson1_vowel_count",
                    "type": "recognize", "prompt": "پرسیاری دووەم",
                    "options": ["٨", "٧"], "answer_index": 0,
                },
            ],
        }
        update, _query = make_update("practice")
        context = SimpleNamespace(user_data={})
        with patch("arami_lesson1_telegram.load_arami_lesson1_interactions", return_value=bank):
            await callback(update, context, "/unused")

        first_message_id = context.user_data["arami_lesson1_message_id"]
        update, query = make_update("submit", message_id=first_message_id)
        await callback(update, context, "/unused")
        self.assertEqual(context.user_data["arami_lesson1_session"]["index"], 0)
        self.assertEqual(len(context.user_data["arami_lesson1_session"]["answers"]), 0)
        query.message.reply_text.assert_awaited_once_with("سەرەتا وەڵامێک هەڵبژێرە.")

        update, _query = make_update("pick:0", message_id=first_message_id)
        await callback(update, context, "/unused")
        update, _query = make_update("submit", message_id=first_message_id)
        await callback(update, context, "/unused")
        self.assertEqual(context.user_data["arami_lesson1_session"]["index"], 1)
        self.assertEqual(len(context.user_data["arami_lesson1_session"]["answers"]), 1)

        update, _query = make_update("next", message_id=first_message_id)
        await callback(update, context, "/unused")
        second_message_id = context.user_data["arami_lesson1_message_id"]
        self.assertNotEqual(second_message_id, first_message_id)
        self.assertEqual(second_message_id, first_message_id + 1)

        update, stale_query = make_update("pick:1", message_id=first_message_id)
        await callback(update, context, "/unused")
        self.assertIsNone(context.user_data["arami_lesson1_session"]["selected_index"])
        stale_query.edit_message_reply_markup.assert_not_awaited()

        update, _query = make_update("pick:0", message_id=second_message_id)
        await callback(update, context, "/unused")
        self.assertEqual(context.user_data["arami_lesson1_session"]["selected_index"], 0)


    async def test_pick_and_submit_state_are_committed_before_callback_acknowledgement(self):
        from pathlib import Path
        base_dir = str(Path(__file__).resolve().parents[1])
        context = SimpleNamespace(user_data={})
        update, _ = make_update("practice")
        await callback(update, context, base_dir)
        message_id = context.user_data["arami_lesson1_message_id"]
        session = context.user_data["arami_lesson1_session"]

        update, pick_query = make_update("pick:0", message_id=message_id)
        async def assert_pick_committed():
            self.assertEqual(session["selected_index"], 0)
        pick_query.answer.side_effect = assert_pick_committed
        await callback(update, context, base_dir)

        update, submit_query = make_update("submit", message_id=message_id)
        async def assert_submit_committed():
            self.assertEqual(session["index"], 1)
            self.assertEqual(len(session["answers"]), 1)
        submit_query.answer.side_effect = assert_submit_committed
        await callback(update, context, base_dir)


    async def test_duplicate_next_callback_sends_only_one_question(self):
        import asyncio
        session = {
            "mode": "practice",
            "questions": [{
                "id": "q1", "section_id": "lesson1", "type": "recognize",
                "prompt": "پرسیار", "options": ["A", "B"], "answer_index": 0,
            }],
            "index": 0, "selected_index": None, "answers": [], "closed": False,
        }
        context = SimpleNamespace(user_data={
            "arami_lesson1_session": session,
            "arami_lesson1_message_id": 10,
        })
        started, release = asyncio.Event(), asyncio.Event()
        async def slow_reply(*args, **kwargs):
            started.set()
            await release.wait()
            return SimpleNamespace(message_id=11)

        first_update, first_query = make_update("next", message_id=10)
        first_query.message.reply_text.side_effect = slow_reply
        task = asyncio.create_task(callback(first_update, context, "/unused"))
        await started.wait()

        second_update, second_query = make_update("next", message_id=10)
        await callback(second_update, context, "/unused")
        second_query.message.reply_text.assert_not_awaited()
        self.assertIsNone(context.user_data["arami_lesson1_message_id"])

        release.set()
        await task
        self.assertEqual(context.user_data["arami_lesson1_message_id"], 11)


if __name__ == "__main__":
    unittest.main()
