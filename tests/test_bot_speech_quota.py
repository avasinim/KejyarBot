import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import AsyncMock, patch

import bot
import database


class SpeechQuotaTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_db_name = database.DB_NAME
        database.DB_NAME = str(Path(self.temp_dir.name) / "speech-quota-test.db")
        database.init_db()
        self.user_id = 12345
        self.quota_date = datetime.now(timezone.utc).date().isoformat()

    def tearDown(self):
        database.DB_NAME = self.old_db_name
        self.temp_dir.cleanup()

    async def test_failed_generation_does_not_consume_daily_quota(self):
        message = type("Message", (), {"reply_voice": AsyncMock()})()
        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock(return_value=None)
        ):
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
        self.assertEqual(database.get_speech_quota_used(self.user_id, self.quota_date), 0)
        message.reply_voice.assert_not_awaited()

    async def test_successful_voice_delivery_consumes_one_quota(self):
        message = type("Message", (), {"reply_voice": AsyncMock()})()
        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock(return_value=b"fake-mp3")
        ):
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
        self.assertEqual(database.get_speech_quota_used(self.user_id, self.quota_date), 1)
        message.reply_voice.assert_awaited_once()

    async def test_failed_delivery_refunds_reserved_quota(self):
        message = type("Message", (), {"reply_voice": AsyncMock(side_effect=RuntimeError("send failed"))})()
        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock(return_value=b"fake-mp3")
        ):
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
        self.assertEqual(database.get_speech_quota_used(self.user_id, self.quota_date), 0)
        message.reply_voice.assert_awaited_once()

    async def test_failed_refund_is_attempted_only_once_and_does_not_escape(self):
        message = type("Message", (), {"reply_voice": AsyncMock()})()
        with (
            patch.object(bot, "speech_is_configured", return_value=True),
            patch.object(bot, "generate_speech", new=AsyncMock(return_value=None)),
            patch.object(bot, "refund_speech_quota", side_effect=RuntimeError("db unavailable")) as refund,
        ):
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
        refund.assert_called_once_with(self.user_id, self.quota_date)
        self.assertEqual(database.get_speech_quota_used(self.user_id, self.quota_date), 1)
        message.reply_voice.assert_not_awaited()

    async def test_daily_cap_prevents_another_generation(self):
        for _ in range(20):
            self.assertTrue(database.reserve_speech_quota(self.user_id, self.quota_date, limit=20))
        message = type("Message", (), {"reply_voice": AsyncMock()})()
        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock()
        ) as generate:
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
        generate.assert_not_awaited()
        message.reply_voice.assert_not_awaited()
        self.assertEqual(database.get_speech_quota_used(self.user_id, self.quota_date), 20)

    async def test_unconfigured_speech_does_not_change_quota(self):
        message = type("Message", (), {"reply_voice": AsyncMock()})()
        with patch.object(bot, "speech_is_configured", return_value=False):
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
        self.assertEqual(database.get_speech_quota_used(self.user_id, self.quota_date), 0)
        message.reply_voice.assert_not_awaited()

    async def test_quota_persists_when_user_state_is_empty(self):
        message = type("Message", (), {"reply_voice": AsyncMock()})()
        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock(return_value=b"fake-mp3")
        ):
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
            await bot.send_conversation_voice(message, "سڵاو", {}, self.user_id)
        self.assertEqual(database.get_speech_quota_used(self.user_id, self.quota_date), 2)
        self.assertEqual(message.reply_voice.await_count, 2)

    async def test_missing_user_id_fails_closed(self):
        message = type("Message", (), {"reply_voice": AsyncMock()})()
        with patch.object(bot, "speech_is_configured", return_value=True), patch.object(
            bot, "generate_speech", new=AsyncMock()
        ) as generate:
            await bot.send_conversation_voice(message, "سڵاو", {})
        generate.assert_not_awaited()
        message.reply_voice.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
