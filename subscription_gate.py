"""Non-admin, self-attested channel participation prompt for KejyarBot.

Telegram does not provide a reliable way for a non-admin bot to verify channel
membership. This gate therefore records only the user's own confirmation in
volatile per-user session data; it is not proof of membership.
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationHandlerStop

REQUIRED_CHANNELS = (
    ("@zimannasi", "https://t.me/zimannasi", "چەنێڵی زمانناسی"),
    ("@f_z_k_pr", "https://t.me/f_z_k_pr", "چەنێڵی دووەم"),
)

SESSION_ATTESTATION_KEY = "required_channels_self_attested"


def subscription_prompt():
    """Build the channel links and self-attestation button."""
    rows = [
        [InlineKeyboardButton(f"📢 بەشداری {title}", url=url)]
        for _chat_id, url, title in REQUIRED_CHANNELS
    ]
    rows.append([
        InlineKeyboardButton(
            "✅ بەشدارییەکانم کردووە — بەردەوام بە",
            callback_data="subscription:check",
        )
    ])
    return InlineKeyboardMarkup(rows)


async def subscription_guard(update, context):
    """Require an explicit user confirmation without claiming API verification."""
    user = update.effective_user
    if user is None:
        return

    if context.user_data.get(SESSION_ATTESTATION_KEY):
        return

    query = update.callback_query
    if query is not None and query.data == "subscription:check":
        # This is deliberately self-attestation, not a Telegram membership check.
        context.user_data[SESSION_ATTESTATION_KEY] = True
        await query.answer("سوپاس! دەتوانیت بەردەوام بیت.")
        return

    if query is not None:
        await query.answer()

    message = update.effective_message
    if message is not None:
        await message.reply_text(
            "🔒 بۆ بەکارهێنانی کەژیار، تکایە سەرەتا بەشداری هەردوو چەنێڵەکە بکە:\n\n"
            "١. @zimannasi\n"
            "٢. @f_z_k_pr\n\n"
            "دوای بەشداری، دوگمەی «بەشدارییەکانم کردووە — بەردەوام بە» دابگرە.\n\n"
            "⚠️ چونکە بۆت ئەدمینی چەنێڵەکان نییە، ناتوانێت ئەندامبوونت بە تەکنیکی بپشکنێت. "
            "کرتەکردنی دوگمەکە تەنها پشتڕاستکردنەوەی خۆتە؛ دڵنیایی تەواوی ئەندامبوون نییە.",
            reply_markup=subscription_prompt(),
        )
    raise ApplicationHandlerStop
