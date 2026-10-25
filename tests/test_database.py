import tempfile
import unittest
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

    def test_quiz_reward_can_be_claimed_only_once(self):
        self.assertTrue(database.complete_quiz(12345, "وانە_2"))
        self.assertFalse(database.complete_quiz(12345, "وانە_2"))
        user = database.get_user(12345)
        self.assertEqual(user[7], 1)  # tests count
        self.assertEqual(user[2], 0)  # database ledger does not award XP itself

    def test_existing_database_schema_is_migrated_idempotently(self):
        database.init_db()
        database.init_db()
        user = database.get_user(12345)
        self.assertEqual(user[0], 12345)


if __name__ == "__main__":
    unittest.main()
