"""Regression coverage for the Course 3 textual Kejyar wordmark."""
import unittest

from course_lesson_adapters import (
    adapt_conversation_lessons,
    adapt_unified_orthography_lessons,
)


class CourseWordmarkTests(unittest.TestCase):
    def test_course3_starts_with_kejyar_wordmark_and_lesson_title(self):
        lessons, _ = adapt_unified_orthography_lessons({
            "course_id": "unified_orthography",
            "lessons": [{
                "number": 1,
                "title": "ئەلفبێ",
                "objective": "ئامانجی وانە",
                "key_points": [],
                "examples": [],
                "exercises": [],
                "comprehension": [],
                "quiz": [],
            }],
        })
        content = lessons["unified_orthography_01"]["content"]
        self.assertTrue(content.startswith("✦ کەژیار ✦\n📖 ئەلفبێ"))

    def test_course2_format_is_unchanged_and_has_no_course3_wordmark(self):
        lessons, _ = adapt_conversation_lessons("daily_conversation", [{
            "lessons": [{
                "number": 1,
                "title": "سڵاو",
                "objective": "ئامانج",
            }],
        }])
        content = lessons["daily_conversation_01"]["content"]
        self.assertTrue(content.startswith("💬 سڵاو"))
        self.assertNotIn("کەژیار", content)


if __name__ == "__main__":
    unittest.main()
