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

    def test_token_is_validated_before_runtime_validation_and_database_init(self):
        source_path = Path(__file__).resolve().parents[1] / "bot.py"
        source = source_path.read_text(encoding="utf-8")
        main_source = source[source.index("def main():"):]

        token_lookup = main_source.index(
            'token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("BOT_TOKEN")'
        )
        missing_token_check = main_source.index("if not token:", token_lookup)
        runtime_validation = main_source.index("validate_activated_course_runtime()")
        database_init = main_source.index("init_db()")

        self.assertLess(token_lookup, missing_token_check)
        self.assertLess(missing_token_check, runtime_validation)
        self.assertLess(
            runtime_validation,
            database_init,
            "Database initialization must happen only after required token validation.",
        )


if __name__ == "__main__":
    unittest.main()
