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
    4: {
        "key_points": (
            (1, 6, "ژمارەی ڕێزمانی و نیشانەکانی کۆ"),
            (7, 9, "ڕەگەزی سروشتی و ڕێزمانی"),
        ),
    },
    5: {
        "key_points": (
            (1, 3, "پۆلێنکردنی واتاییی ناو"),
            (4, 8, "ناسراوی، نەناسراوی و ئاماژە"),
            (9, 12, "پێکهاتەی وشە و داڕشتن"),
        ),
    },
    6: {
        "key_points": (
            (1, 3, "پێناسە و ئەرکی هاوەڵناو"),
            (4, 6, "جیاکردنەوە و ناسینەوەی هاوەڵناو"),
            (7, 9, "ئیزافە و پێکهاتەی گرێی ناوی"),
        ),
    },
    7: {
        "key_points": (
            (1, 2, "جۆرەکانی هاوەڵناو"),
            (3, 6, "دیارخەر، جێناوی پرسیار و ژمارە"),
            (7, 8, "پێکهاتەی مۆرفۆلۆژیی هاوەڵناو"),
        ),
    },
    8: {
        "key_points": (
            (1, 2, "ئەرکی هاوەڵناو لە ڕستەدا"),
            (3, 7, "پلەی چەسپاو، بەراورد و باڵا"),
            (8, 10, "سنووری بەراورد و جیاوازیی هاوەڵناو/هاوەڵکار"),
        ),
    },
    9: {
        "key_points": (
            (1, 3, "پێناسە و پۆلێنکردنی ژمارە"),
            (4, 7, "ژمارەی سادە و داڕێژراو"),
            (8, 13, "ژمارەی لێکدراو و سنووری پێکهاتە"),
        ),
    },
    10: {
        "key_points": (
            (1, 3, "پێناسە و فۆڕمی جێناوی کەسیی سەربەخۆ"),
            (4, 4, "شەش خانەی کەسی لە سۆرانی"),
            (5, 8, "ئەرک، ڕێککەوتن و بەکارهێنانی سیاقی"),
        ),
    },
    11: {
        "key_points": (
            (1, 2, "پێناسە و فۆڕمەکانی جێناوی لکاو"),
            (3, 5, "ئەرکەکانی خاوەنداری، بکەر و تەواوکەر"),
            (6, 8, "جیاکردنەوەی ئەرک و سنووری فۆڕمەکان"),
        ),
    },
    12: {
        "key_points": (
            (1, 2, "پێوەرەکانی ناسینەوەی ئەرکی لکاو"),
            (3, 5, "ڕێکخستنی ئەرجەتیڤی لە ڕابردووی تێپەڕ"),
            (6, 9, "جیاوازیی بکەر و بەرکار و شیکردنەوە"),
        ),
    },
    13: {
        "key_points": (
            (1, 4, "پێناسە، ڕەگ، بنج و فۆڕمی کردار"),
            (5, 9, "کات، ڕانەبردوو و داخوازی"),
            (10, 13, "کەس، پاشبەستە، تێپەڕی و چالاک/نەچالاک"),
        ),
    },
    14: {
        "key_points": (
            (1, 4, "تەواوکەری ناو و ئیزافە"),
            (5, 8, "تەواوکەری کردار و هاوەڵکاری"),
            (9, 10, "ڕێکاری شیکردنەوەی ڕستە"),
        ),
    },
    15: {
        "key_points": (
            (1, 4, "چوار دەمی سەرەکیی ڕابردوو"),
            (5, 7, "فۆڕم و گۆڕانی مۆرفۆلۆژی"),
            (8, 10, "نەرێکردن و لێکدانەوەی سیاقی"),
        ),
    },
    16: {
        "key_points": (
            (1, 4, "دۆزینەوەی بنجی ئێستا"),
            (5, 7, "فۆڕمی ڕانەبردوو و واتای کاتی"),
            (8, 10, "کەس، نەرێ و شیکردنەوەی فۆڕم"),
        ),
    },
    17: {
        "key_points": (
            (1, 2, "پێناسە و کەسی داخوازی"),
            (3, 6, "دروستکردنی فۆڕمی داخوازی و نائاساییەکان"),
            (7, 10, "نەرێکردن، ژمارە و پشکنینی فۆڕم"),
        ),
    },
    18: {
        "key_points": (
            (1, 3, "پێناسە و گۆڕینی چالاک بۆ نەچالاک"),
            (4, 6, "نموونە، ئەنجامدەر و فۆڕمی نەچالاک"),
            (7, 8, "سنووری بەکارهێنان و جیاوازیی ڕێزمانی"),
        ),
    },
    19: {
        "key_points": (
            (1, 2, "پێناسە و جیاوازیی هاوەڵکار/هاوەڵکاری"),
            (3, 4, "هاوەڵکاریی کات و شوێن"),
            (5, 8, "نموونە، گرێی پێشبەندی و ئەرک"),
        ),
    },
    20: {
        "key_points": (
            (1, 3, "داڕشتنی هاوەڵکاری"),
            (4, 6, "جیاوازیی پێشبەندی و وشەی داڕێژراو"),
            (7, 8, "بەراوردی پێشگر و پاشگر"),
        ),
    },
    21: {
        "key_points": (
            (1, 4, "پێکهاتەی کردار و توخمی شوێنی"),
            (5, 6, "هاوەڵناو بە ئەرکی هاوەڵکاری"),
            (7, 8, "جیاوازیی پۆلی وشە و ئەرکی ڕستە"),
        ),
    },
    22: {
        "key_points": (
            (1, 2, "پێناسە و پێشبەندە سەربەخۆکان"),
            (3, 5, "واتا و ئەرکی لە، بە و بۆ"),
            (6, 8, "گرێی پێشبەندی و سنووری پۆلێنکردن"),
        ),
    },
    23: {
        "key_points": (
            (1, 2, "پێناسە و پێوەرەکانی ئامرازی پەیوەندی"),
            (3, 6, "هاولکیی هاوتا و پەیوەندیی هەڵبژاردن/نەرێ"),
            (7, 8, "پارتیکڵ و بەستەرە پێویستەکانی شیکردنەوە"),
        ),
    },
    24: {
        "key_points": (
            (1, 2, "پێناسە و فۆڕمەکانی بانگکردن"),
            (3, 5, "شوێنی پێش و دوای ناوی بانگکراو"),
            (6, 8, "جیاوازیی ئەرک و پۆلێنکردن"),
        ),
    },
    25: {
        "key_points": (
            (1, 3, "پێناسەی ئیزافە و جۆرەکانی"),
            (4, 7, "جیاوازیی ئیزافە و پاشبەستە و سنووری شێوەزار"),
            (8, 8, "ناونانی جۆرەکانی گرێی خستنەپاڵ"),
        ),
    },
    26: {
        "key_points": (
            (1, 4, "پێناسە و نیشانەکانی پارتیکڵی گفتوگۆیی"),
            (5, 8, "ئەرک و شوێنی پارتیکڵەکان"),
            (9, 10, "جیاوازی لە پارتیکڵ و ئامرازەکانی تر"),
        ),
    },
    27: {
        "key_points": (
            (1, 2, "پێناسە و چوارچێوەی ئەرکەکان"),
            (3, 5, "ئەرکی دەربڕینی، ئاڕاستەکراو و پەیوەندی"),
            (6, 10, "جیاوازیی بانگکردن، پارتیکڵ و سنووری بەڵگە"),
        ),
    },
    28: {
        "key_points": (
            (1, 5, "پێناسەی چاوگ و بنەمای شیکردنەوەی بنج"),
            (6, 10, "پێنج گروپی بنجی ڕابردوو"),
            (11, 14, "ناونانی گروپەکان، فۆڕمە نائاسایی و سنووری شێوەزار"),
        ),
    },
    29: {
        "key_points": (
            (1, 3, "پێناسەی چاوگی سادە و چوارچێوەی پۆلێنکردن"),
            (4, 5, "داڕشتن و جیاوازیی لە گەردان"),
            (6, 7, "پارتیکڵی کردار و فۆڕمەکانی"),
            (8, 10, "پاشگر، پێشگر و پێکهاتەی چەندمۆرفیمی"),
            (11, 13, "پێوەرەکانی پۆلێنکردن و شیکردنەوەی نموونە"),
            (14, 14, "گۆڕانی واتا و ڕێکخستنی کردار"),
        ),
        "examples": (
            (1, 2, "نموونەی چاوگی سادە"),
            (3, 4, "نموونەی داڕشتنی پاشگری"),
            (5, 6, "نموونەی پارتیکڵی کردار"),
            (7, 8, "نموونەی -ەوە و پێکهاتەی پێشگر/کردار"),
        ),
        "appendix": (
            (1, 1, "زاراوە و یەکسانیی زاراوە"),
            (2, 4, "سەرچاوە و شیکردنەوەی مۆرفۆلۆژی"),
            (5, 6, "پاشگر و پارتیکڵەکانی کردار"),
            (7, 9, "سەرچاوەی پشتگیری و سنووری بەڵگە"),
            (10, 11, "پەیوەندیی وانەکان و تێبینیی کۆتایی"),
        ),
    },
    30: {
        "key_points": (
            (1, 2, "پێناسەی پێکهاتەی کرداری و LV/NV"),
            (3, 8, "جۆرەکانی پێکهاتە و شێوازی دروستبوون"),
            (9, 10, "واتای کردارە سووکەکان"),
            (11, 13, "ڕێکخستنی تەواوکەر و پێوەرەکانی ناسینەوە"),
            (14, 14, "جیاوازیی ڕێبازە زانستییەکان"),
        ),
        "examples": (
            (1, 2, "پێکهاتەی ناو/هاوەڵناو + کردار"),
            (3, 4, "واتای تایبەتیی کردارە سووکەکان"),
            (5, 6, "گروپی پێشبەندی + کردار"),
            (7, 8, "پێکهاتەی هاوەڵکار و پارتیکڵ + کردار"),
        ),
        "appendix": (
            (1, 1, "زاراوە سەرەکییەکان"),
            (2, 3, "سەرچاوەی بنەڕەتی و نموونەکان"),
            (4, 6, "تایبەتمەندیی LV و NV"),
            (7, 8, "جیاوازیی ڕێباز و شێوازی نووسین"),
            (9, 12, "سنووری بەڵگە و پەیوەندیی وانەکان"),
        ),
    },
    31: {
        "key_points": (
            (1, 2, "پێناسەی چاوگ و ناوکردنی کردار"),
            (3, 6, "بەڵگەی سەرچاوە و پێکهاتەی گرێی ناوی"),
            (7, 10, "ئەرکی سینتاکسی و جیاوازیی فۆڕمەکان"),
            (11, 14, "سنووری بانگەشە و چوارچێوەی زاراوەیی"),
        ),
        "examples": (
            (1, 2, "نموونە سەرچاوەدارەکان"),
            (3, 6, "نموونەی فێرکاریی ئەرکی ناوکردن"),
            (7, 8, "بەراوردی ناوکردن و کردار"),
        ),
        "appendix": (
            (1, 3, "زاراوە و سەرچاوە بنەڕەتییەکان"),
            (4, 5, "جیاوازیی چاوگ و ناوکردن"),
            (6, 7, "ئەرکی سینتاکسی و سنووری نموونەکان"),
            (8, 10, "پەیوەندیی وانەکان و سنووری بەڵگە"),
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
