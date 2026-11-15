"""Presentation-only pagination for Course 4 grammar lessons.

The authored lesson text is never rewritten: pages are assembled from the
existing content lines and only receive navigation labels.
"""
import re

SECTION_HEADINGS = {
    "🎯 ئامانج",
    "🔎 ڕوونکردنەوە و خاڵە سەرەکییەکان",
    "✍️ نموونەکان",
    "📎 پاشکۆ",
    "🎯 چالاکییەکان",
    "🧩 ڕاهێنان",
    "🧠 پرسیارەکانی تێگەیشتن",
    "🛠️ کاری پڕاکتیکی",
}

ITEM_PREFIX = re.compile(r"^(?:•\s+|\d+[.)]\s+)")

def build_grammar_lesson_pages(content, items_per_page=4):
    """Return ordered display pages without changing or dropping source lines.

Only section boundaries and page labels are added to the presentation layer.
"""
    lines = content.splitlines()
    sections = []
    current_title = None
    current_lines = []

    def flush():
        nonlocal current_title, current_lines
        if current_title is not None or current_lines:
            sections.append((current_title, current_lines))
        current_title, current_lines = None, []

    for line in lines:
        stripped = line.strip()
        if stripped in SECTION_HEADINGS:
            flush()
            current_title = line
        else:
            current_lines.append(line)
    flush()

    pages = []
    for title, section_lines in sections:
        meaningful = [line for line in section_lines if line.strip()]
        if not meaningful and not title:
            continue
        if title and title.strip() in {"🎯 ئامانج", "🛠️ کاری پڕاکتیکی"}:
            pages.append("\n".join([title, *meaningful]).strip())
            continue
        if title and meaningful and all(ITEM_PREFIX.match(line.strip()) for line in meaningful):
            for start in range(0, len(meaningful), items_per_page):
                pages.append("\n".join([title, *meaningful[start:start + items_per_page]]).strip())
        else:
            # Introductory text, objective prose, or mixed-format content stays intact.
            pages.append("\n".join(([title] if title else []) + section_lines).strip())

    pages = [page for page in pages if page]
    return pages or [content.strip()]
