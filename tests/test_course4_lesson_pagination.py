"""Regression tests for presentation-only Course 4 grammar lesson pagination."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import bot


class Course4LessonPaginationTests(unittest.IsolatedAsyncioTestCase):
    def test_lesson_pages_preserve_all_rendered_blocks_and_respect_page_limit(self):
        source = "\n\n".join(
            f"بەشی {number}: ئەم دەقە تەنها بۆ تاقیکردنەوەی دابەشکردنی پێشکەشکردنە."
            for number in range(1, 121)
        )
        blocks = bot.render_lesson_html_blocks(source)
        pages = bot.split_lesson_html(blocks, limit=2200)

        self.assertGreater(len(pages), 1)
        self.assertTrue(all(len(page) <= 2200 for page in pages))
        rendered = "\n".join(pages)
        for number in (1, 2, 40, 80, 120):
            self.assertIn(f"بەشی {number}:", rendered)

    def test_academic_pages_keep_section_headings_with_their_content(self):
        blocks = []
        for number in range(1, 4):
            blocks.extend([
                f"<b>📖 بەشی فێرکاری {number}</b>",
                "ڕوونکردنەوەی ئەم بەشە. " * 45,
            ])

        pages = bot.split_lesson_academic_pages(blocks, limit=1250)

        self.assertEqual(len(pages), 3)
        for number, page in enumerate(pages, start=1):
            self.assertTrue(page.startswith(f"<b>📖 بەشی فێرکاری {number}</b>"))
            self.assertIn("ڕوونکردنەوەی ئەم بەشە.", page)
            self.assertLessEqual(len(page), 1250)

    def test_plain_academic_section_titles_start_new_pages(self):
        blocks = [
            "<b>ئامانجەکانی فێربوون</b>",
            "ناوەڕۆکی ئامانج. " * 35,
            "<b>خۆت تاقی بکەرەوە</b>",
            "پرسیارەکانی تاقیکردنەوە. " * 35,
            "<b>کورتەی وانە: گرنگترین خاڵەکان</b>",
            "پوختەی وانە. " * 35,
        ]

        pages = bot.split_lesson_academic_pages(blocks, limit=1000)

        self.assertEqual(len(pages), 3)
        self.assertTrue(pages[0].startswith("<b>ئامانجەکانی فێربوون</b>"))
        self.assertTrue(pages[1].startswith("<b>خۆت تاقی بکەرەوە</b>"))
        self.assertTrue(pages[2].startswith("<b>کورتەی وانە: گرنگترین خاڵەکان</b>"))

    def test_academic_page_labels_classify_instructional_sections(self):
        cases = (
            ("<b>🎯 ئامانج</b>\\nدەقی ئامانج", "ئامانجی فێربوون"),
            ("<b>🔎 ڕوونکردنەوە و خاڵە سەرەکییەکان</b>", "بنەما و ڕوونکردنەوەی زانستی"),
            ("<b>✍️ نموونەکان</b>", "نموونە و شیکردنەوە"),
            ("<b>📎 پاشکۆ</b>", "پاشکۆی زانستی"),
            ("<b>🧩 ڕاهێنان</b>", "ڕاهێنان"),
        )
        for content, expected in cases:
            with self.subTest(content=content):
                self.assertEqual(bot.grammar_academic_page_label(content), expected)

    def test_all_fifty_course4_lessons_produce_telegram_safe_pages(self):
        lesson_ids = bot.COURSE_LESSON_ORDER["grammar"]
        self.assertEqual(len(lesson_ids), 50)
        self.assertEqual(lesson_ids[0], "grammar_01")
        self.assertEqual(lesson_ids[-1], "grammar_50")

        for lesson_id in lesson_ids:
            with self.subTest(lesson=lesson_id):
                content = bot.LESSON_DATA[lesson_id]["content"]
                blocks = bot.render_lesson_html_blocks(content)
                pages = bot.split_lesson_academic_pages(blocks, limit=2200)
                self.assertTrue(pages)
                self.assertTrue(all(page.strip() for page in pages))
                self.assertTrue(all(len(page) <= 2200 for page in pages))


    def test_pagination_preserves_every_rendered_text_block_in_order_for_all_fifty_lessons(self):
        import html
        import re

        def normalized_visible_text(value):
            value = re.sub(r"<[^>]*>", " ", value)
            return " ".join(html.unescape(value).split())

        lesson_ids = bot.COURSE_LESSON_ORDER["grammar"]
        self.assertEqual(len(lesson_ids), 50)

        for lesson_id in lesson_ids:
            with self.subTest(lesson=lesson_id):
                blocks = bot.render_lesson_html_blocks(
                    bot.LESSON_DATA[lesson_id]["content"]
                )
                pages = bot.split_lesson_academic_pages(blocks, limit=2200)
                expected = normalized_visible_text("\n".join(blocks))
                actual = normalized_visible_text("\n".join(pages))
                self.assertEqual(
                    actual,
                    expected,
                    "Pagination must preserve every rendered word and its order.",
                )


    def test_lesson_three_topic_outline_preserves_every_source_item_in_order(self):
        raw = next(
            item for item in bot.GRAMMAR_COURSE4_DRAFT["lessons"]
            if item["number"] == 3
        )
        adapted, _ = bot.adapt_unified_orthography_lessons(
            {"course_id": "grammar", "lessons": [raw]},
            include_extended_sections=True,
        )
        content = adapted["grammar_03"]["content"]

        expected_headings = (
            "📖 پێناسە، ناسینەوە و پۆلێنی ناو",
            "📖 دۆخی ناو و ژمارەی ڕێزمانی",
            "📖 ڕەگەز و پۆلێنکردنی واتایی",
            "📖 پێکهاتەی ناو و وشەسازی",
            "📖 سنووری بابەت: ناو و کردار",
            "📖 لێکدراو، ناوبەند و پشکنینی شێوەزاری",
            "📖 نموونەی پۆل و ئەرکی ناو",
            "📖 نموونەی دۆخ و ژمارە",
            "📖 نموونەی داڕشتن و ناوی چەمکی",
            "📖 نموونەی سنووری بابەت",
            "📖 نموونەی لێکدراو و ناوبەند",
            "📖 پوختەی تیۆری و جیاوازییە بنەڕەتییەکان",
            "📖 سەرچاوە بنەڕەتییەکان",
            "📖 سنووری شێوەزار و سنووری بابەت",
            "📖 تێبینییەکانی بەڵگە، شیکردنەوە و پشکنینی زیاتر",
        )
        for heading in expected_headings:
            self.assertIn(heading, content)

        for field in ("key_points", "examples", "appendix"):
            previous = -1
            for item in raw[field]:
                if field == "key_points":
                    rendered = f"• {item}"
                elif field == "examples":
                    rendered = f"• {item[0]}: {item[1]}"
                else:
                    rendered = f"{raw[field].index(item) + 1}. {item}"
                position = content.find(rendered)
                self.assertGreater(position, previous, f"{field} item missing or reordered")
                previous = position

    def test_navigation_buttons_show_previous_and_next_and_finish_only_on_last_page(self):
        completion = bot.InlineKeyboardMarkup([[
            bot.InlineKeyboardButton("finish", callback_data="finish_grammar_01")
        ]])

        first = bot.lesson_page_keyboard("grammar_01", 0, 3, completion)
        middle = bot.lesson_page_keyboard("grammar_01", 1, 3, completion)
        last = bot.lesson_page_keyboard("grammar_01", 2, 3, completion)

        first_callbacks = [button.callback_data for row in first.inline_keyboard for button in row]
        middle_callbacks = [button.callback_data for row in middle.inline_keyboard for button in row]
        last_callbacks = [button.callback_data for row in last.inline_keyboard for button in row]

        self.assertIn("lessonpage:grammar_01:1", first_callbacks)
        self.assertNotIn("finish_grammar_01", first_callbacks)
        self.assertIn("lessonpage:grammar_01:0", middle_callbacks)
        self.assertIn("lessonpage:grammar_01:2", middle_callbacks)
        self.assertNotIn("finish_grammar_01", middle_callbacks)
        self.assertIn("lessonpage:grammar_01:1", last_callbacks)
        self.assertIn("finish_grammar_01", last_callbacks)

    async def test_grammar_lesson_opens_one_page_with_navigation(self):
        message = SimpleNamespace(reply_text=AsyncMock())
        content = "وانەی تاقیکاری\n\n" + "\n\n".join(
            f"خاڵی فێرکاری {number}: " + ("دەقی فێرکاریی پارێزراو. " * 12)
            for number in range(1, 90)
        )

        await bot.send_lesson_text(
            message,
            content,
            bot.InlineKeyboardMarkup([[
                bot.InlineKeyboardButton("finish", callback_data="finish_grammar_01")
            ]]),
            lesson_id="grammar_01",
            page=0,
        )

        message.reply_text.assert_awaited_once()
        args, kwargs = message.reply_text.await_args
        self.assertIn("پەڕە 1 لە", args[0])
        self.assertIn("وانەی ١", args[0])
        self.assertIsNotNone(kwargs["reply_markup"])
        callbacks = [
            button.callback_data
            for row in kwargs["reply_markup"].inline_keyboard
            for button in row
        ]
        self.assertTrue(any(value.startswith("lessonpage:grammar_01:") for value in callbacks))
        self.assertNotIn("finish_grammar_01", callbacks)

    async def test_page_callback_reopens_only_requested_grammar_page_without_resending_image(self):
        query = SimpleNamespace(
            answer=AsyncMock(),
            data="lessonpage:grammar_01:1",
            from_user=SimpleNamespace(id=12345),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        with patch.object(bot, "can_open", return_value=True), patch.object(
            bot, "send_shared_lesson_image", new=AsyncMock()
        ) as send_image:
            await bot.open_lesson_page(update, SimpleNamespace())

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پەڕە 2 لە", query.message.reply_text.await_args.args[0])
        send_image.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
