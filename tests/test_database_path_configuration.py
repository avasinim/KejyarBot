"""Regression tests for selecting and initializing the configured SQLite path."""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class DatabasePathConfigurationTests(unittest.TestCase):
    def run_database(self, env, code="import database; print(database.DB_NAME)"):
        return subprocess.run(
            [sys.executable, "-c", code],
            cwd=REPOSITORY_ROOT,
            env=env,
            capture_output=True,
            text=True,
        )

    def test_database_module_uses_explicit_environment_path_at_import(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            expected = str((Path(temp_dir) / "persistent" / "kejyar.db").resolve())
            env = os.environ.copy()
            env["KEJYARBOT_DB_PATH"] = expected
            result = self.run_database(env)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), expected)

    def test_database_module_keeps_project_local_default_without_override(self):
        env = os.environ.copy()
        env.pop("KEJYARBOT_DB_PATH", None)
        result = self.run_database(env)
        expected = str((REPOSITORY_ROOT / "kejyar.db").resolve())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), expected)

    def test_tilde_path_is_expanded_and_init_uses_the_same_canonical_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            env = os.environ.copy()
            env["HOME"] = temp_dir
            env["USERPROFILE"] = temp_dir
            env["KEJYARBOT_DB_PATH"] = "~/persistent data/kejyar.db"
            code = (
                "import database; database.init_db(); "
                "print(database.DB_NAME)"
            )
            result = self.run_database(env, code)
            expected = str(
                (Path(temp_dir) / "persistent data" / "kejyar.db").resolve()
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), expected)
            self.assertTrue(Path(expected).is_file())

    def test_blank_database_path_is_rejected_before_sqlite_can_create_a_file(self):
        for invalid_path in ("", "   "):
            with self.subTest(invalid_path=repr(invalid_path)):
                env = os.environ.copy()
                env["KEJYARBOT_DB_PATH"] = invalid_path
                result = self.run_database(env)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("KEJYARBOT_DB_PATH is set but empty", result.stderr)


if __name__ == "__main__":
    unittest.main()
