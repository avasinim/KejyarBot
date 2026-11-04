"""Kurdish month names by dialect, preserving the supplied forms verbatim."""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


MONTH_DIALECTS = {
    "sorani": {
        "title": "سۆرانی",
        "months": [
            ("خاکەلێوە", "فروردین"),
            ("گوڵان / بانەمەڕ", "اردیبهشت"),
            ("جۆزەردان", "خرداد"),
            ("پووشپەڕ", "تیر"),
            ("گەلاوێژ", "مرداد"),
            ("خەرمانان", "شهریور"),
            ("ڕەزبەر", "مهر"),
            ("گەڵاڕێزان", "آبان"),
            ("سەرماوەز", "آذر"),
            ("بەفرانبار", "دی"),
            ("ڕێبەندان", "بهمن"),
            ("ڕەشەمە", "اسفند"),
        ],
    },
    "kurmanji": {
        "title": "کورمانجی",
        "months": [
            ("نیسان", None), ("گوڵان", None), ("حۆزەیران", None),
            ("تیرمە", None), ("تەباخ", None), ("ئيلون", None),
            ("جوتمە", None), ("مژدار", None), ("کانوون", None),
            ("چلە", None), ("سبات (شوبات)", None), ("ئادار", None),
        ],
    },
    "kalhuri": {
        "title": "کەلهوڕی",
        "months": [
            ("نەورووزماڼ، جەژنان", None),
            ("گوڵەزەردە، جۊەزەردان", None),
            ("کەوکڕ، زەردان", None),
            ("گاقووڕ", None),
            ("شەرت‌شوان", None),
            ("واهێڵان", None),
            ("وەڵڼەڕێزان", None),
            ("سەردەوا", None),
            ("هەساوات", None),
            ("سییەماڼ، وەفران", None),
            ("کیسەتەکن", None),
            ("گیاخێزان", None),
        ],
    },
    "hawrami": {
        "title": "هەورامی",
        "months": [
            ("نەورۆز", None), ("پاژەرەژ", None), ("چیڵکڕ", None),
            ("کۆپڕ", None), ("گەلاوێژ", None), ("ئاوەوەرە", None),
            ("ترازیێ", None), ("گەڵاخەزان", None), ("کەڵەهەرز", None),
            ("ئارگا", None), ("ڕابڕان", None), ("سیاوکام", None),
        ],
    },
    "laki": {
        "title": "لەکی",
        "months": [
            ("پەنجە", None), ("میریان", None), ("گاکور", None),
            ("ئاگرانی", None), ("مردار", None), ("ماڵەژێر", None),
            ("ماڵەژێر دوماینە", None), ("تویلتەکن", None),
            ("مانگ سیە", None), ("نەورووژ", None), ("خاکە لیە", None),
            ("مانگ لیە", None),
        ],
    },
}


def months_menu_keyboard():
    """Return the five dialect choices for the Kurdish months learning section."""
    labels = [
        ("سۆرانی", "sorani"),
        ("کورمانجی", "kurmanji"),
        ("کەلهوڕی", "kalhuri"),
        ("هەورامی", "hawrami"),
        ("لەکی", "laki"),
    ]
    rows = [
        [InlineKeyboardButton(label, callback_data=f"months:{key}")]
        for label, key in labels
    ]
    return InlineKeyboardMarkup(rows)


def get_months_lesson(dialect):
    """Build a compact academic-style lesson without inventing cross-dialect matches."""
    record = MONTH_DIALECTS.get(dialect)
    if record is None:
        return None

    lines = [
        f"📘 زانیاریی زانستی — مانگەکانی ساڵ بە شێوەزاری {record['title']}",
        "",
        "🎯 ئامانجی فێربوون",
        "ناسینەوە و خوێندنەوەی ناوی ١٢ مانگی ساڵ لەم شێوەزارەدا.",
        "",
        "📚 لیستی مانگەکان",
    ]
    for number, (name, equivalent) in enumerate(record["months"], 1):
        if equivalent:
            lines.append(f"{number:02d}. {name}  —  {equivalent}")
        else:
            lines.append(f"{number:02d}. {name}")

    lines.extend([
        "",
        "🔎 تێبینی",
        "ناوەکان بەپێی زانیاریی پێشکەشکراو ڕیزکراون. لە شێوەزارەکاندا ناوەکان بە جیاوازی پارێزراون؛ هاوتاکردنی مانگەکان لەنێوان شێوەزارەکاندا بەبێ بەڵگە زیاد نەکراوە.",
        "",
        "✍️ ڕاهێنان",
        "ناوی مانگەکان بە ڕیز بخوێنەوە و دووبارەیان بکەرەوە.",
        "",
        "🤖 کەژیار — KejyarBot@",
    ])
    return "\n".join(lines)
