"""Behavioral regression tests for the startup credential gate."""
import ast
import os
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class StartupTokenGateTests(unittest.TestCase):
    def test_missing_token_stops_before_runtime_validation_and_database_init(self):
        source = (REPOSITORY_ROOT / "bot.py").read_text(encoding="utf-8")
        module = ast.parse(source, filename="bot.py")
        main_node = next(
            node
            for node in module.body
            if isinstance(node, ast.FunctionDef) and node.name == "main"
        )
        isolated_module = ast.Module(body=[main_node], type_ignores=[])
        ast.fix_missing_locations(isolated_module)

        namespace = {
            "os": os,
            "validate_activated_course_runtime": Mock(
                side_effect=AssertionError("runtime validation must not run")
            ),
            "init_db": Mock(
                side_effect=AssertionError("database initialization must not run")
            ),
        }
        exec(compile(isolated_module, "bot.py", "exec"), namespace)

        with patch.dict(
            os.environ,
            {"TELEGRAM_BOT_TOKEN": "", "BOT_TOKEN": ""},
            clear=False,
        ):
            with self.assertRaisesRegex(RuntimeError, "TELEGRAM_BOT_TOKEN"):
                namespace["main"]()

        namespace["validate_activated_course_runtime"].assert_not_called()
        namespace["init_db"].assert_not_called()


if __name__ == "__main__":
    unittest.main()
