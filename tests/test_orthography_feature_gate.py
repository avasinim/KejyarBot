import unittest

from course_data.orthography_feature_gate import (
    ENV_KEY,
    is_orthography_course_enabled,
)


class OrthographyFeatureGateTests(unittest.TestCase):
    def test_missing_flag_is_disabled_by_default(self):
        self.assertFalse(is_orthography_course_enabled({}))

    def test_only_explicit_true_enables_draft_course(self):
        for value in ("1", "yes", "on", "TRUE-ish", "false", ""):
            with self.subTest(value=value):
                self.assertFalse(is_orthography_course_enabled({ENV_KEY: value}))
        self.assertTrue(is_orthography_course_enabled({ENV_KEY: "true"}))
        self.assertTrue(is_orthography_course_enabled({ENV_KEY: " TRUE "}))

    def test_legacy_dynamic_speech_flag_does_not_enable_course(self):
        self.assertFalse(
            is_orthography_course_enabled({"KEJYAR_ENABLE_DYNAMIC_SPEECH": "true"})
        )


if __name__ == "__main__":
    unittest.main()
