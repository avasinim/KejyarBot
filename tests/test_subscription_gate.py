"""Tests for the mandatory two-channel membership gate."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock

from subscription_gate import (
    REQUIRED_CHANNELS,
    SubscriptionCheckError,
    _is_active_member,
    get_missing_channels,
)


class SubscriptionGateTests(unittest.IsolatedAsyncioTestCase):
    def test_required_channels_are_the_two_owner_supplied_channels(self):
        self.assertEqual(
            tuple(item[0] for item in REQUIRED_CHANNELS),
            ("@zimannasi", "@f_z_k_pr"),
        )
        self.assertEqual(
            tuple(item[1] for item in REQUIRED_CHANNELS),
            ("https://t.me/zimannasi", "https://t.me/f_z_k_pr"),
        )

    def test_member_statuses_are_accepted(self):
        for status in ("creator", "administrator", "member"):
            with self.subTest(status=status):
                self.assertTrue(_is_active_member(SimpleNamespace(status=status)))

    def test_restricted_user_must_still_be_a_member(self):
        self.assertTrue(
            _is_active_member(SimpleNamespace(status="restricted", is_member=True))
        )
        self.assertFalse(
            _is_active_member(SimpleNamespace(status="restricted", is_member=False))
        )

    def test_left_and_kicked_users_are_not_members(self):
        for status in ("left", "kicked", None):
            with self.subTest(status=status):
                self.assertFalse(_is_active_member(SimpleNamespace(status=status)))

    async def test_both_joined_returns_no_missing_channels(self):
        bot = SimpleNamespace(
            get_chat_member=AsyncMock(
                side_effect=[
                    SimpleNamespace(status="member"),
                    SimpleNamespace(status="administrator"),
                ]
            )
        )
        self.assertEqual(await get_missing_channels(bot, 12345), [])
        self.assertEqual(bot.get_chat_member.await_count, 2)

    async def test_missing_second_channel_is_reported(self):
        bot = SimpleNamespace(
            get_chat_member=AsyncMock(
                side_effect=[
                    SimpleNamespace(status="member"),
                    SimpleNamespace(status="left"),
                ]
            )
        )
        self.assertEqual(
            await get_missing_channels(bot, 12345),
            [REQUIRED_CHANNELS[1]],
        )

    async def test_api_failure_fails_closed(self):
        bot = SimpleNamespace(
            get_chat_member=AsyncMock(side_effect=RuntimeError("bot is not admin"))
        )
        with self.assertRaises(SubscriptionCheckError):
            await get_missing_channels(bot, 12345)


if __name__ == "__main__":
    unittest.main()
