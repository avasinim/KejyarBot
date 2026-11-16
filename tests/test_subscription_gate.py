"""Tests for the non-admin, self-attested channel prompt."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock

from telegram.ext import ApplicationHandlerStop

from subscription_gate import (
    REQUIRED_CHANNELS,
    SESSION_ATTESTATION_KEY,
    subscription_guard,
    subscription_prompt,
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

    def test_prompt_contains_both_join_links_and_self_attestation(self):
        markup = subscription_prompt()
        buttons = [button for row in markup.inline_keyboard for button in row]
        self.assertEqual(
            [button.url for button in buttons if button.url],
            ["https://t.me/zimannasi", "https://t.me/f_z_k_pr"],
        )
        self.assertEqual(
            [button.callback_data for button in buttons if button.callback_data],
            ["subscription:check"],
        )

    async def test_self_attestation_sets_only_session_state(self):
        query = SimpleNamespace(
            data="subscription:check",
            answer=AsyncMock(),
        )
        context = SimpleNamespace(user_data={})
        update = SimpleNamespace(
            effective_user=SimpleNamespace(id=12345),
            callback_query=query,
            effective_message=SimpleNamespace(reply_text=AsyncMock()),
        )

        await subscription_guard(update, context)

        self.assertTrue(context.user_data[SESSION_ATTESTATION_KEY])
        query.answer.assert_awaited_once()
        update.effective_message.reply_text.assert_not_awaited()

    async def test_attested_user_passes_without_channel_api_or_database(self):
        context = SimpleNamespace(user_data={SESSION_ATTESTATION_KEY: True})
        update = SimpleNamespace(
            effective_user=SimpleNamespace(id=12345),
            callback_query=None,
            effective_message=SimpleNamespace(reply_text=AsyncMock()),
        )

        await subscription_guard(update, context)

        update.effective_message.reply_text.assert_not_awaited()

    async def test_unconfirmed_user_receives_prompt_and_is_stopped(self):
        context = SimpleNamespace(user_data={})
        message = SimpleNamespace(reply_text=AsyncMock())
        update = SimpleNamespace(
            effective_user=SimpleNamespace(id=12345),
            callback_query=None,
            effective_message=message,
        )

        with self.assertRaises(ApplicationHandlerStop):
            await subscription_guard(update, context)

        message.reply_text.assert_awaited_once()
        args, kwargs = message.reply_text.await_args
        self.assertIn("@zimannasi", args[0])
        self.assertIn("@f_z_k_pr", args[0])
        self.assertIn("ناتوانێت ئەندامبوونت", args[0])
        self.assertIsNotNone(kwargs.get("reply_markup"))

    async def test_other_callback_is_blocked_until_confirmation(self):
        query = SimpleNamespace(data="course_example", answer=AsyncMock())
        message = SimpleNamespace(reply_text=AsyncMock())
        context = SimpleNamespace(user_data={})
        update = SimpleNamespace(
            effective_user=SimpleNamespace(id=12345),
            callback_query=query,
            effective_message=message,
        )

        with self.assertRaises(ApplicationHandlerStop):
            await subscription_guard(update, context)

        query.answer.assert_awaited_once()
        message.reply_text.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
