"""Required Telegram channel membership gate for KejyarBot.

The bot must be an administrator in both public channels so Telegram's
getChatMember API can reliably verify every user's membership.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationHandlerStop

logger = logging.getLogger(__name__)

REQUIRED_CHANNELS = (
    ("@zimannasi", "https://t.me/zimannasi", "چەنێڵی زمانناسی"),
    ("@f_z_k_pr", "https://t.me/f_z_k_pr", "چەنێڵی دووەم"),
)


class SubscriptionCheckError(RuntimeError):
    """Raised when Telegram cannot reliably verify channel membership."""


def _is_active_member(member):
    status = getattr(member, "status", None)
    if status in {"creator", "administrator", "member"}:
        return True
    return status == "restricted" and bool(getattr(member, "is_member", False))


async def get_missing_channels(bot, user_id):
    """Return required channels the user has not joined; fail closed on API errors."""
    missing = []
    for chat_id, invite_url, title in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
        except Exception as exc:
            logger.exception("Could not verify user %s in required channel %s", user_id, chat_id)
            raise SubscriptionCheckError(
                f"Membership verification failed for {chat_id}"
            ) from exc
        if not _is_active_member(member):
            missing.append((chat_id, invite_url, title))
    return missing


def subscription_prompt():
    """Build the join links and the explicit membership recheck button."""
    rows = [
        [InlineKeyboardButton(f"📢 بەشداری {title}", url=url)]
        for _chat_id, url, title in REQUIRED_CHANNELS
    ]
    rows.append([
        InlineKeyboardButton(
            "✅ بەشدارییەکانم پشکنین بکە",
            callback_data="subscription:check",
        )
    ])
    return InlineKeyboardMarkup(rows)


async def subscription_guard(update, context):
    """Block every bot interaction until both channel memberships are verified."""
    user = update.effective_user
    if user is None:
        return

    try:
        missing = await get_missing_channels(context.bot, user.id)
    except SubscriptionCheckError:
        message = update.effective_message
        query = update.callback_query
        if query is not None:
            await query.answer()
        if message is not None:
            await message.reply_text(
                "⚠️ ئێستا ناتوانم بەشدارییەکانت پشتڕاست بکەمەوە. "
                "تکایە دواتر هەوڵ بدەرەوە؛ ئەگەر کێشەکە بەردەوام بوو، "
                "پێویستە بەڕێوەبەری بۆت مۆڵەتی ئەدمینی بۆت لە هەردوو چەنێڵدا بدات."
            )
        raise ApplicationHandlerStop

    if not missing:
        return

    query = update.callback_query
    if query is not None:
        await query.answer()
    message = update.effective_message
    if message is not None:
        await message.reply_text(
            "🔒 بۆ بەکارهێنانی کەژیار، پێویستە سەرەتا بەشداری هەردوو چەنێڵەکە بکەیت.\n\n"
            "دوای بەشداری، دوگمەی «پشکنینی بەشداری» دابگرە.",
            reply_markup=subscription_prompt(),
        )
    raise ApplicationHandlerStop
