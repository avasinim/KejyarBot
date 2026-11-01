import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_SOURCE = ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md"
ANSWER_KEY = ROOT / "course_data" / "latin_course_2_quiz_answer_key_draft.md"


def parse_embedded_quizzes(source_text):
    lesson_headers = list(re.finditer(r"(?m)^## Ders (\d+) —", source_text))
    quizzes = {}

    for index, header in enumerate(lesson_headers):
        lesson_number = int(header.group(1))
        lesson_end = (
            lesson_headers[index + 1].start()
            if index + 1 < len(lesson_headers)
            else len(source_text)
        )
        lesson_text = source_text[header.start():lesson_end]
        quiz_header = re.search(
            r"(?m)^### (?:Kuis — 5 pirs|10\. Testa Kejyar)\s*$",
            lesson_text,
        )
        if quiz_header is None:
            continue

        quiz_text = lesson_text[quiz_header.end():]
        question_headers = list(re.finditer(r"(?m)^(\d+)\.\s*(.*)$", quiz_text))
        questions = {}

        for question_index, question_header in enumerate(question_headers):
            question_number = int(question_header.group(1))
            question_end = (
                question_headers[question_index + 1].start()
                if question_index + 1 < len(question_headers)
                else len(quiz_text)
            )
            question_text = question_header.group(2) + "\n" + quiz_text[question_header.end():question_end]
            question_text = re.split(
                r"\n\s*(?:### Xulasa|---|\*\*🤖)",
                question_text,
                maxsplit=1,
            )[0]
            option_matches = list(re.finditer(r"(?<!\S)([ABC])\)\s*", question_text))
            options = {}

            for option_index, option_match in enumerate(option_matches):
                option_end = (
                    option_matches[option_index + 1].start()
                    if option_index + 1 < len(option_matches)
                    else len(question_text)
                )
                options[option_match.group(1)] = re.sub(
                    r"\s+", " ",
                    question_text[option_match.end():option_end],
                ).strip()

            questions[question_number] = options

        quizzes[lesson_number] = questions

    return quizzes


def parse_master_key(key_text):
    rows = {}
    for line in key_text.splitlines():
        match = re.match(
            r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([ABC])\s*\|\s*(.*?)\s*\|",
            line,
        )
        if match:
            lesson, question, option, answer = match.groups()
            key = (int(lesson), int(question))
            if key in rows:
                raise AssertionError(f"Duplicate answer-key row: {key}")
            rows[key] = (option, answer)
    return rows


class CourseTwoQuizAnswerKeyTests(unittest.TestCase):
    def test_master_answer_key_matches_all_embedded_quiz_options(self):
        quizzes = parse_embedded_quizzes(COURSE_SOURCE.read_text(encoding="utf-8"))
        answer_key = parse_master_key(ANSWER_KEY.read_text(encoding="utf-8"))

        expected = {
            (lesson, question)
            for lesson in range(1, 13)
            for question in range(1, 6)
        }
        actual = {
            (lesson, question)
            for lesson, questions in quizzes.items()
            for question in questions
        }

        self.assertEqual(actual, expected)
        self.assertEqual(set(answer_key), expected)
        self.assertEqual(len(answer_key), 60)

        for (lesson, question), (option_letter, answer_text) in answer_key.items():
            with self.subTest(lesson=lesson, question=question):
                options = quizzes[lesson][question]
                self.assertEqual(set(options), {"A", "B", "C"})
                self.assertEqual(answer_text, options[option_letter])

    def test_lesson_eleven_tests_both_distinct_uses_of_ko(self):
        quizzes = parse_embedded_quizzes(COURSE_SOURCE.read_text(encoding="utf-8"))
        answer_key = parse_master_key(ANSWER_KEY.read_text(encoding="utf-8"))

        self.assertIn("ko", quizzes[11][3]["A"])
        self.assertEqual(answer_key[(11, 3)], ("A", "ko"))
        self.assertIn("gihanek", quizzes[11][4]["B"])
        self.assertEqual(answer_key[(11, 4)], ("B", "gihanek"))


if __name__ == "__main__":
    unittest.main()
