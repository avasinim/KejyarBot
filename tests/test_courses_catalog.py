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
        with (ROOT / "course_data" / "daily_conversation_plan.json").open(encoding="utf-8") as handle:
            cls.conversation_plan = json.load(handle)

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

        expected_drafts = {
            "daily_conversation": [f"daily_conversation_{n:02d}" for n in range(1, 13)],
            "unified_orthography": [f"unified_orthography_{n:02d}" for n in range(1, 13)],
        }
        for course_id, expected_ids in expected_drafts.items():
            with self.subTest(course=course_id):
                self.assertEqual(by_id[course_id]["status"], "draft_for_review")
                self.assertEqual(by_id[course_id]["lesson_ids"], expected_ids)
        self.assertEqual(by_id["grammar"]["status"], "planned")
        self.assertEqual(by_id["grammar"]["lesson_ids"], [])

    def test_daily_conversation_plan_is_provisional_and_does_not_activate_course(self):
        by_id = {course["id"]: course for course in self.catalog}
        conversation = by_id["daily_conversation"]
        self.assertEqual(conversation["status"], "draft_for_review")
        self.assertEqual(conversation["lesson_ids"], [f"daily_conversation_{n:02d}" for n in range(1, 13)])
        self.assertEqual(self.conversation_plan["course_id"], "daily_conversation")
        self.assertEqual(self.conversation_plan["status"], "draft_lessons_created_needs_review")
        self.assertEqual(self.conversation_plan["lesson_status"], "titles_and_sequence_are_proposals_only")
        for filename, expected_numbers in (
            ("daily_conversation_lessons_01_06.json", list(range(1, 7))),
            ("daily_conversation_lessons_07_12.json", list(range(7, 13))),
        ):
            with self.subTest(file=filename):
                with (ROOT / "course_data" / filename).open(encoding="utf-8") as handle:
                    draft = json.load(handle)
                self.assertEqual(draft["status"], "draft_for_review")
                self.assertEqual([lesson["number"] for lesson in draft["lessons"]], expected_numbers)
                self.assertTrue(all(lesson.get("dialogue") and lesson.get("vocabulary") and lesson.get("exercises") and lesson.get("quiz") for lesson in draft["lessons"]))
        proposed = self.conversation_plan["proposed_sequence"]
        self.assertEqual([lesson["number"] for lesson in proposed], list(range(1, 13)))
        self.assertTrue(all(lesson["working_title"] and lesson["focus"] for lesson in proposed))
        self.assertEqual(self.conversation_plan["source_status"], "source_text_not_yet_attached_to_this_plan")

    def test_daily_conversation_drafts_have_valid_quiz_answers_and_corrected_phrases(self):
        for filename in (
            "daily_conversation_lessons_01_06.json",
            "daily_conversation_lessons_07_12.json",
        ):
            with self.subTest(file=filename):
                with (ROOT / "course_data" / filename).open(encoding="utf-8") as handle:
                    draft = json.load(handle)
                for lesson in draft["lessons"]:
                    self.assertTrue(lesson["dialogue"])
                    self.assertTrue(lesson["vocabulary"])
                    self.assertTrue(lesson["exercises"])
                    self.assertTrue(lesson["quiz"])
                    self.assertTrue(all(len(item) == 2 and item[0] and item[1] for item in lesson["vocabulary"]))
                    self.assertTrue(all(isinstance(item, str) and item.strip() for item in lesson["exercises"]))
                    for question in lesson["quiz"]:
                        self.assertTrue(question["q"].strip())
                        self.assertGreaterEqual(len(question["options"]), 2)
                        self.assertGreaterEqual(question["answer"], 0)
                        self.assertLess(question["answer"], len(question["options"]))
                        self.assertEqual(len(question["options"]), len(set(question["options"])))

        with (ROOT / "course_data" / "daily_conversation_lessons_07_12.json").open(encoding="utf-8") as handle:
            draft = json.load(handle)
        with (ROOT / "course_data" / "daily_conversation_lessons_01_06.json").open(encoding="utf-8") as handle:
            first_draft = json.load(handle)
        lesson6 = next(lesson for lesson in first_draft["lessons"] if lesson["number"] == 6)
        self.assertEqual(lesson6["dialogue"][3][1], "دەچمە قوتابخانە و لەوێ دەخوێنم.")
        lesson3 = next(lesson for lesson in first_draft["lessons"] if lesson["number"] == 3)
        self.assertEqual(lesson3["dialogue"][3][1], "نزیکەی کاتژمێر دە دەگەمە کتێبخانە.")
        lesson5 = next(lesson for lesson in first_draft["lessons"] if lesson["number"] == 5)
        self.assertEqual(lesson5["dialogue"][1][1], "ماڵمان لە گەڕەکێکی ئارامدایە، نزیک پارکەکە.")
        lesson1 = next(lesson for lesson in first_draft["lessons"] if lesson["number"] == 1)
        self.assertEqual(lesson1["dialogue"][5][1], "باشە، تا دواتر لە بەردەم کتێبخانەکە دەبینمەوە.")

        lesson7 = next(lesson for lesson in draft["lessons"] if lesson["number"] == 7)
        lesson12 = next(lesson for lesson in draft["lessons"] if lesson["number"] == 12)
        self.assertEqual(lesson7["dialogue"][1][1], "بەیانی باش، کەژیار! بەڵێ، نان و پەنیرم خواردووە و چایم خواردووەتەوە. تۆ چی؟")
        self.assertNotIn("dialogue[1][1]", lesson7)
        self.assertEqual(lesson12["dialogue"][7][1], "بە پێ دەڕۆین؛ کتێبخانەکە نزیکە.")

    def test_no_lesson_is_accidentally_assigned_to_multiple_courses(self):
        all_ids = [
            lesson_id
            for course in self.catalog
            for lesson_id in course["lesson_ids"]
        ]
        self.assertEqual(len(all_ids), len(set(all_ids)))


if __name__ == "__main__":
    unittest.main()
