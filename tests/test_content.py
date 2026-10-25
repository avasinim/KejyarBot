import json
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


def load_json(filename):
    with (BASE_DIR / filename).open(encoding="utf-8") as handle:
        return json.load(handle)


class ContentConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lessons = load_json("lessons.json")
        cls.quizzes = load_json("quiz.json")
        cls.learning_path = load_json("learning_path.json")
        cls.grade_01_plan = load_json("curriculum/grade_01_plan.json")["curriculum"]

    def test_learning_path_matches_lesson_titles_and_order(self):
        expected = [
            "وانەی ١: سڵاو و ناساندنی خۆ",
            "وانەی ٢: ئەلفوبێی کوردی",
            "وانەی ٣: وشەکانی ڕۆژانە",
            "وانەی ٤: ژمارەکان",
            "وانەی ٥: ڕەنگەکان",
        ]
        self.assertEqual(self.learning_path["lessons"], expected)
        for index, title in enumerate(expected, start=1):
            self.assertIn(f"وانە_{index}", self.lessons)
            self.assertEqual(self.lessons[f"وانە_{index}"]["title"], title.split(": ", 1)[1])
            self.assertTrue(self.lessons[f"وانە_{index}"]["content"].strip())

    def test_every_quiz_question_has_valid_options_and_answer(self):
        self.assertEqual(set(self.quizzes), {"وانە_1", "وانە_2", "وانە_3", "وانە_4", "وانە_5"})
        for lesson, questions in self.quizzes.items():
            with self.subTest(lesson=lesson):
                self.assertTrue(questions)
                for question in questions:
                    self.assertTrue(question["question"].strip())
                    self.assertGreaterEqual(len(question["options"]), 2)
                    self.assertEqual(len(question["options"]), len(set(question["options"])))
                    self.assertIn(question["answer"], question["options"])



    def test_alphabet_lesson_has_teaching_examples_and_practice(self):
        lesson = self.lessons["وانە_2"]["content"]
        for required in ("ئامانجی وانە", "پیت و دەنگ", "نموونە", "ڕاهێنان", "پیتەکان"):
            with self.subTest(section=required):
                self.assertIn(required, lesson)
        self.assertGreaterEqual(len(self.quizzes["وانە_2"]), 4)

    def test_grade_one_curriculum_outline_is_complete_and_consistent(self):
        plan = self.grade_01_plan
        self.assertEqual(plan["grade"], 1)
        self.assertEqual(plan["stage"], "سەرەتایی")
        self.assertEqual(plan["status"], "outline")
        lessons = plan["lessons"]
        self.assertEqual(len(lessons), 20)
        lesson_ids = [lesson["id"] for lesson in lessons]
        self.assertEqual(len(lesson_ids), len(set(lesson_ids)))
        self.assertEqual(lesson_ids, [f"g1-l{i:02d}" for i in range(1, 21)])
        for lesson in lessons:
            with self.subTest(lesson=lesson["id"]):
                self.assertTrue(lesson["title"].strip())
                self.assertTrue(lesson["goals"])
                self.assertTrue(lesson["activities"])
                self.assertTrue(lesson["assessment"].strip())
                self.assertTrue(all(item.strip() for item in lesson["goals"]))
                self.assertTrue(all(item.strip() for item in lesson["activities"]))
        self.assertNotIn("letter_sound_card_schema", plan)

    def test_quiz_lessons_exist(self):
        for lesson in self.quizzes:
            self.assertIn(lesson, self.lessons)


if __name__ == "__main__":
    unittest.main()
