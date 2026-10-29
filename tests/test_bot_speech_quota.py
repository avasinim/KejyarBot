import sqlite3
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

    def test_concurrent_lesson_completion_rewards_are_granted_once(self):
        from concurrent.futures import ThreadPoolExecutor

        database.get_user(self.user_id)
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(
                lambda _: database.complete_lesson_with_rewards(
                    self.user_id, "daily_conversation_01"
                ),
                range(8),
            ))

        self.assertEqual(sum(results), 1)
        user = database.get_user(self.user_id)
        self.assertIn("daily_conversation_01", user[5].split(","))
        self.assertEqual(user[1], 10)  # score
        self.assertEqual(user[2], 10)  # XP
        self.assertEqual(user[8], 5)   # coins
        self.assertEqual(user[9], 1)   # chest

    def test_concurrent_quiz_completion_rewards_are_granted_once(self):
        from concurrent.futures import ThreadPoolExecutor

        database.get_user(self.user_id)
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(
                lambda _: database.complete_quiz_with_rewards(
                    self.user_id, "daily_conversation_01"
                ),
                range(8),
            ))

        self.assertEqual(sum(results), 1)
        user = database.get_user(self.user_id)
        self.assertIn("daily_conversation_01", user[10].split(","))
        self.assertEqual(user[1], 20)  # score
        self.assertEqual(user[2], 20)  # XP
        self.assertEqual(user[7], 1)   # completed quiz count

    def test_concurrent_chest_opening_consumes_only_available_chest(self):
        from concurrent.futures import ThreadPoolExecutor

        database.get_user(self.user_id)
        database.add_chest(self.user_id)
        with ThreadPoolExecutor(max_workers=10) as pool:
            rewards = list(pool.map(
                lambda _: database.open_chest(self.user_id), range(10)
            ))

        paid_rewards = [reward for reward in rewards if reward > 0]
        self.assertEqual(len(paid_rewards), 1)
        user = database.get_user(self.user_id)
        self.assertEqual(user[9], 0)  # no chest can be consumed twice
        self.assertEqual(user[8], paid_rewards[0])  # coins match the single reward

    def test_chest_opening_rolls_back_if_coin_write_fails(self):
        database.get_user(self.user_id)
        database.add_chest(self.user_id)
        conn = sqlite3.connect(database.DB_NAME)
        try:
            conn.execute("""
                CREATE TRIGGER fail_chest_reward
                BEFORE UPDATE OF coins ON users
                BEGIN
                    SELECT RAISE(ABORT, 'injected chest reward failure');
                END
            """)
            conn.commit()
        finally:
            conn.close()

        with self.assertRaises(sqlite3.IntegrityError):
            database.open_chest(self.user_id)

        user = database.get_user(self.user_id)
        self.assertEqual(user[9], 1)  # failed opening does not consume the chest
        self.assertEqual(user[8], 0)  # failed opening does not grant coins

    def test_lesson_reward_transaction_rolls_back_on_database_error(self):
        database.get_user(self.user_id)
        conn = sqlite3.connect(database.DB_NAME)
        try:
            conn.execute("""
                CREATE TRIGGER fail_lesson_reward
                BEFORE UPDATE OF completed_lessons ON users
                WHEN NEW.completed_lessons LIKE '%daily_conversation_01%'
                BEGIN
                    SELECT RAISE(ABORT, 'injected lesson write failure');
                END
            """)
            conn.commit()
        finally:
            conn.close()

        with self.assertRaises(Exception):
            database.complete_lesson_with_rewards(
                self.user_id, "daily_conversation_01"
            )

        user = database.get_user(self.user_id)
        self.assertEqual(user[5], "")
        self.assertEqual(user[1], 0)  # score
        self.assertEqual(user[2], 0)  # XP
        self.assertEqual(user[8], 0)  # coins
        self.assertEqual(user[9], 0)  # chest

    def test_quiz_reward_transaction_rolls_back_on_database_error(self):
        database.get_user(self.user_id)
        conn = __import__("sqlite3").connect(database.DB_NAME)
        try:
            conn.execute("""
                CREATE TRIGGER fail_quiz_reward
                BEFORE UPDATE OF completed_quizzes ON users
                WHEN NEW.completed_quizzes LIKE '%daily_conversation_01%'
                BEGIN
                    SELECT RAISE(ABORT, 'injected quiz write failure');
                END
            """)
            conn.commit()
        finally:
            conn.close()

        with self.assertRaises(Exception):
            database.complete_quiz_with_rewards(
                self.user_id, "daily_conversation_01"
            )

        user = database.get_user(self.user_id)
        self.assertEqual(user[10], "")
        self.assertEqual(user[1], 0)  # score
        self.assertEqual(user[2], 0)  # XP
        self.assertEqual(user[7], 0)  # completed quiz count

    def test_concurrent_quota_reservations_never_exceed_daily_cap(self):
        from concurrent.futures import ThreadPoolExecutor

        attempts = 60
        cap = 20
        with ThreadPoolExecutor(max_workers=12) as pool:
            results = list(pool.map(
                lambda _: database.reserve_speech_quota(
                    self.user_id, self.quota_date, limit=cap
                ),
                range(attempts),
            ))

        self.assertEqual(sum(results), cap)
        self.assertEqual(
            database.get_speech_quota_used(self.user_id, self.quota_date),
            cap,
        )

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
