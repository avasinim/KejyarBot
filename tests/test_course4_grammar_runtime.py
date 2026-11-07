"""Regression tests for the owner-supplied replacement Course 4 grammar lesson."""
import json
import unittest
from pathlib import Path

import bot


ROOT = Path(__file__).resolve().parents[1]


class Course4GrammarRuntimeTests(unittest.TestCase):
    def test_course4_is_active_with_eight_owner_supplied_lessons(self):
        self.assertTrue(bot.course_is_active("grammar"))
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], ["grammar_01", "grammar_02", "grammar_03", "grammar_04", "grammar_05", "grammar_06", "grammar_07", "grammar_08"])
        self.assertIn("grammar_01", bot.LESSON_DATA)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_01"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_02"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_03"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_04"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_05"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_06"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_07"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_08"]), 8)
        self.assertEqual(bot.LESSON_DATA["grammar_01"]["review_status"],
                         "owner_review_pending_term_clarification")
        self.assertEqual(bot.LESSON_DATA["grammar_02"]["review_status"],
                         "owner_review_pending_sorani_corpus_validation")
        expected_review_status = {
            "grammar_03": "owner_review_pending_sorani_corpus_validation",
            "grammar_04": "owner_review_pending_sorani_plural_and_gender_validation",
            "grammar_05": "owner_review_pending_sorani_morphology_corpus_validation",
            "grammar_06": "owner_review_pending_sorani_adjective_corpus_validation",
            "grammar_07": "owner_review_pending_sorani_adjective_corpus_validation",
            "grammar_08": "owner_review_pending_sorani_adjective_corpus_validation",
        }
        for lesson_id, expected_status in expected_review_status.items():
            self.assertEqual(bot.LESSON_DATA[lesson_id]["review_status"], expected_status)

    def test_source_preserves_course4_content_and_reviewable_quiz(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        self.assertEqual(source["course_id"], "grammar")
        self.assertEqual([lesson["id"] for lesson in source["lessons"]], ["grammar_01", "grammar_02", "grammar_03", "grammar_04", "grammar_05", "grammar_06", "grammar_07", "grammar_08"])
        lesson = source["lessons"][0]
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]) - 2, 8)
        self.assertEqual(len(lesson["examples"]), 3)
        self.assertEqual(len(lesson["appendix"]), 4)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["quiz"]), 8)
        lesson2 = source["lessons"][1]
        self.assertEqual(len(lesson2["exercises"]), 5)
        self.assertEqual(len(lesson2["activities"]), 3)
        self.assertEqual(len(lesson2["appendix"]), 4)
        self.assertEqual(len(lesson2["comprehension"]) - 2, 8)
        self.assertEqual(len(lesson2["quiz"]), 8)
        self.assertIn("کەژیار", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("پاشکۆ", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("چالاکییەکان", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("فێزیۆلۆژی", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("پاشکۆ", bot.LESSON_DATA["grammar_02"]["content"])
        self.assertIn("چالاکییەکان", bot.LESSON_DATA["grammar_02"]["content"])
        lesson2_text = json.dumps(source["lessons"][1], ensure_ascii=False)
        self.assertIn("هاوەڵکار", lesson2_text)
        self.assertNotIn("ئاوەڵکار", lesson2_text)
        lesson6 = next(item for item in source["lessons"] if item["id"] == "grammar_06")
        self.assertIn("هاوەڵکار", " ".join(lesson6["key_points"]))
        expected_appendix_counts = {"grammar_03": 4, "grammar_04": 5, "grammar_05": 7, "grammar_06": 6, "grammar_07": 5, "grammar_08": 6}
        for lesson_id, appendix_count in expected_appendix_counts.items():
            lesson = next(item for item in source["lessons"] if item["id"] == lesson_id)
            self.assertEqual(len(lesson["appendix"]), appendix_count)
            self.assertEqual(len(lesson["activities"]), 3)
            self.assertEqual(len(lesson["exercises"]), 5)
            self.assertEqual(len(lesson["quiz"]), 8)
            self.assertEqual(len(lesson["comprehension"]) - 2, 8)
            self.assertIn("کەژیار", bot.LESSON_DATA[lesson_id]["content"])
            self.assertIn("پاشکۆ", bot.LESSON_DATA[lesson_id]["content"])
            self.assertIn("چالاکییەکان", bot.LESSON_DATA[lesson_id]["content"])
        lesson2_text = json.dumps(lesson2, ensure_ascii=False)
        self.assertIn("پۆلی ژمارەیی (Numeral)", lesson2_text)
        self.assertIn("نەک ژمارەی ڕێزمانیی ناو", lesson2_text)
        self.assertIn("ئامرازی پەیوەندی", lesson2_text)
        self.assertIn("پریپۆزیشن", lesson2_text)
        self.assertIn("پارتیکڵ", lesson2_text)
        self.assertIn("وشەی ژمارەیی", lesson2_text)
        lesson4 = next(item for item in source["lessons"] if item["id"] == "grammar_04")
        lesson5 = next(item for item in source["lessons"] if item["id"] == "grammar_05")
        self.assertIn("ئەو ئەسپانە", " ".join(lesson4["key_points"]))
        self.assertIn("ئەو ئەسپانە", " ".join(lesson5["key_points"]))
        self.assertIn("دیارخەری ئاماژە", " ".join(lesson4["key_points"]))
        self.assertNotIn("جێناوی ئاماژە", " ".join(lesson4["key_points"]))
        self.assertIn("دیارخەری ئاماژە", " ".join(lesson5["key_points"]))
        self.assertNotIn("لە پێکهاتەی جێناوی ئاماژە", " ".join(lesson5["key_points"]))
        self.assertNotIn("لەگەڵ جێناوی ئاماژەدا", " ".join(lesson5["key_points"]))
        self.assertIn("جوان + ـی ← جوانی", str(lesson5["examples"]))
        self.assertIn("ژمارەی ڕێزمانییەوە", " ".join(lesson4["key_points"]))
        self.assertIn("نە پۆلی وشەی ژمارەیی", " ".join(lesson4["key_points"]))
        self.assertIn("دوو کتێب", json.dumps(lesson4["examples"], ensure_ascii=False))
        self.assertEqual(len(lesson4["quiz"]), 8)
        self.assertIn("وشەی ژمارەیی", lesson4["quiz"][7]["q"])
        self.assertIn("ژمارەی ڕێزمانی", lesson4["quiz"][7]["explanation"])
        self.assertIn("کۆی نەناسراو", " ".join(lesson4["key_points"]))
        self.assertNotIn("کۆی گشتی/نەناسراو", " ".join(lesson4["key_points"]))
        lesson5_numbering = " ".join(lesson5["key_points"])
        self.assertIn("«ـان»", lesson5_numbering)
        self.assertIn("واتای گشتیی ناو", lesson5_numbering)
        self.assertIn("دەست + نوێژ ← دەستنوێژ", str(lesson5["examples"]))
        adjective_lessons = [item for item in source["lessons"] if item["id"] in {"grammar_06", "grammar_07", "grammar_08"}]
        self.assertEqual(len(adjective_lessons), 3)
        self.assertTrue(all(item["review_status"] == "owner_review_pending_sorani_adjective_corpus_validation" for item in adjective_lessons))
        lesson7 = next(item for item in source["lessons"] if item["id"] == "grammar_07")
        self.assertIn("ڕوو + خۆش", " ".join(lesson7["examples"][3]))
        self.assertIn("پێویستی بە پشکنینی فەرهەنگ", " ".join(lesson7["key_points"]))
        self.assertIn("ڕووخۆش", lesson7["quiz"][6]["options"][2])
        self.assertIn("ڕووخۆش", lesson7["activities"][0])
        self.assertIn("ژمارەی بنجی", " ".join(lesson7["key_points"]))
        self.assertIn("ژمارەی ڕیزبەندی", " ".join(lesson7["key_points"]))
        self.assertIn("ژمارەی ڕێزمانیی ناو", " ".join(lesson7["key_points"]))
        self.assertIn("دووەم", json.dumps(lesson7["examples"], ensure_ascii=False))
        self.assertNotIn("ڕووڕەش", json.dumps(lesson7["quiz"], ensure_ascii=False))
        self.assertNotIn("ڕووڕەش", " ".join(lesson7["activities"]))
        lesson6 = next(item for item in source["lessons"] if item["id"] == "grammar_06")
        self.assertIn("ئیزافەی کراوە", " ".join(lesson6["key_points"]))
        self.assertIn("نامەی درێژ", " ".join(item[0] for item in lesson6["examples"]))
        self.assertIn("نامە درێژەکە", " ".join(item[0] for item in lesson6["examples"]))
        self.assertIn("Open adjectival izafa", " ".join(lesson6["appendix"]))
        lesson8 = next(item for item in source["lessons"] if item["id"] == "grammar_08")
        self.assertIn("هەرە + هاوەڵناو", " ".join(lesson8["key_points"]))
        self.assertIn("هەرە + هاوەڵناو", " ".join(lesson8["appendix"]))

    def test_all_course4_lesson_quizzes_and_learning_components_are_well_formed(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        for lesson in source["lessons"]:
            with self.subTest(lesson=lesson["id"]):
                self.assertTrue(lesson["objective"].strip())
                self.assertTrue(lesson["key_points"])
                self.assertTrue(lesson["examples"])
                self.assertEqual(len(lesson["activities"]), 3)
                self.assertEqual(len(lesson["exercises"]), 5)
                self.assertEqual(len(lesson["quiz"]), 8)
                self.assertTrue(lesson["appendix"])
                self.assertTrue(lesson["comprehension"])
                self.assertIn("کەژیار", json.dumps(lesson, ensure_ascii=False))
                for question in lesson["quiz"]:
                    self.assertTrue(question["q"].strip())
                    self.assertGreaterEqual(len(question["options"]), 2)
                    self.assertGreaterEqual(question["answer"], 0)
                    self.assertLess(question["answer"], len(question["options"]))
                    self.assertTrue(question["explanation"].strip())

    def test_other_active_courses_keep_their_existing_lesson_counts(self):
        expected = {
            "arami_orthography_foundations": 21,
            "daily_conversation": 42,
            "unified_orthography": 66,
            "kurmanji_latin_orthography": 12,
            "kurmanji_latin_grammar": 12,
        }
        for course_id, count in expected.items():
            with self.subTest(course_id=course_id):
                self.assertTrue(bot.course_is_active(course_id))
                self.assertEqual(len(bot.COURSE_LESSON_ORDER[course_id]), count)

    def test_course4_runtime_validation_accepts_pending_owner_review_lesson(self):
        bot.validate_activated_course_runtime()


    def test_course4_plan_catalog_and_source_lesson_ids_stay_in_sync(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        plan = json.loads(
            (ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8")
        )
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected_ids = [f"grammar_{number:02d}" for number in range(1, 9)]
        source_ids = [lesson["id"] for lesson in source["lessons"]]
        plan_ids = [lesson["id"] for lesson in plan["lessons"]]
        course = next(item for item in catalog["courses"] if item["id"] == "grammar")

        self.assertEqual(source_ids, expected_ids)
        self.assertEqual(plan["lesson_count"], 8)
        self.assertEqual(plan_ids, expected_ids)
        self.assertEqual(course["lesson_ids"], expected_ids)

    def test_each_course4_comprehension_section_has_eight_questions_and_two_markers(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        for lesson in source["lessons"]:
            with self.subTest(lesson=lesson["id"]):
                comprehension = lesson["comprehension"]
                self.assertEqual(len(comprehension), 10)
                self.assertTrue(comprehension[0].startswith("کورتەی وانە:"))
                for number, question in enumerate(comprehension[1:9], start=1):
                    self.assertTrue(question.startswith(f"{number}. "))
                self.assertTrue(comprehension[9].startswith(f"کۆتایی وانەی {lesson['number']}:"))


if __name__ == "__main__":
    unittest.main()
