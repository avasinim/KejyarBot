"""Adapters for loading reviewed multi-course lesson JSON without activating it.

Course 1 remains loaded by its legacy path. These helpers only transform draft
JSON into a predictable in-memory shape; activation is a separate explicit step.
"""
from course_runtime import lesson_key


def adapt_conversation_lessons(course_id, lesson_files):
    """Return namespaced lesson and quiz dictionaries from ordered JSON payloads."""
    lessons_by_id = {}
    quizzes_by_id = {}
    expected = 1
    for payload in lesson_files:
        for raw in payload.get("lessons", []):
            number = raw.get("number")
            if not isinstance(number, int) or isinstance(number, bool) or number < 1:
                raise ValueError(f"Invalid lesson number in {course_id}: {number!r}")
            key = lesson_key(course_id, number)
            if key in lessons_by_id:
                raise ValueError(f"Duplicate lesson number in {course_id}: {number}")
            if number != expected:
                raise ValueError(
                    f"Non-contiguous lesson sequence in {course_id}: "
                    f"expected {expected}, got {number}"
                )
            expected += 1
            title = raw.get("title", "").strip()
            if not title:
                raise ValueError(f"Missing title for {key}")
            lessons_by_id[key] = {
                "title": title,
                "content": format_conversation_lesson(raw),
                "source_number": number,
                "course_id": course_id,
                "review_status": raw.get("review_status", "draft_editorial_review"),
            }
            quiz_items = []
            for question in raw.get("quiz", []):
                options = question.get("options", [])
                answer_index = question.get("answer")
                if (
                    not isinstance(question.get("q"), str)
                    or not question["q"].strip()
                    or not isinstance(options, list)
                    or len(options) < 2
                    or any(not isinstance(option, str) or not option.strip() for option in options)
                    or len(options) != len(set(options))
                    or not isinstance(answer_index, int)
                    or isinstance(answer_index, bool)
                    or not 0 <= answer_index < len(options)
                ):
                    raise ValueError(f"Invalid quiz item for {key}")
                quiz_items.append({
                    "question": question["q"],
                    "options": options,
                    "answer": options[answer_index],
                    "explanation": question.get("explanation", ""),
                })
            quizzes_by_id[key] = quiz_items
    return lessons_by_id, quizzes_by_id


def format_conversation_lesson(lesson):
    """Format a draft conversation lesson as plain Telegram-readable text."""
    sections = [f"💬 {lesson['title']}"]
    if lesson.get("objective"):
        sections.extend(["", "🎯 ئامانج", lesson["objective"]])
    if lesson.get("dialogue"):
        sections.extend(["", "🗣️ گفتوگۆ"])
        for speaker, line in lesson["dialogue"]:
            sections.append(f"{speaker}: {line}")
    if lesson.get("vocabulary"):
        sections.extend(["", "📚 وشە و دەستەواژە"])
        sections.extend(f"• {word}: {meaning}" for word, meaning in lesson["vocabulary"])
    for label, field in (
        ("✍️ ڕاهێنان", "exercises"),
        ("🧠 تێگەیشتن", "comprehension"),
    ):
        if lesson.get(field):
            sections.extend(["", label])
            sections.extend(f"{index}. {item}" for index, item in enumerate(lesson[field], 1))
    if lesson.get("role_play"):
        sections.extend(["", "🎭 ڕۆڵگێڕی", lesson["role_play"]])
    return "\n".join(sections)



# Presentation-only outline for the exceptionally dense third grammar lesson.
# Ranges are 1-based source positions: no source item is rewritten or reordered.
GRAMMAR_ACADEMIC_OUTLINES = {
    3: {
        "key_points": (
            (1, 9, "پێناسە، ناسینەوە و پۆلێنی ناو"),
            (10, 18, "دۆخی ناو و ژمارەی ڕێزمانی"),
            (19, 21, "ڕەگەز و پۆلێنکردنی واتایی"),
            (22, 25, "پێکهاتەی ناو و وشەسازی"),
            (26, 27, "سنووری بابەت: ناو و کردار"),
            (28, 35, "لێکدراو، ناوبەند و پشکنینی شێوەزاری"),
        ),
        "examples": (
            (1, 4, "نموونەی پۆل و ئەرکی ناو"),
            (5, 7, "نموونەی دۆخ و ژمارە"),
            (8, 9, "نموونەی داڕشتن و ناوی چەمکی"),
            (10, 10, "نموونەی سنووری بابەت"),
            (11, 15, "نموونەی لێکدراو و ناوبەند"),
        ),
        "appendix": (
            (1, 4, "پوختەی تیۆری و جیاوازییە بنەڕەتییەکان"),
            (5, 7, "سەرچاوە بنەڕەتییەکان"),
            (8, 10, "سنووری شێوەزار و سنووری بابەت"),
            (11, 30, "تێبینییەکانی بەڵگە، شیکردنەوە و پشکنینی زیاتر"),
        ),
    },
}


