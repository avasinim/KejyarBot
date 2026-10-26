import json
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


class CourseProgressionInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (BASE_DIR / "courses.json").open(encoding="utf-8") as handle:
            cls.manifest = json.load(handle)
        with (BASE_DIR / "lessons.json").open(encoding="utf-8") as handle:
            cls.lessons = json.load(handle)
        cls.courses = sorted(cls.manifest["courses"], key=lambda item: item["order"])

    def test_course_sequences_are_contiguous_and_do_not_overlap(self):
        seen = set()
        for course in self.courses:
            ids = course["lesson_ids"]
            self.assertEqual(len(ids), len(set(ids)), course["id"])
            self.assertFalse(seen.intersection(ids), course["id"])
            seen.update(ids)
            for lesson_id in ids:
                self.assertIn(lesson_id, self.lessons)
        self.assertEqual(seen, set(self.lessons))

    def test_course_end_does_not_implicitly_start_next_course(self):
        for course in self.courses:
            ids = course["lesson_ids"]
            if not ids:
                continue
            # The next lesson after a course's final lesson must not be inferred
            # from the global legacy lesson order.
            last = ids[-1]
            self.assertIn(last, self.lessons)
            if course is not self.courses[-1]:
                later_ids = [lesson for later in self.courses[self.courses.index(course) + 1:] for lesson in later["lesson_ids"]]
                self.assertNotIn(later_ids[0] if later_ids else None, ids)

    def test_future_courses_are_not_accidentally_activated_without_lessons(self):
        for course in self.courses:
            if course["id"] in {"unified_orthography", "grammar"}:
                self.assertEqual(course["lesson_ids"], [])
                self.assertEqual(course["status"], "planned")

    def test_dynamic_speech_remains_disabled_in_manifest(self):
        self.assertFalse(self.manifest["policy"]["dynamic_speech_enabled"])


if __name__ == "__main__":
    unittest.main()
