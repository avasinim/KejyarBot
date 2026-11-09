# Daily Preservation Record — 2026-11-09

> Append-only handoff record. This file records the state and decisions known at the end of 2026-11-09. Do not rewrite this record to reflect later work; add a new dated record instead. The code and review branches listed below remain the authoritative source artifacts.

## Purpose

Preserve today's KejyarBot work before any Botkeep restart, import, or runtime change. This record is a handoff and inventory, not a deployment authorization. No Botkeep import, server restart, PR merge, or database mutation is performed by creating this file.

## GitHub work preserved

### PR #125 — runtime/menu hardening
- PR: https://github.com/avasinim/KejyarBot/pull/125
- Branch: `botkeep-menu-clean-2026-11-09`
- Recorded head at time of this note: `f8cddf17f5ac5c5da5171fce4c7b7294aa84a50a`
- Scope: academic course menu presentation; course/quiz/lesson pagination; lesson access and stale callback safety; Course 4 Beta progress separation; HTML escaping; malformed Unicode callback validation; regression tests.
- Verification recorded in PR: 519 tests discovered, 508 passed, 11 skipped (retired legacy Course 1 tests); orthography structure tests 4 passed. The PR states the workflows passed on the recorded head.
- State at inspection: open, unmerged. Keep as the primary runtime candidate pending final review and Botkeep staging.

### PR #126 — Course 1 Round 1 source-preserving audit
- PR: https://github.com/avasinim/KejyarBot/pull/126
- Branch: `work/course1-round1-review-2026-11-09`
- Recorded head at time of this note: `fbd2464ade03a5b7acade10a216024ba919abe35`
- Scope: audit of all 21 Course 1 lessons; review matrix; 210 practice/assessment items; image inventory; text-only policy; presentation consistency; source-gap warnings; source-preserving lesson reviews.
- Explicit source gaps: Lesson 4 source contains sections 3–8 only (do not invent sections 1–2); Lesson 14 title mentions “هێشوو” but the preserved body does not contain that section.
- No original lesson-body wording, examples, questions, definitions, or order were authorized for rewriting.
- Verification caveat: compileall and 521 tests (510 passed, 11 skipped) are recorded for code commit `049a4df8841c73ca1f2bb624d37035ae75e1d0a7`. The latest branch updates were documentation/manifest metadata and had not yet received a fresh CI run at inspection.
- State at inspection: open Draft, unmerged. Keep separate from runtime deployment until PR #125 is resolved and its review is complete.

## Course 1 preservation rules and inventory

- Course 1 contains 21 lessons; 105 practice and 105 assessment questions (210 total).
- Course 1 runtime policy is text-only. Do not restore audio files, audio playback, speech APIs, or an audio delivery path.
- The Course 1 audio catalog and restored audio files were removed from the recovery branch as documented in PR #126; PR #127 was closed. Do not reintroduce audio.
- Six mapped lesson infographic PNGs are assigned to Lessons 1, 2, 3, 4, 6, and 7. Preserve these assets and mappings.
- Lesson 5 has no assigned infographic; do not fabricate one.
- Keep source-gap warnings visible; do not reconstruct missing source material.
- Existing historical hash/URL strings are text-only references, not playable audio.
- Presentation consistency improvements must not alter lesson source wording without explicit user approval.

## Course 4 preservation rules

- Preserve all existing Course 4 lesson content. Changes are append-only patches, review notes, and supporting archive packages; do not replace or delete source material.
- There are 46 active lessons. Lessons 32–46 remain owner-review items; quizzes remain inactive pending approval.
- Draft lessons 47–50 are archived drafts, not active lessons.
- The academic layout redesign is to be validated on Lesson 1 before applying across Lessons 1–46.
- Use Saeed Karimi's `وشەناسیی زمانی کوردی (کرمانجیی ناوەڕاست)` as a reference throughout the redesign.
- Keep the distinction between official completion and Course 4 Beta review progress; Beta progress must not unlock official rewards, quizzes, badges, or lessons.
- Preserve lesson images with their designated lessons and avoid broad changes to lesson text.

## Botkeep/runtime state known at inspection

- Botkeep server: `KejyarBot-Test`; Python 3.12; status previously shown as Offline.
- Linked repository: `avasinim/KejyarBot`; linked branch: `main`; linked commit shown by Botkeep: `bdd08e6`; last sync shown: 2026-11-04 16:38:19.
- Botkeep import choices: Merge files overwrites matching files and keeps other files/folders; Replace files removes existing application files; Import into a folder does not replace the active root application.
- Import limits shown: 1,000 files; 4 MB per file; 20 MB total. Environment secrets and Botkeep configuration are not imported.
- Startup command already configured and confirmed: `python -m pip install -r requirements.txt && python bot.py`. Do not ask the owner to re-send it.
- Runtime requires `TELEGRAM_BOT_TOKEN` or `BOT_TOKEN` in Botkeep environment. Never put token values in Git, logs, screenshots, or this record.
- `database.py` stores `kejyar.db` beside the application code. A destructive Replace files import risks removing the live database and must not be used without a verified independent restore plan.
- Use Merge files only after reviewing the final branch contents and confirming the backup is available. Merge preserves unrelated server files, so any unwanted old files must be reviewed separately.
- No Botkeep import, Start, restart, database change, or deployment was confirmed as completed in this record.

## Backup and data safety

- Botkeep backup `KejyarBot_PreUpdate_2026-11-09`: 8.4 MB; UI previously showed Completed, slot 1/1. The owner downloaded it. It has not been restore-tested.
- Database download `kejyar (1).db`: approximately 32 KB; it has not been opened or integrity-checked.
- Treat the backup as an available recovery copy, not as proof of a successful restore.
- Do not delete the server, its files, the database, or backups during the restart/import process.
- Do not expose or commit Telegram credentials. If a token has been exposed, rotate it via BotFather and update the Botkeep environment before starting the bot.

## Release gates and next actions

1. Keep PR #125 and PR #126 unmerged until their respective review and CI requirements are satisfied; PR #126 remains a draft audit, not a runtime release.
2. Confirm the final PR #125 head and CI status before importing it.
3. In Botkeep, select repository `avasinim/KejyarBot`, branch `botkeep-menu-clean-2026-11-09`, and **Merge files** (not Replace files). The owner must perform the UI action; this assistant has no direct Botkeep UI access.
4. Preserve the existing database and environment variables. Verify the Telegram token variable exists without exposing its value.
5. Only after the owner authorizes the actual import/start, perform the Botkeep action and inspect logs and bot behavior.
6. After activation, test start-up, course menu, lesson access, pagination, quiz/lesson callback safety, and text-only Course 1 behavior.
7. Keep PR #126 audit findings and Course 4 work as separate preserved work; do not silently merge them into the runtime branch.

## Continuity note

This record captures the known work and release constraints available on 2026-11-09. It does not claim that every historical chat message or every Botkeep server file has been copied into Git. The PRs, their branch commits, existing project documentation, and the Botkeep backup remain the primary source artifacts. For any subsequent work, add a new dated preservation record rather than overwriting this one.
