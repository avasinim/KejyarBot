import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "course_data" / "latin_courses_manifest_draft.json"


class LatinCoursesManifestTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def _assert_complete_unique_question_keys(self, question_ids, key_ids, expected_numbers):
        expected = set(expected_numbers)
        self.assertEqual(len(question_ids), len(set(question_ids)))
        self.assertEqual(set(question_ids), expected)
        self.assertEqual(len(key_ids), len(set(key_ids)))
        self.assertEqual(set(key_ids), expected)

    def test_manifest_is_draft_and_not_runtime_loaded(self):
        self.assertEqual(self.manifest["status"], "draft_not_loaded_by_runtime")

    def test_two_latin_courses_are_separate_and_ordered(self):
        courses = self.manifest["courses"]
        self.assertEqual(len(courses), 2)
        self.assertEqual(
            [course["id"] for course in courses],
            ["kurmanji_latin_orthography", "kurmanji_latin_grammar"],
        )
        self.assertEqual([course["order"] for course in courses], [1, 2])
        self.assertEqual([course["status"] for course in courses], ["draft", "draft"])

    def test_each_course_has_twelve_unique_namespaced_lessons(self):
        all_ids = []
        for course in self.manifest["courses"]:
            lesson_ids = course["lesson_ids"]
            self.assertEqual(len(lesson_ids), 12)
            self.assertEqual(len(set(lesson_ids)), 12)
            self.assertTrue(all(item.startswith(course["id"] + "_") for item in lesson_ids))
            all_ids.extend(lesson_ids)
        self.assertEqual(len(all_ids), len(set(all_ids)))

    def test_source_parts_are_not_mixed(self):
        first, second = self.manifest["courses"]
        self.assertIn("Part I", first["source_part"])
        self.assertIn("Part II", second["source_part"])
        self.assertNotEqual(first["source_part"], second["source_part"])


    def test_course_two_lesson_one_tracks_four_source_elements_and_exact_answer_key(self):
        import re

        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_2_quiz_answer_key_draft.md").read_text(encoding="utf-8")
        lesson_one = lesson_text.split("## وانەی ١ —", 1)[1].split("## وانەی ٢ —", 1)[0]

        self.assertIn("tevahiya qaydeyên rastaxaftin û rastnivîsandina ziman", lesson_one)
        self.assertIn("çar hêmanên bingehîn", lesson_one)
        self.assertIn("tîp → kît → bêje → kom", lesson_one)
        self.assertIn("Qiset", lesson_one)
        self.assertIn("wek hêmaneke pêncemîn nayê hejmartin", lesson_one)
        self.assertNotIn("Parêz çûbû Rewanê", lesson_one)

        questions = {}
        current = None
        in_quiz = False
        for line in lesson_one.splitlines():
            if line.startswith("### Kuis"):
                in_quiz = True
                continue
            if not in_quiz:
                continue
            question = re.match(r"^(\d+)\. (.+)$", line)
            if question:
                current = int(question.group(1))
                self.assertNotIn(current, questions)
                questions[current] = {}
                for letter, option in re.findall(r"([ABC])\) (.*?)(?= [ABC]\) |$)", question.group(2)):
                    questions[current][letter] = option
                continue
        key_rows = re.findall(
            r"^\| 1 \| (\d+) \| ([ABC]) \| ([^|]+) \|",
            key_text,
            flags=re.MULTILINE,
        )
        self.assertEqual(set(questions), set(range(1, 6)))
        self.assertEqual(len(key_rows), 5)
        for number, option, answer in key_rows:
            self.assertEqual(questions[int(number)][option], answer.strip())


    def test_course_two_lesson_nine_includes_all_three_pronoun_genders(self):
        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        lesson_nine = lesson_text.split("## وانەی ٩ —", 1)[1].split("## وانەی ١٠ —", 1)[0]
        self.assertIn("Sê zayendên pronav", lesson_nine)
        self.assertIn("sêyem yekjimar nêtar", lesson_nine)
        self.assertIn("wî", lesson_nine)
        self.assertIn("wê", lesson_nine)
        self.assertIn("ew", lesson_nine)


    def test_course_two_lessons_four_and_five_separate_number_from_noun_inflection(self):
        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        lesson_four = lesson_text.split("## وانەی ٤ —", 1)[1].split("## وانەی ٥ —", 1)[0]
        lesson_five = lesson_text.split("## وانەی ٥ —", 1)[1].split("## وانەی ٦ —", 1)[0]

        self.assertIn("`Mîr hat.`", lesson_four)
        self.assertIn("`Mîr hatin.`", lesson_four)
        self.assertIn("`Ev mehin e.`", lesson_four)
        self.assertIn("`Ev mehin in.`", lesson_four)
        self.assertIn("`hespek/hespin`", lesson_four)
        self.assertIn("tenê wek nîşana gelemjimarê", lesson_four)
        self.assertNotIn("`hesp` → `hespan`", lesson_four)

        self.assertIn("`Hesp hat.`", lesson_five)
        self.assertIn("`Ez hespî dibînim.`", lesson_five)
        self.assertIn("`Ez mehinê dibînim.`", lesson_five)
        self.assertIn("`Ez hespan dibînim.`", lesson_five)
        self.assertIn("`Ez mehînan dibînim.`", lesson_five)
        self.assertIn("`kum`", lesson_five)
        self.assertIn("`gund`", lesson_five)
        self.assertIn("`maseyan → masan`", lesson_five)

    def test_course_two_lessons_seven_and_eight_distinguish_determiner_environments(self):
        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        lesson_seven = lesson_text.split("## وانەی ٧ —", 1)[1].split("## وانەی ٨ —", 1)[0]
        lesson_eight = lesson_text.split("## وانەی ٨ —", 1)[1].split("## وانەی ٩ —", 1)[0]

        for form in ("`-ê`", "`-a`", "`-ên`", "`Ez ê gewir dixwazim.`", "`Ez a sor dixwazim.`", "`Ez ên sor dixwazim.`"):
            self.assertIn(form, lesson_seven)

        for form in ("`-ek`", "`-in`", "`-ekî`", "`-eke`", "`-ine`", "`-ekê`", "`-ina`", "`mehîneke delal hat`"):
            self.assertIn(form, lesson_eight)


    def test_course_two_lessons_ten_and_eleven_cover_remaining_source_pronoun_types(self):
        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        lesson_ten = lesson_text.split("## وانەی ١٠ —", 1)[1].split("## وانەی ١١ —", 1)[0]
        lesson_eleven = lesson_text.split("## وانەی ١١ —", 1)[1].split("## وانەی ١٢ —", 1)[0]

        for form in ("Pronavên lihevxisitî", "`jê`", "`lê`", "`pê`", "`tê`", "`jev/jêk`", "`pev/pêk`", "Pronavê nêtar `xwe`", "`Wî xwe kuşt.`", "Pronavê nêtar ê `ê`", "`Min da ê`"):
            self.assertIn(form, lesson_ten)

        for form in ("Pronavên nebinavkirî", "`yek`", "`her kes`", "`hinek`", "Pronavên îşarkî yên qerse", "`Yê ko hat bira yê min bû.`", "`Yên ko hatin bira yên min bûn.`", "`Ya ko hat dotmama min bû.`", "Pronavên xwemalîn", "`yê min`", "`ya min`", "`yên min`", "`destmalên min — yên min`"):
            self.assertIn(form, lesson_eleven)

        self.assertIn("Pronavê nêtar `xwe`", lesson_ten)
        self.assertIn("Pronavên xwemalîn xwedîtiyê nîşan didin", lesson_eleven)
        self.assertIn("ji du pronavan pêk tên", lesson_eleven)


    def test_course_two_lesson_twelve_has_one_canonical_selected_version(self):
        master = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        snapshot = (ROOT / "course_data" / "latin_course_2_lesson_12_replacement_draft.md").read_text(encoding="utf-8")
        lesson_twelve = master.split("## وانەی ١٢ —", 1)[1].split("## تێبینیی سەرچاوە", 1)[0]
        self.assertIn("Şeş cureyên rengdêrên di çavkaniyê de nas bike.", lesson_twelve)
        self.assertIn("Rengdêrên xwemalîn", lesson_twelve)
        self.assertIn("Dereceyên rengdêrên wesfîn", lesson_twelve)
        self.assertIn("Rêzîn", lesson_twelve)
        self.assertIn("`stûna çaran`", lesson_twelve)
        self.assertIn("`a pêncan`", lesson_twelve)
        for example in ("`vî hespî / van hespan`", "`wî hespî / wan hespan`", "`vê mehinê / van mehinan`", "`wê mehinê / wan mehinan`", "`deh mirov hatin`", "`deh mirovan got`", "`kîjan mirov hat?`", "`tu mirov`", "`her mirov`", "`gelek fêkî`", "`hevqas pere`", "`mehinên te`", "`qelemên wê`"):
            self.assertIn(example, lesson_twelve)
        self.assertIn("SELECTED CONTENT", snapshot)
        self.assertIn("do not load it separately", snapshot)
        self.assertEqual(master.count("## وانەی ١٢ —"), 1)

    def test_course_two_lesson_document_has_real_markdown_line_breaks(self):
        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        self.assertNotIn(r"\n", lesson_text)
        self.assertIn("**دۆخی گەڕاندنەوە:**", lesson_text)

    def test_course_two_quiz_answer_key_matches_exact_option_text(self):
        import re

        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_2_quiz_answer_key_draft.md").read_text(encoding="utf-8")
        questions = {}
        lesson_number = 0
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            heading = re.match(r"^## وانەی ([٠-٩]+)", line)
            if heading:
                digits = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
                lesson_number = int(heading.group(1).translate(digits))
                in_quiz = False
                current = None
                continue
            if line.startswith("### Kuis") or line.startswith("### 10. Testa Kejyar"):
                in_quiz = True
                current = None
                continue
            if not in_quiz:
                continue
            if line.startswith("### Xulasa") or line.startswith("## "):
                in_quiz = False
                current = None
                continue
            question = re.match(r"^(\d+)\. (.+)$", line)
            if question:
                current = (lesson_number, int(question.group(1)))
                self.assertNotIn(current, questions)
                questions[current] = {}
                # Lessons 1–11 use inline options; selected Lesson 12 uses
                # one option per line. Support both without weakening checks.
                inline_options = re.findall(
                    r"([ABC])\) (.*?)(?= [ABC]\) |$)",
                    question.group(2),
                )
                for letter, option_text in inline_options:
                    self.assertNotIn(letter, questions[current])
                    questions[current][letter] = option_text
                continue
            option = re.match(r"^([ABC])\) (.+)$", line)
            if option and current is not None:
                self.assertNotIn(option.group(1), questions[current])
                questions[current][option.group(1)] = option.group(2)

        key_rows = re.findall(
            r"^\| (\d+) \| (\d+) \| ([ABC]) \| ([^|]+) \|",
            key_text, flags=re.MULTILINE
        )
        expected_ids = {
            (lesson, question)
            for lesson in range(1, 13)
            for question in range(1, 6)
        }
        self.assertEqual(len(questions), 60)
        self.assertEqual(len(key_rows), 60)
        self._assert_complete_unique_question_keys(
            list(questions),
            [(int(lesson), int(question)) for lesson, question, _, _ in key_rows],
            expected_ids,
        )
        for question_id, options in questions.items():
            self.assertEqual(set(options), set("ABC"), f"Incomplete options for {question_id}")
        for lesson, question, option, answer_text in key_rows:
            selected = questions[(int(lesson), int(question))][option]
            self.assertEqual(answer_text.strip(), selected, f"Answer-key mismatch at lesson {lesson}, question {question}, option {option}")

    def test_master_latin_course_pack_has_24_ordered_lessons_and_complete_quizzes(self):
        import re

        master = (ROOT / "course_data" / "latin_courses_master_draft.md").read_text(encoding="utf-8")
        self.assertIn("not runtime-loaded", master)
        course_one, course_two = master.split("## Course 2 —", 1)
        c1_numbers = [int(number) for number in re.findall(r"^## Ders (\\d+):", course_one, flags=re.MULTILINE)]
        digit_map = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
        c2_numbers = [int(number.translate(digit_map)) for number in re.findall(r"^## وانەی ([٠-٩]+) —", course_two, flags=re.MULTILINE)]
        self.assertEqual(c1_numbers, list(range(1, 13)))
        self.assertEqual(c2_numbers, list(range(1, 13)))
        self.assertEqual(master.count("### Provenance — Course 1"), 12)
        self.assertEqual(master.count("### Provenance — Course 2"), 12)
        self.assertNotIn("orthography_foundations", master)

        lesson_heads = list(re.finditer(r"^## (?:Ders \\d+:.*|وانەی [٠-٩]+ —.*)$", master, flags=re.MULTILINE))
        self.assertEqual(len(lesson_heads), 24)
        for index, heading in enumerate(lesson_heads):
            end = lesson_heads[index + 1].start() if index + 1 < len(lesson_heads) else len(master)
            lesson = master[heading.start():end]
            quiz_head = re.search(r"^### .*?(?:Testa|Kuis).*$", lesson, flags=re.MULTILINE)
            self.assertIsNotNone(quiz_head, heading.group(0))
            quiz = lesson[quiz_head.start():]
            summary = re.search(r"^### Xulasa.*$", quiz, flags=re.MULTILINE)
            if summary:
                quiz = quiz[:summary.start()]
            questions = re.findall(r"^\\d+\\. ", quiz, flags=re.MULTILINE)
            self.assertEqual(len(questions), 5, heading.group(0))

        self.assertIn("New replacement draft. The earlier exact transcript body is confirmed to have existed but is not available verbatim.", master)
        self.assertIn("New source-aligned replacement draft; the earlier exact transcript body is not available.", master)

    def test_course_one_lesson_six_recovered_prose_is_consistently_latin_script(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_06_recovered_draft.md").read_text(encoding="utf-8")
        self.assertFalse(any(chr(0x0600) <= char <= chr(0x06FF) for char in lesson_text))
        self.assertIn("Peyvên li jêr bi du koman veqetîne", lesson_text)
        self.assertIn("ji aliyê wateyê ve wekhev", lesson_text)

    def test_course_one_recovered_lessons_02_03_06_match_master_answer_keys(self):
        import re

        key_text = (ROOT / "course_data" / "latin_course_1_quiz_answer_key_draft.md").read_text(encoding="utf-8")
        paths = {
            2: "latin_course_1_lesson_02_recovered_draft.md",
            3: "latin_course_1_lesson_03_recovered_draft.md",
            6: "latin_course_1_lesson_06_recovered_draft.md",
        }
        for lesson_number, filename in paths.items():
            lesson_text = (ROOT / "course_data" / filename).read_text(encoding="utf-8")
            questions = {}
            current = None
            in_quiz = False
            for line in lesson_text.splitlines():
                if line.startswith("### 7. Testa dersê") or line.startswith("### 6. Testa Kejyarê"):
                    in_quiz = True
                    current = None
                    continue
                if in_quiz and line.startswith("### Xulasa"):
                    in_quiz = False
                    current = None
                    continue
                if not in_quiz:
                    continue
                question = re.match(r"^(\d+)\. (.+)$", line)
                if question:
                    current = int(question.group(1))
                    self.assertNotIn(current, questions)
                    questions[current] = {}
                    continue
                option = re.match(r"^\s*-\s+([A-D])\) (.+)$", line)
                if option and current is not None:
                    self.assertNotIn(option.group(1), questions[current])
                    questions[current][option.group(1)] = option.group(2)

            key_rows = re.findall(
                rf"^\| {lesson_number} \| (\d+) \| ([A-D]) \| ([^|]+) \|",
                key_text, flags=re.MULTILINE
            )
            expected = set(range(1, 6))
            self._assert_complete_unique_question_keys(
                list(questions),
                [int(number) for number, _, _ in key_rows],
                expected,
            )
            self.assertEqual(len(key_rows), 5)
            for number, letter, answer in key_rows:
                self.assertEqual(
                    questions[int(number)][letter],
                    answer.strip(),
                    f"Course 1 lesson {lesson_number}, question {number}, option {letter}",
                )

    def test_course_one_replacement_vowel_lessons_include_bedir_xan_source_examples(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lessons_04_05_replacement_draft.md").read_text(encoding="utf-8")
        lesson_four, lesson_five = lesson_text.split("## Ders 5:", 1)
        source_short = ("der", "şer", "ser", "kin", "din", "bin", "kur", "kurd", "kul")
        source_long = ("av", "sar", "bar", "dêr", "şêr", "mêr", "tîr", "zîv", "şîv", "dor", "sor", "kor", "kûr", "şûr", "dûr")
        self.assertIn("tenê dirêjahiya heman dengî nayê watekirin", lesson_four + lesson_five)
        self.assertIn("cihê derxistina dengdêrên kin û dirêj", lesson_four + lesson_five)
        for example in source_short:
            self.assertIn(f"| {example} |", lesson_four)
        for example in source_long:
            self.assertIn(f"| {example} |", lesson_five)
        self.assertNotIn("| bûk | U |", lesson_four)
        self.assertNotIn("| şûştin | U |", lesson_four)
        self.assertIn("| bûk | Û |", lesson_five)
        self.assertIn("| şûştin | Û |", lesson_five)

    def test_course_one_replacement_lessons_have_exact_answer_keys(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lessons_04_05_replacement_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lessons_04_05_answer_key.md").read_text(encoding="utf-8")
        import re

        questions = {}
        lesson_number = None
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            heading = re.match(r"^## Ders ([45]):", line)
            if heading:
                lesson_number = int(heading.group(1))
                current = None
                in_quiz = False
                continue
            if re.match(r"^### \d+\. Testa Kejyar$", line):
                in_quiz = True
                current = None
                continue
            if in_quiz and line.startswith("### Xulasa"):
                in_quiz = False
                current = None
                continue
            if not in_quiz:
                continue
            question = re.match(r"^(\d+)\. (.+)$", line)
            if question:
                current = (lesson_number, int(question.group(1)))
                self.assertNotIn(current, questions)
                questions[current] = {}
                continue
            option = re.match(r"^([A-D])\) (.+)$", line)
            if option and current is not None:
                self.assertNotIn(option.group(1), questions[current])
                questions[current][option.group(1)] = option.group(2)

        key_rows = re.findall(
            r"^\| ([45]) \| (\d+) \| ([A-D]) \| ([^|]+) \|",
            key_text, flags=re.MULTILINE
        )
        self.assertEqual(len(questions), 10)
        self.assertEqual(len(key_rows), 10)
        expected = {(lesson, question) for lesson in (4, 5) for question in range(1, 6)}
        self._assert_complete_unique_question_keys(
            list(questions),
            [(int(lesson), int(question)) for lesson, question, _, _ in key_rows],
            expected,
        )
        for question_id, options in questions.items():
            self.assertEqual(set(options), set("ABCD"), f"Incomplete options for {question_id}")
        for lesson, question, letter, answer in key_rows:
            self.assertEqual(
                questions[(int(lesson), int(question))][letter],
                answer.strip(),
            )


    def test_course_one_recovered_lessons_08_09_keys_match_original_option_order(self):
        lesson_path = ROOT / "course_data" / "latin_course_1_lessons_08_09_recovered_draft.md"
        key_path = ROOT / "course_data" / "latin_course_1_lessons_08_09_answer_key.md"
        lesson_text = lesson_path.read_text(encoding="utf-8")
        key_text = key_path.read_text(encoding="utf-8")
        questions = {}
        lesson_number = 0
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("## Ders 8:"):
                lesson_number = 8
                in_quiz = False
            elif line.startswith("## Ders 9:"):
                lesson_number = 9
                in_quiz = False
            if line.startswith("### 6. Testa Kejyar") or line.startswith("### 8. Testa Kejyar"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                if line and line[0].isdigit() and ". " in line:
                    number, _ = line.split(". ", 1)
                    current = (lesson_number, int(number))
                    self.assertNotIn(current, questions)
                    questions[current] = {}
                    continue
                if len(line) > 3 and line[0] in "ABCD" and line[1:3] == ") " and current is not None:
                    questions[current][line[0]] = line[3:]

        rows = []
        for line in key_text.splitlines():
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) >= 4 and cells[0] in {"8", "9"} and cells[1].isdigit():
                rows.append((cells[0], cells[1], cells[2], cells[3]))
        self.assertEqual(len(questions), 10)
        self.assertEqual(len(rows), 10)
        expected = {(lesson, question) for lesson in (8, 9) for question in range(1, 6)}
        self._assert_complete_unique_question_keys(list(questions), [(int(l), int(q)) for l, q, _, _ in rows], expected)
        for lesson, number, option, answer in rows:
            self.assertEqual(questions[(int(lesson), int(number))][option], answer)
        self.assertEqual([questions[(9, q)]["B"] for q in range(1, 6)], ["Ç", "Ê", "Î", "Ş", "Û"])

        lesson_eight, lesson_nine = lesson_text.split("## Ders 9:", 1)
        self.assertIn("| zivistan | navîn |", lesson_eight)
        self.assertIn("| xwîn | Î |", lesson_nine)
        circumflex_section = lesson_nine.split("### 5. Herfa Û", 1)[1].split("### 6.", 1)[0]
        self.assertNotIn("xwîn", circumflex_section)
        self.assertIn("U / Û", lesson_nine)
        self.assertNotIn("U / Ûr", lesson_nine)


    def test_course_one_lesson_twelve_recovered_practice_uses_correct_locative_form(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_12_recovered_draft.md").read_text(encoding="utf-8")
        self.assertIn("Peyv: `pirtûk — dibistanê — av — mamoste — heval`", lesson_text)
        self.assertIn("Zarok di ______ de ne.", lesson_text)
        self.assertIn("Ev pirtûka min e.", lesson_text)
        self.assertNotIn("Ev pirtûk a min e.", lesson_text)

    def test_course_one_lesson_one_describes_short_i_position_correctly(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_01_corrected_draft.md").read_text(encoding="utf-8")
        self.assertIn("Peyva `kin` bi K dest pê dike û I di nav xwe de dihewîne", lesson_text)
        self.assertIn("peyva `jin` bi J dest pê dike", lesson_text)
        self.assertNotIn("Peyva kin bi I dest pê dike", lesson_text)

    def test_course_one_lesson_one_answer_key_matches_exact_options(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_01_corrected_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lesson_01_answer_key.md").read_text(encoding="utf-8")
        questions = {}
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("### 6. Testa Kejyar"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                question = re.match(r"^\\s*(\\d+)\\. (.+)$", line)
                if question:
                    current = int(question.group(1))
                    questions[current] = {}
                    continue
                option = re.match(r"^\\s*-?\\s*([A-D])\\) (.+)$", line)
                if option and current is not None:
                    questions[current][option.group(1)] = option.group(2)
        rows = []
        for line in key_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) >= 3 and cells[0].isdigit():
                    rows.append((int(cells[0]), cells[1], cells[2]))
        self.assertEqual(len(questions), 5)
        self.assertEqual(len(rows), 5)
        self._assert_complete_unique_question_keys(list(questions), [number for number, _, _ in rows], range(1, 6))
        for number, letter, answer in rows:
            self.assertEqual(questions[number][letter], answer)


    def test_course_one_lesson_seven_answer_key_matches_exact_options(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_07_corrected_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lesson_07_answer_key.md").read_text(encoding="utf-8")
        questions = {}
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("### 6. Testa Kejyar"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                if line and line[0].isdigit() and ". " in line:
                    number, _ = line.split(". ", 1)
                    current = int(number)
                    questions[current] = {}
                    continue
                if len(line) > 3 and line[0] in "ABCD" and line[1:3] == ") ":
                    questions[current][line[0]] = line[3:]
        rows = []
        for line in key_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) >= 3 and cells[0].isdigit():
                    rows.append((int(cells[0]), cells[1], cells[2]))
        self.assertEqual(len(questions), 5)
        self.assertEqual(len(rows), 5)
        self._assert_complete_unique_question_keys(list(questions), [number for number, _, _ in rows], range(1, 6))
        for number, letter, answer in rows:
            self.assertEqual(questions[number][letter], answer)


    def test_course_one_latin_drafts_keep_latin_script_and_vowel_labels(self):
        import re
        paths = (
            "latin_course_1_lesson_01_corrected_draft.md",
            "latin_course_1_lesson_07_corrected_draft.md",
            "latin_course_1_lessons_04_05_replacement_draft.md",
            "latin_course_1_lessons_08_09_recovered_draft.md",
            "latin_course_1_lesson_10_corrected_draft.md",
            "latin_course_1_lesson_11_corrected_draft.md",
            "latin_course_1_lesson_12_recovered_draft.md",
        )
        drafts = [(ROOT / "course_data" / name).read_text(encoding="utf-8") for name in paths]
        for draft in drafts:
            self.assertIsNone(re.search(r"[\\u0600-\\u06FF]", draft))
        self.assertIn("| xwîn | Î |", drafts[2])
        self.assertNotIn("| xwîn | Û |", drafts[2])
        self.assertIn("dev/dew", drafts[3])
        self.assertIn("xwîn | Î", drafts[3])
        self.assertIn("Ev pirtûka min e.", drafts[6])


    def test_course_one_lesson_seven_does_not_misclassify_xwin_as_u_circumflex(self):
        lesson = (ROOT / "course_data" / "latin_course_1_lesson_07_corrected_draft.md").read_text(encoding="utf-8")
        long_u_section = lesson.split("### 2. Dengdêra Û", 1)[1].split("### 3.", 1)[0]
        self.assertNotIn("| xwîn | Û |", long_u_section)
        self.assertIn("xwîn", long_u_section)
        self.assertIn("bi Î tê nivîsîn", long_u_section)


    def test_course_two_replacement_lesson_twelve_key_matches_exact_options(self):
        lesson_text = (ROOT / "course_data" / "latin_course_2_lesson_12_replacement_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_2_lesson_12_answer_key.md").read_text(encoding="utf-8")
        questions = {}
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("### 10. Testa Kejyar"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                if line and line[0].isdigit() and ". " in line:
                    number, _ = line.split(". ", 1)
                    current = int(number)
                    questions[current] = {}
                    continue
                if len(line) > 3 and line[0] in "ABC" and line[1:3] == ") ":
                    questions[current][line[0]] = line[3:]
        rows = []
        for line in key_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) >= 3 and cells[0].isdigit():
                    rows.append((int(cells[0]), cells[1], cells[2]))
        self.assertEqual(len(questions), 5)
        self.assertEqual(len(rows), 5)
        self._assert_complete_unique_question_keys(list(questions), [number for number, _, _ in rows], range(1, 6))
        for number, letter, answer_text in rows:
            self.assertEqual(questions[number][letter], answer_text)


    def test_course_one_lesson_twelve_answer_key_matches_exact_options(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_12_recovered_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lesson_12_answer_key.md").read_text(encoding="utf-8")
        questions = {}
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("### 7. Testa dawî ya korsa yekem"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                if line and line[0].isdigit() and ". " in line:
                    number, _ = line.split(". ", 1)
                    current = int(number)
                    questions[current] = {}
                    continue
                if len(line) > 3 and line[0] in "ABCD" and line[1:3] == ") ":
                    questions[current][line[0]] = line[3:]
        rows = []
        for line in key_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) >= 3 and cells[0].isdigit():
                    rows.append((int(cells[0]), cells[1], cells[2]))
        self.assertEqual(len(questions), 5)
        self.assertEqual(len(rows), 5)
        self._assert_complete_unique_question_keys(list(questions), [number for number, _, _ in rows], range(1, 6))
        for number, letter, answer in rows:
            self.assertEqual(questions[number][letter], answer)


    def test_course_one_lesson_ten_answer_key_matches_exact_options(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_10_corrected_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lesson_10_answer_key.md").read_text(encoding="utf-8")
        questions = {}
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("### 7. Testa Kejyar"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                if line and line[0].isdigit() and ". " in line:
                    number, _ = line.split(". ", 1)
                    current = int(number)
                    questions[current] = {}
                    continue
                if len(line) > 3 and line[0] in "ABCD" and line[1:3] == ") ":
                    questions[current][line[0]] = line[3:]
        rows = []
        for line in key_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) >= 3 and cells[0].isdigit():
                    rows.append((int(cells[0]), cells[1], cells[2]))
        self.assertEqual(len(questions), 5)
        self.assertEqual(len(rows), 5)
        self._assert_complete_unique_question_keys(list(questions), [number for number, _, _ in rows], range(1, 6))
        for number, letter, answer in rows:
            self.assertEqual(questions[number][letter], answer)


    def test_course_one_lesson_eleven_answer_key_matches_exact_options(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_11_corrected_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lesson_11_answer_key.md").read_text(encoding="utf-8")
        questions = {}
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("### 7. Testa Kejyar"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                if line and line[0].isdigit() and ". " in line:
                    number, _ = line.split(". ", 1)
                    current = int(number)
                    questions[current] = {}
                    continue
                if len(line) > 3 and line[0] in "ABCD" and line[1:3] == ") ":
                    questions[current][line[0]] = line[3:]
        rows = []
        for line in key_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) >= 3 and cells[0].isdigit():
                    rows.append((int(cells[0]), cells[1], cells[2]))
        self.assertEqual(len(questions), 5)
        self.assertEqual(len(rows), 5)
        self._assert_complete_unique_question_keys(list(questions), [number for number, _, _ in rows], range(1, 6))
        for number, letter, answer in rows:
            self.assertEqual(questions[number][letter], answer)


    def test_course_one_replacement_lessons_four_and_five_keys_match_exact_options(self):
        import re

        lesson_text = (ROOT / "course_data" / "latin_course_1_lessons_04_05_replacement_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lessons_04_05_answer_key.md").read_text(encoding="utf-8")

        self.assertIn("li gorî dirêjî û kurtahiya dengê xwe", lesson_text)
        self.assertIn("E — I — U", lesson_text)
        self.assertIn("A — Ê — Î — O — Û", lesson_text)

        questions = {}
        lesson_number = None
        current_question = None
        in_quiz = False

        for raw_line in lesson_text.splitlines():
            line = raw_line.strip()
            lesson_heading = re.match(r"^## Ders ([45]):", line)
            if lesson_heading:
                lesson_number = int(lesson_heading.group(1))
                in_quiz = False
                continue
            if line.startswith("### ") and "Testa Kejyar" in line:
                in_quiz = True
                continue
            if in_quiz:
                if line == "### Xulasa":
                    in_quiz = False
                    continue
                question_match = re.match(r"^(\d+)\.\s+", line)
                if question_match:
                    current_question = (lesson_number, int(question_match.group(1)))
                    self.assertNotIn(current_question, questions)
                    questions[current_question] = {}
                    continue
                option_match = re.match(r"^([A-D])\)\s+(.+)$", line)
                if option_match:
                    self.assertIsNotNone(current_question)
                    option, answer = option_match.groups()
                    self.assertNotIn(option, questions[current_question])
                    questions[current_question][option] = answer

        rows = []
        for line in key_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) >= 4 and cells[0] in {"4", "5"} and cells[1].isdigit():
                    rows.append((int(cells[0]), int(cells[1]), cells[2], cells[3]))

        expected = {(lesson, question) for lesson in (4, 5) for question in range(1, 6)}
        self.assertEqual(set(questions), expected)
        self.assertEqual(len(rows), 10)
        self._assert_complete_unique_question_keys(
            list(questions),
            [(lesson, question) for lesson, question, _, _ in rows],
            expected,
        )
        for lesson, number, option, answer in rows:
            self.assertEqual(questions[(lesson, number)][option], answer)


    def test_course_one_master_answer_key_covers_all_lessons_and_matches_selected_keys(self):
        master_text = (ROOT / "course_data" / "latin_course_1_quiz_answer_key_draft.md").read_text(encoding="utf-8")
        master = {}
        for line in master_text.splitlines():
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) >= 4 and cells[0].isdigit() and cells[1].isdigit():
                key = (int(cells[0]), int(cells[1]))
                self.assertNotIn(key, master)
                master[key] = (cells[2], cells[3])

        expected = {(lesson, question) for lesson in range(1, 13) for question in range(1, 6)}
        self.assertEqual(set(master), expected)
        self.assertEqual(len(master), 60)

        selected_key_files = [
            (1, "latin_course_1_lesson_01_answer_key.md", "single"),
            (4, "latin_course_1_lessons_04_05_answer_key.md", "multi"),
            (5, "latin_course_1_lessons_04_05_answer_key.md", "multi"),
            (7, "latin_course_1_lesson_07_answer_key.md", "single"),
            (8, "latin_course_1_lessons_08_09_answer_key.md", "multi"),
            (9, "latin_course_1_lessons_08_09_answer_key.md", "multi"),
            (10, "latin_course_1_lesson_10_answer_key.md", "single"),
            (11, "latin_course_1_lesson_11_answer_key.md", "single"),
            (12, "latin_course_1_lesson_12_answer_key.md", "single"),
        ]
        for lesson, filename, shape in selected_key_files:
            key_text = (ROOT / "course_data" / filename).read_text(encoding="utf-8")
            rows = {}
            for line in key_text.splitlines():
                if not line.startswith("|"):
                    continue
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if shape == "single" and len(cells) >= 3 and cells[0].isdigit():
                    rows[int(cells[0])] = (cells[1], cells[2])
                elif shape == "multi" and len(cells) >= 4 and cells[0].isdigit() and int(cells[0]) == lesson:
                    rows[int(cells[1])] = (cells[2], cells[3])
            self.assertEqual(set(rows), set(range(1, 6)), f"Incomplete selected key for lesson {lesson}")
            for question, answer in rows.items():
                self.assertEqual(master[(lesson, question)], answer, f"Master key mismatch at lesson {lesson}, question {question}")


if __name__ == "__main__":
    unittest.main()
