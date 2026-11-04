import json
import re
import unittest
from pathlib import Path

from latin_course_runtime import load_latin_courses


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "course_data" / "latin_courses_manifest_draft.json"
COURSE1_SOURCE = ROOT / "course_data" / "latin_course_1_source_aligned_lessons_01_12.md"
COURSE2_SOURCE = ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md"
COURSE1_KEY = ROOT / "course_data" / "latin_course_1_quiz_answer_key_draft.md"
COURSE2_KEY = ROOT / "course_data" / "latin_course_2_quiz_answer_key_draft.md"
SIGNATURE = "🤖 کەژیار — KejyarBot@"


class LatinCoursesManifestTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_manifest_has_exactly_two_source_separated_latin_courses(self):
        courses = self.manifest["courses"]
        self.assertEqual(
            [course["id"] for course in courses],
            ["kurmanji_latin_orthography", "kurmanji_latin_grammar"],
        )
        self.assertEqual([course["order"] for course in courses], [1, 2])

    def test_each_course_has_twelve_unique_namespaced_lessons(self):
        all_ids = []
        for course in self.manifest["courses"]:
            ids = course["lesson_ids"]
            self.assertEqual(len(ids), 12)
            self.assertEqual(len(ids), len(set(ids)))
            self.assertTrue(all(item.startswith(course["id"] + "_") for item in ids))
            all_ids.extend(ids)
        self.assertEqual(len(all_ids), 24)
        self.assertEqual(len(all_ids), len(set(all_ids)))

    def test_source_metadata_names_the_two_distinct_parts_of_the_same_book(self):
        first, second = self.manifest["courses"]
        self.assertIn("Part I", first["source_part"])
        self.assertIn("Celadet Alî Bedir-Xan", first["source_part"])
        self.assertIn("Part I", first["source_part"])
        self.assertIn("Part II", second["source_part"])
        self.assertIn("Celadet Alî Bedir-Xan", second["source_part"])
        self.assertIn("Nefel, Stockholm, 2002", second["source_part"])
        self.assertNotEqual(first["source_part"], second["source_part"])

    def test_course_one_and_course_two_documents_never_mix_book_sources(self):
        first = COURSE1_SOURCE.read_text(encoding="utf-8")
        second = COURSE2_SOURCE.read_text(encoding="utf-8")
        self.assertIn("Celadet Alî Bedir-Xan", first)
        self.assertIn("Part I", first)
        self.assertNotIn("Part II", first)
        self.assertIn("Celadet Alî Bedir-Xan", second)
        self.assertIn("Nefel, Stockholm, 2002", second)
        self.assertIn("Part II", second)

    def test_both_canonical_documents_have_twelve_ordered_lesson_headings(self):
        first = COURSE1_SOURCE.read_text(encoding="utf-8")
        second = COURSE2_SOURCE.read_text(encoding="utf-8")
        first_numbers = [int(x) for x in re.findall(r"(?m)^## Ders (\d+)", first)]
        second_numbers = [int(x) for x in re.findall(r"(?m)^## Ders (\d+)", second)]
        self.assertEqual(first_numbers, list(range(1, 13)))
        self.assertEqual(second_numbers, list(range(1, 13)))

    def test_each_answer_key_has_sixty_rows_and_all_lessons(self):
        for key_path in (COURSE1_KEY, COURSE2_KEY):
            rows = []
            for line in key_path.read_text(encoding="utf-8").splitlines():
                match = re.match(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*[A-D]\s*\|", line)
                if match:
                    rows.append((int(match.group(1)), int(match.group(2))))
            expected = {(lesson, question) for lesson in range(1, 13) for question in range(1, 6)}
            self.assertEqual(len(rows), 60)
            self.assertEqual(len(rows), len(set(rows)))
            self.assertEqual(set(rows), expected)

    def test_runtime_loads_twenty_four_lessons_and_one_quiz_per_lesson(self):
        lessons, quizzes, courses = load_latin_courses()
        self.assertEqual(len(courses), 2)
        self.assertEqual(len(lessons), 24)
        self.assertEqual(len(quizzes), 24)
        for lesson_ids in (course["lesson_ids"] for course in courses):
            self.assertEqual(len(lesson_ids), 12)
            self.assertTrue(all(len(quizzes[lesson_id]) == 5 for lesson_id in lesson_ids))

    def test_course_one_lessons_eleven_and_twelve_use_part_one_material(self):
        lessons, quizzes, _ = load_latin_courses()
        lesson11 = lessons["kurmanji_latin_orthography_11"]["content"]
        lesson12 = lessons["kurmanji_latin_orthography_12"]["content"]
        self.assertIn("Nisbeta Herfên Kurdî", lesson11)
        self.assertIn("2200", lesson11)
        self.assertIn("417", lesson11)
        self.assertIn("Pêdaçûna Giştî", lesson12)
        self.assertIn("31 herf", lesson12)
        self.assertEqual(len(quizzes["kurmanji_latin_orthography_11"]), 5)
        self.assertEqual(len(quizzes["kurmanji_latin_orthography_12"]), 5)

    def test_course_two_lesson_five_preserves_the_three_source_variants(self):
        lessons, _, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_05"]["content"]
        for example in (
            "Soro kevirî tavêje",
            "Soro kê vir tavêje",
            "Soro kevir tavêje",
        ):
            self.assertIn(example, lesson)
        self.assertNotIn("Soro kê virî tavêje", lesson)

    def test_course_two_lesson_eleven_distinguishes_relative_ko_and_conjunction_ko(self):
        lessons, quizzes, _ = load_latin_courses()
        lesson = lessons["kurmanji_latin_grammar_11"]["content"]
        self.assertIn("pronavê girêkî", lesson)
        self.assertIn("gihanek", quizzes["kurmanji_latin_grammar_11"][3]["options"][1])
        self.assertEqual(quizzes["kurmanji_latin_grammar_11"][3]["answer"], "gihanek")

    def test_latin_course_lessons_keep_kurmanji_latin_text_and_kejyar_branding(self):
        lessons, _, _ = load_latin_courses()
        arabic_script = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")
        for lesson in lessons.values():
            content = lesson["content"]
            self.assertIsNone(arabic_script.search(content.replace(SIGNATURE, "")))

    def test_legacy_master_file_is_only_an_editorial_index_not_a_mixed_runtime_source(self):
        master = (ROOT / "course_data" / "latin_courses_master_draft.md").read_text(encoding="utf-8")
        self.assertIn("latin_course_1_source_aligned_lessons_01_12.md", master)
        self.assertIn("latin_course_2_source_aligned_lessons_01_12.md", master)
        self.assertNotRegex(master, r"(?m)^## Ders \d+")


if __name__ == "__main__":
    unittest.main()
