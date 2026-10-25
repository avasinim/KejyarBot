"""Optional speech generation for the configured, consented Kejyar voice.

Set ELEVENLABS_API_KEY and KEJYAR_VOICE_ID only after the voice owner has
authorized use and the voice has been created in the provider account.
No audio is generated or uploaded when configuration is missing.
"""

import asyncio
import json
import logging
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


logger = logging.getLogger(__name__)


def speech_is_configured() -> bool:
    return bool(os.getenv("ELEVENLABS_API_KEY") and os.getenv("KEJYAR_VOICE_ID"))


def _generate_speech(text: str) -> bytes | None:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("KEJYAR_VOICE_ID")
    if not api_key or not voice_id or not text.strip():
        return None

    # Keep responses short for conversational latency and API reliability.
    payload = {
        "inputs": [{"text": text[:1500], "voice_id": voice_id}],
        "model_id": "eleven_v4",
        "apply_text_normalization": "auto",
    }
    request = Request(
        "https://api.elevenlabs.io/v1/text-to-dialogue?output_format=mp3_44100_128",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=25) as response:
            audio = response.read()
            return audio or None
    except HTTPError as exc:
        # Do not log request headers or credentials.
        logger.warning("Speech provider returned HTTP %s", exc.code)
        return None
    except (URLError, TimeoutError, OSError) as exc:
        logger.warning("Speech provider request failed: %s", type(exc).__name__)
        return None


async def generate_speech(text: str) -> bytes | None:
    """Generate MP3 speech without blocking Telegram's async event loop."""
    return await asyncio.to_thread(_generate_speech, text)
