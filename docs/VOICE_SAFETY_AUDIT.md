# Voice Safety Audit — KejyarBot

Date: 2026-10-25  
Branch: `fix/kejyarbot-stability-2026-10-25`

## User requirement

The bot must preserve the exact existing woman's Kejyar voice. Do not silently substitute a different voice. No production deployment or production bot changes are authorized by this audit.

## Findings

- GitHub reports all four prerecorded files (`voices/kejyar.mp3`, `voices/lesson_done.mp3`, `voices/lesson_start.mp3`, and `voices/reward.mp3`) as 1,415,880 bytes with the same Git blob SHA `33b67c66445c93bfdbd93eae1daad157aa843a20`. They are byte-identical in the repository. They have not been replaced because the approved source recordings for distinct event prompts are not available for comparison.
- Dynamic generation previously relied on environment credentials and matching voice IDs alone. A matching pair of environment values is not proof that the ID is the original Kejyar voice.
- ElevenLabs documentation currently describes Eleven v4/Text to Dialogue, but Kurdish is not named in the published list of Eleven v4 supported languages. A mocked unit test only verifies request construction; it does not prove real Kurdish pronunciation or voice identity.

## Safeguards applied

- Dynamic speech now requires `KEJYAR_ENABLE_DYNAMIC_SPEECH=true` as an explicit opt-in.
- It also requires `ELEVENLABS_API_KEY`, `KEJYAR_VOICE_ID`, and `KEJYAR_APPROVED_VOICE_ID`, with the two voice IDs matching exactly.
- README instructions leave dynamic speech disabled by default until the original voice ID and real Kurdish output are verified.
- Tests cover disabled-by-default behavior and reject a mismatched voice ID.
- No prerecorded audio file was modified. No production bot, production database, or `main` branch was changed.

## Remaining verification before enabling dynamic speech

1. Recover and verify the exact approved original voice ID from the authorized provider account; do not guess it.
2. Confirm consent and access rights for that voice.
3. Make a real, authorized Kurdish sample test and have a competent Kurdish speaker check pronunciation and whether the voice still matches the intended speaker.
4. If Kurdish output is not supported or the voice cannot be verified, keep dynamic speech disabled and use the existing prerecorded assets.
5. If distinct event prompts are required, obtain the original approved recordings rather than inventing replacements.

CI success validates code/tests only; it does not certify the sound, speaker identity, consent, or Kurdish pronunciation.
