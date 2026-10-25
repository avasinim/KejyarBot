import json
import os
import unittest
from unittest.mock import patch, MagicMock

import speech


class SpeechGenerationTests(unittest.TestCase):
    def test_generation_is_disabled_without_credentials(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(speech.speech_is_configured())
            self.assertIsNone(speech._generate_speech("سڵاو"))

    def test_request_uses_one_configured_voice_and_kurdish_text(self):
        audio = b"fake-mp3-audio"
        response = MagicMock()
        response.__enter__.return_value.read.return_value = audio
        with patch.dict(os.environ, {
            "ELEVENLABS_API_KEY": "test-key",
            "KEJYAR_VOICE_ID": "authorized-test-voice",
            "KEJYAR_APPROVED_VOICE_ID": "authorized-test-voice",
        }, clear=True), patch.object(speech, "urlopen", return_value=response) as mocked:
            result = speech._generate_speech("سڵاو، چۆنیت؟")

        self.assertEqual(result, audio)
        request = mocked.call_args.args[0]
        self.assertEqual(request.full_url, "https://api.elevenlabs.io/v1/text-to-dialogue?output_format=mp3_44100_128")
        body = json.loads(request.data.decode("utf-8"))
        self.assertEqual(body["model_id"], "eleven_v4")
        self.assertEqual(body["inputs"], [{
            "text": "سڵاو، چۆنیت؟",
            "voice_id": "authorized-test-voice",
        }])
        self.assertEqual(mocked.call_args.kwargs["timeout"], 25)

    def test_generation_is_disabled_if_voice_is_not_explicitly_approved(self):
        with patch.dict(os.environ, {
            "ELEVENLABS_API_KEY": "test-key",
            "KEJYAR_VOICE_ID": "different-voice",
            "KEJYAR_APPROVED_VOICE_ID": "original-kejyar-voice",
        }, clear=True), patch.object(speech, "urlopen") as mocked:
            self.assertFalse(speech.speech_is_configured())
            self.assertIsNone(speech._generate_speech("سڵاو"))
            mocked.assert_not_called()

    def test_generation_is_disabled_without_approved_voice_id(self):
        with patch.dict(os.environ, {
            "ELEVENLABS_API_KEY": "test-key",
            "KEJYAR_VOICE_ID": "some-voice",
        }, clear=True):
            self.assertFalse(speech.speech_is_configured())
            self.assertIsNone(speech._generate_speech("سڵاو"))

    def test_provider_http_error_fails_gracefully(self):
        from urllib.error import HTTPError
        with patch.dict(os.environ, {
            "ELEVENLABS_API_KEY": "test-key",
            "KEJYAR_VOICE_ID": "authorized-test-voice",
            "KEJYAR_APPROVED_VOICE_ID": "authorized-test-voice",
        }, clear=True), patch.object(
            speech, "urlopen",
            side_effect=HTTPError("https://example.invalid", 401, "unauthorized", {}, None),
        ):
            self.assertIsNone(speech._generate_speech("سڵاو"))


if __name__ == "__main__":
    unittest.main()
