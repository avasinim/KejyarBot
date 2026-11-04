import unittest

from kurdish_months import MONTH_DIALECTS, get_months_lesson


class KurdishMonthsTests(unittest.TestCase):
    def test_five_dialects_are_available(self):
        self.assertEqual(
            set(MONTH_DIALECTS),
            {"sorani", "kurmanji", "kalhuri", "hawrami", "laki"},
        )

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
                self.assertTrue(all(value is None for _, value in MONTH_DIALECTS[dialect]["months"]))

    def test_unknown_dialect_is_rejected(self):
        self.assertIsNone(get_months_lesson("unknown"))

    def test_lesson_uses_kejyar_brand_signature(self):
        self.assertIn("🤖 کەژیار — KejyarBot@", get_months_lesson("hawrami"))


if __name__ == "__main__":
    unittest.main()
