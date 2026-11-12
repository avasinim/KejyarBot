"""Regression checks for startup environment configuration order."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class EnvironmentConfigurationOrderTests(unittest.TestCase):
    def test_dotenv_is_loaded_before_database_module_import(self):
        source_path = REPOSITORY_ROOT / "bot.py"
        source = source_path.read_text(encoding="utf-8")

        dotenv_load = source.index('load_dotenv(BASE_DIR / ".env")')
        database_import = source.index("from database import")

        self.assertLess(
            dotenv_load,
            database_import,
            "The .env file must be loaded before database.py resolves "
            "KEJYARBOT_DB_PATH at import time.",
        )

    def test_dotenv_database_path_is_applied_before_database_import(self):
        source = (REPOSITORY_ROOT / "bot.py").read_text(encoding="utf-8")
        # Execute the real startup prefix, stopping before Telegram imports.
        startup_prefix = source.split("\\nfrom telegram import", 1)[0] + "\\n"

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            shutil.copy2(REPOSITORY_ROOT / "database.py", temp_root / "database.py")
            bot_path = temp_root / "bot.py"
            bot_path.write_text(startup_prefix, encoding="utf-8")
            expected = str((temp_root / "persistent data" / "kejyar.db").resolve())
            (temp_root / ".env").write_text(
                f"KEJYARBOT_DB_PATH={expected}\\n",
                encoding="utf-8",
            )

            env = os.environ.copy()
            env.pop("KEJYARBOT_DB_PATH", None)
            code = (
                "import sys; "
                f"sys.path.insert(0, {str(temp_root)!r}); "
                f"ns = {{'__file__': {str(bot_path)!r}, '__name__': 'isolated_bot'}}; "
                f"exec(compile({startup_prefix!r}, {str(bot_path)!r}, 'exec'), ns); "
                "import database; print(database.DB_NAME)"
            )
            result = subprocess.run(
                [sys.executable, "-c", code],
                cwd=temp_root,
                env=env,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), expected)

    def test_host_environment_database_path_overrides_dotenv(self):
        source = (REPOSITORY_ROOT / "bot.py").read_text(encoding="utf-8")
        # Execute the real startup prefix, stopping before Telegram imports.
        startup_prefix = source.split("\\nfrom telegram import", 1)[0] + "\\n"

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            shutil.copy2(REPOSITORY_ROOT / "database.py", temp_root / "database.py")
            bot_path = temp_root / "bot.py"
            bot_path.write_text(startup_prefix, encoding="utf-8")
            dotenv_path = str((temp_root / "dotenv" / "kejyar.db").resolve())
            host_path = str((temp_root / "host" / "kejyar.db").resolve())
            (temp_root / ".env").write_text(
                f"KEJYARBOT_DB_PATH={dotenv_path}\\n",
                encoding="utf-8",
            )

            env = os.environ.copy()
            env["KEJYARBOT_DB_PATH"] = host_path
            code = (
                "import sys; "
                f"sys.path.insert(0, {str(temp_root)!r}); "
                f"ns = {{'__file__': {str(bot_path)!r}, '__name__': 'isolated_bot'}}; "
                f"exec(compile({startup_prefix!r}, {str(bot_path)!r}, 'exec'), ns); "
                "import database; print(database.DB_NAME)"
            )
            result = subprocess.run(
                [sys.executable, "-c", code],
                cwd=temp_root,
                env=env,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), host_path)

    def test_token_is_validated_before_runtime_validation_and_database_init(self):
        source_path = REPOSITORY_ROOT / "bot.py"
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
