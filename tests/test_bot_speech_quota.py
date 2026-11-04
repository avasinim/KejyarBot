"""Regression guard: speech quota accounting is no longer part of the bot."""
import unittest

import database


class NoSpeechQuotaTests(unittest.TestCase):
    def test_database_exposes_no_speech_quota_api(self):
        for name in ("reserve_speech_quota", "refund_speech_quota", "get_speech_quota_used"):
            self.assertFalse(hasattr(database, name), name)


if __name__ == "__main__":
    unittest.main()
