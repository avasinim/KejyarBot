import tempfile
import unittest
from pathlib import Path

from arami_course1_runtime import (
    load_arami_lesson5_interactions,
    load_arami_lesson5_source,
)


class AramiLesson5RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]

    def test_lesson5_source_is_loaded_as_its_own_lesson(self):
        source = load_arami_lesson5_source(self.root)
        self.assertIn("وانەی ٥", source)
        self.assertIn("پیتەکانی زمانی کوردی بە نووسینی کوردی و لاتینی", source)
        self.assertNotIn("وانەی ٢:", source)

    def test_lesson5_practice_and_assessment_have_six_source_items(self):
        bank = load_arami_lesson5_interactions(self.root)
        self.assertEqual(len(bank["practice"]), 6)
        self.assertEqual(len(bank["assessment"]), 6)
        self.assertEqual(
            [item["id"] for item in bank["practice"]],
            [f"arami5_practice_{i:02d}" for i in range(1, 7)],
        )

    def test_lesson5_loader_rejects_mismatched_course_or_lesson(self):
        import json
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "course_data").mkdir()
            (root / "course_data" / "arami_course1_manifest.json").write_text(
                (self.root / "course_data" / "arami_course1_manifest.json").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            bank = json.loads((self.root / "course_data" / "arami_course1_lesson_05_interactions.json").read_text(encoding="utf-8"))
            bank["lesson_id"] = "arami_course1_lesson_02"
            (root / "course_data" / "arami_course1_lesson_05_interactions.json").write_text(
                json.dumps(bank, ensure_ascii=False), encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                load_arami_lesson5_interactions(root)


if __name__ == "__main__":
    unittest.main()
