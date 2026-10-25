import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

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

    def test_parallel_first_access_creates_single_user_row(self):
        user_id = 456789
        with ThreadPoolExecutor(max_workers=8) as pool:
            rows = list(pool.map(lambda _: database.get_user(user_id), range(12)))
        self.assertEqual(len(rows), 12)
        self.assertTrue(all(row[0] == user_id for row in rows))
        with database.sqlite3.connect(database.DB_NAME) as conn:
            count = conn.execute(
                "SELECT COUNT(*) FROM users WHERE user_id=?", (user_id,)
            ).fetchone()[0]
        self.assertEqual(count, 1)

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


if __name__ == "__main__":
    unittest.main()
