import unittest

from kurdish_months import MONTH_DIALECTS, get_months_lesson, months_menu_keyboard


class KurdishMonthsTests(unittest.TestCase):
    EXPECTED = {
        "sorani": [
            "خاکەلێوە", "گوڵان / بانەمەڕ", "جۆزەردان", "پووشپەڕ",
            "گەلاوێژ", "خەرمانان", "ڕەزبەر", "گەڵاڕێزان",
            "سەرماوەز", "بەفرانبار", "ڕێبەندان", "ڕەشەمە",
        ],
        "kurmanji": [
            "نیسان", "گوڵان", "حۆزەیران", "تیرمە", "تەباخ", "ئیلون",
            "جوتمە", "مژدار", "کانوون", "چلە", "سبات (شوبات)", "ئادار",
        ],
        "kalhuri": [
            "نەورووزماڼ، جەژنان", "گوڵەزەردە، جۊەزەردان", "کەوکڕ، زەردان",
            "گاقووڕ", "شەرت‌شوان", "واهێڵان", "وەڵڼەڕێزان", "سەردەوا",
            "هەساوات", "سییەماڼ، وەفران", "کیسەتەکن", "گیاخێزان",
        ],
        "hawrami": [
            "نەورۆز", "پاژەرەژ", "چیڵکڕ", "کۆپڕ", "گەلاوێژ", "ئاوەوەرە",
            "ترازیێ", "گەڵاخەزان", "کەڵەهەرز", "ئارگا", "ڕابڕان", "سیاوکام",
        ],
        "laki": [
            "پەنجە", "میریان", "گاکور", "ئاگرانی", "مردار", "ماڵەژێر",
            "ماڵەژێر دوماینە", "تویلتەکن", "مانگ سیە", "نەورووژ",
            "خاکە لیە", "مانگ لیە",
        ],
    }

    def test_all_supplied_month_names_and_order_are_preserved(self):
        self.assertEqual(set(MONTH_DIALECTS), set(self.EXPECTED))
        for dialect, expected in self.EXPECTED.items():
            with self.subTest(dialect=dialect):
                actual = [name for name, _ in MONTH_DIALECTS[dialect]["months"]]
                self.assertEqual(actual, expected)

    def test_each_dialect_has_twelve_month_entries(self):
        for dialect, record in MONTH_DIALECTS.items():
            with self.subTest(dialect=dialect):
                self.assertEqual(len(record["months"]), 12)

    def test_sorani_persian_equivalents_are_preserved(self):
        lesson = get_months_lesson("sorani")
        self.assertIn("خاکەلێوە  —  فروردین", lesson)
        self.assertIn("گوڵان / بانەمەڕ  —  اردیبهشت", lesson)
        self.assertIn("ڕەشەمە  —  اسفند", lesson)

    def test_other_dialects_do_not_get_invented_persian_equivalents(self):
        for dialect in ("kurmanji", "kalhuri", "hawrami", "laki"):
            with self.subTest(dialect=dialect):
                self.assertTrue(
                    all(value is None for _, value in MONTH_DIALECTS[dialect]["months"])
                )

    def test_unknown_dialect_is_rejected(self):
        self.assertIsNone(get_months_lesson("unknown"))

    def test_lesson_uses_kejyar_brand_signature(self):
        self.assertIn("🤖 کەژیار — KejyarBot@", get_months_lesson("hawrami"))

    def test_dialect_keyboard_has_all_five_callback_routes(self):
        keyboard = months_menu_keyboard()
        callback_data = [row[0].callback_data for row in keyboard.inline_keyboard]
        self.assertEqual(
            callback_data,
            ["months:sorani", "months:kurmanji", "months:kalhuri", "months:hawrami", "months:laki"],
        )

    def test_lesson_numbers_use_kurdish_digits(self):
        lesson = get_months_lesson("laki")
        self.assertIn("٠١. پەنجە", lesson)
        self.assertIn("١٢. مانگ لیە", lesson)


if __name__ == "__main__":
    unittest.main()
