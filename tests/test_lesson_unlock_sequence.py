import unittest
from unittest.mock import patch

import bot


class LessonUnlockSequenceTests(unittest.TestCase):
    def test_each_lesson_unlocks_only_after_its_immediate_predecessor(self):
        for number in range(1, 23):
            lesson = f"وانە_{number}"
            with self.subTest(lesson=lesson):
                if number == 1:
                    completed = []
                    expected = True
                else:
                    completed = [f"وانە_{number - 2}"] if number > 2 else []
                    expected = number == 1
                with patch.object(bot, "get_completed_lessons", return_value=completed):
                    self.assertEqual(bot.can_open(12345, lesson), expected)

                if number > 1:
                    with patch.object(bot, "get_completed_lessons", return_value=[f"وانە_{number - 1}"]):
                        self.assertTrue(bot.can_open(12345, lesson))

    def test_course_progress_cannot_unlock_another_course(self):
        active_courses = [
            course for course in bot.COURSES
            if course.get("status") == "active"
        ]
        self.assertGreaterEqual(len(active_courses), 2)
        for course in active_courses:
            lesson_ids = bot.COURSE_LESSON_ORDER[course["id"]]
            self.assertGreaterEqual(len(lesson_ids), 2)
            first, second = lesson_ids[0], lesson_ids[1]
            with self.subTest(course=course["id"], lesson=second):
                # Completing an identically positioned lesson in a different
                # course must not satisfy this course's immediate predecessor.
                other_course_completion = next(
                    (
                        ids[0]
                        for other_id, ids in bot.COURSE_LESSON_ORDER.items()
                        if other_id != course["id"] and ids
                    ),
                    None,
                )
                with patch.object(
                    bot, "get_completed_lessons",
                    return_value=[other_course_completion] if other_course_completion else [],
                ):
                    self.assertFalse(bot.can_open(12345, second))
                with patch.object(bot, "get_completed_lessons", return_value=[first]):
                    self.assertTrue(bot.can_open(12345, second))

    def test_planned_course_cannot_open_even_if_it_has_runtime_lessons(self):
        planned = next(
            course for course in bot.COURSES
            if course.get("status") != "active"
        )
        lesson_ids = bot.COURSE_LESSON_ORDER.get(planned["id"], [])
        if lesson_ids:
            with patch.object(bot, "get_completed_lessons", return_value=[]):
                self.assertFalse(bot.can_open(12345, lesson_ids[0]))


    def test_unknown_lesson_never_opens(self):
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertFalse(bot.can_open(12345, "وانە_999"))


if __name__ == "__main__":
    unittest.main()
