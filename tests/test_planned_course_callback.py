"""A planned course must remain blocked when its callback is invoked directly."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class PlannedCourseCallbackTests(unittest.IsolatedAsyncioTestCase):
    async def test_direct_grammar_callback_does_not_show_lessons(self):
        query = SimpleNamespace(
            data="course_grammar",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        # Even if runtime data is accidentally populated later, manifest status
        # must be checked before a course catalog can be displayed.
        with patch.dict(bot.COURSE_LESSON_ORDER, {"grammar": ["grammar_01"]}):
            await bot.open_course(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        args, kwargs = query.message.reply_text.await_args
        self.assertIn("لە پلانداناندا", args[0])
        self.assertNotIn("reply_markup", kwargs)
        self.assertNotIn("grammar_01", args[0])

    async def test_unknown_course_callback_returns_clear_message(self):
        query = SimpleNamespace(
            data="course_unknown",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)

        await bot.open_course(update, SimpleNamespace(user_data={}))

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("ئەم کۆرسە نەدۆزرایەوە", query.message.reply_text.await_args.args[0])
        self.assertNotIn("reply_markup", query.message.reply_text.await_args.kwargs)


if __name__ == "__main__":
    unittest.main()
