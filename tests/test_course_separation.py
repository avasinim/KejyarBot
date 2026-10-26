import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CourseSeparationTests(unittest.TestCase):
    def test_legacy_runtime_keeps_its_existing_ten_lessons(self):
        lessons = json.loads((ROOT / "lessons.json").read_text(encoding="utf-8"))
        self.assertEqual(set(lessons), {f"وانە_{n}" for n in range(1, 11)})

    def test_new_course_draft_has_22_lessons_and_is_not_wired_into_bot(self):
        curriculum = json.loads(
            (ROOT / "course_data" / "orthography_foundations.json").read_text(encoding="utf-8")
        )
        self.assertEqual(curriculum["course_id"], "orthography_foundations")
        self.assertEqual(len(curriculum["lessons"]), 22)

        bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")
        self.assertIn('load_json("lessons.json")', bot_source)
        self.assertIn('load_json("quiz.json")', bot_source)
        self.assertNotIn("orthography_quiz_runtime", bot_source)
        self.assertNotIn("orthography_quiz_adapter", bot_source)


    def test_curriculum_and_quiz_ids_numbers_and_titles_are_consistent(self):
        curriculum = json.loads(
            (ROOT / "course_data" / "orthography_foundations.json").read_text(encoding="utf-8")
        )
        draft = json.loads(
            (ROOT / "course_data" / "orthography_foundations_quiz_draft.json").read_text(encoding="utf-8")
        )
        lessons = curriculum["lessons"]
        quizzes = draft["quizzes"]

        self.assertEqual(curriculum["lesson_count"], len(lessons))
        self.assertEqual(draft["lesson_quiz_count"], len(quizzes))
        self.assertEqual(
            [(lesson["id"], lesson["number"]) for lesson in lessons],
            [(f"lesson_{number:02d}", number) for number in range(1, 23)],
        )
        self.assertEqual(
            [(group["lesson_id"], group["lesson_number"]) for group in quizzes],
            [(f"lesson_{number:02d}", number) for number in range(1, 23)],
        )
        lesson_titles = {lesson["id"]: lesson["title"] for lesson in lessons}
        self.assertEqual(curriculum["title"], draft["course_title"])
        self.assertEqual(len(lesson_titles), len(lessons))

    def test_draft_quiz_groups_match_all_22_curriculum_lessons(self):
        draft = json.loads(
            (ROOT / "course_data" / "orthography_foundations_quiz_draft.json").read_text(encoding="utf-8")
        )
        numbers = [group["lesson_number"] for group in draft["quizzes"]]
        self.assertEqual(len(numbers), 22)
        self.assertEqual(set(numbers), set(range(1, 23)))
        self.assertEqual(len(numbers), len(set(numbers)))


if __name__ == "__main__":
    unittest.main()
