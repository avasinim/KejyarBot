import json
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

    def test_lesson_catalog_contains_only_six_lesson_records(self):
        self.assertEqual(set(self.lessons), {f"وانە_{index}" for index in range(1, 7)})
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
        ]
        self.assertEqual(self.learning_path["lessons"], expected)
        for index, title in enumerate(expected, start=1):
            self.assertIn(f"وانە_{index}", self.lessons)
            self.assertEqual(self.lessons[f"وانە_{index}"]["title"], title.split(": ", 1)[1])
            self.assertTrue(self.lessons[f"وانە_{index}"]["content"].strip())

    def test_every_quiz_question_has_valid_options_and_answer(self):
        self.assertEqual(set(self.quizzes), {"وانە_1", "وانە_2", "وانە_3", "وانە_4", "وانە_5", "وانە_6"})
        for lesson, questions in self.quizzes.items():
            with self.subTest(lesson=lesson):
                self.assertTrue(questions)
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



    def test_recent_example_expansion_remains_in_all_six_lessons(self):
        required_phrases = {
            "وانە_1": ("نموونەی زیاتر", "خۆشحاڵم بە ناسینت"),
            "وانە_2": ("نموونەی زیاتر بۆ پیتەکان", "لیستی تەواوی ئەلفبێ"),
            "وانە_3": ("دەربڕینی زیاتر لە ژیانی ڕۆژانەدا", "دەتوانیت یارمەتیم بدەیت؟"),
            "وانە_4": ("نموونەی ژمارەکردنی زیاتر", "چەند دەفتەرت هەیە؟"),
            "وانە_5": ("نموونەی ڕەنگ لە ڕستەی زیاتر", "پێنووسەکەت چ ڕەنگێکە؟"),
            "وانە_6": ("وشە و ڕستەی زیاتر", "دەفتەرەکەم لە کوێیە؟"),
        }
        for lesson_key, phrases in required_phrases.items():
            with self.subTest(lesson=lesson_key):
                content = self.lessons[lesson_key]["content"]
                for phrase in phrases:
                    self.assertIn(phrase, content)

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


    def test_all_six_lessons_have_an_infographic_asset(self):
        expected_assets = [
            "lesson-01-greetings.svg",
            "lesson-02-letters-sample.svg",
            "lesson-03-daily-words.svg",
            "lesson-04-numbers.svg",
            "lesson-05-colors.svg",
            "lesson-06-home-school.svg",
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
        self.assertIn("وانەی ٦: لە ماڵ و قوتابخانە", final_lesson)
        self.assertIn('"quiz_6_start"', bot_source)
        self.assertNotIn('"quiz_5_start"', bot_source)

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
        for index in range(1, 7):
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
        for index in range(1, 7):
            with self.subTest(lesson=index):
                self.assertIn(f'"وانە_{index}"', handler)
        self.assertIn("🏅 زانای ماڵ و قوتابخانە", handler)

    def test_quiz_lessons_exist(self):
        for lesson in self.quizzes:
            self.assertIn(lesson, self.lessons)


if __name__ == "__main__":
    unittest.main()
