import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "course_data" / "latin_courses_manifest_draft.json"


class LatinCoursesManifestTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

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


    def test_course_two_quiz_answer_key_matches_exact_option_text(self):
        lesson_text = (ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_2_quiz_answer_key_draft.md").read_text(encoding="utf-8")
        questions = {}
        lesson_number = 0
        in_quiz = False
        for line in lesson_text.splitlines():
            heading = __import__("re").match(r"^## وانەی ([٠-٩]+)", line)
            if heading:
                digits = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
                lesson_number = int(heading.group(1).translate(digits))
                in_quiz = False
            if line.startswith("### Kuis"):
                in_quiz = True
                continue
            if in_quiz:
                match = __import__("re").match(r"^(\d+)\. .*? A\) (.*?) B\) (.*?) C\) (.*?)$", line)
                if match:
                    questions[(lesson_number, int(match.group(1)))] = {
                        "A": match.group(2), "B": match.group(3), "C": match.group(4)
                    }
                if line.startswith("## "):
                    in_quiz = False

        key_rows = __import__("re").findall(
            r"^\| (\d+) \| (\d+) \| ([ABC]) \| ([^|]+) \|",
            key_text, flags=__import__("re").MULTILINE
        )
        self.assertEqual(len(questions), 60)
        self.assertEqual(len(key_rows), 60)
        for lesson, question, option, answer_text in key_rows:
            selected = questions[(int(lesson), int(question))][option]
            self.assertEqual(answer_text.strip(), selected)


    def test_course_one_replacement_lessons_have_exact_answer_keys(self):
        lesson_text = (ROOT / "course_data" / "latin_course_1_lessons_04_05_replacement_draft.md").read_text(encoding="utf-8")
        key_text = (ROOT / "course_data" / "latin_course_1_lessons_04_05_answer_key.md").read_text(encoding="utf-8")
        import re
        questions = {}
        lesson_number = 0
        for line in lesson_text.splitlines():
            heading = re.match(r"^## Ders ([45]):", line)
            if heading:
                lesson_number = int(heading.group(1))
            match = re.match(r"^(\d+)\. (.+)$", line)
            if match and lesson_number in (4, 5):
                questions[(lesson_number, int(match.group(1)))] = {}
                current = (lesson_number, int(match.group(1)))
                continue
            option = re.match(r"^([A-D])\) (.+)$", line)
            if option and 'current' in locals():
                questions[current][option.group(1)] = option.group(2)

        key_rows = re.findall(
            r"^\| ([45]) \| (\d+) \| ([A-D]) \| ([^|]+) \|",
            key_text, flags=re.MULTILINE
        )
        self.assertEqual(len(questions), 10)
        self.assertEqual(len(key_rows), 10)
        for lesson, question, letter, answer in key_rows:
            self.assertEqual(questions[(int(lesson), int(question))][letter], answer.strip())




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
        for number, letter, answer in rows:
            self.assertEqual(questions[number][letter], answer)


    def test_course_one_replacement_drafts_keep_latin_script_and_vowel_labels(self):
        import re
        lesson_45 = (ROOT / "course_data" / "latin_course_1_lessons_04_05_replacement_draft.md").read_text(encoding="utf-8")
        lesson_89 = (ROOT / "course_data" / "latin_course_1_lessons_08_09_replacement_draft.md").read_text(encoding="utf-8")
        for draft in (lesson_45, lesson_89):
            self.assertIsNone(re.search(r"[\u0600-\u06FF]", draft))
        self.assertIn("| xwîn | Î |", lesson_45)
        self.assertNotIn("| xwîn | Û |", lesson_45)
        self.assertIn("cotên wateyî yeksan", lesson_89)


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
        for number, letter, answer in rows:
            self.assertEqual(questions[number][letter], answer)


if __name__ == "__main__":
    unittest.main()