def _append_grouped_academic_items(sections, items, groups, formatter):
    """Insert navigable topic headings while preserving every source item in order."""
    expected_start = 1
    for start, end, heading in groups:
        if start != expected_start or end < start or end > len(items):
            raise ValueError("Invalid academic outline range")
        sections.extend(["", f"📖 {heading}"])
        for index in range(start - 1, end):
            sections.append(formatter(items[index], index + 1))
        expected_start = end + 1
    if expected_start != len(items) + 1:
        raise ValueError("Academic outline does not cover every source item")


def adapt_unified_orthography_lessons(payload, include_extended_sections=False):
    """Adapt course drafts to namespaced lesson and quiz records.

    Extended appendix/activity sections are opt-in so the shared adapter does
    not change the presentation of existing courses. Activation is separate.
    """
    lessons_by_id = {}
    quizzes_by_id = {}
    expected = 1
    course_id = payload.get("course_id", "unified_orthography")
    for raw in payload.get("lessons", []):
        number = raw.get("number")
        if not isinstance(number, int) or isinstance(number, bool) or number < 1:
            raise ValueError(f"Invalid lesson number in {course_id}: {number!r}")
        key = lesson_key(course_id, number)
        if key in lessons_by_id:
            raise ValueError(f"Duplicate lesson number in {course_id}: {number}")
        if number != expected:
            raise ValueError(
                f"Non-contiguous lesson sequence in {course_id}: "
                f"expected {expected}, got {number}"
            )
        expected += 1
        title = raw.get("title", "").strip()
        if not title:
            raise ValueError(f"Missing title for {key}")
        sections = [
            "✦ کەژیار ✦",
            f"📖 {title}",
        ]
        if raw.get("objective"):
            sections.extend(["", "🎯 ئامانج", raw["objective"]])
        outline = GRAMMAR_ACADEMIC_OUTLINES.get(number, {}) if course_id == "grammar" else {}
        if raw.get("key_points"):
            sections.extend(["", "🔎 ڕوونکردنەوە و خاڵە سەرەکییەکان"])
            if "key_points" in outline:
                _append_grouped_academic_items(
                    sections, raw["key_points"], outline["key_points"],
                    lambda item, index: f"• {item}",
                )
            else:
                sections.extend(f"• {point}" for point in raw["key_points"])
        if raw.get("examples"):
            sections.extend(["", "✍️ نموونەکان"])
            valid_examples = [
                example for example in raw["examples"]
                if isinstance(example, (list, tuple)) and len(example) == 2
            ]
            if "examples" in outline:
                _append_grouped_academic_items(
                    sections, valid_examples, outline["examples"],
                    lambda example, index: f"• {example[0]}: {example[1]}",
                )
            else:
                sections.extend(
                    f"• {example[0]}: {example[1]}"
                    for example in valid_examples
                )
        if include_extended_sections:
            for label, field in (
                ("📎 پاشکۆ", "appendix"),
                ("🎯 چالاکییەکان", "activities"),
            ):
                if raw.get(field):
                    sections.extend(["", label])
                    if field in outline:
                        _append_grouped_academic_items(
                            sections, raw[field], outline[field],
                            lambda item, index: f"{index}. {item}",
                        )
                    else:
                        sections.extend(
                            f"{index}. {item}"
                            for index, item in enumerate(raw[field], 1)
                        )
        for label, field in (
            ("🧩 ڕاهێنان", "exercises"),
            ("🧠 پرسیارەکانی تێگەیشتن", "comprehension"),
        ):
            if raw.get(field):
                sections.extend(["", label])
                sections.extend(
                    f"{index}. {item}"
                    for index, item in enumerate(raw[field], 1)
                )
        if raw.get("role_play"):
            sections.extend(["", "🛠️ کاری پڕاکتیکی", raw["role_play"]])
        lessons_by_id[key] = {
            "title": title,
            "content": "\n".join(sections),
            "source_number": number,
            "course_id": course_id,
            "review_status": raw.get("review_status", "draft_editorial_review"),
        }
        quiz_items = []
        for question in raw.get("quiz", []):
            options = question.get("options", [])
            answer_index = question.get("answer")
            if (
                not isinstance(question.get("q"), str)
                or not question["q"].strip()
                or not isinstance(options, list)
                or len(options) < 2
                or any(not isinstance(option, str) or not option.strip() for option in options)
                or len(options) != len(set(options))
                or not isinstance(answer_index, int)
                or isinstance(answer_index, bool)
                or not 0 <= answer_index < len(options)
            ):
                raise ValueError(f"Invalid quiz item for {key}")
            quiz_items.append({
                "question": question["q"],
                "options": options,
                "answer": options[answer_index],
                "explanation": question.get("explanation", ""),
            })
        quizzes_by_id[key] = quiz_items
    return lessons_by_id, quizzes_by_id
