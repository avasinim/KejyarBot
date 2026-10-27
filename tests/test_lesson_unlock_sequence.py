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

    def test_unknown_lesson_never_opens(self):
        with patch.object(bot, "get_completed_lessons", return_value=[]):
            self.assertFalse(bot.can_open(12345, "وانە_999"))


if __name__ == "__main__":
    unittest.main()
