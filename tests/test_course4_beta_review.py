import unittest

from course_runtime import is_beta_review_lesson


class Course4BetaReviewPolicyTests(unittest.TestCase):
    def test_lesson_32_is_beta_progression_eligible(self):
        self.assertTrue(is_beta_review_lesson(
            "grammar", "grammar_32",
            {"source_number": 32, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_lesson_46_is_beta_progression_eligible(self):
        self.assertTrue(is_beta_review_lesson(
            "grammar", "grammar_46",
            {"source_number": 46, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_lessons_outside_32_to_46_are_not_eligible(self):
        for number in (31, 47, 0, -1):
            with self.subTest(number=number):
                self.assertFalse(is_beta_review_lesson(
                    "grammar", f"grammar_{number:02d}",
                    {"source_number": number, "review_status": "owner_review_pending_expanded_draft"},
                ))

    def test_other_courses_are_not_eligible(self):
        self.assertFalse(is_beta_review_lesson(
            "unified_orthography", "unified_orthography_32",
            {"source_number": 32, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_approved_or_other_review_states_are_not_beta_drafts(self):
        for status in ("approved", "scientific_review_complete_with_qualified_notes", "draft"):
            with self.subTest(status=status):
                self.assertFalse(is_beta_review_lesson(
                    "grammar", "grammar_32",
                    {"source_number": 32, "review_status": status},
                ))

    def test_id_and_source_number_must_match(self):
        self.assertFalse(is_beta_review_lesson(
            "grammar", "grammar_33",
            {"source_number": 32, "review_status": "owner_review_pending_expanded_draft"},
        ))

    def test_boolean_is_not_accepted_as_a_lesson_number(self):
        self.assertFalse(is_beta_review_lesson(
            "grammar", "grammar_01",
            {"source_number": True, "review_status": "owner_review_pending_expanded_draft"},
        ))


if __name__ == "__main__":
    unittest.main()
