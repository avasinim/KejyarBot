"""Regression tests for selecting the configured SQLite database path."""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class DatabasePathConfigurationTests(unittest.TestCase):
    def test_database_module_uses_explicit_environment_path_at_import(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            expected = str(Path(temp_dir) / "persistent" / "kejyar.db")
            env = os.environ.copy()
            env["KEJYARBOT_DB_PATH"] = expected
            result = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    "import database; print(database.DB_NAME)",
                ],
                cwd=Path(__file__).resolve().parents[1],
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )
            self.assertEqual(result.stdout.strip(), expected)

    def test_database_module_keeps_project_local_default_without_override(self):
        env = os.environ.copy()
        env.pop("KEJYARBOT_DB_PATH", None)
        result = subprocess.run(
            [
                sys.executable,
                "-c",
                "import database; print(database.DB_NAME)",
            ],
            cwd=Path(__file__).resolve().parents[1],
            env=env,
            capture_output=True,
            text=True,
            check=True,
        )
        expected = str(Path(__file__).resolve().parents[1] / "kejyar.db")
        self.assertEqual(result.stdout.strip(), expected)


if __name__ == "__main__":
    unittest.main()
