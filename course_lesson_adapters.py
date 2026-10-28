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
                "review_status": raw.get("review_status", "draft_source_check_required"),
            }
            quiz_items = []
            for question in raw.get("quiz", []):
                options = question.get("options", [])
                answer_index = question.get("answer")
                if (
                    not question.get("q")
                    or not isinstance(options, list)
                    or len(options) < 2
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
    if lesson.get("source_note"):
        sections.extend(["", "📚 تێبینیی سەرچاوە", lesson["source_note"]])
    if lesson.get("review_status"):
        sections.extend(["", f"📌 دۆخی پشکنین: {lesson['review_status']}"])
    return "\n".join(sections)


def adapt_unified_orthography_lessons(payload):
    """Adapt unified-orthography drafts to namespaced lesson and quiz records.

    The returned records remain drafts; callers must not activate the course
    until every source-review flag has been resolved by an editor.
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
        sections = [f"📖 {title}"]
        if raw.get("objective"):
            sections.extend(["", "🎯 ئامانج", raw["objective"]])
        if raw.get("key_points"):
            sections.extend(["", "🔎 ڕوونکردنەوە و خاڵە سەرەکییەکان"])
            sections.extend(f"• {point}" for point in raw["key_points"])
        if raw.get("examples"):
            sections.extend(["", "✍️ نموونەکان"])
            sections.extend(
                f"• {example[0]}: {example[1]}"
                for example in raw["examples"]
                if isinstance(example, (list, tuple)) and len(example) == 2
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
        if raw.get("source_note"):
            sections.extend(["", "📚 تێبینیی سەرچاوە", raw["source_note"]])
        if raw.get("review_status"):
            sections.extend(["", f"📌 دۆخی پشکنین: {raw['review_status']}"])
        lessons_by_id[key] = {
            "title": title,
            "content": "\n".join(sections),
            "source_number": number,
            "course_id": course_id,
            "review_status": raw.get("review_status", "draft_source_check_required"),
        }
        quiz_items = []
        for question in raw.get("quiz", []):
            options = question.get("options", [])
            answer_index = question.get("answer")
            if (
                not question.get("q")
                or not isinstance(options, list)
                or len(options) < 2
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
