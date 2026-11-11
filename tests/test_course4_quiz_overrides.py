"""Source-integrity and runtime tests for append-only Course 4 quiz overrides."""
import json
import unittest
from pathlib import Path

import bot


ROOT = Path(__file__).resolve().parents[1]


class Course4QuizOverrideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        cls.payload = json.loads(
            (ROOT / "course_data" / "grammar_course4_quiz_overrides.json").read_text(encoding="utf-8")
        )
        cls.lessons = {lesson["id"]: lesson for lesson in cls.source["lessons"]}

    def test_override_source_snapshots_match_without_mutating_authored_bank(self):
        self.assertEqual(self.payload["course_id"], "grammar")
        self.assertEqual(len(self.payload["overrides"]), 50)
        for item in self.payload["overrides"]:
            lesson = self.lessons[item["lesson_id"]]
            original = lesson["quiz"][item["question_index"]]
            self.assertEqual(
                {
                    "q": original["q"],
                    "options": original["options"],
                    "answer": original["answer"],
                    "explanation": original["explanation"],
                },
                item["original_snapshot"],
            )

    def test_override_records_are_unique_and_well_formed(self):
        seen = set()
        for item in self.payload["overrides"]:
            key = (item["lesson_id"], item["question_index"])
            self.assertNotIn(key, seen)
            seen.add(key)
            replacement = item["replacement"]
            self.assertTrue(replacement["q"].strip())
            self.assertTrue(replacement["explanation"].strip())
            self.assertEqual(len(replacement["options"]), 4)
            self.assertEqual(len(set(replacement["options"])), 4)
            self.assertTrue(all(option.strip() for option in replacement["options"]))
            self.assertGreaterEqual(replacement["answer"], 0)
            self.assertLess(replacement["answer"], 4)

    def test_override_scope_is_44_questions_in_lessons_1_to_30_and_6_in_lesson_31(self):
        counts = {}
        for item in self.payload["overrides"]:
            counts[item["lesson_id"]] = counts.get(item["lesson_id"], 0) + 1
        self.assertEqual(sum(count for lesson_id, count in counts.items()
                             if int(lesson_id.rsplit("_", 1)[1]) <= 30), 44)
        self.assertEqual(counts.get("grammar_31"), 6)
        self.assertEqual(set(counts) - {"grammar_31"} <= {
            f"grammar_{number:02d}" for number in range(1, 31)
        }, True)

    def test_runtime_uses_validated_replacements_while_source_questions_remain_unchanged(self):
        for item in self.payload["overrides"]:
            lesson_id = item["lesson_id"]
            index = item["question_index"]
            replacement = item["replacement"]
            runtime = bot.QUIZ_DATA[lesson_id][index]
            self.assertEqual(runtime["question"], replacement["q"])
            self.assertEqual(runtime["options"], replacement["options"])
            self.assertEqual(runtime["answer"], replacement["options"][replacement["answer"]])
            self.assertEqual(runtime["explanation"], replacement["explanation"])
            self.assertEqual(
                self.lessons[lesson_id]["quiz"][index]["q"],
                item["original_snapshot"]["q"],
            )


if __name__ == "__main__":
    unittest.main()
