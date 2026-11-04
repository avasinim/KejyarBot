"""Regression guard: the bot is intentionally text-only and has no speech provider."""
import unittest

import bot


class TextOnlyRuntimeTests(unittest.TestCase):
    def test_bot_has_no_voice_or_speech_delivery_helpers(self):
        for name in ("send_voice", "send_conversation_voice", "send_kejyar_course_cue"):
            self.assertFalse(hasattr(bot, name), name)

    def test_bot_has_no_speech_provider_or_voice_module_imports(self):
        self.assertFalse(hasattr(bot, "generate_speech"))
        self.assertFalse(hasattr(bot, "speech_is_configured"))
        self.assertFalse(hasattr(bot, "get_voice"))


if __name__ == "__main__":
    unittest.main()
