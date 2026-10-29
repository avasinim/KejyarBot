import tempfile
import unittest
from pathlib import Path

from course_infographics import course_infographic_path


class CourseInfographicPathTests(unittest.TestCase):
    def test_course3_uses_namespaced_png(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "assets" / "infographics" / "course3-lesson-01.png"
            target.parent.mkdir(parents=True)
            target.write_bytes(b"test")
            path = course_infographic_path(
                "unified_orthography_1",
                {"course_id": "unified_orthography", "source_number": 1},
                temp,
            )
            self.assertEqual(path, target)

    def test_does_not_reuse_daily_conversation_assets(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / "assets" / "infographics"
            folder.mkdir(parents=True)
            (folder / "lesson-01-greetings.svg").write_text("<svg/>", encoding="utf-8")
            self.assertIsNone(course_infographic_path(
                "daily_conversation_1",
                {"course_id": "daily_conversation", "source_number": 1},
                temp,
            ))

    def test_missing_artwork_does_not_resolve(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertIsNone(course_infographic_path(
                "unified_orthography_1",
                {"course_id": "unified_orthography", "source_number": 1},
                temp,
            ))

    def test_rejects_invalid_lesson_numbers(self):
        with tempfile.TemporaryDirectory() as temp:
            for number in (0, 67, True, "1", None):
                self.assertIsNone(course_infographic_path(
                    "unified_orthography_1",
                    {"course_id": "unified_orthography", "source_number": number},
                    temp,
                ))


if ( __name__ == "__main__"):
    unittest.main()
