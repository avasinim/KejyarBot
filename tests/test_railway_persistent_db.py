import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import database


class RailwayPersistentDatabasePathTests(unittest.TestCase):
    def test_init_db_creates_missing_parent_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            db_path = Path(temporary) / "mounted" / "data" / "kejyar.db"
            with patch.object(database, "DB_NAME", str(db_path)):
                database.init_db()
                self.assertTrue(db_path.is_file())
                self.assertTrue(db_path.parent.is_dir())


if __name__ == "__main__":
    unittest.main()
