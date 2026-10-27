import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CourseCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / "courses.json").open(encoding="utf-8") as handle:
            cls.catalog = json.load(handle)["courses"]
        with (ROOT / "course_data" / "orthography_foundations.json").open(encoding="utf-8") as handle:
            cls.orthography = json.load(handle)

    def test_four_courses_have_unique_ids_and_order(self):
        self.assertEqual(len(self.catalog), 4)
        self.assertEqual([course["order"] for course in self.catalog], [1, 2, 3, 4])
        self.assertEqual(len({course["id"] for course in self.catalog}), 4)
        self.assertEqual(len({course["key"] for course in self.catalog}), 4)

    def test_only_ready_orthography_course_has_structured_lesson_ids(self):
        by_id = {course["id"]: course for course in self.catalog}
        first = by_id["orthography_basic"]
        self.assertEqual(first["status"], "active")
        self.assertEqual(len(first["lesson_ids"]), 22)
        self.assertEqual(first["lesson_ids"], [f"وانە_{n}" for n in range(1, 23)])
        self.assertEqual(len(set(first["lesson_ids"])), 22)
        self.assertEqual(self.orthography["lesson_count"], 22)

        for course_id in ("daily_conversation", "unified_orthography", "grammar"):
            with self.subTest(course=course_id):
                self.assertEqual(by_id[course_id]["status"], "planned")
                self.assertEqual(by_id[course_id]["lesson_ids"], [])

    def test_no_lesson_is_accidentally_assigned_to_multiple_courses(self):
        all_ids = [
            lesson_id
            for course in self.catalog
            for lesson_id in course["lesson_ids"]
        ]
        self.assertEqual(len(all_ids), len(set(all_ids)))


if __name__ == "__main__":
    unittest.main()
