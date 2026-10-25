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

    def test_goodbye_takes_priority_over_greeting_and_clears_roleplay(self):
        state = {
            "daily_chat_mode": True,
            "daily_chat_scenario": "market",
            "daily_chat_stage": 1,
        }
        reply = reply_to_daily_message("سڵاو، خواحافیز", state)
        self.assertIn("خواحافیز", reply)
        self.assertFalse(state["daily_chat_mode"])
        self.assertNotIn("daily_chat_scenario", state)
        self.assertNotIn("daily_chat_stage", state)

    def test_empty_input_is_handled(self):
        self.assertTrue(reply_to_daily_message("   ").strip())

    def test_exit_clears_roleplay_state(self):
        state = {
            "daily_chat_mode": True,
            "daily_chat_scenario": "market",
            "daily_chat_stage": 2,
        }
        reply_to_daily_message("خواحافیز", state)
        self.assertFalse(state["daily_chat_mode"])
        self.assertNotIn("daily_chat_scenario", state)
        self.assertNotIn("daily_chat_stage", state)

    def test_market_roleplay_remembers_the_scenario(self):
        state = {"daily_chat_mode": True}
        first = reply_to_daily_message("با لە بازاڕ گفتوگۆ بکەین", state)
        second = reply_to_daily_message("تکایە، ئەمە چەندە؟", state)
        self.assertIn("فرۆشیار", first)
        self.assertIn("داشکاندن", second)
        self.assertEqual(state["daily_chat_scenario"], "market")
        self.assertEqual(state["daily_chat_stage"], 2)

    def test_food_roleplay_has_a_followup_turn(self):
        state = {"daily_chat_mode": True}
        first = reply_to_daily_message("با لە خواردن گفتوگۆ بکەین", state)
        second = reply_to_daily_message("چای دەمەوێت", state)
        self.assertIn("چێشتخانە", first)
        self.assertIn("داواکاری", second)


if __name__ == "__main__":
    unittest.main()
