# Runtime package follow-up — subscription gate closure

Date: 2026-11-16

## Finding

The non-admin channel confirmation gate was merged into the active release branch at source commit `0866c05ba2e9a3dd4156cc4bd21b8b303b7ec9ca`. The runtime imports `subscription_gate.py` from `bot.py`, but the existing allowlisted runtime package workflow did not include that module.

A ZIP built with the previous allowlist would therefore be incomplete and could fail at startup with an import error.

## Correction

- Add `subscription_gate.py` to `.github/workflows/build-runtime-package.yml` immediately before `requirements.txt`.
- The allowlist grows from 61 to 62 files.
- Keep the existing seven approved PNG assets and all previous runtime allowlist entries unchanged.
- Continue excluding `.env`, Telegram credentials, SQLite databases and sidecars, PDFs, audio, JPG/JPEG, SVG, tests, and documentation from the runtime ZIP.
- This correction changes packaging only. It does not modify course content, lesson assets, learner data, SQLite, or Altare settings.

## Verification gate

The package workflow must run on the release branch after this correction is merged. Confirm the resulting artifact contains exactly 62 entries, including `subscription_gate.py`, and passes the existing archive exclusion assertions before it is considered deployable.

## Deployment boundary

This record and the packaging correction do not upload files to Altare, change environment variables, replace a database, or start/restart the bot. The active Altare app remains `kejyarbot`; `AUTO_UPDATE=0`.
