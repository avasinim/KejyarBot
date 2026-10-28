"""Regression guards for the legacy Course 1 identity and course activation gates."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


class CourseManifestRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = read_json("courses.json")["courses"]
        cls.by_id = {course["id"]: course for course in cls.manifest}
        cls.bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")

    def test_legacy_course_one_ids_remain_stable(self):
        course = self.by_id["orthography_basic"]
        self.assertEqual(course["status"], "active")
        self.assertEqual(course["lesson_ids"], [f"وانە_{i}" for i in range(1, 23)])

    def test_courses_two_and_three_are_wired_but_not_activated(self):
        for course_id in ("daily_conversation", "unified_orthography"):
            with self.subTest(course=course_id):
                course = self.by_id[course_id]
                self.assertEqual(course["status"], "draft_for_review")
                self.assertEqual(
                    course["lesson_ids"],
                    [f"{course_id}_{number:02d}" for number in range(1, 13)],
                )
        self.assertEqual(self.by_id["grammar"]["status"], "planned")
        self.assertEqual(self.by_id["grammar"]["lesson_ids"], [])
        self.assertIn("adapt_conversation_lessons", self.bot_source)
        self.assertIn("adapt_unified_orthography_lessons", self.bot_source)

    def test_legacy_reward_and_progress_keys_are_still_used(self):
        # The legacy lesson identifiers are deliberately not renamed during
        # multi-course work, because existing SQLite progress is keyed by them.
        self.assertIn('lesson_key = f"وانە_{number}"', self.bot_source)
        self.assertIn("complete_lesson_with_rewards(user_id, lesson)", self.bot_source)
        self.assertIn("complete_quiz_with_rewards(update.effective_user.id, lesson)", self.bot_source)

    def test_course_runtime_keeps_draft_courses_behind_activation_gate(self):
        self.assertIn('lesson_ids = [lesson for lesson in course.get("lesson_ids", []) if lesson in LESSON_DATA]', self.bot_source)
        self.assertIn('"ئەم کۆرسە وانەی ڕێکخراوی ئامادەی نییە', self.bot_source)

    def test_quiz_menu_preserves_namespaced_lesson_ids(self):
        # Splitting on underscores would truncate daily_conversation_01.
        self.assertIn('lesson.removeprefix("وانە_") if lesson.startswith("وانە_") else lesson', self.bot_source)
        self.assertIn('callback_data=f"quiz_{quiz_lesson_id}_start"', self.bot_source)
        self.assertIn('suffix.isdigit() else suffix', self.bot_source)
        self.assertNotIn("lesson.split", self.bot_source)


if __name__ == "__main__":
    unittest.main()
