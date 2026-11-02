"""Keep the public Course 1 count aligned with its canonical manifest."""
import unittest
from pathlib import Path

from arami_course1_telegram import load_manifest


ROOT = Path(__file__).resolve().parents[1]


class Course1ReadmeCountTests(unittest.TestCase):
    def test_readme_course1_count_matches_manifest(self):
        manifest = load_manifest(ROOT)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        expected = f"- کۆرسی ١: {manifest['course_size']} وانەی ڕێنووسی سەرەتاییی زمانی کوردی"
        self.assertIn(expected, readme)


if __name__ == "__main__":
    unittest.main()
