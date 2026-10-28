import unittest

from course_runtime import can_open_lesson, lesson_key, visible_course_lessons


class CourseRuntimeHelperTests(unittest.TestCase):
    def test_course_one_keys_remain_legacy_compatible(self):
        self.assertEqual(lesson_key("orthography_basic", 1), "وانە_1")
        self.assertEqual(lesson_key("orthography_basic", 22), "وانە_22")

    def test_new_course_keys_are_namespaced_and_zero_padded(self):
        self.assertEqual(lesson_key("daily_conversation", 1), "daily_conversation_01")
        self.assertEqual(lesson_key("unified_orthography", 12), "unified_orthography_12")

    def test_invalid_numbers_are_rejected(self):
        for value in (0, -1, True, 1.5):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    lesson_key("daily_conversation", value)

    def test_unlocking_is_scoped_to_the_supplied_course_order(self):
        order = ["daily_conversation_01", "daily_conversation_02", "daily_conversation_03"]
        self.assertTrue(can_open_lesson(order, set(), order[0]))
        self.assertFalse(can_open_lesson(order, set(), order[1]))
        self.assertTrue(can_open_lesson(order, {order[0]}, order[1]))
        # Completing a lesson from another course cannot unlock this course.
        self.assertFalse(can_open_lesson(order, {"وانە_1"}, order[1]))

    def test_unknown_lessons_are_never_openable(self):
        self.assertFalse(can_open_lesson(["daily_conversation_01"], set(), "unified_01"))

    def test_manifest_lessons_must_exist_in_runtime_data(self):
        course = {"lesson_ids": ["وانە_1", "daily_conversation_01", "missing"]}
        data = {"وانە_1": {}, "daily_conversation_01": {}}
        self.assertEqual(visible_course_lessons(course, data), ["وانە_1", "daily_conversation_01"])


if __name__ == "__main__":
    unittest.main()
