import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from latin_course_runtime import load_latin_courses
from course_runtime import can_open_lesson


class LatinCourseRuntimeTests(unittest.TestCase):
    def test_loads_exactly_two_separate_courses_and_24_lessons(self):
        lessons, quizzes, courses = load_latin_courses()
        self.assertEqual(len(courses), 2)
        self.assertEqual([len(course["lesson_ids"]) for course in courses], [12, 12])
        self.assertEqual(len(lessons), 24)
        self.assertEqual(len(quizzes), 24)
        self.assertEqual(courses[0]["id"], "kurmanji_latin_orthography")
        self.assertEqual(courses[1]["id"], "kurmanji_latin_grammar")
        self.assertIn("Rê zimanê Kurmancî", courses[0]["source_part"])
        self.assertIn("Beşa II", courses[1]["source_part"])

    def test_each_lesson_keeps_full_markdown_and_five_questions(self):
        lessons, quizzes, _ = load_latin_courses()
        for lesson_id, lesson in lessons.items():
            self.assertTrue(lesson["content"].startswith("## Ders "))
            self.assertIn("###", lesson["content"])
            self.assertEqual(len(quizzes[lesson_id]), 5)
            self.assertTrue(all(len(question["options"]) in (3, 4) for question in quizzes[lesson_id]))

    def test_bot_runtime_loads_both_latin_courses_without_collisions(self):
        import bot

        expected = {
            "kurmanji_latin_orthography": "Rê zimanê Kurmancî",
            "kurmanji_latin_grammar": "Beşa II",
        }
        for course_id, source_part in expected.items():
            self.assertTrue(bot.course_is_active(course_id))
            lesson_ids = bot.COURSE_LESSON_ORDER[course_id]
            self.assertEqual(len(lesson_ids), 12)
            self.assertEqual(len(set(lesson_ids)), 12)
            self.assertTrue(all(bot.LESSON_COURSE[item] == course_id for item in lesson_ids))
            self.assertTrue(all(len(bot.QUIZ_DATA[item]) == 5 for item in lesson_ids))
            self.assertTrue(all(source_part in course["source_part"] for course in bot.COURSES if course["id"] == course_id))
        self.assertEqual(len(bot.COURSES), 6)
        self.assertEqual(len(bot.ORDER), 22)


    def test_both_latin_courses_and_answer_keys_are_kurmanji_latin(self):
        import re

        lessons, _, _ = load_latin_courses()
        arabic_script = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")
        signature = "🤖 کەژیار — KejyarBot@"
        for lesson in lessons.values():
            content = lesson["content"].replace(signature, "")
            self.assertIsNone(arabic_script.search(content))

        for filename in (
            "latin_course_1_quiz_answer_key_draft.md",
            "latin_course_2_quiz_answer_key_draft.md",
        ):
            content = (ROOT / "course_data" / filename).read_text(encoding="utf-8")
            self.assertIsNone(arabic_script.search(content))

    def test_bot_routes_course_selection_callbacks_for_both_latin_courses(self):
        bot_source = (ROOT / "bot.py").read_text(encoding="utf-8")
        self.assertIn("kurmanji_latin_orthography|kurmanji_latin_grammar", bot_source)
        self.assertIn('pattern=r"^course_', bot_source)

    def test_course_progress_unlocking_is_isolated_between_the_two_courses(self):
        lessons, _, courses = load_latin_courses()
        first, second = [course["lesson_ids"] for course in courses]
        # Completing the first lesson in Course 1 must not unlock Course 2's
        # second lesson, and vice versa; each course has its own ordered IDs.
        self.assertTrue(can_open_lesson(first, [], first[0]))
        self.assertFalse(can_open_lesson(second, [first[0]], second[1]))
        self.assertTrue(can_open_lesson(second, [], second[0]))
        self.assertFalse(can_open_lesson(first, [second[0]], first[1]))
        self.assertFalse(set(first).intersection(second))

    def test_each_latin_course_uses_its_own_exclusive_source_document(self):
        course1_source = (ROOT / "course_data" / "latin_course_1_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        course2_source = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        self.assertEqual(len([line for line in course1_source.splitlines() if line.startswith("## Ders ")]), 12)
        self.assertEqual(len([line for line in course2_source.splitlines() if line.startswith("## Ders ")]), 12)
        self.assertIn("*Rê zimanê Kurmancî*", course1_source)
        self.assertNotIn("Bingehên gramera kurdmancî", course1_source)
        self.assertNotIn("Celadet Alî Bedir-Xan", course1_source)
        self.assertIn("Bingehên gramera kurdmancî", course2_source)
        self.assertIn("Celadet Alî Bedir-Xan", course2_source)
        self.assertNotIn("Şikofteh", course2_source)
        self.assertNotIn("## Ders 1: Elfabeya Kurdî ya Latînî", course2_source)
        lessons, _, _ = load_latin_courses()
        self.assertEqual(sum(item["course_id"] == "kurmanji_latin_orthography" for item in lessons.values()), 12)
        self.assertEqual(sum(item["course_id"] == "kurmanji_latin_grammar" for item in lessons.values()), 12)

    def test_course_one_distinguishes_bedeng_inventory_from_semivowel_function(self):
        lessons, _, _ = load_latin_courses()
        alphabet_lesson = lessons["kurmanji_latin_orthography_03"]["content"]
        vw_lesson = lessons["kurmanji_latin_orthography_08"]["content"]
        self.assertIn("23 herfên din", alphabet_lesson)
        self.assertIn("Dengdêr û dengdar", alphabet_lesson)
        self.assertIn("Dengdêr ew deng in", alphabet_lesson)
        self.assertNotIn("8 dengdar", alphabet_lesson)
        self.assertIn("W û Y wek **nîvdeng**", alphabet_lesson)
        self.assertIn("V` dengdareke kurmancî ye", vw_lesson)
        self.assertIn("W` nîvdeng e", vw_lesson)
        self.assertIn("Y` jî di heman komê de ye", vw_lesson)



    def test_course_one_i_ii_u_uu_examples_follow_shikofteh(self):
        lessons, _, _ = load_latin_courses()
        lesson6 = lessons["kurmanji_latin_orthography_06"]["content"]
        lesson7 = lessons["kurmanji_latin_orthography_07"]["content"]
        for word in ("bizin", "zivistan", "hêstir", "dîk", "dîwar", "îşev", "şîr"):
            self.assertIn(f"| {word} |", lesson6)
        for word in ("kur", "gur", "kum", "gul", "kul", "dûr", "bûk", "bûn", "kûr", "mû"):
            self.assertIn(f"| {word} |", lesson7)
        for unsupported in ("hilbijartin", "nivîs", "mîr", "nîv"):
            self.assertNotIn(f"| {unsupported} |", lesson6)
        for unsupported in ("kulîlk", "şûştin", "gund", "xurt"):
            self.assertNotIn(unsupported, lesson7)

    def test_course_one_uses_consistent_kurmanci_vowel_and_consonant_terms(self):
        lessons, _, _ = load_latin_courses()
        lesson1 = lessons["kurmanji_latin_orthography_01"]["content"]
        lesson3 = lessons["kurmanji_latin_orthography_03"]["content"]
        lesson4 = lessons["kurmanji_latin_orthography_04"]["content"]
        lesson5 = lessons["kurmanji_latin_orthography_05"]["content"]
        lesson8 = lessons["kurmanji_latin_orthography_08"]["content"]
        lesson9 = lessons["kurmanji_latin_orthography_09"]["content"]
        lesson11 = lessons["kurmanji_latin_orthography_11"]["content"]
        lesson12 = lessons["kurmanji_latin_orthography_12"]["content"]
        self.assertIn("8 dengdêr û 23 herfên din", lesson1)
        self.assertNotIn("8 dengdar", lesson1)
        self.assertIn("Dengdêr û dengdar", lesson3)
        self.assertIn("Dengdarên din", lesson3)
        self.assertNotIn("bêdeng", lesson3.lower())
        self.assertIn("Dengdêrên kin", lesson4)
        self.assertIn("Dengdêrên dirêj", lesson5)
        self.assertIn("V` dengdareke kurmancî ye", lesson8)
        self.assertIn("X dengdareke kurmancî ye", lesson9)
        self.assertIn("Z dengdareke kurmancî ye", lesson9)
        self.assertNotIn("C) Bêdeng", lesson9)
        self.assertIn("Dengdêrek nû tê zêdekirin", lesson11)
        self.assertIn("dengdêrekê dihewîne", lesson12)

    def test_course_one_lesson_eleven_treats_adjacent_vowels_not_consonants(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_orthography_11"]["content"]
        self.assertIn("Dengdêrên Lihev", lesson)
        self.assertIn("du dengdêr", lesson)
        self.assertIn("gî + an", lesson)
        self.assertIn("gîyan", lesson)
        self.assertNotIn("du dengdar", lesson)

    def test_course_one_separates_w_semivowel_from_pevdeng_clusters(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_orthography_08"]["content"]
        self.assertIn("W` bi dengdêran re", lesson)
        self.assertIn("wek pevdeng", lesson)
        self.assertIn("| kew | dawî |", lesson)
        self.assertIn("| dew | dawî |", lesson)
        self.assertNotIn("| xew | dawî |", lesson)
        self.assertNotIn("| law | dawî |", lesson)
        self.assertNotIn("| xwarin | navîn |", lesson)
    def test_course_one_lessons_four_and_five_use_shikofteh_vowel_examples(self):
        lessons, _, _ = load_latin_courses()
        short = lessons["kurmanji_latin_orthography_04"]["content"]
        for term in ("| ewr | E |", "| bizin | I |", "| dil | I |", "| gur | U |", "| kum | U |", "| kul | U |"):
            self.assertIn(term, short)
        for term in ("| nivîs | I |", "| hilbijartin | I |", "| gund | U |", "| xurt | U |", "| kulîlk | U |"):
            self.assertNotIn(term, short)
        long = lessons["kurmanji_latin_orthography_05"]["content"]
        for term in ("| ard | A |", "| êzing | Ê |", "| dîk | Î |", "| îşev | Î |", "| dîwar | Î |", "| ordek | O |", "| por | O |", "| bûk | Û |", "| mû | Û |"):
            self.assertIn(term, long)
        for term in ("| şûştin | Û |", "| jîn | Î |", "| çêkirin | Ê |"):
            self.assertNotIn(term, long)

    def test_course_one_i_ii_examples_and_w_examples_are_source_attested(self):
        lessons, _, _ = load_latin_courses()
        lesson6 = lessons["kurmanji_latin_orthography_06"]["content"]
        self.assertIn("| îşev | Î |", lesson6)
        self.assertNotIn("rêzên pîr", lesson6)
        lesson8 = lessons["kurmanji_latin_orthography_08"]["content"]
        self.assertIn("| kew | dawî |", lesson8)
        self.assertIn("| vedan | destpêk |", lesson8)
        self.assertIn("| çav | dawî |", lesson8)
        self.assertIn("| dirav | navîn |", lesson8)
        self.assertIn("| kevir | navîn |", lesson8)
        self.assertIn("| wî | destpêk |", lesson8)
        self.assertIn("| wêran | destpêk |", lesson8)
        self.assertIn("`vegerîn — wan — çav — wêran — welat — veşartin`", lesson8)
        self.assertNotIn("| wê | destpêk |", lesson8)
        self.assertIn("| dev | dew |", lesson8)
        self.assertIn("| vir | wîr |", lesson8)
        self.assertIn("| ava | awa |", lesson8)
        self.assertIn("| evî | ewî |", lesson8)
        self.assertIn("`kew`", lesson8)
        self.assertNotIn("`law`", lesson8)
        self.assertNotIn("| law | dawî |", lesson8)

    def test_course_one_lesson_nine_tracks_source_x_y_z_descriptions(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_orthography_09"]["content"]
        self.assertIn("Dengên X, Y û Z", lesson)
        self.assertIn("X ji nîveka qirikê", lesson)
        self.assertIn("Y nîvdeng e", lesson)
        self.assertIn("Z di navbera diranan de", lesson)
        self.assertIn("X dengdareke kurmancî ye", lesson)
        self.assertIn("Z dengdareke kurmancî ye", lesson)
        self.assertIn("| zozan | Z |", lesson)
        self.assertNotIn("Herfên Taybet di Elfabeya Kurmancî de", lesson)

    def test_course_two_lessons_four_and_five_separate_number_and_oblique_forms(self):
        lessons, _, _ = load_latin_courses()
        number = lessons["kurmanji_latin_grammar_04"]["content"]
        self.assertIn("`hespek/hespin`", number)
        self.assertIn("`mehînek/mehînin`", number)
        self.assertIn("`hespan` û `mehînan`", number)
        self.assertIn("bi tewangê ve girêdayî ne", number)
        oblique = lessons["kurmanji_latin_grammar_05"]["content"]
        self.assertIn("`hespan` û `mehînan` şêweyên tewandî ne", oblique)
        self.assertIn("`hespin` û `mehînin`", oblique)
        self.assertIn("Bi gelemperî, navdêrên nêr", oblique)
        self.assertNotIn("Bi gelemperî di gelemperî de", oblique)

    def test_course_two_lesson_eight_keeps_indefinite_suffix_patterns_distinct(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_08"]["content"]
        for term in ("`hespek hat`", "`mehînek hat`", "`hespin hatin`", "`mehînin hatin`"):
            self.assertIn(term, lesson)
        for term in ("`hespekî delal hat`", "`mehîneke delal hat`", "`mehînine delal hatin`"):
            self.assertIn(term, lesson)
        self.assertIn("`-ekî`, `-ekê`, `-ina`", lesson)
        self.assertNotIn("`-ina` ji bo gelemjara giştî", lesson)

    def test_course_two_lesson_three_preserves_celadet_dar_gender_by_meaning(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_03"]["content"]
        self.assertIn("`vê darê`", lesson)
        self.assertIn("`vî darî`", lesson)
        self.assertIn("wateya dara kesk/riwekê dide mê ye", lesson)
        self.assertIn("wateya dara hişk/çûbê dide nêr e", lesson)

    def test_course_two_lesson_twelve_preserves_celadet_adjective_and_numeral_classes(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_12"]["content"]
        for term in ("wesfîn", "îşarkî", "jmarîn", "pirsiyarkî", "nebinavkirî", "xwemalîn"):
            self.assertIn(term, lesson)
        for term in ("bingehîn", "rêzîn", "birewîn", "komelîn"):
            self.assertIn(term, lesson)

    def test_course_two_lesson_eleven_distinguishes_celadet_demonstrative_groups(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_11"]["content"]
        self.assertIn("Yên pî ve:", lesson)
        self.assertIn("Yên qerse:", lesson)
        self.assertIn("yê, ya, yên", lesson)
        self.assertNotIn("di ravekirina veqetandekên binavkirî de girêk dide", lesson)

    def test_course_two_lesson_five_preserves_celadet_three_variant_examples(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_05"]["content"]
        self.assertIn("Soro kevirî tavêje", lesson)
        self.assertIn("Soro kê vir tavêje", lesson)
        self.assertIn("Soro kevir tavêje", lesson)
        self.assertNotIn("Soro kê virî tavêje", lesson)

    def test_course_two_reciprocal_e_k_region_matches_celadet_source(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_10"]["content"]
        self.assertIn("hev` û `êk", lesson)
        self.assertIn("li nîvrohelatê Kurdistanê", lesson)
        self.assertNotIn("li Kurdistana navendî", lesson)

    def test_course_two_neuter_personal_pronoun_has_no_invented_agent_form(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_09"]["content"]
        self.assertIn("| sêyem yekjimar nêtar | ew | — |", lesson)
        self.assertIn("Celadet tenê `wî` û `wê` dide", lesson)
        self.assertNotIn("| sêyem yekjimar nêtar | ew | ew |", lesson)

    def test_course_two_runtime_uses_dedicated_source_aligned_document(self):
        lessons, _, _ = load_latin_courses()
        first = lessons["kurmanji_latin_grammar_01"]["content"]
        last = lessons["kurmanji_latin_grammar_12"]["content"]
        self.assertIn("çar hêmanên bingehîn", first)
        self.assertIn("Şeş cureyên rengdêr ev in:", last)
        self.assertIn("jmarnavên binavkirî", last)

    def test_course_two_lesson_twelve_uses_selected_expanded_lesson(self):
        lessons, quizzes, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_12"]["content"]
        self.assertIn("Şeş cureyên", lesson)
        self.assertIn("jmarnav", lesson)
        self.assertEqual(len(quizzes["kurmanji_latin_grammar_12"]), 5)

    def test_every_delivered_lesson_gets_kejyar_brand_signature(self):
        import bot

        signature = "🤖 کەژیار — KejyarBot@"
        self.assertEqual(bot.add_kejyar_brand_signature("Lesson body"), f"Lesson body\n\n{signature}")
        self.assertEqual(bot.add_kejyar_brand_signature(f"Lesson body\n\n{signature}"), f"Lesson body\n\n{signature}")
        self.assertIn(signature, bot.add_kejyar_brand_signature("کۆرسی ٣"))
    def test_telegram_chunking_preserves_every_character_and_respects_limit(self):
        import bot

        content = ("ئەڤە دەقی وانەیە.\n" * 500) + ("x" * 4100) + "\nکۆتایی."
        chunks = bot.split_lesson_text(content, limit=3800)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk) <= 3800 for chunk in chunks))
        self.assertEqual("".join(chunks), content.strip())

    def test_telegram_chunking_handles_empty_and_exact_limit(self):
        import bot

        self.assertEqual(bot.split_lesson_text("  "), ["⚠️ ناوەڕۆکی ئەم وانەیە بەردەست نییە."])
        exact = "ک" * 3800
        self.assertEqual(bot.split_lesson_text(exact), [exact])

    def test_bot_renders_markdown_tables_as_readable_telegram_rows(self):
        import bot

        source = (
            "| Mezin | Biçûk |\n"
            "|---|---|\n"
            "| A | a |\n"
            "| B | b |"
        )
        rendered = bot.format_lesson_draft(source)
        self.assertIn("Mezin: A • Biçûk: a", rendered)
        self.assertIn("Mezin: B • Biçûk: b", rendered)
        self.assertNotIn("|---|", rendered)
        self.assertNotIn("| A |", rendered)
        wrapped = bot.format_lesson_draft("Before\n---\n<text>Heşt herfên dengdêr</text>\nAfter")
        self.assertEqual(wrapped, "Before\nHeşt herfên dengdêr\nAfter")

    def test_lesson_content_is_not_reformatted_or_truncated(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_orthography_01"]["content"]
        self.assertIn("| Mezin | Biçûk |", lesson)
        self.assertIn("### 6. Testa Kejyar", lesson)
        self.assertIn("### Xulasa", lesson)


if __name__ == "__main__":
    unittest.main()
