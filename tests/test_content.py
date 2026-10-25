import json
import re
import unittest
import xml.etree.ElementTree as ET
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

    def test_lesson_catalog_contains_ten_lesson_records(self):
        self.assertEqual(set(self.lessons), {f"وانە_{index}" for index in range(1, 11)})
        for key, lesson in self.lessons.items():
            with self.subTest(lesson=key):
                self.assertTrue(lesson.get("title", "").strip())
                self.assertTrue(lesson.get("content", "").strip())

    def test_learning_path_matches_lesson_titles_and_order(self):
        expected = [
            "وانەی ١: سڵاو و ناساندنی خۆ",
            "وانەی ٢: ئەلفبێی کوردی",
            "وانەی ٣: وشەکانی ڕۆژانە",
            "وانەی ٤: ژمارەکان",
            "وانەی ٥: ڕەنگەکان",
            "وانەی ٦: لە ماڵ و قوتابخانە",
            "وانەی ٧: خێزان و کەسانی نزیک",
            "وانەی ٨: خواردن و خواردنەوە",
            "وانەی ٩: ڕۆژەکانی هەفتە و کات",
            "وانەی ١٠: ڕستەی سادە و پرسیارکردن",
        ]
        self.assertEqual(self.learning_path["lessons"], expected)
        for index, title in enumerate(expected, start=1):
            self.assertIn(f"وانە_{index}", self.lessons)
            self.assertEqual(self.lessons[f"وانە_{index}"]["title"], title.split(": ", 1)[1])
            self.assertTrue(self.lessons[f"وانە_{index}"]["content"].strip())

    def test_alphabet_quiz_definitions_match_lesson_explanations(self):
        lesson = self.lessons["وانە_2"]["content"]
        questions = self.quizzes["وانە_2"]
        alphabet_question = next(question for question in questions if question["question"] == "ئەلفبێ چییە؟")
        letter_question = next(question for question in questions if question["question"] == "پیت چییە؟")
        contrast_question = next(question for question in questions if question["question"].startswith("کام جووتە پیت"))

        self.assertIn("ئەلفبێ کۆمەڵە نیشانەیەکە", lesson)
        self.assertEqual(alphabet_question["answer"].rstrip("."), "ئەلفبێ کۆمەڵە نیشانەیەکە کە بە ڕێکخستنێکی دیاریکراو بۆ نووسینی زمانێک بەکاردێت")
        self.assertIn("پیت نیشانەی نووسراوە", lesson)
        self.assertEqual(letter_question["answer"], "نیشانەی نووسراوە")
        self.assertIn("«ر» و «ڕ» یەک نین", lesson)
        self.assertEqual(contrast_question["answer"], "«ر» و «ڕ»")

    def test_new_quiz_questions_use_terms_taught_in_their_lessons(self):
        lesson_one = self.lessons["وانە_1"]["content"]
        question_one = next(
            question for question in self.quizzes["وانە_1"]
            if question["question"] == "کام دەربڕین بۆ سڵاوکردنی بەیانی گونجاوە؟"
        )
        self.assertIn("بەیانی باش", lesson_one)
        self.assertEqual(question_one["answer"], "بەیانی باش")
        self.assertIn(question_one["answer"], lesson_one)

        lesson_three = self.lessons["وانە_3"]["content"]
        question_three = next(
            question for question in self.quizzes["وانە_3"]
            if question["question"].startswith("وشەی «بەڵێ»")
        )
        self.assertIn("بەڵێ — بۆ وەڵامی ئەرێنی", lesson_three)
        self.assertIn(question_three["answer"], lesson_three)

    def test_every_quiz_question_has_valid_options_and_answer(self):
        self.assertEqual(set(self.quizzes), {f"وانە_{index}" for index in range(1, 11)})
        for lesson, questions in self.quizzes.items():
            with self.subTest(lesson=lesson):
                self.assertGreaterEqual(len(questions), 6, "Each beginner lesson must provide at least six quiz questions.")
                question_texts = [question["question"].strip() for question in questions]
                self.assertEqual(
                    len(question_texts),
                    len(set(question_texts)),
                    "A lesson quiz must not repeat the same question text.",
                )
                for question in questions:
                    self.assertTrue(question["question"].strip())
                    self.assertGreaterEqual(len(question["options"]), 2)
                    self.assertEqual(len(question["options"]), len(set(question["options"])))
                    self.assertIn(question["answer"], question["options"])



    def test_example_expansion_remains_in_all_ten_lessons(self):
        required_phrases = {
            "وانە_1": ("نموونەی زیاتر", "خۆشحاڵم بە ناسینت"),
            "وانە_2": ("پیت و وشەی نموونە", "ڕیزبەندی و ژمارەکردنی پیتەکان"),
            "وانە_3": ("دەربڕینی زیاتر لە ژیانی ڕۆژانەدا", "دەتوانیت یارمەتیم بدەیت؟"),
            "وانە_4": ("نموونەی ژمارەکردنی زیاتر", "چەند دەفتەرت هەیە؟"),
            "وانە_5": ("نموونەی ڕەنگ لە ڕستەی زیاتر", "پێنووسەکەت چ ڕەنگێکە؟"),
            "وانە_6": ("وشە و ڕستەی زیاتر", "دەفتەرەکەم لە کوێیە؟"),
            "وانە_7": ("وشەکانی وانە", "ئەوە باوکمە."),
            "وانە_8": ("وشەکانی وانە", "تکایە، پەرداخێک ئاو بدە."),
            "وانە_9": ("ڕۆژەکانی هەفتە", "سبەی سێشەممەیە."),
            "وانە_10": ("وشەی پرسیار", "ئەمە چییە؟"),
        }
        for lesson_key, phrases in required_phrases.items():
            with self.subTest(lesson=lesson_key):
                content = self.lessons[lesson_key]["content"]
                for phrase in phrases:
                    self.assertIn(phrase, content)

    def test_lessons_seven_to_ten_have_ten_more_examples_six_quiz_questions_and_updated_infographics(self):
        expected_examples = {
            "وانە_7": ("ئەمە باپیرمە و ئەوە داپیرمە.", "براکەم لە قوتابخانە دەخوێنێت", "خێزانەکە لە کۆتایی هەفتەدا"),
            "وانە_8": ("بۆ نانی بەیانی هێلکە و نان دەخۆم", "من چای بەبێ شەکر حەز لێ دەکەم", "شیرەکە ساردە، چایەکە گەرمە"),
            "وانە_9": ("دووشەممە و چوارشەممە وانەمان هەیە", "کاتژمێر حەوت و نیوە", "سبەی پاش نیوەڕۆ"),
            "وانە_10": ("من هەموو ڕۆژێک زمانی کوردی دەخوێنم", "بۆچی ئەمڕۆ درەنگ هاتیت؟", "چۆن دەتوانم ئەم وشەیە بخوێنمەوە؟"),
        }
        shared_examples = {
            "وانە_7": ("ئەمە دایکمە.", "ئەوە باوکمە.", "ناوی ئەو شیرینە."),
            "وانە_8": ("بۆ بەیانی نان و پەنیر دەخۆم.", "شۆرباکە گەرمە.", "ئاو دەخۆمەوە، نەک چای."),
            "وانە_9": ("ئەمڕۆ دووشەممەیە.", "سبەی سێشەممەیە.", "وانەکە کاتژمێر نۆ دەست پێ دەکات."),
            "وانە_10": ("من قوتابیم.", "ناوت چییە؟ — ناوم ئارامە.", "کتێبەکە لە کوێیە؟"),
        }
        infographic_names = {
            "وانە_7": "lesson-07-family.svg",
            "وانە_8": "lesson-08-food-drink.svg",
            "وانە_9": "lesson-09-days-time.svg",
            "وانە_10": "lesson-10-simple-sentences.svg",
        }
        for lesson_key, examples in expected_examples.items():
            with self.subTest(lesson=lesson_key):
                content = self.lessons[lesson_key]["content"]
                start = content.index("📖 نموونەی زیاتر")
                end = content.index("🧩 ڕاهێنان", start)
                example_lines = [line for line in content[start:end].splitlines() if line.startswith("• ")]
                self.assertEqual(len(example_lines), 10)
                self.assertGreaterEqual(len(self.quizzes[lesson_key]), 6)
                for phrase in examples:
                    self.assertIn(phrase, content)
                svg_root = ET.parse(BASE_DIR / "assets" / "infographics" / infographic_names[lesson_key]).getroot()
                svg_text = " ".join(node.text.strip() for node in svg_root.iter() if node.text and node.text.strip())
                for phrase in shared_examples[lesson_key]:
                    self.assertIn(phrase, content)
                    self.assertIn(phrase, svg_text)

    def test_alphabet_lesson_and_infographic_provide_five_examples_for_all_34_entries(self):
        lesson = self.lessons["وانە_2"]["content"]
        svg_path = BASE_DIR / "assets" / "infographics" / "lesson-02-letters-sample.svg"
        root = ET.parse(svg_path).getroot()
        svg_text = " ".join(node.text.strip() for node in root.iter() if node.text and node.text.strip())
        section_start = lesson.index("🔤 پیت و وشەی نموونە")
        section_end = lesson.index("🧠 چۆن ئەم لیستە بخوێنیتەوە؟", section_start)
        section = lesson[section_start:section_end]
        entries = []
        for line in section.splitlines()[1:]:
            if " — " not in line:
                continue
            letter, raw_words = line.split(" — ", 1)
            words = [word.strip() for word in raw_words.split("،") if word.strip()]
            entries.append((letter.strip(), words))
        self.assertEqual(len(entries), 34)
        for letter, words in entries:
            with self.subTest(letter=letter):
                self.assertEqual(len(words), 5, f"{letter} must have exactly five examples")
                self.assertIn(letter, svg_text)
                for word in words:
                    with self.subTest(word=word):
                        self.assertIn(word, lesson)
                        self.assertIn(word, svg_text)

    def test_alphabet_spelling_matches_selected_reference(self):
        lesson = self.lessons["وانە_2"]["title"] + "\n" + self.lessons["وانە_2"]["content"]
        path_text = "\n".join(self.learning_path["lessons"])
        quiz_text = "\n".join(
            question["question"] + "\n" + "\n".join(question["options"])
            for question in self.quizzes["وانە_2"]
        )
        svg_text = (
            BASE_DIR / "assets" / "infographics" / "lesson-02-letters-sample.svg"
        ).read_text(encoding="utf-8")
        combined = "\n".join((lesson, path_text, quiz_text, svg_text))
        self.assertIn("ئەلفبێ", combined)
        self.assertNotIn("ئەلفوبێ", combined)
        self.assertNotIn("ئەلف بێ", combined)

    def test_alphabet_lesson_has_teaching_examples_and_practice(self):
        lesson = self.lessons["وانە_2"]["content"]
        for required in ("ئامانجی وانە", "پیت و دەنگ", "نموونە", "ڕاهێنان", "پیتەکان"):
            with self.subTest(section=required):
                self.assertIn(required, lesson)
        self.assertGreaterEqual(len(self.quizzes["وانە_2"]), 4)


    def test_alphabet_infographic_examples_match_lesson_two(self):
        lesson = self.lessons["وانە_2"]["content"]
        svg_path = BASE_DIR / "assets" / "infographics" / "lesson-02-letters-sample.svg"
        root = ET.parse(svg_path).getroot()
        svg_text = " ".join(node.text.strip() for node in root.iter() if node.text and node.text.strip())
        examples = (("ب", "باوک"), ("پ", "پیاو"), ("چ", "چاو"),
                    ("ڕ", "ڕۆژ"), ("ش", "شاخ"), ("گ", "گوڵ"))
        for letter, word in examples:
            with self.subTest(letter=letter, word=word):
                self.assertIn(letter, lesson)
                self.assertIn(word, lesson)
                self.assertIn(letter, svg_text)
                self.assertIn(word, svg_text)

    def test_everyday_vocabulary_lesson_has_dialogue_and_practice(self):
        lesson = self.lessons["وانە_3"]["content"]
        for required in ("ئامانجی وانە", "نموونەی گفتوگۆ", "وشە لە ناو ڕستەدا", "ڕاهێنان", "پێداچوونەوە"):
            with self.subTest(section=required):
                self.assertIn(required, lesson)
        self.assertGreaterEqual(len(self.quizzes["وانە_3"]), 4)


    def test_lessons_four_to_six_include_examples_and_practice(self):
        expectations = {
            "وانە_4": ("ژمارەکان", "نموونە لە گفتوگۆدا", "ڕاهێنان", "پێداچوونەوە"),
            "وانە_5": ("ڕەنگەکان", "نموونەی ڕستە", "ڕاهێنان", "پێداچوونەوە"),
            "وانە_6": ("لە ماڵ و قوتابخانە", "ڕستەی نموونە", "ڕاهێنان", "پێداچوونەوە"),
        }
        for lesson_key, sections in expectations.items():
            with self.subTest(lesson=lesson_key):
                for section in sections:
                    self.assertIn(section, self.lessons[lesson_key]["content"])
                self.assertGreaterEqual(len(self.quizzes[lesson_key]), 4)


    def test_all_ten_lessons_have_an_infographic_asset(self):
        expected_assets = [
            "lesson-01-greetings.svg",
            "lesson-02-letters-sample.svg",
            "lesson-03-daily-words.svg",
            "lesson-04-numbers.svg",
            "lesson-05-colors.svg",
            "lesson-06-home-school.svg",
            "lesson-07-family.svg",
            "lesson-08-food-drink.svg",
            "lesson-09-days-time.svg",
            "lesson-10-simple-sentences.svg",
        ]
        assets_dir = BASE_DIR / "assets" / "infographics"
        for filename in expected_assets:
            with self.subTest(asset=filename):
                self.assertTrue((assets_dir / filename).is_file())
                self.assertIn("<svg", (assets_dir / filename).read_text(encoding="utf-8"))

    def test_infographics_are_well_formed_rtl_svg(self):
        assets_dir = BASE_DIR / "assets" / "infographics"
        for path in sorted(assets_dir.glob("*.svg")):
            with self.subTest(asset=path.name):
                root = ET.parse(path).getroot()
                self.assertTrue(root.tag.endswith("svg"))
                self.assertTrue(root.attrib.get("viewBox"))
                svg_text = path.read_text(encoding="utf-8")
                self.assertIn('direction="rtl"', svg_text)
                self.assertIn('unicode-bidi="plaintext"', svg_text)
                self.assertIn("Noto Naskh Arabic", svg_text)

    def test_kejyarbot_orthography_policy_keeps_avasin_separate(self):
        policy_path = BASE_DIR / "docs" / "ORTHOGRAPHY_POLICY.md"
        self.assertTrue(policy_path.is_file())
        policy = policy_path.read_text(encoding="utf-8")
        self.assertIn("کۆدی ئاڤاشین", policy)
        self.assertIn("دیاکۆ هاشمی", policy)

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

    def test_quiz_callback_validates_before_claiming_question(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        start = bot_source.index("async def quiz_answer(")
        end = bot_source.find("\nasync def ", start + 1)
        handler = bot_source[start:end if end >= 0 else len(bot_source)]
        self.assertLess(
            handler.index('if not raw_index.isdigit():'),
            handler.index('quiz["question_message_id"] = None'),
        )
        self.assertLess(
            handler.index('if choice_index < 0 or choice_index >= len(question["options"]):'),
            handler.index('quiz["question_message_id"] = None'),
        )

    def test_final_lesson_points_to_its_own_quiz(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        final_lesson = self.learning_path["lessons"][-1]
        self.assertIn("وانەی ١٠: ڕستەی سادە و پرسیارکردن", final_lesson)
        self.assertIn('callback_data=f"quiz_{last_lesson_number}_start"', bot_source)
        self.assertNotIn('callback_data="quiz_5_start"', bot_source)

    def test_quiz_start_rejects_lessons_outside_learning_path(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        start = bot_source.index("async def start_quiz(")
        end = bot_source.find("\nasync def ", start + 1)
        handler = bot_source[start:end if end >= 0 else len(bot_source)]
        self.assertIn("if lesson not in ORDER:", handler)
        self.assertLess(
            handler.index("if lesson not in ORDER:"),
            handler.index("questions = QUIZ_DATA.get(lesson)"),
        )
        self.assertIn("if lesson not in get_completed_lessons(user_id):", handler)

    def test_lesson_menu_references_only_existing_lessons(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        start = bot_source.index("LESSON_BUTTONS = {")
        end = bot_source.index("\n}", start) + 2
        block = bot_source[start:end]
        for index in range(1, 11):
            lesson = f"وانە_{index}"
            with self.subTest(lesson=lesson):
                self.assertIn(lesson, block)
                self.assertIn(lesson, self.lessons)

    def test_quiz_menu_filters_to_completed_lessons(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        start = bot_source.index('if text == "📝 تاقیکردنەوەکان":')
        end = bot_source.find("\n    if text ==", start + 1)
        handler = bot_source[start:end if end >= 0 else len(bot_source)]
        self.assertIn("lesson in completed", handler)
        self.assertIn("QUIZ_DATA.get(lesson)", handler)
    def test_every_lesson_has_a_completion_badge(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        start = bot_source.index("def check_badges(")
        end = bot_source.index("\ndef lesson_keyboard(", start)
        handler = bot_source[start:end]
        for index in range(1, 11):
            with self.subTest(lesson=index):
                self.assertIn(f'"وانە_{index}"', handler)
        self.assertIn("🏅 زانای ماڵ و قوتابخانە", handler)

    def test_quiz_lessons_exist(self):
        for lesson in self.quizzes:
            self.assertIn(lesson, self.lessons)


    def test_lesson_nine_and_ten_quizzes_cover_distinct_skills(self):
        lesson_nine_questions = [item["question"] for item in self.quizzes["وانە_9"]]
        lesson_ten_questions = [item["question"] for item in self.quizzes["وانە_10"]]
        self.assertEqual(len(lesson_nine_questions), len(set(lesson_nine_questions)))
        self.assertEqual(len(lesson_ten_questions), len(set(lesson_ten_questions)))
        self.assertIn("کام ڕستە بەرنامەی ڕۆژانە دەردەخات؟", lesson_nine_questions)
        self.assertIn("کام پرسیار بۆ زانینی هۆکار بەکاردێت؟", lesson_ten_questions)
        for lesson_key in ("وانە_9", "وانە_10"):
            for item in self.quizzes[lesson_key]:
                with self.subTest(lesson=lesson_key, question=item["question"]):
                    self.assertIn(item["answer"], item["options"])
                    self.assertIn(item["answer"], self.lessons[lesson_key]["content"])


    def test_lessons_one_and_five_quizzes_cover_distinct_skills(self):
        lesson_one = self.lessons["وانە_1"]["content"]
        lesson_five = self.lessons["وانە_5"]["content"]
        lesson_one_item = next(
            item for item in self.quizzes["وانە_1"]
            if item["question"].startswith("ئەگەر ناوی کەسێک")
        )
        lesson_five_item = next(
            item for item in self.quizzes["وانە_5"]
            if item["question"].startswith("کام ڕستە جیاوازیی نێوان")
        )

        self.assertIn("تکایە، ناوت دووبارە دەڵێیتەوە؟", lesson_one)
        self.assertEqual(lesson_one_item["answer"], "تکایە، ناوت دووبارە دەڵێیتەوە؟")
        self.assertIn(lesson_one_item["answer"], lesson_one_item["options"])

        contrast_example = "ئەم پەڕەیە زەردە، بەڵام ئەو پەڕەیە سپییە."
        self.assertIn(contrast_example, lesson_five)
        self.assertEqual(lesson_five_item["answer"], contrast_example)
        self.assertIn(lesson_five_item["answer"], lesson_five_item["options"])


    def test_lesson_four_examples_stay_within_beginner_number_scope(self):
        lesson = self.lessons["وانە_4"]["content"]
        self.assertIn("ژمارەکانی ٠ تا ١٠", lesson)
        self.assertIn("لە پۆلەکەدا هەشت قوتابی دانیشتوون.", lesson)
        self.assertIn("لەسەر مێزەکە سێ کتێب و دوو پێنووس هەیە.", lesson)
        self.assertNotIn("دوازدە مانگ", lesson)
        self.assertNotIn("یەکشەممەیە؛ سبەی دووشەممەیە", lesson)



    def test_lesson_four_quiz_assesses_number_in_context(self):
        lesson = self.lessons["وانە_4"]["content"]
        item = next(
            item for item in self.quizzes["وانە_4"]
            if item["question"] == "کام ڕستە ژمارە و شت بە دروستی پەیوەست دەکات؟"
        )
        self.assertIn("دوو پێنووسم هەیە.", lesson)
        self.assertEqual(item["answer"], "دوو پێنووسم هەیە.")
        self.assertIn(item["answer"], item["options"])



    def test_lesson_six_quiz_uses_taught_writing_tool_term(self):
        lesson = self.lessons["وانە_6"]["content"]
        item = next(
            item for item in self.quizzes["وانە_6"]
            if item["question"] == "کام شت بۆ نووسین لە قوتابخانە بەکاردێت؟"
        )
        self.assertIn("پێنووس", lesson)
        self.assertEqual(item["answer"], "پێنووس")
        self.assertIn(item["answer"], item["options"])



    def test_lesson_one_quiz_covers_morning_greeting(self):
        lesson = self.lessons["وانە_1"]["content"]
        item = next(
            item for item in self.quizzes["وانە_1"]
            if item["question"] == "کام دەربڕین بۆ سڵاوکردنی بەیانی گونجاوە؟"
        )
        self.assertIn("بەیانی باش", lesson)
        self.assertEqual(item["answer"], "بەیانی باش")
        self.assertIn(item["answer"], item["options"])



    def test_lesson_three_quiz_applies_polite_request_in_context(self):
        lesson = self.lessons["وانە_3"]["content"]
        item = next(
            item for item in self.quizzes["وانە_3"]
            if item["question"] == "لە بازاڕدا بۆ پرسیارکردن لە نرخ، کام دەربڕین گونجاوە؟"
        )
        self.assertIn("تکایە، ئەمە چەندە؟", lesson)
        self.assertEqual(item["answer"], "تکایە، ئەمە چەندە؟")
        self.assertIn(item["answer"], item["options"])



    def test_lesson_two_alphabet_practice_entries_have_five_examples_each(self):
        content = self.lessons["وانە_2"]["content"]
        section = content.split("🔤 پیت و وشەی نموونە", 1)[1].split("🧠 چۆن ئەم لیستە بخوێنیتەوە؟", 1)[0]
        entries = [line.strip() for line in section.splitlines() if " — " in line]
        self.assertEqual(len(entries), 34)
        for entry in entries:
            with self.subTest(entry=entry):
                letter, examples = entry.split(" — ", 1)
                words = [word.strip() for word in examples.split("،")]
                self.assertTrue(letter.strip())
                self.assertEqual(len(words), 5)
                self.assertTrue(all(words))



    def test_lesson_four_quiz_checks_simple_addition_in_context(self):
        lesson = self.lessons["وانە_4"]["content"]
        item = next(
            item for item in self.quizzes["وانە_4"]
            if item["question"] == "ئەگەر سێ سێو و دوو سێوی تر هەبێت، کۆی سێوەکان چەندە؟"
        )
        self.assertIn("کۆی گشتی پێنج کتێبە", lesson)
        self.assertEqual(item["answer"], "٥")
        self.assertIn(item["answer"], item["options"])

    def test_lesson_five_quiz_checks_comparing_two_colors(self):
        lesson = self.lessons["وانە_5"]["content"]
        contrast_example = "ئەم پەڕەیە زەردە، بەڵام ئەو پەڕەیە سپییە."
        item = next(
            item for item in self.quizzes["وانە_5"]
            if item["question"] == "کام ڕستە جیاوازیی نێوان دوو ڕەنگ نیشان دەدات؟"
        )
        self.assertIn(contrast_example, lesson)
        self.assertEqual(item["answer"], contrast_example)
        self.assertIn(item["answer"], item["options"])



    def test_lesson_eight_quiz_covers_breakfast_vocabulary_not_duplicate_request(self):
        lesson = self.lessons["وانە_8"]["content"]
        item = next(
            item for item in self.quizzes["وانە_8"]
            if item["question"] == "لە نموونەکەدا بۆ نانی بەیانی چی دەخورێت؟"
        )
        self.assertIn("هێلکە و نان دەخۆم", lesson)
        self.assertEqual(item["answer"], "هێلکە و نان")
        self.assertIn(item["answer"], item["options"])


if __name__ == "__main__":
    unittest.main()
