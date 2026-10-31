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


    def test_course_two_lesson_twelve_has_one_canonical_selected_version(self):
        master = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        snapshot = (ROOT / "course_data" / "latin_course_2_lesson_12_replacement_draft.md").read_text(encoding="utf-8")
        lesson_twelve = master.split("## وانەی ١٢ —", 1)[1].split("## تێبینیی سەرچاوە", 1)[0]
        self.assertIn("Şeş cureyên rengdêrên di çavkaniyê de nas bike.", lesson_twelve)
        self.assertIn("Rengdêrên xwemalîn", lesson_twelve)
        self.assertIn("Dereceyên rengdêrên wesfîn", lesson_twelve)
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
                option = re.match(r"^- ([A-D])\) (.+)$", line)
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


    def test_course_one_replacement_lessons_08_09_keys_match_exact_options(self):
        lesson_path = ROOT / "course_data" / "latin_course_1_lessons_08_09_replacement_draft.md"
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
            if line.startswith("### 6. Testa Kejyar"):
                in_quiz = True
                continue
            if in_quiz:
                if line.startswith("### Xulasa"):
                    in_quiz = False
                    continue
                if line and line[0].isdigit() and ". " in line:
                    number, _ = line.split(". ", 1)
                    current = (lesson_number, int(number))
                    questions[current] = {}
                    continue
                if len(line) > 3 and line[0] in "ABCD" and line[1:3] == ") ":
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
            "latin_course_1_lessons_08_09_replacement_draft.md",
            "latin_course_1_lesson_10_corrected_draft.md",
            "latin_course_1_lesson_11_corrected_draft.md",
            "latin_course_1_lesson_12_corrected_draft.md",
        )
        drafts = [(ROOT / "course_data" / name).read_text(encoding="utf-8") for name in paths]
        for draft in drafts:
            self.assertIsNone(re.search(r"[\u0600-\u06FF]", draft))
        self.assertIn("| xwîn | Î |", drafts[2])
        self.assertNotIn("| xwîn | Û |", drafts[2])
        self.assertIn("cotên wateyî yeksan", drafts[3])

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
        lesson_text = (ROOT / "course_data" / "latin_course_1_lesson_12_corrected_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lesson_12_answer_key.md").read_text(encoding="utf-8")
        questions = {}
        current = None
        in_quiz = False
        for line in lesson_text.splitlines():
            if line.startswith("### 7. Testa dawî"):
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


if __name__ == "__main__":
    unittest.main()
