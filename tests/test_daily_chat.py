import unittest

from daily_chat import reply_to_daily_message


class DailyConversationTests(unittest.TestCase):
    def test_greeting_starts_a_conversation(self):
        self.assertIn("سڵاو", reply_to_daily_message("سڵاو"))

    def test_identity_is_clear(self):
        self.assertIn("کەژیارم", reply_to_daily_message("ناوت چییە؟"))

    def test_daily_market_prompt_is_useful(self):
        answer = reply_to_daily_message("لە بازاڕدا چۆن پرسیار لە نرخ بکەم؟")
        self.assertIn("چەندە", answer)

    def test_exit_phrase_disables_chat_mode(self):
        state = {"daily_chat_mode": True}
        reply_to_daily_message("خواحافیز", state)
        self.assertFalse(state["daily_chat_mode"])

    def test_empty_input_is_handled(self):
        self.assertTrue(reply_to_daily_message("   ").strip())


if __name__ == "__main__":
    unittest.main()
