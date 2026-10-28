"""Safely verify the configured Telegram bot token without starting polling.

Uses the isolated checkout's .env or the process environment. Never prints the
token or raw Telegram exception details, which can contain request URLs.
"""
import asyncio
import os
from pathlib import Path

from telegram import Bot
from telegram.error import InvalidToken, NetworkError, TelegramError, TimedOut


BASE_DIR = Path(__file__).resolve().parent


def load_local_env():
    """Load .env values only when the host environment has not set them."""
    env_file = BASE_DIR / ".env"
    if not env_file.is_file():
        return
    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


async def check_telegram():
    load_local_env()
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("BOT_TOKEN")
    if not token or token == "YOUR_TELEGRAM_BOT_TOKEN":
        print("CONFIG ERROR: no usable Telegram test-bot token is configured.")
        return 2

    bot = Bot(token=token)
    initialized = False
    try:
        await bot.initialize()
        initialized = True
        info = await bot.get_me()
    except InvalidToken:
        print("AUTH ERROR: Telegram rejected the configured token. Check the isolated test-bot token.")
        return 3
    except TimedOut:
        print("NETWORK ERROR: Telegram API request timed out. Check connectivity/firewall and retry.")
        return 4
    except NetworkError:
        print("NETWORK ERROR: could not reach Telegram API. Check internet/proxy/firewall settings.")
        return 5
    except TelegramError as exc:
        # Print only the exception class; its message can include request details.
        print(f"TELEGRAM ERROR: {type(exc).__name__}. Token and request details were withheld.")
        return 6
    finally:
        if initialized:
            await bot.shutdown()

    print(f"TELEGRAM AUTH OK: @{info.username} (bot_id={info.id}). Token was not displayed.")
    print("This verifies authentication only; it does not start polling or test message delivery.")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(check_telegram()))
