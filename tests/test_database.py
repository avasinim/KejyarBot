import tempfile
from contextlib import closing
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import MagicMock, patch

import database


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_db_name = database.DB_NAME
        database.DB_NAME = str(Path(self.temp_dir.name) / "test.db")
        database.init_db()
        database.get_user(12345)

    def tearDown(self):
        database.DB_NAME = self.old_db_name
        self.temp_dir.cleanup()


    def test_init_db_rolls_back_and_closes_when_schema_setup_fails(self):
        connection = MagicMock()
        connection.cursor.return_value.execute.side_effect = RuntimeError("schema failure")
        with patch.object(database.sqlite3, "connect", return_value=connection):
            with self.assertRaisesRegex(RuntimeError, "schema failure"):
                database.init_db()
        connection.rollback.assert_called_once_with()
        connection.close.assert_called_once_with()

    def test_parallel_first_access_creates_single_user_row(self):
        user_id = 456789
        with ThreadPoolExecutor(max_workers=8) as pool:
            rows = list(pool.map(lambda _: database.get_user(user_id), range(12)))
        self.assertEqual(len(rows), 12)
        self.assertTrue(all(row[0] == user_id for row in rows))
        with closing(database.sqlite3.connect(database.DB_NAME)) as conn:
            count = conn.execute(
                "SELECT COUNT(*) FROM users WHERE user_id=?", (user_id,)
            ).fetchone()[0]
        self.assertEqual(count, 1)

    def test_reward_helpers_update_expected_fields_and_level(self):
        database.add_score(12345, 45)
        user = database.get_user(12345)
        self.assertEqual(user[1], 45)  # score
        self.assertEqual(user[2], 45)  # XP
        self.assertEqual(user[8], 5)   # score helper coin bonus
        self.assertEqual(user[3], "A1.1 🌱")

        database.add_xp(12345, 10)
        user = database.get_user(12345)
        self.assertEqual(user[1], 55)
        self.assertEqual(user[2], 55)
        self.assertEqual(user[8], 5)   # XP helper has no coin bonus
        self.assertEqual(user[3], "A1.2 🌿")

        database.add_coins(12345, 7)
        database.add_chest(12345)
        user = database.get_user(12345)
        self.assertEqual(user[8], 12)
        self.assertEqual(user[9], 1)

    def test_level_thresholds_are_consistent_at_boundaries(self):
        expected = {
            0: 'A1.1 🌱', 49: 'A1.1 🌱', 50: 'A1.2 🌿',
            99: 'A1.2 🌿', 100: 'A2.1 📘', 149: 'A2.1 📘',
            150: 'A2.2 📖', 299: 'A2.2 📖', 300: 'B1.1 🚀',
            449: 'B1.1 🚀', 450: 'B1.2 🔥', 599: 'B1.2 🔥',
            600: 'B2.1 🏆', 799: 'B2.1 🏆', 800: 'B2.2 👑',
        }
        for xp, level in expected.items():
            with self.subTest(xp=xp):
                self.assertEqual(database.calculate_level(xp), level)
    def test_lesson_completion_is_recorded_only_once(self):
        self.assertTrue(database.complete_lesson(12345, "وانە_1"))
        self.assertFalse(database.complete_lesson(12345, "وانە_1"))
        self.assertEqual(database.get_completed_lessons(12345), ["وانە_1"])

    def test_lesson_completion_grants_rewards_only_once(self):
        self.assertTrue(database.complete_lesson_with_rewards(12345, "وانە_1"))
        self.assertFalse(database.complete_lesson_with_rewards(12345, "وانە_1"))
        user = database.get_user(12345)
        self.assertEqual(user[2], 10)  # XP
        self.assertEqual(user[1], 10)  # score
        self.assertEqual(user[8], 5)   # coins
        self.assertEqual(user[9], 1)   # chests
        self.assertEqual(user[5], "وانە_1")

    def test_concurrent_lesson_reward_is_granted_once(self):
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(
                lambda _: database.complete_lesson_with_rewards(12345, "وانە_2"),
                range(16),
            ))
        self.assertEqual(sum(results), 1)
        user = database.get_user(12345)
        self.assertEqual(user[2], 10)
        self.assertEqual(user[8], 5)
        self.assertEqual(user[9], 1)

    def test_concurrent_lesson_completion_has_one_winner(self):
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(
                lambda _: database.complete_lesson(12345, "وانە_2"),
                range(16),
            ))
        self.assertEqual(sum(results), 1)
        self.assertEqual(database.get_completed_lessons(12345), ["وانە_2"])

    def test_concurrent_quiz_completion_has_one_winner(self):
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(
                lambda _: database.complete_quiz(12345, "وانە_3"),
                range(16),
            ))
        self.assertEqual(sum(results), 1)
        self.assertEqual(database.get_user(12345)[7], 1)

    def test_quiz_reward_can_be_claimed_only_once(self):
        self.assertTrue(database.complete_quiz(12345, "وانە_2"))
        self.assertFalse(database.complete_quiz(12345, "وانە_2"))
        user = database.get_user(12345)
        self.assertEqual(user[7], 1)  # tests count
        self.assertEqual(user[2], 0)  # database ledger does not award XP itself

    def test_quiz_completion_grants_xp_only_once(self):
        self.assertTrue(database.complete_quiz_with_rewards(12345, "وانە_1"))
        self.assertFalse(database.complete_quiz_with_rewards(12345, "وانە_1"))
        user = database.get_user(12345)
        self.assertEqual(user[2], 20)  # XP
        self.assertEqual(user[1], 20)  # score
        self.assertEqual(user[7], 1)   # tests
        self.assertEqual(user[8], 0)   # no lesson coin bonus

    def test_concurrent_quiz_reward_is_granted_once(self):
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(
                lambda _: database.complete_quiz_with_rewards(12345, "وانە_4"),
                range(16),
            ))
        self.assertEqual(sum(results), 1)
        user = database.get_user(12345)
        self.assertEqual(user[2], 20)
        self.assertEqual(user[7], 1)

    def test_namespaced_course_rewards_do_not_collide_with_legacy_course_one(self):
        self.assertTrue(database.complete_lesson_with_rewards(12345, "وانە_1"))
        self.assertTrue(database.complete_lesson_with_rewards(12345, "daily_conversation_01"))
        self.assertFalse(database.complete_lesson_with_rewards(12345, "وانە_1"))
        user = database.get_user(12345)
        self.assertEqual(user[2], 20)
        self.assertEqual(user[1], 20)
        self.assertEqual(user[8], 10)
        self.assertEqual(user[9], 2)
        self.assertEqual(
            set(database.get_completed_lessons(12345)),
            {"وانە_1", "daily_conversation_01"},
        )

    def test_namespaced_quiz_rewards_do_not_collide_with_legacy_course_one(self):
        self.assertTrue(database.complete_quiz_with_rewards(12345, "وانە_1"))
        self.assertTrue(database.complete_quiz_with_rewards(12345, "daily_conversation_01"))
        self.assertFalse(database.complete_quiz_with_rewards(12345, "وانە_1"))
        user = database.get_user(12345)
        self.assertEqual(user[2], 40)
        self.assertEqual(user[1], 40)
        self.assertEqual(user[7], 2)
        self.assertEqual(
            set(user[10].split(",")),
            {"وانە_1", "daily_conversation_01"},
        )

    def test_xp_reward_does_not_add_coin_bonus(self):
        before = database.get_user(12345)
        database.add_xp(12345, 20)
        after = database.get_user(12345)
        self.assertEqual(after[2] - before[2], 20)
        self.assertEqual(after[8] - before[8], 0)

    def test_chest_cannot_be_opened_without_inventory(self):
        before = database.get_user(12345)
        self.assertEqual(database.open_chest(12345), 0)
        after = database.get_user(12345)
        self.assertEqual(after[9], before[9])
        self.assertEqual(after[8], before[8])

    def test_opening_chest_consumes_one_and_awards_valid_coins(self):
        database.add_chest(12345)
        before = database.get_user(12345)
        reward = database.open_chest(12345)
        after = database.get_user(12345)
        self.assertIn(reward, {10, 20, 50, 100})
        self.assertEqual(after[9], before[9] - 1)
        self.assertEqual(after[8], before[8] + reward)

    def test_concurrent_chest_opening_never_overdraws_inventory(self):
        database.add_chest(12345)
        with ThreadPoolExecutor(max_workers=8) as pool:
            rewards = list(pool.map(lambda _: database.open_chest(12345), range(16)))
        paid_rewards = [reward for reward in rewards if reward > 0]
        self.assertEqual(len(paid_rewards), 1)
        self.assertEqual(database.get_user(12345)[9], 0)
        self.assertIn(paid_rewards[0], {10, 20, 50, 100})

    def test_concurrent_badge_updates_do_not_overwrite_each_other(self):
        badges = [f"badge-{index}" for index in range(12)]
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(lambda badge: database.add_badge(12345, badge), badges))
        self.assertEqual(set(database.get_badges(12345)), set(badges))

    def test_badges_are_not_duplicated(self):
        database.add_badge(12345, "🏅 وانەی یەکەم")
        database.add_badge(12345, "🏅 وانەی یەکەم")
        self.assertEqual(database.get_badges(12345), ["🏅 وانەی یەکەم"])

    def test_existing_database_schema_is_migrated_idempotently(self):
        database.init_db()
        database.init_db()
        user = database.get_user(12345)
        self.assertEqual(user[0], 12345)


    def test_speech_quota_persists_and_respects_daily_limit(self):
        day = "2026-10-25"
        for _ in range(20):
            self.assertTrue(database.reserve_speech_quota(12345, day, limit=20))
        self.assertFalse(database.reserve_speech_quota(12345, day, limit=20))
        # Re-reading from the database models a process restart.
        self.assertEqual(database.get_speech_quota_used(12345, day), 20)

    def test_speech_quota_is_independent_per_user_and_date(self):
        self.assertTrue(database.reserve_speech_quota(12345, "2026-10-25", limit=1))
        self.assertFalse(database.reserve_speech_quota(12345, "2026-10-25", limit=1))
        self.assertTrue(database.reserve_speech_quota(54321, "2026-10-25", limit=1))
        self.assertTrue(database.reserve_speech_quota(12345, "2026-10-26", limit=1))

    def test_concurrent_speech_quota_never_exceeds_limit(self):
        day = "2026-10-25"
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(
                lambda _: database.reserve_speech_quota(12345, day, limit=5),
                range(20),
            ))
        self.assertEqual(sum(results), 5)
        self.assertEqual(database.get_speech_quota_used(12345, day), 5)

    def test_refund_releases_only_an_existing_reservation(self):
        day = "2026-10-25"
        database.refund_speech_quota(12345, day)
        self.assertEqual(database.get_speech_quota_used(12345, day), 0)
        self.assertTrue(database.reserve_speech_quota(12345, day, limit=1))
        database.refund_speech_quota(12345, day)
        self.assertEqual(database.get_speech_quota_used(12345, day), 0)

if __name__ == "__main__":
    unittest.main()
