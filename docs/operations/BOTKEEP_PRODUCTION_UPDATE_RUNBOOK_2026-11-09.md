# KejyarBot on Botkeep — production update runbook
Last reviewed: 2026-11-13

## Purpose and safety boundary

KejyarBot is hosted on the existing Botkeep workload `KejyarBot-Test`. The objective is to update and reactivate that same workload, not migrate to another host.

This runbook is operational guidance, not evidence that a deployment has happened. Never claim the bot is online until Botkeep reports a confirmed healthy runtime and Telegram polling has been verified.

**Never use “Replace files” for the current recovery.** Do not delete/recreate the workload, overwrite the SQLite database, expose secrets, or change the hosting provider as part of routine recovery.

## Current verified release and hosting state (2026-11-13)

- Repository: `avasinim/KejyarBot`
- Intended Botkeep source branch: `release/main-based-reconciled-2026-11-11`
- Verified release head: `6fd58338b05a110262ddff32b3696a8df852d272`
- Botkeep GitHub tab previously showed the branch but still displayed the old linked-source revision `main` / `bdd08e6`; the current release head is `6fd5833` and has not been confirmed imported.
- Import mode selected: **Merge files** (overwrite matching files, retain other files/folders).
- The linked-source panel still showed the old `main` revision `bdd08e6` and last sync 2026-11-04 16:38:19 before the attempted sync.
- The attempted sync returned: `Source staging was interrupted. Existing application files were not changed. Resume or cancel the import.`
- Therefore the new source has **not** been verified as applied. Do not infer that a sync completed.
- Botkeep panel displayed Offline and “Waiting for a fresh runtime update. The displayed state is not yet confirmed.” This is not a confirmed live runtime state.
- Botkeep support incident: `#a1a7aa05`. A support escalation was sent on 2026-11-13 asking for Node17/Wings and GitHub staging investigation, current-commit comparison, recovery validation, and an ETA.
- A completed Botkeep backup exists: `KejyarBot_PreManualTransfer_2026-11-13` (8.4 MB); a local downloaded copy was confirmed. The backup snapshot was taken while the panel showed Offline.
- No Botkeep restart or successful source sync has been verified.

## Current release review hold (2026-11-13)

- The release branch contains the latest intended source revision `6fd58338b05a110262ddff32b3696a8df852d272`.
- Its four checked CI workflows pass, but this is not sufficient deployment approval.
- A source-level review found a likely regression: the new global academic-review gate treats every active course as requiring explicit approval, while the course adapters default missing review metadata to `draft_editorial_review`. This likely blocks lesson completion and rewards for Courses 2 and 3 and the two active Kurmanji courses. See PR #152's 2026-11-13 high-priority review comment. Do not sync this revision until the gate is corrected and the unaffected course paths are verified.
- The owner's intended media inventory is instructional text and images; no PDF or audio lesson files are expected. The release tree has 17 image/vector assets and no PDF/audio/video media. Preserve those image assets.
- The downloaded 2026-11-13 backup's inspected tar listing showed six root-level files; that partial listing does not prove nested image assets are included. Obtain a complete recursive backup inventory and Botkeep's live-file comparison before relying on it as a complete media recovery point.

## Verified repository runtime contract

- Project root: repository root (contains `requirements.txt` and `bot.py`)
- Botkeep runtime shown: Python 3.12
- Dependencies: `python-telegram-bot>=22,<23` and `python-dotenv>=1,<2`
- Expected start command: `python bot.py`
- Token environment variable: `TELEGRAM_BOT_TOKEN`; legacy `BOT_TOKEN` is also accepted
- SQLite default path: `kejyar.db` beside `database.py`, unless `KEJYARBOT_DB_PATH` is configured
- `bot.py` loads the project-root `.env` before importing `database.py`.
- The application uses Telegram polling; only one active polling process should use this bot token.

The code's default DB path does not independently prove which database path the live Botkeep process used. Keep the existing DB and Environment settings intact unless Botkeep support verifies the actual configuration.

## Backup and preservation

1. Keep the completed 2026-11-13 Botkeep backup and its downloaded local copy.
2. Never share or print `.env`, Telegram tokens, credentials, or secret values.
3. Never import a repository copy of `kejyar.db` over the existing server database.
4. Preserve server-only files and Botkeep configuration. The merge preview must be inspected before any further sync attempt.
5. Do not treat a successful archive inventory as proof of the live server's changed-file list.

## GitHub source update procedure

