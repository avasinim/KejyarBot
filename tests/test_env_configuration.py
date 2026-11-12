"""Regression checks for startup environment configuration order."""
import unittest
from pathlib import Path


class EnvironmentConfigurationOrderTests(unittest.TestCase):
    def test_dotenv_is_loaded_before_database_module_import(self):
        source_path = Path(__file__).resolve().parents[1] / "bot.py"
        source = source_path.read_text(encoding="utf-8")

        dotenv_load = source.index('load_dotenv(BASE_DIR / ".env")')
        database_import = source.index("from database import")

        self.assertLess(
            dotenv_load,
            database_import,
            "The .env file must be loaded before database.py resolves "
            "KEJYARBOT_DB_PATH at import time.",
        )


if __name__ == "__main__":
    unittest.main()
