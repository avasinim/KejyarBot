import json
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


class CourseManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (BASE_DIR / "courses.json").open(encoding="utf-8") as handle:
            cls.manifest = json.load(handle)
        with (BASE_DIR / "lessons.json").open(encoding="utf-8") as handle:
            cls.lessons = json.load(handle)

    def test_four_courses_have_stable_unique_ids_and_keys(self):
        courses = self.manifest["courses"]
        self.assertEqual(len(courses), 4)
        self.assertEqual([course["order"] for course in courses], [1, 2, 3, 4])
        self.assertEqual(len({course["id"] for course in courses}), 4)
        self.assertEqual(len({course["key"] for course in courses}), 4)

    def test_existing_lessons_are_assigned_once_and_preserved(self):
        courses = self.manifest["courses"]
        assigned = [lesson for course in courses for lesson in course["lesson_ids"]]
        self.assertEqual(len(assigned), len(set(assigned)))
        self.assertEqual(set(assigned), set(self.lessons))
        for course in courses:
            self.assertTrue(set(course["legacy_lesson_ids"]).issubset(set(course["lesson_ids"])))

    def test_curriculum_titles_and_course_keys_are_stable(self):
        courses = self.manifest["courses"]
        self.assertEqual(
            [course["title"] for course in courses],
            [
                "دەورەی ١: ڕێنووسی سەرەتایی",
                "دەورەی ٢: وت‌وێژی ڕۆژانە",
                "دەورەی ٣: ڕێنووسی یەکگرتوو",
                "دەورەی ٤: ڕێزمان",
            ],
        )
        self.assertEqual(
            [course["key"] for course in courses],
            [
                "course_orthography_basic",
                "course_daily_conversation",
                "course_unified_orthography",
                "course_grammar",
            ],
        )

    def test_future_courses_are_not_misrepresented_as_ready(self):
        courses = {course["id"]: course for course in self.manifest["courses"]}
        for course_id in ("unified_orthography", "grammar"):
            self.assertEqual(courses[course_id]["status"], "planned")
            self.assertEqual(courses[course_id]["lesson_ids"], [])

    def test_production_sensitive_features_remain_guarded(self):
        policy = self.manifest["policy"]
        self.assertTrue(policy["preserve_student_progress"])
        self.assertTrue(policy["preserve_legacy_lesson_ids"])
        self.assertTrue(policy["preserve_xp_rewards_and_quiz_ids"])
        self.assertTrue(policy["course_progress_is_independent"])
        self.assertFalse(policy["dynamic_speech_enabled"])


if __name__ == "__main__":
    unittest.main()