1. Confirm repository `avasinim/KejyarBot`, branch `release/main-based-reconciled-2026-11-11`, and the exact reviewed head. At this checkpoint, `6fd58338b05a110262ddff32b3696a8df852d272` is the current head but is **on review hold**; do not import it until the global academic-review gate regression is fixed and CI/source review passes.
2. Select **Merge files**. Never select **Replace files**. Do not use “Import into a folder” unless the runtime root/start command is deliberately reconfigured and reviewed.
3. Inspect the exact changed-file preview. Confirm that `.env`, `.botkeep`, `kejyar.db`, and existing server-only files are not overwritten or removed.
4. If source staging is interrupted, stop repeated retries. Record the exact message and ask Botkeep support to diagnose/recover the staging job and confirm whether it is safe to resume. The panel message stated existing application files were not changed; verify this with the provider.
5. Do not enable “Pull before Start / Restart” until the first manual sync has succeeded and the effect on local edits is understood.
6. After a confirmed sync, verify startup settings and dependencies before a separately planned restart.
7. Watch Console for successful initialization and Telegram polling. A panel status alone is insufficient.
8. Run controlled Telegram smoke tests: `/start`, course menu, Course 4 beta progression, quiz suppression, and no official XP/coins/chests/badges for beta lessons. Explicitly verify Courses 2 and 3 and both Kurmanji courses can still open, complete lessons, take their existing assessments, and receive expected rewards.
9. If startup or smoke tests fail, stop and use the verified backup/recovery path. Do not delete the workload or database while investigating.

## If the workload was uploaded as ZIP

Build a clean archive from the verified release branch. Include required runtime modules, `requirements.txt`, `bot.py`, and course data. Exclude `.env`, tokens, credentials, local environments, caches, and the production SQLite database. Preserve production data separately through a verified backup/restore process.

## Post-update verification

- Botkeep reports a confirmed healthy runtime.
- Console confirms Telegram initialization and polling.
- The existing bot responds to `/start`.
- Existing progress/data remain intact.
- Course 4 beta lessons remain clearly marked as beta review drafts.
- Beta completion does not grant official completion, XP, coins, chests, or badges.
- Quizzes remain unavailable for beta review drafts.
- Lesson 46 does not unlock or fabricate Lesson 47.
- Previously approved lessons and Courses 1–3 retain expected behavior.

## Historical note

The previous version of this runbook named `main` as the production source branch and described the workload as active. Those details are stale for the current recovery. The release branch and hosting state above supersede those historical statements.

## Official Botkeep references

- GitHub deployment guide: https://botkeep.cloud/docs/github
- Hosting and backup guidance: https://botkeep.cloud/docs/hosting
- FAQ (restart, backup, runtime state): https://botkeep.cloud/faq



---

## Append-only correction and latest checkpoint (2026-11-13 06:40 UTC)

This addendum supersedes earlier statements in this runbook where they conflict with the verified state below. Earlier text is retained for audit history.

### Latest source and CI
- Latest release-branch / PR #152 head at this checkpoint: `7ee4269f92c71d315d499bd479c90c5979902bed`.
- Four PR-triggered workflows checked against this exact head completed successfully: Python checks, Course 4 beta review safety, Orthography course structure tests, and Kurdish months tests.
- PR #152 remains open, unmerged, and mergeable. CI success is not academic approval or production deployment approval.
- The earlier runbook's references to `6fd5833...` as latest are historical; use the exact current head above for any future source comparison.

### Correct authoritative course numbering
**Kurdish courses**
1. Course 1 — Introductory Orthography (ڕێنووسی سەرەتاییی)
2. Course 2 — Conversation (وتووێژ)
3. Course 3 — Unified Orthography (ڕێنووسی یەکگرتوو)
4. Course 4 — Grammar (ڕێزمان)

**Separate Kurmanji Latin courses**
1. Kurmanji Latin Course 1 — Introductory Orthography
2. Kurmanji Latin Course 2 — Grammar

The two sequences are separate. Do not label a Kurdish course with a Latin course number or vice versa. The active manifest uses `arami_orthography_foundations` for Kurdish Course 1; the old `orthography_basic` entry is retired/replaced. Kurdish Course 2 is `daily_conversation`; Course 3 is `unified_orthography`; Course 4 is `grammar`. Latin Course 1 is `kurmanji_latin_orthography`; Latin Course 2 is `kurmanji_latin_grammar`.

### Academic review gate — corrected interpretation
- Source inspection confirms the global gate applies to every active course: official assessments, rewards, and badges remain unavailable unless lesson review status is explicitly approved.
- Conversation and Unified Orthography adapters default missing review status to `draft_editorial_review`; the Latin runtime assigns that status to both separate Latin course lesson sets.
- This confirms a policy/documentation mismatch with a nearby source comment, but does **not** prove a code regression or establish that these courses should be automatically approved.
- Do not weaken the fail-closed gate or mass-change review statuses without an explicit owner policy decision and appropriate academic/source evidence.
- Course 4 has its separate Beta progression behavior for specifically designated review lessons. Keep Beta completion separate from official assessment/reward records.

### Production and Botkeep boundary remains unchanged
- No successful Botkeep source sync, restart, or healthy Telegram polling has been verified. The bot must not be described as online.
- The earlier staging error remains unresolved: `Source staging was interrupted. Existing application files were not changed. Resume or cancel the import.`
- Do not blindly resume or cancel the interrupted import. Wait for Botkeep support to diagnose staging and provide a fresh Merge preview for the exact latest release head.
- Preserve `.env`, `.botkeep`, `kejyar.db`, server-only files, and the completed 2026-11-13 backup. Never use Replace files, overwrite the live database, or enable pull-before-start before a successful reviewed manual sync.
- User clarification remains authoritative: no PDF or audio files are expected in the bot; its teaching material includes instructional text and some images.

