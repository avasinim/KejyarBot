import unittest
from unittest.mock import patch

import bot


class RuntimeCourseProgressionTests(unittest.TestCase):
    def test_next_lesson_stays_inside_the_assigned_course(self):
        for course in bot.COURSES:
            lessons = bot.course_lessons(course["id"])
            for index, lesson in enumerate(lessons):
                expected = lessons[index + 1] if index + 1 < len(lessons) else None
                self.assertEqual(bot.next_lesson_in_course(lesson), expected, lesson)
                if expected is not None:
                    self.assertIs(bot.COURSE_BY_LESSON[expected], course)

    def test_course_boundary_never_uses_global_legacy_order(self):
        active_courses = [course for course in bot.COURSES if bot.course_lessons(course["id"])]
        for course in active_courses:
            last = bot.course_lessons(course["id"])[-1]
            self.assertIsNone(bot.next_lesson_in_course(last), last)

    def test_first_lesson_of_each_active_course_has_independent_entry(self):
        active_courses = [course for course in bot.COURSES if bot.course_lessons(course["id"])]
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            for course in active_courses:
                first_lesson = bot.course_lessons(course["id"])[0]
                self.assertTrue(bot.can_open(987654321, first_lesson), first_lesson)

    def test_second_lesson_requires_previous_lesson_in_same_course(self):
        active_courses = [course for course in bot.COURSES if len(bot.course_lessons(course["id"])) > 1]
        for course in active_courses:
            lessons = bot.course_lessons(course["id"])
            with patch.object(bot, "get_completed_lessons", return_value=[]):
                self.assertFalse(bot.can_open(987654321, lessons[1]), lessons[1])
            with patch.object(bot, "get_completed_lessons", return_value=[lessons[0]]):
                self.assertTrue(bot.can_open(987654321, lessons[1]), lessons[1])


if __name__ == "__main__":
    unittest.main()
