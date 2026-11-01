import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from arami_lesson1_telegram import callback, menu_keyboard


def make_update(action, message_id=10):
    message = SimpleNamespace(
        message_id=message_id,
        reply_text=AsyncMock(return_value=SimpleNamespace(message_id=message_id + 1)),
        reply_voice=AsyncMock(),
    )
    query = SimpleNamespace(
        data=f"arami1:{action}",
        message=message,
        answer=AsyncMock(),
        edit_message_reply_markup=AsyncMock(),
        edit_message_text=AsyncMock(),
    )
    return SimpleNamespace(callback_query=query), query


class AramiLesson1TelegramTests(unittest.IsolatedAsyncioTestCase):
    def test_menu_exposes_only_lesson1_actions(self):
        keyboard = menu_keyboard()
        callbacks = [
            button.callback_data
            for row in keyboard.inline_keyboard
            for button in row
        ]
        self.assertEqual(callbacks, [
            "arami1:lesson", "arami1:audio",
            "arami1:practice", "arami1:assessment",
        ])

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
        with patch("arami_lesson1_telegram.load_arami_lesson1_content", return_value=lesson):
            await callback(update, SimpleNamespace(user_data={}), "/unused")
        self.assertEqual(query.message.reply_text.await_count, 10)
        self.assertIn("وانەی ١", query.message.reply_text.await_args_list[0].args[0])
        self.assertIn("بەشی ٨", query.message.reply_text.await_args_list[8].args[0])
        self.assertIn("پوختە", query.message.reply_text.await_args_list[-1].args[0])

    async def test_audio_callback_sends_only_confirmed_asset_path(self):
        update, query = make_update("audio")
        with tempfile.TemporaryDirectory() as directory:
            audio = Path(directory) / "دەنگەکانی ئەلفبێ.ogg"
            audio.write_bytes(b"OggS-test")
            with patch("arami_lesson1_telegram.get_arami_lesson1_audio_path", return_value=audio):
                await callback(update, SimpleNamespace(user_data={}), directory)
        query.message.reply_voice.assert_awaited_once()

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


if __name__ == "__main__":
    unittest.main()
