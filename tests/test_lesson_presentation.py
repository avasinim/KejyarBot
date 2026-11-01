import html
import re
import unittest

from bot import render_lesson_html_blocks, split_lesson_html


class LessonPresentationTests(unittest.TestCase):
    def test_academic_headings_and_sections_are_styled(self):
        blocks = render_lesson_html_blocks(
            "📘 Course title\n\nوانەی ١ — پیت و دەنگ\n\n"
            "ئامانجەکانی فێربوون\n"
            "١. دەنگ چییە؟\n"
            "نموونە: وشەی کورد\n"
            "کورتەی وانە: پیت نیشانەی نووسراوە."
        )
        rendered = "\n".join(blocks)
        self.assertIn("<b>📘 Course title</b>", rendered)
        self.assertIn("<b>وانەی ١ — پیت و دەنگ</b>", rendered)
        self.assertIn("<b>ئامانجەکانی فێربوون</b>", rendered)
        self.assertIn("<blockquote>نموونە: وشەی کورد</blockquote>", rendered)
        self.assertIn("کورتەی وانە: پیت نیشانەی نووسراوە.", rendered)

    def test_lesson_wording_is_html_escaped_not_rewritten(self):
        source = "دەقی وانە <test> & پیت و دەنگ"
        blocks = render_lesson_html_blocks(source)
        recovered = html.unescape(re.sub(r"<[^>]+>", "", "\n".join(blocks)))
        self.assertEqual(recovered, source)

    def test_long_lessons_are_split_into_telegram_safe_chunks(self):
        blocks = render_lesson_html_blocks("دەقی وانە\n" + ("وشەی فێرکاری " * 700))
        chunks = split_lesson_html(blocks)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk) <= 3500 for chunk in chunks))


if __name__ == "__main__":
    unittest.main()
