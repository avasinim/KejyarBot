"""Startup safety: missing credentials must fail before touching local state."""
import os
import unittest
from unittest.mock import patch

import bot


class BotStartupSafetyTests(unittest.TestCase):
    def test_missing_token_fails_before_database_or_telegram_initialization(self):
        with (
            patch.dict(os.environ, {}, clear=True),
            patch.object(bot, "init_db") as init_db,
            patch.object(bot, "Application") as application,
        ):
            with self.assertRaisesRegex(
                RuntimeError,
                r"TELEGRAM_BOT_TOKEN \(or BOT_TOKEN\) is missing",
            ):
                bot.main()

        init_db.assert_not_called()
        application.builder.assert_not_called()


if __name__ == "__main__":
    unittest.main()
