import json
import re
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET
from pathlib import Path

import speech


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
                    self.assertGreaterEqual(len(question["options"]), 3)
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


    def test_kurdish_specific_letters_use_their_exact_unicode_characters(self):
        svg_path = BASE_DIR / "assets" / "infographics" / "lesson-02-letters-sample.svg"
        root = ET.parse(svg_path).getroot()
        svg_text = " ".join(node.text.strip() for node in root.iter() if node.text and node.text.strip())
        lesson = self.lessons["وانە_2"]["content"]
        # Assert the actual Kurdish characters, not visually similar Arabic/Persian substitutes.
        required_letters = ("ڕ", "ڵ", "ۆ", "ێ", "ە", "ڤ", "پ", "چ", "ژ")
        for letter in required_letters:
            with self.subTest(letter=letter, codepoint=f"U+{ord(letter):04X}"):
                self.assertIn(letter, lesson)
                self.assertIn(letter, svg_text)
        self.assertEqual(ord("ڕ"), 0x0695)
        self.assertEqual(ord("ڵ"), 0x06B5)
        self.assertEqual(ord("ۆ"), 0x06C6)
        self.assertEqual(ord("ێ"), 0x06CE)
        self.assertEqual(ord("ە"), 0x06D5)

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

    def test_kurdish_text_nodes_have_explicit_rtl_shaping_attributes(self):
        assets_dir = BASE_DIR / "assets" / "infographics"
        kurdish_letters = set("ئاپتجچحخدرڕزژسشعغفڤقکگلڵمنهەووۆیێ")
        for path in sorted(assets_dir.glob("*.svg")):
            root = ET.parse(path).getroot()
            text_nodes = [node for node in root.iter() if node.tag.endswith("text")]
            for node in text_nodes:
                text_value = "".join(node.itertext())
                if not any(character in kurdish_letters for character in text_value):
                    continue
                with self.subTest(asset=path.name, text=text_value[:50]):
                    self.assertEqual(node.attrib.get("direction"), "rtl")
                    self.assertEqual(node.attrib.get("unicode-bidi"), "plaintext")

    def test_dynamic_speech_requires_explicit_enablement_and_matching_approved_voice(self):
        with patch.dict("os.environ", {}, clear=True):
            self.assertFalse(speech.speech_is_configured())
            self.assertIsNone(speech._generate_speech("سڵاو"))

        with patch.dict("os.environ", {
            "ELEVENLABS_API_KEY": "test-key",
            "KEJYAR_VOICE_ID": "voice-a",
            "KEJYAR_APPROVED_VOICE_ID": "voice-a",
        }, clear=True):
            self.assertFalse(speech.speech_is_configured())
            self.assertIsNone(speech._generate_speech("سڵاو"))

        with patch.dict("os.environ", {
            "KEJYAR_ENABLE_DYNAMIC_SPEECH": "true",
            "ELEVENLABS_API_KEY": "test-key",
            "KEJYAR_VOICE_ID": "voice-a",
            "KEJYAR_APPROVED_VOICE_ID": "voice-b",
        }, clear=True):
            self.assertFalse(speech.speech_is_configured())
            self.assertIsNone(speech._generate_speech("سڵاو"))

        with patch.dict("os.environ", {
            "KEJYAR_ENABLE_DYNAMIC_SPEECH": "true",
            "ELEVENLABS_API_KEY": "test-key",
            "KEJYAR_VOICE_ID": "voice-a",
            "KEJYAR_APPROVED_VOICE_ID": "voice-a",
        }, clear=True):
            self.assertTrue(speech.speech_is_configured())

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
        self.assertIn('quiz_lesson_id = lesson.removeprefix("وانە_") if lesson.startswith("وانە_") else lesson', bot_source)
        self.assertIn('callback_data=f"quiz_{quiz_lesson_id}_start"', bot_source)
        self.assertNotIn('callback_data="quiz_5_start"', bot_source)

    def test_quiz_start_rejects_lessons_outside_learning_path(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        start = bot_source.index("async def start_quiz(")
        end = bot_source.find("\nasync def ", start + 1)
        handler = bot_source[start:end if end >= 0 else len(bot_source)]
        self.assertIn("if lesson not in LESSON_COURSE:", handler)
        self.assertLess(
            handler.index("if lesson not in LESSON_COURSE:"),
            handler.index("questions = QUIZ_DATA.get(lesson)"),
        )
        self.assertIn("if lesson not in get_completed_lessons(user_id):", handler)

    def test_lesson_menu_references_only_existing_runtime_lessons(self):
        import bot

        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        self.assertIn('for course_lesson in ORTHOGRAPHY_COURSE.get("lessons", [])', bot_source)
        self.assertIn('LESSON_BUTTONS[f"وانەی {kurdish_digits(number)}: {title}"] = lesson_key', bot_source)
        self.assertEqual(len(bot.ORDER), 22)
        self.assertEqual(bot.ORDER, [f"وانە_{index}" for index in range(1, 23)])
        self.assertEqual(set(bot.LESSON_BUTTONS.values()), set(bot.ORDER))
        for lesson in bot.ORDER:
            with self.subTest(lesson=lesson):
                self.assertTrue(bot.LESSON_DATA[lesson]["title"].strip())

    def test_quiz_menu_filters_to_completed_lessons(self):
        bot_source = (BASE_DIR / "bot.py").read_text(encoding="utf-8")
        start = bot_source.index('if text == "📝 تاقیکردنەوەکان":')
        end = bot_source.find("\n    if text ==", start + 1)
        handler = bot_source[start:end if end >= 0 else len(bot_source)]
        self.assertIn("lesson not in completed", handler)
        self.assertIn("QUIZ_DATA.get(lesson)", handler)
    def test_completed_lessons_receive_dynamic_badges_within_runtime_order(self):
        import bot

        with (
            patch.object(bot, "get_completed_lessons", return_value=[
                "وانە_1", "وانە_22", "not-a-lesson", "وانە_999"
            ]),
            patch.object(bot, "add_badge") as add_badge,
        ):
            bot.check_badges(12345)

        self.assertCountEqual(
            add_badge.call_args_list,
            [
                unittest.mock.call(12345, "🏅 کۆرسی ڕێنووسی — وانەی 1"),
                unittest.mock.call(12345, "🏅 کۆرسی ڕێنووسی — وانەی 22"),
            ],
        )

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





    def test_quiz_options_are_unique_and_correct_answer_occurs_once(self):
        for lesson_key, questions in self.quizzes.items():
            for index, question in enumerate(questions, start=1):
                with self.subTest(lesson=lesson_key, question=index):
                    options = question["options"]
                    self.assertGreaterEqual(len(options), 2)
                    self.assertEqual(len(options), len(set(options)))
                    self.assertEqual(options.count(question["answer"]), 1)
                    self.assertTrue(question["question"].strip())

    def test_lesson_two_practice_order_matches_selected_2024_reference(self):
        expected = [
            "ئ", "ا", "ب", "پ", "ت", "ج", "چ", "ح", "خ", "د", "ر", "ڕ",
            "ز", "ژ", "س", "ش", "ع", "غ", "ف", "ڤ", "ق", "ک", "گ", "ل",
            "ڵ", "م", "ن", "ه", "ە", "و", "وو", "ۆ", "ی", "ێ",
        ]
        content = self.lessons["وانە_2"]["content"]
        section = content.split("🔤 پیت و وشەی نموونە", 1)[1].split(
            "🧠 چۆن ئەم لیستە بخوێنیتەوە؟", 1
        )[0]
        lesson_order = [
            line.strip().split(" — ", 1)[0]
            for line in section.splitlines()
            if " — " in line
        ]
        self.assertEqual(lesson_order, expected)

        svg_path = BASE_DIR / "assets" / "infographics" / "lesson-02-letters-sample.svg"
        root = ET.parse(svg_path).getroot()
        namespace = "{http://www.w3.org/2000/svg}"
        card_order = [
            group.findall(f"{namespace}text")[0].text
            for group in root.findall(f".//{namespace}g")
        ]
        self.assertEqual(card_order, expected)

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


    def test_lesson_nine_quiz_checks_specific_clock_time(self):
        lesson = self.lessons["وانە_9"]["content"]
        item = next(
            item for item in self.quizzes["وانە_9"]
            if item["question"] == "وانەکە کاتژمێر چەند دەست پێ دەکات؟"
        )
        self.assertIn("وانەکە کاتژمێر نۆ دەست پێ دەکات", lesson)
        self.assertEqual(item["answer"], "کاتژمێر نۆ")
        self.assertIn(item["answer"], item["options"])


    def test_every_quiz_answer_is_taught_in_its_matching_lesson(self):
        for lesson_key, questions in self.quizzes.items():
            lesson_content = self.lessons[lesson_key]["content"]
            for index, question in enumerate(questions, start=1):
                with self.subTest(lesson=lesson_key, question=index):
                    self.assertIn(
                        question["answer"],
                        lesson_content,
                        "Correct answers must be supported by the matching lesson content.",
                    )


    def test_quiz_set_sizes_match_the_audited_beginner_curriculum(self):
        expected_counts = {f"وانە_{index}": 6 for index in range(1, 11)}
        expected_counts["وانە_2"] = 8
        self.assertEqual(
            {lesson_key: len(questions) for lesson_key, questions in self.quizzes.items()},
            expected_counts,
        )
        self.assertEqual(sum(len(questions) for questions in self.quizzes.values()), 62)


    def test_infographic_accessible_labels_match_their_lesson(self):
        expected_labels = {
            "lesson-01-greetings.svg": "وانەی ١: سڵاو و ناساندنی خۆ",
            "lesson-02-letters-sample.svg": "وانەی ٢: ئەلفبێی کوردی بە پیت و وشە و وێنەی نموونە",
            "lesson-03-daily-words.svg": "وانەی ٣: وشەکانی ڕۆژانە",
            "lesson-04-numbers.svg": "وانەی ٤: ژمارەکان",
            "lesson-05-colors.svg": "وانەی ٥: ڕەنگەکان",
            "lesson-06-home-school.svg": "وانەی ٦: لە ماڵ و قوتابخانە",
            "lesson-07-family.svg": "وانەی ٧: خێزان و کەسانی نزیک",
            "lesson-08-food-drink.svg": "وانەی ٨: خواردن و خواردنەوە",
            "lesson-09-days-time.svg": "وانەی ٩: ڕۆژەکانی هەفتە و کات",
            "lesson-10-simple-sentences.svg": "وانەی ١٠: ڕستەی سادە و پرسیارکردن",
        }
        assets_dir = BASE_DIR / "assets" / "infographics"
        for filename, expected_label in expected_labels.items():
            with self.subTest(infographic=filename):
                root = ET.parse(assets_dir / filename).getroot()
                self.assertEqual(root.attrib.get("aria-label"), expected_label)


    def test_infographic_svg_ids_are_unique_and_have_no_external_references(self):
        assets_dir = BASE_DIR / "assets" / "infographics"
        xlink_href = "{http://www.w3.org/1999/xlink}href"
        for path in sorted(assets_dir.glob("*.svg")):
            with self.subTest(asset=path.name):
                root = ET.parse(path).getroot()
                ids = [
                    element.attrib["id"]
                    for element in root.iter()
                    if element.attrib.get("id")
                ]
                self.assertEqual(len(ids), len(set(ids)), "SVG IDs must be unique")
                for element in root.iter():
                    href = element.attrib.get("href") or element.attrib.get(xlink_href)
                    if href:
                        self.assertTrue(
                            href.startswith("#"),
                            f"External SVG reference is not allowed: {href}",
                        )


    def test_infographic_teaching_phrases_are_present_in_matching_lessons(self):
        expectations = {
            "lesson-01-greetings.svg": (
                "وانە_1",
                ("سڵاو!", "چۆنی؟", "باشم، سوپاس."),
            ),
            "lesson-03-daily-words.svg": (
                "وانە_3",
                ("تکایە، دەرگاکە بکەرەوە.", "سوپاس", "ببورە"),
            ),
            "lesson-04-numbers.svg": (
                "وانە_4",
                ("٠ — سفر", "١ — یەک", "٢ — دوو", "٣ — سێ"),
            ),
            "lesson-05-colors.svg": (
                "وانە_5",
                ("سوور", "شین", "سەوز", "زەرد", "ڕەش", "سپی"),
            ),
            "lesson-06-home-school.svg": (
                "وانە_6",
                ("دەرگا", "پەنجەرە", "کورسی", "کتێب"),
            ),
            "lesson-07-family.svg": (
                "وانە_7",
                ("ئەمە دایکمە.", "ئەوە باوکمە.", "براکەم قوتابییە."),
            ),
            "lesson-08-food-drink.svg": (
                "وانە_8",
                ("بۆ بەیانی نان و پەنیر دەخۆم.", "شۆرباکە گەرمە.", "تکایە، پەرداخێک ئاو بدە."),
            ),
            "lesson-09-days-time.svg": (
                "وانە_9",
                ("ئەمڕۆ دووشەممەیە.", "سبەی سێشەممەیە.", "دوێنێ لە کتێبخانە بووم."),
            ),
            "lesson-10-simple-sentences.svg": (
                "وانە_10",
                ("من قوتابیم.", "ئێمە زمانی کوردی فێر دەبین.", "ئەم سێوە سوورە."),
            ),
        }
        assets_dir = BASE_DIR / "assets" / "infographics"
        for filename, (lesson_key, phrases) in expectations.items():
            with self.subTest(infographic=filename):
                svg_text = (assets_dir / filename).read_text(encoding="utf-8")
                lesson_text = self.lessons[lesson_key]["content"]
                for phrase in phrases:
                    with self.subTest(phrase=phrase):
                        self.assertIn(phrase, lesson_text)
                        self.assertIn(phrase, svg_text)


if __name__ == "__main__":
    unittest.main()
