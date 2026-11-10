"""Regression tests for the owner-supplied replacement Course 4 grammar lesson."""
import json
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch
from pathlib import Path

import bot


ROOT = Path(__file__).resolve().parents[1]


class Course4GrammarRuntimeTests(unittest.TestCase):
    def test_all_forty_six_lessons_keep_complete_content_schema_and_catalog_alignment(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        lessons = source["lessons"]
        expected_ids = [f"grammar_{number:02d}" for number in range(1, 51)]
        self.assertEqual(len(lessons), 50)
        self.assertEqual([item["id"] for item in lessons], expected_ids)
        self.assertEqual([item["id"] for item in plan["lessons"]], expected_ids)
        self.assertEqual(plan["lesson_count"], 50)
        course = next(item for item in catalog["courses"] if item["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected_ids)
        kurdish_digits = "٠١٢٣٤٥٦٧٨٩"
        for number, lesson in enumerate(lessons[:31], start=1):
            localized_number = "".join(kurdish_digits[int(digit)] for digit in str(number))
            self.assertTrue(lesson["title"].startswith(f"وانەی {localized_number}:"))
            self.assertTrue(lesson["key_points"], lesson["id"])
            self.assertTrue(lesson["appendix"], lesson["id"])
            self.assertEqual(len(lesson["activities"]), 3, lesson["id"])
            self.assertEqual(len(lesson["exercises"]), 5, lesson["id"])
            self.assertEqual(len(lesson["comprehension"]), 10, lesson["id"])
            self.assertTrue(lesson["comprehension"][0].startswith("کورتەی وانە"), lesson["id"])
            self.assertTrue(lesson["comprehension"][-1].startswith("کۆتایی وانە"), lesson["id"])
            self.assertEqual(len(lesson["quiz"]), 8, lesson["id"])
            for example in lesson["examples"]:
                self.assertIsInstance(example, list, lesson["id"])
                self.assertEqual(len(example), 2, lesson["id"])
                self.assertTrue(all(isinstance(part, str) and part.strip() for part in example), lesson["id"])
            for question in lesson["quiz"]:
                self.assertTrue(question.get("q", "").strip(), lesson["id"])
                self.assertEqual(len(question["options"]), 4, lesson["id"])
                self.assertGreaterEqual(question["answer"], 0, lesson["id"])
                self.assertLess(question["answer"], len(question["options"]), lesson["id"])
                self.assertTrue(question.get("explanation", "").strip(), lesson["id"])
            answer_positions = [question["answer"] for question in lesson["quiz"]]
            self.assertEqual([answer_positions.count(position) for position in range(4)], [2, 2, 2, 2], lesson["id"])

        for lesson in lessons[31:]:
            self.assertEqual(lesson["review_status"], "owner_review_pending_expanded_draft")
            self.assertEqual(lesson["quiz"], [])
            self.assertTrue(lesson.get("source_markdown", "").strip())
            runtime_lesson = bot.LESSON_DATA[lesson["id"]]
            self.assertEqual(runtime_lesson["review_status"], lesson["review_status"])
            self.assertTrue(runtime_lesson["content"].strip())
            self.assertEqual(bot.QUIZ_DATA[lesson["id"]], [])

    def test_course4_is_active_with_forty_six_lessons(self):
        self.assertTrue(bot.course_is_active("grammar"))
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], [f"grammar_{number:02d}" for number in range(1, 51)])
        self.assertIn("grammar_01", bot.LESSON_DATA)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_01"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_02"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_03"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_04"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_05"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_06"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_07"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_08"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_09"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_10"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_11"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_12"]), 8)
        self.assertEqual(len(bot.QUIZ_DATA["grammar_13"]), 8)
        for lesson_id in ("grammar_14", "grammar_15", "grammar_16", "grammar_17"):
            self.assertEqual(len(bot.QUIZ_DATA[lesson_id]), 8)
        self.assertEqual(bot.LESSON_DATA["grammar_01"]["review_status"],
                         "scientific_review_complete_with_qualified_notes")
        self.assertEqual(bot.LESSON_DATA["grammar_02"]["review_status"],
                         "scientific_review_complete_with_qualified_notes")
        expected_review_status = {
            "grammar_03": "scientific_review_complete_with_qualified_notes",
            "grammar_04": "scientific_review_complete_with_qualified_notes",
            "grammar_05": "scientific_review_complete_with_qualified_notes",
            "grammar_06": "scientific_review_complete_with_qualified_notes",
            "grammar_07": "scientific_review_complete_with_qualified_notes",
            "grammar_08": "scientific_review_complete_with_qualified_notes",
            "grammar_09": "scientific_review_complete_with_qualified_notes",
            "grammar_10": "scientific_review_complete_with_qualified_notes",
            "grammar_11": "scientific_review_complete_with_qualified_notes",
            "grammar_12": "scientific_review_complete_with_qualified_notes",
            "grammar_13": "internal_cross_lesson_synthesis_no_external_source_mapping",
        }
        for lesson_id, expected_status in expected_review_status.items():
            self.assertEqual(bot.LESSON_DATA[lesson_id]["review_status"], expected_status)


    def test_lessons_1_to_5_scientific_review_corrections(self):
        lessons = {item["id"]: item for item in json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )["lessons"]}
        qualified = "scientific_review_complete_with_qualified_notes"
        for lesson_id in ("grammar_01", "grammar_02", "grammar_03", "grammar_04", "grammar_05"):
            self.assertEqual(lessons[lesson_id]["review_status"], qualified)
            self.assertEqual(len(lessons[lesson_id]["activities"]), 3)
            self.assertEqual(len(lessons[lesson_id]["exercises"]), 5)
            self.assertEqual(len(lessons[lesson_id]["comprehension"]), 10)
            self.assertEqual(len(lessons[lesson_id]["quiz"]), 8)
            for question in lessons[lesson_id]["quiz"]:
                self.assertGreaterEqual(question["answer"], 0)
                self.assertLess(question["answer"], len(question["options"]))
                self.assertTrue(question.get("explanation"))

        lesson1 = lessons["grammar_01"]
        self.assertNotIn("فێزیۆلۆژی", " ".join(lesson1["key_points"]))
        self.assertIn("فێزیۆلۆژی", " ".join(lesson1["appendix"]))
        self.assertIn("ڕێزمانی گەردوونی", " ".join(lesson1["appendix"]))
        self.assertNotIn("ڕەچەڵەکی زاراوەکە", lesson1["objective"])

        lesson2_text = " ".join(lessons["grammar_02"]["key_points"])
        self.assertIn("«لە»، «بە» و «بۆ»", lesson2_text)
        self.assertIn("لە ... دا", lesson2_text)
        self.assertNotIn("تایبەتمەندییەکی زمانی ئینگلیزی و ڕووسییە", lesson2_text)

        lesson4_text = " ".join(lessons["grammar_04"]["appendix"])
        self.assertIn("کۆی نەناسراو", lesson4_text)
        self.assertNotIn("کۆی گشتی/نەناسراو", lesson4_text)

    def test_source_preserves_course4_content_and_reviewable_quiz(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        self.assertEqual(source["course_id"], "grammar")
        self.assertEqual([lesson["id"] for lesson in source["lessons"]], [f"grammar_{number:02d}" for number in range(1, 51)])
        lesson = source["lessons"][0]
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]) - 2, 8)
        self.assertEqual(len(lesson["examples"]), 3)
        self.assertEqual(len(lesson["appendix"]), 5)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["quiz"]), 8)
        lesson2 = source["lessons"][1]
        self.assertEqual(len(lesson2["exercises"]), 5)
        self.assertEqual(len(lesson2["activities"]), 3)
        self.assertEqual(len(lesson2["appendix"]), 5)
        self.assertEqual(len(lesson2["comprehension"]) - 2, 8)
        self.assertEqual(len(lesson2["quiz"]), 8)
        self.assertIn("کەژیار", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("پاشکۆ", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertIn("چالاکییەکان", bot.LESSON_DATA["grammar_01"]["content"])
        self.assertNotIn("فێزیۆلۆژی", " ".join(lesson["key_points"]))
        self.assertIn("فێزیۆلۆژی", " ".join(lesson["appendix"]))
        self.assertIn("پاشکۆ", bot.LESSON_DATA["grammar_02"]["content"])
        self.assertIn("چالاکییەکان", bot.LESSON_DATA["grammar_02"]["content"])
        lesson2_text = json.dumps(source["lessons"][1], ensure_ascii=False)
        self.assertIn("هاوەڵکار", lesson2_text)
        self.assertNotIn("ئاوەڵکار", lesson2_text)
        lesson6 = next(item for item in source["lessons"] if item["id"] == "grammar_06")
        self.assertIn("هاوەڵکار", " ".join(lesson6["key_points"]))
        self.assertIn("ناوەکە وەسف دەکات", lesson6["key_points"][0])
        self.assertNotIn("ئاماژەی جێناویش دەکات", lesson6["key_points"][0])
        expected_appendix_counts = {"grammar_03": 30, "grammar_04": 6, "grammar_05": 7, "grammar_06": 6, "grammar_07": 5, "grammar_08": 6, "grammar_10": 4, "grammar_11": 5, "grammar_12": 5, "grammar_13": 9, "grammar_14": 8, "grammar_15": 9, "grammar_16": 8, "grammar_17": 8, "grammar_18": 7, "grammar_19": 8, "grammar_20": 8, "grammar_21": 8, "grammar_22": 8, "grammar_23": 9}
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
        self.assertIn("پۆلی وشەی ژمارەیی (Numeral)", lesson2_text)
        self.assertIn("نەک ژمارەی ڕێزمانیی ناو", lesson2_text)
        self.assertIn("ئامرازی پەیوەندی", lesson2_text)
        self.assertIn("پێشبەند (Preposition)", lesson2_text)
        self.assertIn("پارتیکڵ", lesson2_text)
        self.assertIn("وشەی ژمارەیی", lesson2_text)
        lesson4 = next(item for item in source["lessons"] if item["id"] == "grammar_04")
        lesson5 = next(item for item in source["lessons"] if item["id"] == "grammar_05")
        self.assertIn("ئەو ئەسپانە", " ".join(lesson4["key_points"]))
        self.assertIn("فۆڕمی ئاماژەی کۆ", " ".join(lesson4["key_points"]))
        self.assertNotIn("ناو + کۆ + نیشانەی ناسراوی", " ".join(lesson4["key_points"]))
        self.assertIn("ئەو ئەسپانە", " ".join(lesson5["key_points"]))
        self.assertIn("فۆڕمی ئاماژەی کۆ", " ".join(lesson5["key_points"]))
        self.assertNotIn("نیشانەی ناسراوی «ـە»", " ".join(lesson5["key_points"]))
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
        self.assertTrue(all(item["review_status"] == "scientific_review_complete_with_qualified_notes" for item in adjective_lessons))
        lesson7 = next(item for item in source["lessons"] if item["id"] == "grammar_07")
        self.assertIn("ڕوو + خۆش", " ".join(lesson7["examples"][3]))
        self.assertIn("فەرهەنگی زمانی یەکگرتووی کوردی", " ".join(lesson7["key_points"]))
        self.assertIn("پێویستی بە پشکنینی فەرهەنگ", " ".join(lesson7["key_points"]))
        self.assertIn("بە + هێز", lesson7["quiz"][5]["explanation"])
        self.assertIn("هەنبانە بۆرینە", lesson7["quiz"][6]["explanation"])
        self.assertTrue(any("ڕووخۆش" in option for option in lesson7["quiz"][6]["options"]))
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
        lesson9 = next(item for item in source["lessons"] if item["id"] == "grammar_09")
        self.assertEqual(len(lesson9["quiz"]), 8)
        self.assertIn("ژمارەی ڕێزمانی", " ".join(lesson9["key_points"]))
        self.assertIn("دوو منداڵ", json.dumps(lesson9["examples"], ensure_ascii=False))
        self.assertIn("scientific_review_complete_with_qualified_notes", lesson9["review_status"])
        self.assertIn("دووشەممە", json.dumps(lesson9, ensure_ascii=False))
        self.assertIn("یەکگرتن", json.dumps(lesson9, ensure_ascii=False))

    def test_all_course4_lesson_quizzes_and_learning_components_are_well_formed(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        for lesson in source["lessons"]:
            with self.subTest(lesson=lesson["id"]):
                if lesson.get("review_status") == "owner_review_pending_expanded_draft":
                    self.assertTrue(lesson.get("source_markdown", "").strip())
                    self.assertEqual(lesson["quiz"], [])
                    self.assertEqual(lesson["review_status"], "owner_review_pending_expanded_draft")
                    continue
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
        expected_ids = [f"grammar_{number:02d}" for number in range(1, 51)]
        source_ids = [lesson["id"] for lesson in source["lessons"]]
        plan_ids = [lesson["id"] for lesson in plan["lessons"]]
        course = next(item for item in catalog["courses"] if item["id"] == "grammar")

        self.assertEqual(source_ids, expected_ids)
        self.assertEqual(plan["lesson_count"], 50)
        self.assertEqual(plan_ids, expected_ids)
        self.assertEqual(course["lesson_ids"], expected_ids)

    def test_each_course4_comprehension_section_has_eight_questions_and_two_markers(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        for lesson in source["lessons"][:31]:
            with self.subTest(lesson=lesson["id"]):
                comprehension = lesson["comprehension"]
                self.assertEqual(len(comprehension), 10)
                self.assertTrue(comprehension[0].startswith("کورتەی وانە:"))
                kurdish_digits = "١٢٣٤٥٦٧٨"
                for number, question in enumerate(comprehension[1:9]):
                    self.assertTrue(question.startswith(f"{kurdish_digits[number]}. "))
                lesson_digit = str(lesson["number"]).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
                self.assertTrue(comprehension[9].startswith(f"کۆتایی وانەی {lesson_digit}:"))


    def test_pronoun_unit_scientific_distinctions(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["id"]: item for item in source["lessons"]}
        for lesson_id in ("grammar_10", "grammar_11", "grammar_12"):
            lesson = lessons[lesson_id]
            self.assertEqual(len(lesson["quiz"]), 8)
            self.assertEqual(len(lesson["activities"]), 3)
            self.assertEqual(len(lesson["exercises"]), 5)
            self.assertEqual(len(lesson["comprehension"]) - 2, 8)
            self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        for pronoun in ("من", "تۆ", "ئەو", "ئێمە", "ئێوە", "ئەوان"):
            self.assertIn(pronoun, " ".join(lessons["grammar_10"]["key_points"]))
        self.assertIn("خاوەنداری", " ".join(lessons["grammar_11"]["key_points"]))
        self.assertIn("ئەرجەتیڤی", " ".join(lessons["grammar_12"]["key_points"]))
        self.assertNotIn("هەموو", " ".join(lessons["grammar_12"]["key_points"][:1]))

if __name__ == "__main__":
    unittest.main()



class Course4GrammarLesson13Tests(unittest.TestCase):
    def test_lesson13_is_internal_cross_lesson_synthesis_without_external_source_mapping(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_13")
        self.assertEqual(lesson["number"], 13)
        self.assertEqual(lesson["review_status"], "internal_cross_lesson_synthesis_no_external_source_mapping")
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["appendix"]), 9)
        content = " ".join(lesson["key_points"] + lesson["appendix"])
        examples = " ".join(item[1] for item in lesson["examples"])
        self.assertIn("چاوگ", content)
        self.assertIn("Root = ڕەگ", content)
        self.assertIn("بنجی ئێستا", content)
        self.assertIn("پاشبەستە", content)
        self.assertIn("دەخۆم", examples)
        self.assertNotIn("مرداندن", content + examples)
        self.assertNotIn("نووسراوم", content + examples)
        self.assertNotIn("Percolation", content + examples)
        self.assertNotIn("Konjunktiv", content + examples)
        self.assertNotIn("لاپەڕەکانی ٨٥–٨٧", content)
        self.assertIn("هیچ کتێب، PDF، لاپەڕە یان سەرچاوەی دەرەکی", content)
        appendix = (ROOT / "docs" / "COURSE4_GRAMMAR_APPENDIX.md").read_text(encoding="utf-8")
        appendix_lesson13 = appendix.split("## 25. وانەی ١٣", 1)[1].split("\\n## 26.", 1)[0]
        self.assertIn("هیچ mappingی لاپەڕەیی", appendix_lesson13)
        self.assertNotIn("٦٢–٨٤", appendix_lesson13)
        self.assertNotIn("٨٥–٨٧", appendix_lesson13)
        self.assertNotIn("A New Revision about the Rules of Kurdish Verbs and Tenses", appendix_lesson13)
        self.assertNotIn("د. سەروەت محەمەد ئەمین", appendix_lesson13)

    def test_lesson13_registered_in_source_plan_and_manifest(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        plan = json.loads(
            (ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8")
        )
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected_ids = [f"grammar_{number:02d}" for number in range(1, 51)]
        self.assertEqual([item["id"] for item in source["lessons"]], expected_ids)
        self.assertEqual(plan["lesson_count"], 50)
        self.assertEqual([item["id"] for item in plan["lessons"]], expected_ids)
        course = next(item for item in catalog["courses"] if item["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected_ids)


class Course4PendingDraftRuntimeTests(unittest.IsolatedAsyncioTestCase):
    async def test_beta_draft_is_readable_with_warning_and_has_beta_completion_button(self):
        lesson_id = "grammar_32"
        self.assertTrue(bot.lesson_is_pending_review(lesson_id))
        keyboard = bot.lesson_keyboard(lesson_id)
        self.assertIsNotNone(keyboard)
        self.assertEqual(keyboard.inline_keyboard[0][0].callback_data, f"finish_{lesson_id}")
        content = bot.lesson_display_content(lesson_id, bot.LESSON_DATA[lesson_id]["content"])
        self.assertIn("وەشانی تاقیکاریی (Beta)", content)
        self.assertIn(bot.LESSON_DATA[lesson_id]["content"], content)

    def test_lesson_13_internal_synthesis_is_beta_readable_but_not_quiz_eligible(self):
        lesson_id = "grammar_13"
        self.assertTrue(bot.lesson_is_beta_review(lesson_id))
        self.assertFalse(bot.lesson_quiz_is_available(lesson_id))
        content = bot.lesson_display_content(lesson_id, bot.LESSON_DATA[lesson_id]["content"])
        self.assertIn("وەشانی تاقیکاریی (Beta)", content)

    async def test_inflight_quiz_for_pending_lesson_is_cleared_without_rewards(self):
        lesson_id = "grammar_50"
        query = SimpleNamespace(
            data="answer_0",
            message_id=987,
            answer=AsyncMock(),
            message=SimpleNamespace(message_id=987, reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={"quiz": {"lesson": lesson_id}})
        with patch.object(bot, "complete_quiz_with_rewards") as reward:
            await bot.quiz_answer(update, context)
        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێداچوونەوەی سەرچاوە", query.message.reply_text.await_args.args[0])
        self.assertNotIn("quiz", context.user_data)
        reward.assert_not_called()

    async def test_next_lesson_route_marks_draft_as_beta_and_offers_progress_button(self):
        query = SimpleNamespace(
            data="next_lesson_grammar_32",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})
        with patch.object(bot, "can_open", return_value=True), patch.object(
            bot, "send_lesson_text", new_callable=AsyncMock
        ) as send:
            await bot.open_next_lesson(update, context)

        sent_content = send.await_args.args[1]
        self.assertIn("وەشانی تاقیکاریی (Beta)", sent_content)
        self.assertIsNotNone(send.await_args.args[2])

    def test_beta_progress_never_appears_as_official_progress_badges(self):
        beta_ids = [f"grammar_{number:02d}" for number in range(32, 51)]
        with (
            patch.object(bot, "get_completed_lessons", return_value=[]),
            patch.object(bot, "get_completed_beta_lessons", return_value=beta_ids),
            patch.object(bot, "course_is_active", side_effect=lambda course_id: course_id == "grammar"),
        ):
            self.assertEqual(bot.current_progress_badges(12345), [])

    def test_beta_lesson_ids_in_legacy_official_ledger_do_not_create_badges(self):
        completed = [f"grammar_{number:02d}" for number in range(1, 51)]
        with (
            patch.object(bot, "get_completed_lessons", return_value=completed),
            patch.object(bot, "course_is_active", side_effect=lambda course_id: course_id == "grammar"),
            patch.object(bot, "add_badge") as add_badge,
        ):
            bot.check_badges(12345)

        added = [call.args[1] for call in add_badge.call_args_list]
        self.assertEqual(len(added), 12)
        self.assertTrue(all("وانەی ٣٢" not in badge for badge in added))

    async def test_beta_draft_quiz_callback_is_rejected_without_creating_quiz_state(self):
        lesson_id = "grammar_46"
        query = SimpleNamespace(
            data=f"quiz_{lesson_id}_start",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(
            callback_query=query,
            effective_user=SimpleNamespace(id=12345),
        )
        context = SimpleNamespace(user_data={})

        await bot.start_quiz(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێداچوونەوەی سەرچاوە", query.message.reply_text.await_args.args[0])
        self.assertNotIn("quiz", context.user_data)
        self.assertFalse(bot.lesson_quiz_is_available(lesson_id))


    async def test_stale_finish_callback_cannot_complete_lesson_in_inactive_course(self):
        query = SimpleNamespace(
            data="finish_grammar_32",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=False),
            patch.object(bot, "complete_beta_lesson") as beta_progress,
            patch.object(bot, "complete_lesson_with_rewards") as official_reward,
        ):
            await bot.finish_lesson(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێشووتر", query.message.reply_text.await_args.args[0])
        beta_progress.assert_not_called()
        official_reward.assert_not_called()


    async def test_duplicate_beta_finish_callback_does_not_repeat_progress_or_rewards(self):
        query = SimpleNamespace(
            data="finish_grammar_32",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "complete_beta_lesson", return_value=False) as beta_progress,
            patch.object(bot, "complete_lesson_with_rewards") as official_reward,
            patch.object(bot, "check_badges") as badge_check,
        ):
            await bot.finish_lesson(update, context)

        query.answer.assert_awaited_once()
        message = query.message.reply_text.await_args.args[0]
        self.assertIn("پێشتر بۆ پێشچوونی Beta تۆمار کراوە", message)
        self.assertIn("خەڵاتێکی بۆ نییە", message)
        beta_progress.assert_called_once_with(12345, "grammar_32")
        official_reward.assert_not_called()
        badge_check.assert_not_called()

    async def test_beta_draft_records_separate_progress_without_rewards(self):
        query = SimpleNamespace(
            data="finish_grammar_32",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "complete_beta_lesson", return_value=True) as beta_progress,
            patch.object(bot, "complete_lesson_with_rewards") as official_reward,
            patch.object(bot, "next_course_lesson", return_value=None),
        ):
            await bot.finish_lesson(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        self.assertIn("پێشچوونی Beta", query.message.reply_text.await_args.args[0])
        self.assertIn("هیچ XP", query.message.reply_text.await_args.args[0])
        beta_progress.assert_called_once_with(12345, "grammar_32")
        official_reward.assert_not_called()

    async def test_final_beta_lesson_does_not_claim_official_course_completion(self):
        query = SimpleNamespace(
            data="finish_grammar_50",
            from_user=SimpleNamespace(id=12345),
            answer=AsyncMock(),
            message=SimpleNamespace(reply_text=AsyncMock()),
        )
        update = SimpleNamespace(callback_query=query)
        context = SimpleNamespace(user_data={})

        with (
            patch.object(bot, "can_open", return_value=True),
            patch.object(bot, "complete_beta_lesson", return_value=True) as beta_progress,
            patch.object(bot, "complete_lesson_with_rewards") as official_reward,
            patch.object(bot, "next_course_lesson", return_value=None),
        ):
            await bot.finish_lesson(update, context)

        query.answer.assert_awaited_once()
        query.message.reply_text.assert_awaited_once()
        final_message = query.message.reply_text.await_args.args[0]
        self.assertIn("ڕێڕەوی تاقیکاریی Beta تەواو بوو", final_message)
        self.assertIn("\n\n🧪 ڕێڕەوی تاقیکاریی Beta تەواو بوو", final_message)
        self.assertIn("چاوەڕوانی پێداچوونەوە و پەسەندکردنی ئەکادیمین", final_message)
        self.assertIn("تەواوبوونی فەرمی کۆرس نییە", final_message)
        self.assertNotIn("🎓 ئەم کۆرسە تەواو بوو", final_message)
        beta_progress.assert_called_once_with(12345, "grammar_50")
        official_reward.assert_not_called()

    async def test_approved_lesson_keeps_its_completion_button(self):
        self.assertFalse(bot.lesson_is_pending_review("grammar_31"))
        self.assertIsNotNone(bot.lesson_keyboard("grammar_31"))


class Course4GrammarLessons14To17Tests(unittest.TestCase):
    def test_lessons_14_to_17_are_complete_and_scientifically_qualified(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["id"]: item for item in source["lessons"]}
        for lesson_id in ("grammar_14", "grammar_15", "grammar_16", "grammar_17"):
            with self.subTest(lesson=lesson_id):
                lesson = lessons[lesson_id]
                self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
                self.assertEqual(len(lesson["quiz"]), 8)
                self.assertEqual(len(lesson["activities"]), 3)
                self.assertEqual(len(lesson["exercises"]), 5)
                self.assertEqual(len(lesson["comprehension"]), 10)
                self.assertEqual(len(lesson["appendix"]), 9 if lesson_id == "grammar_15" else 8)
        self.assertIn("ئەرکی گرووپی ناوی", " ".join(lessons["grammar_14"]["key_points"]))
        self.assertIn("پێشترتەواو", " ".join(lessons["grammar_15"]["key_points"]))
        self.assertIn("بە تەنها کاتی داهاتوو نیشان نادات", " ".join(lessons["grammar_16"]["key_points"]))
        self.assertIn("نەرێی داخوازی", " ".join(lessons["grammar_17"]["appendix"]))

    def test_lessons_14_to_17_registered_in_all_course4_indexes(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected = [f"grammar_{n:02d}" for n in range(1, 51)]
        self.assertEqual([x["id"] for x in source["lessons"]], expected)
        self.assertEqual([x["id"] for x in plan["lessons"]], expected)
        self.assertEqual(plan["lesson_count"], 50)
        course = next(x for x in catalog["courses"] if x["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected)


class Course4TerminologyConsistencyTests(unittest.TestCase):
    def test_numeral_term_is_identical_across_all_lessons(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        serialized = json.dumps(source, ensure_ascii=False)
        self.assertIn("پۆلی وشەی ژمارەیی", serialized)
        self.assertNotIn("پۆلی ژمارەیی", serialized.replace("پۆلی وشەی ژمارەیی", ""))
        for lesson in source["lessons"]:
            with self.subTest(lesson=lesson["id"]):
                lesson_number = int(lesson["id"].rsplit("_", 1)[1])
                expected_status = (
                    "owner_review_pending_expanded_draft"
                    if lesson_number >= 32
                    else (
                        "internal_cross_lesson_synthesis_no_external_source_mapping"
                        if lesson["id"] == "grammar_13"
                        else "scientific_review_complete_with_qualified_notes"
                    )
                )
                self.assertEqual(lesson["review_status"], expected_status)

    def test_previously_standardized_core_terms_remain_stable(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        serialized = json.dumps(source, ensure_ascii=False)
        self.assertNotIn("ئاوەڵکار", serialized)
        self.assertIn("هاوەڵکار", serialized)
        self.assertIn("دیارخەری ئاماژە", serialized)
        self.assertIn("جێناوی ئاماژە", serialized)
        self.assertIn("ژمارەی ڕێزمانی", serialized)
        self.assertIn("کۆی نەناسراو", serialized)
        self.assertNotIn("کۆی گشتی/نەناسراو", serialized)


class Course4ComprehensionFormattingTests(unittest.TestCase):
    def test_comprehension_questions_have_single_kurdish_digit_prefix(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        for lesson in source["lessons"]:
            with self.subTest(lesson=lesson["id"]):
                if lesson.get("review_status") == "owner_review_pending_expanded_draft":
                    self.assertTrue(lesson.get("source_markdown", "").strip())
                    continue
                questions = lesson["comprehension"][1:9]
                self.assertEqual(len(questions), 8)
                for number, question in enumerate(questions, start=1):
                    expected = f"{str(number).translate(str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩'))}. "
                    self.assertTrue(question.startswith(expected), question)
                    self.assertFalse(question.startswith(f"{expected}{expected}"), question)


class Course4AdapterIsolationTests(unittest.TestCase):
    def test_extended_sections_are_opt_in_and_do_not_leak_to_shared_courses(self):
        from course_lesson_adapters import adapt_unified_orthography_lessons

        payload = {
            "course_id": "adapter_scope_test",
            "lessons": [{
                "number": 1,
                "title": "تاقیکردنەوە",
                "appendix": ["پاشکۆی تاقیکردنەوە"],
                "activities": ["چالاکیی تاقیکردنەوە"],
                "quiz": [],
            }],
        }
        default_lessons, _ = adapt_unified_orthography_lessons(payload)
        course4_lessons, _ = adapt_unified_orthography_lessons(
            payload, include_extended_sections=True
        )
        self.assertNotIn("پاشکۆی تاقیکردنەوە", default_lessons["adapter_scope_test_01"]["content"])
        self.assertNotIn("چالاکیی تاقیکردنەوە", default_lessons["adapter_scope_test_01"]["content"])
        self.assertIn("پاشکۆی تاقیکردنەوە", course4_lessons["adapter_scope_test_01"]["content"])
        self.assertIn("چالاکیی تاقیکردنەوە", course4_lessons["adapter_scope_test_01"]["content"])


class Course4AdverbLessonsTests(unittest.TestCase):
    def test_adverb_lessons_have_complete_learning_components(self):
        source = json.loads((ROOT / 'course_data' / 'grammar_course4_lessons.json').read_text(encoding='utf-8'))
        lessons = {item['id']: item for item in source['lessons']}
        for lesson_id in ('grammar_19', 'grammar_20', 'grammar_21'):
            item = lessons[lesson_id]
            self.assertEqual(len(item['key_points']), 8)
            self.assertEqual(len(item['examples']), 8)
            self.assertEqual(len(item['activities']), 3)
            self.assertEqual(len(item['exercises']), 5)
            self.assertEqual(len(item['comprehension']) - 2, 8)
            self.assertEqual(len(item['quiz']), 8)
            self.assertEqual(len(item['appendix']), 8)
            self.assertTrue(all(question['explanation'].strip() for question in item['quiz']))
        self.assertIn('hardly', ' '.join(lessons['grammar_20']['key_points']))
        self.assertIn('هاوەڵناو', ' '.join(lessons['grammar_21']['key_points']))


class Course4PrepositionLesson22Tests(unittest.TestCase):
    def test_lesson_22_is_complete_and_scientifically_qualified(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_22")
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["key_points"]), 8)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["appendix"]), 8)
        self.assertIn("ـە", " ".join(lesson["key_points"]))
        self.assertIn("بەرکاری ناڕاستەوخۆ", " ".join(lesson["key_points"]))
        self.assertIn("ماددەی ڕاستەوخۆی نێردراوی خاوەن پڕۆژە", " ".join(lesson["appendix"]))
        self.assertTrue(all(q["explanation"].strip() for q in lesson["quiz"]))

    def test_course4_catalogs_register_31_lessons_without_changing_other_courses(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected = [f"grammar_{n:02d}" for n in range(1, 51)]
        self.assertEqual([x["id"] for x in source["lessons"]], expected)
        self.assertEqual([x["id"] for x in plan["lessons"]], expected)
        self.assertEqual(plan["lesson_count"], 50)
        course = next(x for x in catalog["courses"] if x["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected)


class Course4ConjunctionLesson23Tests(unittest.TestCase):
    def test_lesson_23_is_complete_and_distinguishes_particles(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_23")
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["key_points"]), 8)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["appendix"]), 9)
        self.assertIn("پارتیکڵی زیادکردن", " ".join(lesson["key_points"]))
        self.assertTrue(all(q["explanation"].strip() for q in lesson["quiz"]))

    def test_course4_has_31_registered_lessons(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected = [f"grammar_{n:02d}" for n in range(1, 51)]
        self.assertEqual([x["id"] for x in source["lessons"]], expected)
        self.assertEqual([x["id"] for x in plan["lessons"]], expected)
        self.assertEqual(plan["lesson_count"], 50)
        course = next(x for x in catalog["courses"] if x["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected)


class Course4VocativeLesson24Tests(unittest.TestCase):
    def test_lesson_24_is_complete_and_distinguishes_vocative_markers(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_24")
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["key_points"]), 8)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["appendix"]), 8)
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        for marker in ("یا", "ئەی", "ا"):
            self.assertIn(marker, joined)
        self.assertIn("فراوانکردنی فێرکاری", " ".join(lesson["appendix"]))
        self.assertTrue(all(q["explanation"].strip() for q in lesson["quiz"]))

    def test_course4_has_31_registered_lessons(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected = [f"grammar_{n:02d}" for n in range(1, 51)]
        self.assertEqual([x["id"] for x in source["lessons"]], expected)
        self.assertEqual([x["id"] for x in plan["lessons"]], expected)
        self.assertEqual(plan["lesson_count"], 50)
        course = next(x for x in catalog["courses"] if x["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected)


class Course4IzafaLesson25Tests(unittest.TestCase):
    def test_lesson_25_is_complete_and_qualifies_dialectal_forms(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_25")
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["key_points"]), 8)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["appendix"]), 8)
        text = " ".join(lesson["key_points"] + lesson["appendix"])
        for sample in ("چەم سیروان", "پارک ئاشتی", "چرای ماڵ", "دەسەی گوڵ", "پەنجەرەی شکاو"):
            self.assertIn(sample, text)
        self.assertIn("تەشبیهی", " ".join(lesson["appendix"]))
        self.assertIn("ئیزافەی کراوە", " ".join(lesson["key_points"]))
        self.assertIn("پاشبەستی خاوەنداری", " ".join(lesson["key_points"]))
        self.assertTrue(all(q["explanation"].strip() for q in lesson["quiz"]))

    def test_course4_has_31_registered_lessons(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected = [f"grammar_{n:02d}" for n in range(1, 51)]
        self.assertEqual([x["id"] for x in source["lessons"]], expected)
        self.assertEqual([x["id"] for x in plan["lessons"]], expected)
        self.assertEqual(plan["lesson_count"], 50)
        course = next(x for x in catalog["courses"] if x["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected)


class Course4IzafaCrossLessonConsistencyTests(unittest.TestCase):
    def test_lesson25_preserves_lesson6_and_lesson14_distinctions(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        l6 = " ".join(lessons[6]["key_points"] + lessons[6]["appendix"])
        l14 = " ".join(lessons[14]["key_points"] + lessons[14]["examples"][3])
        l25 = " ".join(lessons[25]["key_points"] + lessons[25]["appendix"])
        self.assertIn("ئیزافەی کراوە", l6)
        self.assertIn("ئیزافەی داخراو", l6)
        self.assertIn("پاشبەستەی خاوەندارییە", l14)
        self.assertIn("ئیزافەی کراوە", l25)
        self.assertIn("ئیزافەی داخراو", l25)
        self.assertIn("پاشبەستی خاوەنداری", l25)
        self.assertIn("نامە درێژەکە", l25)
        self.assertIn("گوڵەکەی چاند", l25)


class Course4Lesson18SourceExclusionTests(unittest.TestCase):
    def test_lesson18_appendix_has_no_withdrawn_source_or_page_mapping(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["number"] == 18)
        appendix = " ".join(lesson["appendix"])
        self.assertNotIn("Active and Passive", appendix)
        self.assertNotIn("لاپەڕەی ١١٢", appendix)
        self.assertIn("هیچ کتێب یان فایلێکی دەرەکی", appendix)


class Course4CurriculumDocumentationConsistencyTests(unittest.TestCase):
    def test_all_lesson_titles_and_numbers_match_curriculum_plan(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        self.assertEqual(
            [(item["number"], item["title"]) for item in source["lessons"]],
            [(item["number"], item["title"]) for item in plan["lessons"]],
        )

    def test_active_appendix_has_no_withdrawn_auxiliary_verb_page_claim(self):
        appendix = (ROOT / "docs" / "COURSE4_GRAMMAR_APPENDIX.md").read_text(encoding="utf-8")
        section = appendix.split("## 36. وانەکانی ١٩–٢١ — هاوەڵکار", 1)[1].split("\n## 37.", 1)[0]
        self.assertNotIn("لاپەڕەی ١٢٥", section)
        self.assertNotIn("Rezmany_axawtny_kurdy.pdf", section)
        historical = appendix.split("## 34. تۆماری بڕیاری هەڵوەشاندنەوەی سەرچاوە", 1)[1].split("## 35.", 1)[0]
        self.assertNotIn("p.", historical)
        self.assertNotIn("pp.", historical)


class Course4PrepositionTerminologyConsistencyTests(unittest.TestCase):
    def test_preposition_synonyms_are_explicit_and_prefix_is_distinct(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        lesson2 = " ".join(lessons[2]["key_points"] + lessons[2]["appendix"])
        lesson11 = " ".join(lessons[11]["key_points"] + lessons[11]["appendix"])
        lesson22 = " ".join(lessons[22]["key_points"] + lessons[22]["appendix"])
        self.assertIn("Preposition = پێشبەند", lesson2)
        self.assertIn("پێشبەند (Preposition", lesson22)
        self.assertIn("Prepositional Phrase؛ لە زاراوەی وانەکانی تر: گرێی پێشبەندی", lesson22)
        self.assertIn("لە پێشبەندەکاندا جێناوی لکاو", lesson11)
        self.assertNotIn("پێشگر/پێشبەند", lesson11)


class Course4VerbStemTerminologyTests(unittest.TestCase):
    def test_present_and_past_stem_terms_are_distinct_and_aligned(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        plan_titles = {item["number"]: item["title"] for item in plan["lessons"]}
        self.assertEqual(lessons[16]["title"], plan_titles[16])
        self.assertIn("بنجی ئێستا", " ".join(lessons[16]["key_points"]))
        self.assertNotIn("بنجی ئێستا/ڕەگی ئێستا", " ".join(lessons[16]["key_points"]))
        self.assertIn("بنجی ڕابردوو", " ".join(lessons[15]["key_points"]))
        self.assertIn("Present stem = بنجی ئێستا", " ".join(lessons[13]["appendix"]))
        self.assertIn("Past stem = بنجی ڕابردوو", " ".join(lessons[13]["appendix"]))
        self.assertIn("Infinitive = چاوگ", " ".join(lessons[13]["appendix"]))


class Course4CliticAndPastPerfectTerminologyTests(unittest.TestCase):
    def test_clitic_enclitic_and_suffix_are_not_conflated(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        self.assertIn("Clitic = لکاو", lessons[11]["appendix"][0])
        self.assertIn("Enclitic = پاشبەستە (لکاوی دواوە)", lessons[11]["appendix"][0])
        self.assertIn("Enclitic = پاشبەستە", " ".join(lessons[12]["appendix"]))
        self.assertIn("Clitic = لکاو", " ".join(lessons[13]["appendix"]))
        self.assertIn("Enclitic = پاشبەستە", " ".join(lessons[13]["appendix"]))
        self.assertIn("پاشبەستە لە پاشگر جیاوازە", " ".join(lessons[13]["key_points"]))

    def test_boo_is_not_automatically_classified_as_a_suffix(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["number"] == 15)
        content = " ".join(lesson["key_points"] + lesson["appendix"])
        self.assertNotIn("پاشگرەکانی «ـووە/ـوە» و «بوو»", content)
        self.assertIn("نابێت بە خۆکار هەموویان وەک پاشگر پۆلێن بکرێن", content)


class Course4TenseAspectMoodConsistencyTests(unittest.TestCase):
    def test_tense_aspect_mood_are_separate_concepts_across_lessons_15_to_17(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        lesson15 = " ".join(lessons[15]["key_points"] + lessons[15]["appendix"])
        lesson16 = " ".join(lessons[16]["key_points"] + lessons[16]["appendix"])
        lesson17 = " ".join(lessons[17]["key_points"] + lessons[17]["appendix"])
        self.assertIn("Tense = دەم/کاتی ڕێزمانی", lesson15)
        self.assertIn("Aspect = «ڕووی کردار»", lesson15)
        self.assertIn("Mood = ڕەوشی کردار", lesson17)
        self.assertIn("ڕووی کردار", lesson17)
        self.assertIn("فۆڕمی ڕانەبردوو", lesson16)
        self.assertIn("خوێندنەوەی ئێستا، عادەت یان داهاتوو", lesson16)
        self.assertIn("کاتیی ڕاستەقینە", lesson16)
        self.assertNotIn("Aspect = ڕەوش", lesson15 + lesson16 + lesson17)
        self.assertNotIn("Mood = دەم", lesson15 + lesson16 + lesson17)

    def test_lesson15_aspect_labels_are_not_presented_as_four_identical_tenses(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["number"] == 15)
        note = lesson["appendix"][-1]
        self.assertIn("ڕابردووی بەردەوام", note)
        self.assertIn("ڕابردووی تەواو", note)
        self.assertIn("پێشترتەواو", note)
        self.assertIn("نە بانگەشەی یەک شیکردنەوەی تاک", note)


class Course4VoiceAndErgativeAlignmentConsistencyTests(unittest.TestCase):
    def test_lesson18_active_example_accounts_for_past_transitive_clitic(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        lesson18 = lessons[18]
        active_example = " ".join(lesson18["key_points"] + [item[1] for item in lesson18["examples"]])
        self.assertIn("«ـی» لکاوی نیشانەی بکەری سێیەمی تاکە", active_example)
        self.assertIn("وانەی ١٢", active_example)
        self.assertIn("نابێت بە خاوەنداری لێک بدرێتەوە", active_example)
        lesson15_example = lessons[15]["examples"][0][1]
        self.assertIn("«ـی» لکاوی نیشانەی بکەری سێیەمی تاکە", lesson15_example)
        self.assertIn("وانەی ١٢", lesson15_example)

    def test_voice_is_distinguished_from_ergative_alignment(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson18 = next(item for item in source["lessons"] if item["number"] == 18)
        appendix = " ".join(lesson18["appendix"])
        self.assertIn("Voice", appendix)
        self.assertIn("Alignment", appendix)
        self.assertIn("جیاوازن", appendix)
        self.assertIn("نابێت «لەلایەن» وەک نیشانەی یەکگرتووی ئەنجامدەر", appendix)


class Course4Lessons18To21CrossAuditTests(unittest.TestCase):
    def test_quiz_schema_has_no_duplicate_or_unrecognized_question_fields(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        for number in range(18, 22):
            for question in lessons[number]["quiz"]:
                self.assertEqual(set(question), {"q", "options", "answer", "explanation"})
        self.assertIn("خوێندنەوەی چالاکی ڕابردووی تێپەڕ", lessons[18]["quiz"][2]["q"])

    def test_lesson21_does_not_present_incomplete_darkirdin_sentence_as_valid_example(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson21 = next(item for item in source["lessons"] if item["number"] == 21)
        example = lesson21["examples"][0][1]
        self.assertIn("ڕستەی نموونەی سەرچاوە تەواو و ڕوون نەبوو", example)
        self.assertNotIn("ئەو دەرکردنی لە ژوورەکە.", example)
        self.assertIn("پێویستیان بە پشکنینی فەرهەنگی هەیە", " ".join(lesson21["appendix"]))


class Course4Lessons19To25CrossAuditTests(unittest.TestCase):
    def test_adverb_adverbial_and_derived_form_distinctions_persist(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        l19 = " ".join(lessons[19]["key_points"] + lessons[19]["appendix"])
        l20 = " ".join(lessons[20]["key_points"] + lessons[20]["appendix"])
        l21 = " ".join(lessons[21]["key_points"] + lessons[21]["appendix"])
        self.assertIn("هاوەڵکار (Adverb) پۆلی وشەییە", l19)
        self.assertIn("هاوەڵکاری (Adverbial) ئەرکی ڕستەییە", l19)
        self.assertIn("پێشبەند", l20)
        self.assertIn("پێشگری کوردی", l20)
        self.assertIn("hardly", l20)
        self.assertIn("هاوەڵناو دەتوانێت ئەرکی هاوەڵکاری ببینێت", l21)
        self.assertIn("پۆلی وشە و ئەرکی ڕستەیی جیاوازن", l21)

    def test_preposition_conjunction_and_vocative_roles_are_not_conflated(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        l22 = " ".join(lessons[22]["key_points"] + lessons[22]["appendix"])
        l23 = " ".join(lessons[23]["key_points"] + lessons[23]["appendix"])
        l24 = " ".join(lessons[24]["key_points"] + lessons[24]["appendix"])
        self.assertIn("پێشبەند (Preposition", l22)
        self.assertIn("ـە", l22)
        self.assertIn("پارتیکڵی زیادکردن/جەخت", l23)
        self.assertIn("ئامرازی بانگکردن", l24)
        self.assertIn("پێویستی بە سیاق و پێکهاتەی ڕستە هەیە", l24)
        self.assertIn("یا", l24)
        self.assertIn("ئامرازی پەیوەندی", l24)

    def test_izafa_distinction_remains_aligned_with_lessons_6_and_14(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        l6 = " ".join(lessons[6]["key_points"] + lessons[6]["appendix"])
        l14 = " ".join(lessons[14]["examples"][3])
        l25 = " ".join(lessons[25]["key_points"] + lessons[25]["appendix"])
        self.assertIn("ئیزافەی کراوە", l6)
        self.assertIn("ئیزافەی داخراو", l6)
        self.assertIn("گوڵەکەی چاند", l14)
        self.assertIn("ئیزافەی کراوە", l25)
        self.assertIn("ئیزافەی داخراو", l25)
        self.assertIn("پاشبەستی خاوەنداری", l25)
        self.assertIn("ئەردەڵان/سنە", l25)
        self.assertIn("نابێت وەک یاسای گشتی", l25)

    def test_lessons_22_to_27_keep_functional_categories_distinct(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        l22 = " ".join(lessons[22]["key_points"] + lessons[22]["appendix"])
        l23 = " ".join(lessons[23]["key_points"] + lessons[23]["appendix"])
        l24 = " ".join(lessons[24]["key_points"] + lessons[24]["appendix"])
        l25 = " ".join(lessons[25]["key_points"] + lessons[25]["appendix"])
        l26 = " ".join(lessons[26]["key_points"] + lessons[26]["appendix"])
        self.assertIn("پێشبەند", l22)
        self.assertIn("ئامرازی پەیوەندی", l23)
        self.assertIn("«ـیش»", l23)
        self.assertIn("لکاوی زیادکردن/جەخت", l26)
        self.assertIn("ئامرازی بانگکردن", l24)
        self.assertIn("ئیزافە", l25)
        self.assertIn("پارتیکڵی گفتوگۆیی", l26)
        self.assertIn("جێناوی ئاماژەی سەربەخۆ", l26)
        self.assertIn("دیارخەری ئاماژە", l26)
        self.assertIn("وانەی ٢٥", l26)
        self.assertNotIn("ش/یش", l23)

    def test_lessons_19_to_25_keep_the_standard_quiz_schema_and_counts(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = {item["number"]: item for item in source["lessons"]}
        for number in range(19, 26):
            lesson = lessons[number]
            self.assertEqual(len(lesson["key_points"]), 8)
            self.assertEqual(len(lesson["examples"]), 8)
            self.assertEqual(len(lesson["activities"]), 3)
            self.assertEqual(len(lesson["exercises"]), 5)
            self.assertEqual(len(lesson["comprehension"]), 10)
            self.assertEqual(len(lesson["quiz"]), 8)
            self.assertTrue(all(set(q) == {"q", "options", "answer", "explanation"} for q in lesson["quiz"]))
            self.assertTrue(all(0 <= q["answer"] < len(q["options"]) for q in lesson["quiz"]))
            self.assertTrue(all(q["explanation"].strip() for q in lesson["quiz"]))


class Course4DiscourseParticleLesson26Tests(unittest.TestCase):
    def test_lesson_26_has_complete_lesson_schema_and_source_caveats(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_26")
        self.assertEqual(lesson["number"], 26)
        self.assertEqual(len(lesson["key_points"]), 10)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertTrue(all(0 <= item["answer"] < len(item["options"]) for item in lesson["quiz"]))
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        for term in ("پارتیکڵی گفتوگۆیی", "لکاوی زیادکردن/جەخت", "کۆرپەس", "Radnia (2022)", "Ahmadi (2021)"):
            self.assertIn(term, joined)

    def test_lesson_26_examples_are_sorani_discourse_particle_examples(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_26")
        examples = " ".join(" ".join(item) for item in lesson["examples"])
        for form in ("ئەرێ", "جا", "باشە", "ئەوە", "خۆ", "مەگەم", "دەی", "ڕاست"):
            self.assertIn(form, examples)

    def test_lesson_23_additive_ish_is_cross_referenced_as_a_clitic(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_23")
        self.assertTrue(any("لکاوی زیادکردن/جەختە" in item for item in lesson["appendix"]))
        self.assertIn("«ـیش»", " ".join(lesson["key_points"] + lesson["appendix"]))
        self.assertNotIn("ش/یش", " ".join(lesson["key_points"] + lesson["appendix"]))

    def test_course4_quiz_overrides_preserve_original_bank_and_apply_44_reviewed_replacements(self):
        override_file = bot.load_json("course_data/grammar_course4_quiz_overrides.json")
        overrides = override_file["overrides"]
        self.assertEqual(len(overrides), 44)
        raw_by_id = {lesson["id"]: lesson for lesson in bot.GRAMMAR_COURSE4_DRAFT["lessons"]}
        seen = set()
        for override in overrides:
            lesson_id = override["lesson_id"]
            index = override["question_index"]
            key = (lesson_id, index)
            self.assertNotIn(key, seen)
            seen.add(key)
            self.assertEqual(raw_by_id[lesson_id]["quiz"][index], override["original_snapshot"])
            replacement = override["replacement"]
            runtime_question = bot.QUIZ_DATA[lesson_id][index]
            self.assertEqual(runtime_question["question"], replacement["q"])
            self.assertEqual(runtime_question["options"], replacement["options"])
            self.assertEqual(runtime_question["answer"], replacement["options"][replacement["answer"]])
            self.assertEqual(runtime_question["explanation"], replacement["explanation"])
            self.assertEqual(len(replacement["options"]), 4)
        self.assertEqual(
            sum(len(bot.QUIZ_DATA[f"grammar_{number:02d}"]) for number in range(1, 31)),
            240,
        )

    def test_course4_has_50_lessons_and_plan_records_lesson_28(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        self.assertEqual(source["lesson_count"], 50)
        self.assertEqual(plan["lesson_count"], 50)
        self.assertEqual(plan["lessons"][-1]["id"], "grammar_50")
        self.assertEqual(plan["source_alignment_map"][-1]["lessons"], "50")


class Course4InterjectionLesson27Tests(unittest.TestCase):
    def test_lesson_27_has_complete_schema_and_scientific_distinctions(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_27")
        self.assertEqual(lesson["number"], 27)
        self.assertEqual(len(lesson["key_points"]), 10)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertTrue(all(len(item) == 2 for item in lesson["examples"]))
        self.assertTrue(all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 and q["explanation"].strip() for q in lesson["quiz"]))
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        for term in ("Interjection", "Vocative", "ڕستەی سەرسووڕمان", "Ameka (1992)", "McCarus (2009)", "Taha (2022)"):
            self.assertIn(term, joined)
        for form in ("ئەرێ", "«جا»", "«خۆ»", "«دەی»"):
            self.assertIn(form, joined)

    def test_lesson_27_preserves_owner_list_and_distinguishes_lessons_24_and_26(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_27")
        appendix = " ".join(lesson["appendix"])
        for form in ("ئەک", "وەی", "هەی", "داد", "چش", "حەک", "بەهبەهـ", "هەیهۆ", "هەیهوو", "دەی", "خۆ", "جا"):
            self.assertIn(form, appendix)
        self.assertIn("ئامرازی بانگکردن", " ".join(lesson["key_points"]))
        self.assertIn("پارتیکڵی گفتوگۆیی", " ".join(lesson["key_points"]))


class Course4InfinitiveLesson28Tests(unittest.TestCase):
    def test_lesson_28_has_complete_schema_and_corrects_the_five_group_analysis(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_28")
        self.assertEqual(lesson["number"], 28)
        self.assertEqual(len(lesson["key_points"]), 14)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertTrue(all(len(item) == 2 for item in lesson["examples"]))
        self.assertTrue(all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 and q["explanation"].strip() for q in lesson["quiz"]))
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        for term in ("Infinitive", "Past Stem", "Present Stem", "Kareem (2016)", "Haig (2018)", "Ahmadi (2021)"):
            self.assertIn(term, joined)
        self.assertIn("گروپی بنجی ڕابردوو", joined)
        self.assertIn("پێنج جۆری سەربەخۆی چاوگ", joined)
        self.assertIn("بنجی ئێستا", joined)

    def test_lesson_28_separates_finite_forms_and_keeps_gorani_examples_qualified(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_28")
        joined = " ".join(lesson["key_points"] + lesson["examples"][-1] + lesson["appendix"])
        self.assertIn("خواردم", joined)
        self.assertIn("واردەیێ", joined)
        self.assertIn("هەورامی", joined)
        self.assertIn("چاوگ", joined)


class Course4DerivedVerbLesson29Tests(unittest.TestCase):
    def test_lesson_29_has_complete_schema_and_distinguishes_derivation(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_29")
        self.assertEqual(lesson["number"], 29)
        self.assertEqual(len(lesson["key_points"]), 14)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertTrue(all(len(item) == 2 for item in lesson["examples"]))
        self.assertTrue(all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 and q["explanation"].strip() for q in lesson["quiz"]))
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        for term in ("Derivation", "Inflection", "Ahmadi (2021)", "Ahmadi & Mahmudi (2023)", "پارتیکڵی کردار", "ـەوە"):
            self.assertIn(term, joined)
        self.assertIn("لە هەموو توێژینەوەکاندا یەکسان نییە", joined)
        self.assertIn("چوارچێوەیەکی شیکارییە", joined)

    def test_lesson_29_separates_derived_verbs_from_compounds_and_particles(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_29")
        joined = " ".join(lesson["key_points"] + lesson["appendix"] + [" ".join(x) for x in lesson["examples"]])
        self.assertIn("مراندن", joined)
        self.assertIn("سووتاندن", joined)
        self.assertIn("هەڵگرتن", joined)
        self.assertIn("کردارە لێکدراوەکان", joined)
        self.assertIn("پارتیکڵ-کردار", joined)
        self.assertIn("پاشگری داڕێژەیی", joined)
        self.assertIn("وانەی ٣٠", joined)
        self.assertNotIn("Rezmany_axawtny_kurdy.pdf", joined.split("سنووری بەڵگە", 1)[0])

    def test_course4_has_50_registered_lessons_and_pagination_reaches_lesson_50(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        self.assertEqual(source["lesson_count"], 50)
        self.assertEqual(plan["lesson_count"], 50)
        self.assertEqual(plan["lessons"][-1]["id"], "grammar_50")
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], [f"grammar_{number:02d}" for number in range(1, 51)])


class Course4ComplexPredicateLesson30Tests(unittest.TestCase):
    def test_lesson_30_schema_and_complex_predicate_components(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_30")
        self.assertEqual(lesson["number"], 30)
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["key_points"]), 14)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertTrue(all(len(item) == 2 for item in lesson["examples"]))
        self.assertTrue(all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 and q["explanation"].strip() for q in lesson["quiz"]))
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        for term in ("Kareem (2016)", "Ahmadi (2021)", "Ahmadi (2020)", "Light Verb", "Non-verbal Element", "پارتیکڵ"):
            self.assertIn(term, joined)

    def test_lesson_30_distinguishes_light_and_lexical_verbs_and_frameworks(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_30")
        joined = " ".join(lesson["key_points"] + lesson["appendix"] + [" ".join(x) for x in lesson["examples"]])
        for term in ("بەڵێن دان", "ئیستقالە دان", "ئامادەکردن", "NV", "LV", "ڕێباز"):
            self.assertIn(term, joined)
        self.assertIn("وانەی ٣١", joined)
        self.assertNotIn("Rezmany_axawtny_kurdy.pdf", joined.split("سنووری بەڵگە", 1)[0])



class Course4TerminologyChainTests(unittest.TestCase):
    def test_course4_uses_consistent_preposition_interjection_and_verb_stem_terms(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lessons = source["lessons"]
        all_text = " ".join(
            value
            for lesson in lessons
            for value in self._strings(lesson)
        )
        self.assertNotIn("پریپۆزیشن", all_text)
        self.assertNotIn("ئامرازی سەرسوڕمان", all_text)
        self.assertIn("پێشبەند (Preposition", all_text)
        self.assertIn("ئامرازی سەرسووڕمان (Interjection)", all_text)
        lesson13 = next(item for item in lessons if item["id"] == "grammar_13")
        glossary = " ".join(lesson13["appendix"])
        self.assertIn("Root = ڕەگ", glossary)
        self.assertIn("Verb stem = بنج", glossary)
        self.assertIn("Root و Stem هاوتای یەکتر نین", glossary)
        lesson16 = next(item for item in lessons if item["id"] == "grammar_16")
        self.assertIn("بنجی ئێستا", lesson16["title"])
        self.assertNotIn("بنەمای ئێستا", all_text)
        self.assertNotIn("بنەمای ڕابردوو", all_text)

    @staticmethod
    def _strings(value):
        if isinstance(value, str):
            return [value]
        if isinstance(value, list):
            return [part for item in value for part in Course4TerminologyChainTests._strings(item)]
        if isinstance(value, dict):
            return [part for item in value.values() for part in Course4TerminologyChainTests._strings(item)]
        return []


class Course4NominalizedInfinitiveLesson31Tests(unittest.TestCase):
    def test_lesson_31_schema_and_nominalization_evidence(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_31")
        self.assertEqual(lesson["number"], 31)
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["key_points"]), 14)
        self.assertEqual(len(lesson["examples"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertTrue(all(len(item) == 2 for item in lesson["examples"]))
        self.assertTrue(all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 and q["explanation"].strip() for q in lesson["quiz"]))
        joined = " ".join(lesson["key_points"] + lesson["appendix"] + [" ".join(x) for x in lesson["examples"]])
        for term in ("Kareem (2016)", "Salavati", "Ahmadi (2018)", "کوشتنی ئاژەڵەکە", "دەنگدانمان", "Nominalization"):
            self.assertIn(term, joined)
        self.assertIn("پەیوەندیی وانەی ٢٨ و ٣١", joined)
        self.assertIn("-in/-n", joined)
        self.assertIn("نابێت وەک یاسای سۆرانی پێشکەش بکرێن", joined)

    def test_lesson_31_does_not_assert_unverified_five_and_seven_lists(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_31")
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        self.assertIn("پێنج تایبەتمەندیی ناوی", joined)
        self.assertIn("حەوت ئەرکی سینتاکسی", joined)
        self.assertIn("پشتڕاست نەکرانەوە", joined)
        self.assertIn("وانەی ٣٠", joined)
        self.assertNotIn("Rezmany_axawtny_kurdy.pdf", joined.split("سنووری", 1)[0])


class Course4NounLesson3Tests(unittest.TestCase):
    def test_lesson_3_noun_expansion_keeps_runtime_schema_and_curriculum_alignment(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_03")
        planned = next(item for item in plan["lessons"] if item["id"] == "grammar_03")
        self.assertEqual(lesson["title"], planned["title"])
        self.assertIn("تایبەتمەندییەکانی ناو", lesson["title"])
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["examples"]), 15)
        self.assertEqual(len(lesson["appendix"]), 30)
        self.assertTrue(all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 and q["explanation"].strip() for q in lesson["quiz"]))
        self.assertIn("ناوبەندی -ە- و -و-", lesson["quiz"][-1]["q"])
        correct_interfix_option = lesson["quiz"][-1]["options"][lesson["quiz"][-1]["answer"]]
        self.assertIn("-ە-", correct_interfix_option)
        self.assertIn("-و-", correct_interfix_option)
        joined = " ".join(lesson["key_points"] + lesson["appendix"])
        for term in ("-(y)ێک", "-ان", "-ەکان", "ڕەگەزی سروشتی", "ڕەگەزی ڕێزمانی", "Jambrović", "Thackston", "وانەی ٣١", "وانەی ٣٠", "گوڵەباخ", "گاکێوی", "ئاسنگەر", "کچۆڵە", "Mirmokri", "براکە", "هەڵۆیەک", "Interfix", "Huseen", "Shuani", "ناوبەندی -ە-", "ناوبەندی -و-", "دەنگی پەیوەستکەری فۆنۆلۆژی"):
            self.assertIn(term, joined)
        self.assertIn("پیاوەکان", joined)
        self.assertIn("پیاوێک", joined)
        self.assertIn("پۆلێنکردنی جیاوازن", joined)
        self.assertIn("بەڵگەی فەرهەنگی", joined)
        self.assertIn("dar-u-mar", joined)
        self.assertIn("گوڵەگەنم", joined)
        self.assertIn("ئاو و هەوا", joined)
        self.assertIn("کاندیدی پشکنین", joined)
        self.assertNotIn("Rezmany_axawtny_kurdy.pdf", joined.split("سنووری شێوەزار", 1)[0])


    def test_lesson_29_quiz_explanation_matches_ەوە_question(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_29")
        question = lesson["quiz"][5]
        self.assertIn("ـەوە", question["q"])
        self.assertIn("ـەوە", question["explanation"])
        self.assertNotIn("هەڵـ", question["explanation"])


class Course4Mainline26LessonPreservationTests(unittest.TestCase):
    def test_mainline_first_26_lessons_keep_full_learning_component_counts(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        lessons = {item["id"]: item for item in source["lessons"]}
        for number in range(1, 27):
            lesson_id = f"grammar_{number:02d}"
            with self.subTest(lesson=lesson_id):
                lesson = lessons[lesson_id]
                self.assertEqual(len(lesson["activities"]), 3)
                self.assertEqual(len(lesson["exercises"]), 5)
                self.assertEqual(len(lesson["comprehension"]), 10)
                self.assertEqual(len(lesson["quiz"]), 8)

    def test_course4_expansion_preserves_first_26_and_marks_only_new_drafts_pending(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        plan = json.loads(
            (ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8")
        )
        expected_ids = [f"grammar_{number:02d}" for number in range(1, 51)]
        self.assertEqual([item["id"] for item in source["lessons"]], expected_ids)
        self.assertEqual([item["id"] for item in plan["lessons"]], expected_ids)
        self.assertEqual(source["lesson_count"], 50)
        self.assertEqual(plan["lesson_count"], 50)
        for number in range(1, 27):
            self.assertNotEqual(
                source["lessons"][number - 1].get("review_status"),
                "owner_review_pending_expanded_draft",
            )
        for number in range(32, 51):
            lesson = source["lessons"][number - 1]
            self.assertEqual(lesson["review_status"], "owner_review_pending_expanded_draft")
            self.assertEqual(lesson["quiz"], [])

