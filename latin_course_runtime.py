"""Lossless runtime loader for two source-separated Kurmanji Latin course drafts.

Each course reads its own dedicated lesson document and answer key. This loader
checks structure and quiz consistency; it does not certify scientific source
alignment. Lesson bodies are extracted without rewriting examples or formatting.
"""
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
COURSE1_SOURCE_PATH = ROOT / "course_data" / "latin_course_1_source_aligned_lessons_01_12.md"
COURSE2_SOURCE_PATH = ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md"
COURSE1_KEY_PATH = ROOT / "course_data" / "latin_course_1_quiz_answer_key_draft.md"
COURSE2_KEY_PATH = ROOT / "course_data" / "latin_course_2_quiz_answer_key_draft.md"

COURSES = (
    {
        "id": "kurmanji_latin_orthography",
        "source_part": "Part I — Celadet Alî Bedir-Xan — Elfabêya kurdî (Nefel, Stockholm, 2002), printed pages 11–36.",
        "first_heading": "## Ders 1:",
        "lesson_prefix": "kurmanji_latin_orthography",
        "key_path": COURSE1_KEY_PATH,
    },
    {
        "id": "kurmanji_latin_grammar",
        "source_part": "Part II — Celadet Alî Bedir-Xan — Bingehên gramera kurdmancî (Nefel, Stockholm, 2002), printed pages 37–100.",
        "first_heading": "## Ders 1 —",
        "lesson_prefix": "kurmanji_latin_grammar",
        "key_path": COURSE2_KEY_PATH,
    },
)
LESSON_HEADING = re.compile(r"^## Ders (\d+)\s*[:—-]\s*(.+?)\s*$")
QUIZ_HEADING = re.compile(r"^### .*?(?:Testa|Kuis)", re.IGNORECASE)
QUESTION = re.compile(r"^\s*(\d+)\.\s*(.*?)\s*$")
OPTION = re.compile(r"(?:^|\s)([A-D])\)\s*")


def _read(path):
    return path.read_text(encoding="utf-8")


def _split_master(master_text):
    lines = master_text.splitlines()
    starts = []
    for index, line in enumerate(lines):
        match = LESSON_HEADING.match(line)
        if match:
            starts.append((index, int(match.group(1)), match.group(2).strip()))
    blocks = []
    for position, (start, number, title) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        body = "\n".join(lines[start:end]).strip()
        # Editorial provenance notes belong in the source document, not in learner-facing lesson text.
        body = re.sub(r"(?ms)^### Provenance[^\n]*\n.*?(?=^## Ders |\Z)", "", body).strip()
        blocks.append((number, title, body))
    return blocks


def _read_answer_key(path):
    answers = {}
    for line in _read(path).splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or not cells[0].isdigit() or not cells[1].isdigit():
            continue
        lesson_number, question_number = int(cells[0]), int(cells[1])
        letter, answer = cells[2], cells[3]
        if not re.fullmatch(r"[A-D]", letter):
            raise ValueError(f"Invalid answer option in {path.name}: {line}")
        key = (lesson_number, question_number)
        if key in answers:
            raise ValueError(f"Duplicate answer key row {key} in {path.name}")
        answers[key] = (letter, answer)
    return answers


