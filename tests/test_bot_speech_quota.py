import unittest
from unittest.mock import AsyncMock, patch

import bot


class SpeechQuotaTests(unittest.IsolatedAsyncioTestCase):
    async def test_failed_generation_does_not_consume_daily_quota(self):
        state = {"speech_quota_date": bot.date.today().isoformat(), "speech_quota_used": 3}
        message = type("Message", (), {"reply_voice": AsyncMock()})()

        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock(return_value=None)
        ):
            await bot.send_conversation_voice(message, "سڵاو", state)

        self.assertEqual(state["speech_quota_used"], 3)
        message.reply_voice.assert_not_awaited()

    async def test_successful_voice_delivery_consumes_one_quota(self):
        state = {"speech_quota_date": bot.date.today().isoformat(), "speech_quota_used": 3}
        message = type("Message", (), {"reply_voice": AsyncMock()})()

        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock(return_value=b"fake-mp3")
        ):
            await bot.send_conversation_voice(message, "سڵاو", state)

        self.assertEqual(state["speech_quota_used"], 4)
        message.reply_voice.assert_awaited_once()

    async def test_unconfigured_speech_does_not_change_quota(self):
        state = {"speech_quota_date": bot.date.today().isoformat(), "speech_quota_used": 3}
        message = type("Message", (), {"reply_voice": AsyncMock()})()

        with patch.object(bot, "speech_is_configured", return_value=False):
            await bot.send_conversation_voice(message, "سڵاو", state)

        self.assertEqual(state["speech_quota_used"], 3)
        message.reply_voice.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
