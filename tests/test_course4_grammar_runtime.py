"""Regression tests for the owner-supplied replacement Course 4 grammar lesson."""
import json
import unittest
from pathlib import Path

import bot


ROOT = Path(__file__).resolve().parents[1]


class Course4GrammarRuntimeTests(unittest.TestCase):
    def test_course4_is_active_with_twenty_two_owner_supplied_lessons(self):
        self.assertTrue(bot.course_is_active("grammar"))
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], ["grammar_01", "grammar_02", "grammar_03", "grammar_04", "grammar_05", "grammar_06", "grammar_07", "grammar_08", "grammar_09", "grammar_10", "grammar_11", "grammar_12", "grammar_13", "grammar_14", "grammar_15", "grammar_16", "grammar_17", "grammar_18", "grammar_19", "grammar_20", "grammar_21", "grammar_22"])
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
            "grammar_13": "scientific_review_complete_with_qualified_notes",
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
        self.assertEqual([lesson["id"] for lesson in source["lessons"]], ["grammar_01", "grammar_02", "grammar_03", "grammar_04", "grammar_05", "grammar_06", "grammar_07", "grammar_08", "grammar_09", "grammar_10", "grammar_11", "grammar_12", "grammar_13", "grammar_14", "grammar_15", "grammar_16", "grammar_17", "grammar_18", "grammar_19", "grammar_20", "grammar_21", "grammar_22"])
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
        expected_appendix_counts = {"grammar_03": 4, "grammar_04": 6, "grammar_05": 7, "grammar_06": 6, "grammar_07": 5, "grammar_08": 6, "grammar_10": 4, "grammar_11": 5, "grammar_12": 5, "grammar_13": 13, "grammar_14": 8, "grammar_15": 8, "grammar_16": 8, "grammar_17": 8, "grammar_18": 4, "grammar_19": 8, "grammar_20": 8, "grammar_21": 8, "grammar_22": 8}
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
        self.assertIn("پریپۆزیشن", lesson2_text)
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
        expected_ids = [f"grammar_{number:02d}" for number in range(1, 23)]
        source_ids = [lesson["id"] for lesson in source["lessons"]]
        plan_ids = [lesson["id"] for lesson in plan["lessons"]]
        course = next(item for item in catalog["courses"] if item["id"] == "grammar")

        self.assertEqual(source_ids, expected_ids)
        self.assertEqual(plan["lesson_count"], 22)
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
    def test_lesson13_verb_morphology_is_complete_and_source_qualified(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        lesson = next(item for item in source["lessons"] if item["id"] == "grammar_13")
        self.assertEqual(lesson["number"], 13)
        self.assertEqual(lesson["review_status"], "scientific_review_complete_with_qualified_notes")
        self.assertEqual(len(lesson["quiz"]), 8)
        self.assertEqual(len(lesson["activities"]), 3)
        self.assertEqual(len(lesson["exercises"]), 5)
        self.assertEqual(len(lesson["comprehension"]), 10)
        self.assertGreaterEqual(len(lesson["appendix"]), 8)
        self.assertIn("چاوگ", " ".join(lesson["key_points"]))
        self.assertIn("ڕەگی کردار", " ".join(lesson["key_points"]))
        self.assertIn("کاریگەری", " ".join(lesson["key_points"]))
        self.assertIn("هۆکاری", " ".join(lesson["key_points"]))
        self.assertIn("دەنووسم", " ".join(item[1] for item in lesson["examples"]))
        self.assertIn("مرداندن", " ".join(item[1] for item in lesson["examples"]))
        self.assertIn("پوختەی وتاری دووەم", " ".join(lesson["key_points"]))
        self.assertIn("لاپەڕەکانی ٨٥–٨٧", " ".join(lesson["appendix"]))
        self.assertIn("ڕابردوو پێنج نیشانەی پاشگری", " ".join(lesson["appendix"]))
        self.assertIn("هیچ ڕستەیەک بەبێ کردار", " ".join(lesson["appendix"]))

    def test_lesson13_registered_in_source_plan_and_manifest(self):
        source = json.loads(
            (ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8")
        )
        plan = json.loads(
            (ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8")
        )
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected_ids = [f"grammar_{number:02d}" for number in range(1, 23)]
        self.assertEqual([item["id"] for item in source["lessons"]], expected_ids)
        self.assertEqual(plan["lesson_count"], 22)
        self.assertEqual([item["id"] for item in plan["lessons"]], expected_ids)
        course = next(item for item in catalog["courses"] if item["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected_ids)


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
                self.assertEqual(len(lesson["appendix"]), 8)
        self.assertIn("ئەرکی گرووپی ناوی", " ".join(lessons["grammar_14"]["key_points"]))
        self.assertIn("پێشترتەواو", " ".join(lessons["grammar_15"]["key_points"]))
        self.assertIn("بە تەنها کاتی داهاتوو نیشان نادات", " ".join(lessons["grammar_16"]["key_points"]))
        self.assertIn("نەرێی داخوازی", " ".join(lessons["grammar_17"]["appendix"]))

    def test_lessons_14_to_17_registered_in_all_course4_indexes(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected = [f"grammar_{n:02d}" for n in range(1, 23)]
        self.assertEqual([x["id"] for x in source["lessons"]], expected)
        self.assertEqual([x["id"] for x in plan["lessons"]], expected)
        self.assertEqual(plan["lesson_count"], 22)
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
                self.assertEqual(
                    lesson["review_status"],
                    "scientific_review_complete_with_qualified_notes",
                )

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

    def test_course4_catalogs_register_22_lessons_without_changing_other_courses(self):
        source = json.loads((ROOT / "course_data" / "grammar_course4_lessons.json").read_text(encoding="utf-8"))
        plan = json.loads((ROOT / "curriculum" / "grammar_course4_plan.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "courses.json").read_text(encoding="utf-8"))
        expected = [f"grammar_{n:02d}" for n in range(1, 23)]
        self.assertEqual([x["id"] for x in source["lessons"]], expected)
        self.assertEqual([x["id"] for x in plan["lessons"]], expected)
        self.assertEqual(plan["lesson_count"], 22)
        course = next(x for x in catalog["courses"] if x["id"] == "grammar")
        self.assertEqual(course["lesson_ids"], expected)