This addendum records source inspection and owner clarifications only. It does not change application code, course content, review statuses, database, Botkeep settings, or production runtime.

---

## Append-only correction — exact release head and CI result (2026-11-13 06:45 UTC)

This entry supersedes earlier checkpoint references in this runbook where they name `7ee4269...` or `6fd5833...` as the latest release head. Those references remain as historical records.

### Exact current source checkpoint
- Repository: `avasinim/KejyarBot`
- Branch: `release/main-based-reconciled-2026-11-11`
- Exact release branch / PR #152 head: `958a56ad0ba8349ed29fd38420f9a6ffd7ceb4c9`.
- Compared with parent `7ee4269f92c71d315d499bd479c90c5979902bed`, this head is one commit ahead and changes exactly one file: `docs/operations/BOTKEEP_PRODUCTION_UPDATE_RUNBOOK_2026-11-09.md` (+43 lines, 0 deletions). No application code, course data, quiz, review status, database, or runtime file changed in that final commit.
- All four GitHub Actions workflows completed successfully on this exact head:
  - Python checks — run `43380392078`
  - Course 4 beta review safety — run `43380391946`
  - Orthography course structure tests — run `43380391879`
  - Kurdish months tests — run `43380391864`
- PR #152 was rechecked and remains open, unmerged, and reported mergeable. A verification comment was appended as PR comment `6846202506`.

### What CI does and does not establish
- The four successful workflows establish that the configured automated checks passed on exact head `958a56a`.
- They do not constitute academic sign-off, a decision to change the global fail-closed academic review policy, Botkeep import clearance, a successful restart, Telegram polling confirmation, or proof that the bot is online.
- The global academic review gate remains a confirmed source behavior and policy/documentation mismatch; do not change lesson statuses or weaken the gate without explicit owner policy and source-based academic review.

### Botkeep remains blocked
- No new Botkeep support reply had arrived by the 2026-11-13 06:45 UTC check; the latest located provider reply remained dated 2026-11-12 14:00:29 UTC.
- The interrupted source-staging attempt remains unresolved. Do not resume or cancel it blindly.
- The next safe provider-side prerequisite is a fresh Merge preview for exact head `958a56ad0ba8349ed29fd38420f9a6ffd7ceb4c9`, with a comparison against the live workload and explicit confirmation that `.env`, `.botkeep`, `kejyar.db`, server-only files, and existing user data will be preserved.
- Keep the completed 2026-11-13 backup. Do not merge PR #152, sync, restart, restore, replace files, or enable pull-before-start as part of this checkpoint.

This is an append-only evidence correction. Earlier runbook text remains intact. No application, course, database, Botkeep configuration, or production runtime change was made.

---

## Append-only correction — exact release head and current blocker (2026-11-13 06:51 UTC)

This entry supersedes the 06:45 checkpoint above where it names `958a56ad0ba8349ed29fd38420f9a6ffd7ceb4c9` as the latest release head. That checkpoint remains as historical evidence.

### Exact current repository state
- Repository: `avasinim/KejyarBot`
- Branch: `release/main-based-reconciled-2026-11-11`
- PR #152 and release branch head: `c4b0c147dd02aecba0ee4d1d2a16c373a767d5b3`.
- PR #152 remains open, unmerged, and reported mergeable. The GitHub review endpoint currently returns no submitted reviews and no inline review comments.
- Comparing `958a56ad0ba8349ed29fd38420f9a6ffd7ceb4c9` to `c4b0c147dd02aecba0ee4d1d2a16c373a767d5b3` shows exactly one changed file: this runbook, with 31 additions and zero deletions. No application code, lesson/course content, quizzes, academic statuses, database, or runtime files changed in this increment.
- All four configured workflows on exact head `c4b0c14` completed successfully: Python checks, Course 4 beta review safety, Orthography course structure tests, and Kurdish months tests.

### Provider support state
- Gmail search of the Botkeep support thread `#a1a7aa05` through 2026-11-13 06:50 UTC found no provider reply later than 2026-11-12 14:00:29 UTC.
- The owner's latest escalation remains 2026-11-13 06:11:05 UTC.
- The interrupted staging attempt remains unresolved. No fresh Merge preview or live-workload file comparison has been supplied.
- Do not send repetitive follow-up messages without new evidence. Do not blindly resume or cancel the interrupted import.

### Required safety boundary
- Keep PR #152 open and unmerged.
- Do not import/sync, restart, restore, replace files, alter environment settings, or enable pull-before-start until Botkeep diagnoses staging and provides a fresh exact-head Merge preview plus explicit preservation confirmation for `.env`, `.botkeep`, `kejyar.db`, server-only files, and user data.
- Keep the completed 2026-11-13 backup and its downloaded copy.
- CI success and documentation-only changes do not establish academic approval, Botkeep clearance, Telegram polling, or a healthy live bot.

This addendum is append-only operational evidence. No production or application changes were made.