def _parse_quiz(lesson_body, lesson_number, answer_key):
    lines = lesson_body.splitlines()
    quiz_start = next((i for i, line in enumerate(lines) if QUIZ_HEADING.match(line)), None)
    if quiz_start is None:
        raise ValueError(f"Lesson {lesson_number} has no quiz heading")
    questions = []
    current = None

    def finish():
        nonlocal current
        if current is None:
            return
        if not current["question"].strip():
            raise ValueError(f"Empty question {lesson_number}.{current['number']}")
        if len(current["options"]) < 2:
            raise ValueError(f"Too few options in {lesson_number}.{current['number']}")
        normalized_options = [value.strip().casefold() for _, value in current["options"]]
        if len(normalized_options) != len(set(normalized_options)):
            raise ValueError(
                f"Duplicate quiz options in {lesson_number}.{current['number']}"
            )
        expected_letters = [chr(ord("A") + i) for i in range(len(current["options"]))]
        actual_letters = [letter for letter, _ in current["options"]]
        if actual_letters != expected_letters:
            raise ValueError(
                f"Non-contiguous option labels in {lesson_number}.{current['number']}: "
                f"{actual_letters}"
            )
        key = (lesson_number, current["number"])
        if key not in answer_key:
            raise ValueError(f"Missing answer-key row {key}")
        answer_letter, answer_text = answer_key[key]
        option_map = dict(current["options"])
        if answer_letter not in option_map or option_map[answer_letter] != answer_text:
            raise ValueError(
                f"Answer key mismatch at {key}: {answer_letter}={answer_text!r}; "
                f"source option={option_map.get(answer_letter)!r}"
            )
        if sum(value == answer_text for value in option_map.values()) != 1:
            raise ValueError(f"Correct answer must occur exactly once at {key}")
        questions.append({
            "question": current["question"].strip(),
            "options": [text for _, text in current["options"]],
            "answer": answer_text,
            "answer_letter": answer_letter,
        })
        current = None

    for line in lines[quiz_start + 1:]:
        # The KejyarBot signature is lesson branding, never part of the final MCQ option.
        if line.strip().startswith("**🤖 کەژیار — KejyarBot@**"):
            break
        qmatch = QUESTION.match(line)
        if qmatch:
            finish()
            current = {
                "number": int(qmatch.group(1)),
                "question": qmatch.group(2),
                "options": [],
            }
            # Some source lines place all options on the same line as the question.
            _append_inline_options(current, qmatch.group(2))
            if current["options"]:
                current["question"] = _strip_inline_options(qmatch.group(2))
            continue
        if current is None:
            if line.startswith("### ") or line.startswith("## "):
                break
            continue
        if line.startswith("### ") or line.startswith("## "):
            break
        option_line = line.strip()
        if option_line in {"---", "***", "___"}:
            continue
        option_line = re.sub(r"^-\s*", "", option_line)
        if re.match(r"^[A-D]\)\s*", option_line):
            _append_inline_options(current, option_line)
        elif current["options"] and option_line and not option_line.startswith("#"):
            letter, value = current["options"][-1]
            current["options"][-1] = (letter, value + " " + option_line)
    finish()
    if len(questions) != 5:
        raise ValueError(
            f"Lesson {lesson_number} must have five quiz questions; got {len(questions)}"
        )
    return questions


def _append_inline_options(target, text):
    matches = list(OPTION.finditer(text))
    if not matches:
        return
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        value = text[match.end():end].strip()
        if value:
            target["options"].append((match.group(1), value))


def _strip_inline_options(text):
    match = OPTION.search(text)
    return text[:match.start()].strip() if match else text.strip()


def load_latin_courses():
    """Return (lesson_data, quiz_data, course_records), validating all 24 lessons."""
    lesson_data, quiz_data, course_records = {}, {}, []
    for course in COURSES:
        # Each Latin course reads only its own source section/document.
        # Course 2 is never inferred as the second half of a combined master.
        source_path = (
            COURSE2_SOURCE_PATH
            if course["id"] == "kurmanji_latin_grammar"
            else COURSE1_SOURCE_PATH
        )
        source_text = _read(source_path)
        selected = _split_master(source_text)
        selected = [item for item in selected if item[2].startswith("## Ders")][:12]
        if len(selected) != 12:
            raise ValueError(f"{course['id']} must contain exactly 12 lessons; got {len(selected)}")
        answer_key = _read_answer_key(course["key_path"])
        if len(answer_key) != 60:
            raise ValueError(f"{course['id']} must have 60 answer-key rows; got {len(answer_key)}")
        ids = []
        for expected_number, (number, title, body) in enumerate(selected, 1):
            if number != expected_number:
                raise ValueError(
                    f"Non-contiguous {course['id']} sequence: expected {expected_number}, got {number}"
                )
            lesson_id = f"{course['lesson_prefix']}_{number:02d}"
            if lesson_id in lesson_data:
                raise ValueError(f"Duplicate lesson ID: {lesson_id}")
            quiz = _parse_quiz(body, number, answer_key)
            lesson_data[lesson_id] = {
                "title": title,
                "content": body,
                "source_number": number,
                "course_id": course["id"],
                "review_status": "draft_editorial_review",
            }
            quiz_data[lesson_id] = quiz
            ids.append(lesson_id)
        course_records.append({
            "id": course["id"],
            "source_part": course["source_part"],
            "lesson_ids": ids,
        })
    if len(lesson_data) != 24 or len(quiz_data) != 24:
        raise ValueError("Latin runtime loader did not produce exactly 24 lessons and quizzes")
    return lesson_data, quiz_data, course_records
