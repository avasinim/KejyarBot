# KejyarBot — Work Session Handoff

**Date:** 2026-10-29  
**Purpose:** Safely pause work and resume from this checkpoint in the next session.

## Active workspace and safety boundary

- Repository: `avasinim/KejyarBot`
- Working branch: `fix/integration-daily-conversation-48-2026-10-29`
- This is a test-branch checkpoint only.
- Do not merge to `main`, deploy, change the production bot/token/service, or touch production data without the user's explicit permission.
- Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`. Do not replace the existing woman's voice or modify voice files.
- Do not edit lesson language/content or orthography unless the user specifically asks; the user will identify content issues for correction.
- Course 1 follows the user's specified source/orthography for the bot and must not be confused with the separate Avasin website orthography.

## Work completed / verified

- Four-course manifest is documented in README:
  - Course 1 — introductory orthography: 22 lessons.
  - Course 2 — daily conversation: 48 lessons; technically active in the integration manifest at the owner's explicit request.
  - Course 3 — unified orthography: 12 lessons.
  - Course 4 — grammar: planned, with no active lessons.
- Runtime course separation, lesson unlocking, namespaced lesson IDs for courses 2 and 3, quiz callback validation, duplicate reward prevention, startup token guard, speech quota checks, and Botkeep packaging have dedicated tests.
- Courses 2 and 3 are technically active on this integration branch at the owner's explicit request. Their lesson records retain editorial-review metadata; this does not certify final language review or authorize production deployment.
- Branding check: runtime course-one lesson headers and the lesson-one infographic caption use **کەژیار**.
- A failed branding test had searched the entire lesson body and accidentally matched a linguistic example in lesson 18. The test was narrowed to inspect the actual lesson header only; lesson content was left untouched.
- CI for commit `0ee813a99468d1b3bc04c97b7dc58cd5ddd0f69b` succeeded: https://github.com/avasinim/KejyarBot/actions/runs/40756095356
- Handoff documentation commit `661d8f257790236ed63013bf562e709161000abf` also passed CI: https://github.com/avasinim/KejyarBot/actions/runs/40756398723
- Historical CI checkpoints above refer to the earlier 2026-10-28 branch state, not this integration head.
- Recent CI run for the test that only blocks direct callbacks to planned courses also succeeded: https://github.com/avasinim/KejyarBot/actions/runs/40755119546

## Remaining work for the next session

1. Re-check the current branch head and latest GitHub Actions result before making further edits.
2. Continue a focused technical audit of course navigation, progress persistence, quiz/reward idempotency, and the Botkeep ZIP contents; add or fix tests only where a concrete gap is found.
3. Keep all changes on the test branch, and re-read changed files after edits.
4. Report clearly what is verified versus still pending. Do not claim production readiness just because CI passes.
5. Do not create or upload the Botkeep package, change the running bot, or deploy unless specifically authorized.
6. Keep infographics as a later task, after lesson intake/content work; do not interrupt technical stabilization with new image design.

## Safe local test commands

From the project directory, with the project's virtual environment activated:

```powershell
python -m unittest discover -s tests -v
python -m compileall -q .
git diff --check
git status --short --branch
git log -5 --oneline --decorate
```

If the project uses its Windows virtual environment, prefer:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Do not commit local secrets, `.env`, SQLite databases, backups, or generated runtime data.


## Continuation checkpoint — 2026-10-29

- Current integration branch: `fix/integration-daily-conversation-48-2026-10-29`.
- Owner's local run on code head `d4af297a0e54e790ed8e0e31397c775da066bf7c` passed all 244 tests in 7.238 seconds. The quiz-bank structure guards in `tests/test_course_quiz_content_quality.py` passed in CI on `66a4364` (246 tests). `tests/test_botkeep_packager.py` exercises the actual ZIP creation path using an isolated temporary repository and verifies required runtime files are present while `.env`, a SQLite database, backups, test/docs/tools files, and prerecorded audio are excluded. A behavioral regression test verifies direct quiz-start callbacks are rejected for every Course 1 quiz flagged for review, complementing the stale answer-callback gate test. Two further async tests now verify that stale `next_lesson_...` callbacks cannot send locked lesson content and stale `finish_...` callbacks cannot award rewards. GitHub Actions run [40882262853](https://github.com/avasinim/KejyarBot/actions/runs/40882262853) passed on `882672ab5311214825b535ade7fa3220a71b728f`: `compileall` and all 250 tests passed. These tests verify package-building behavior and access-gate behavior, not editorial correctness or a live Telegram smoke test.
- Editorial status trackers were corrected to reflect the 48-lesson active Course 2, 12-lesson active Course 3, retained review metadata, and the current integration branch. Production is not deployed.
- CI succeeded for that commit: https://github.com/avasinim/KejyarBot/actions/runs/40822621759. The run completed the compileall and full unittest steps successfully.
- The root image `photo_2026-10-27_00-13-52.jpg` is tracked in the development branch and is the optional Course 1, Lesson 1 infographic. `tools/prepare_botkeep_zip.py` intentionally excludes JPG/binary files; the image must be transferred separately by SFTP after the server exists. The lesson text is designed to remain available if the image is absent.
- `docs/BOTKEEP_DEPLOYMENT.md` now states this correctly. `tests/test_botkeep_packager.py` includes a guard asserting that the exact image exists in the repository but is excluded from the ZIP package.
- No ZIP was created or uploaded. No production service/token/data was changed, no merge/deployment occurred, and dynamic speech remains disabled unless the user explicitly approves otherwise.
- Next safe work: continue focused review of course navigation, progress persistence, quiz/reward idempotency, and package constraints; make only evidence-based changes on this test branch and verify CI after each change.

## Additional audit checkpoint — 2026-10-29

- Verified branch head before this change: `1554d86abf87794f98f709c2d715acb1273c3474`; latest known CI run `40882340339` passed with the 250-test suite.
- Focused review of `.gitignore` found that SQLite rollback-journal sidecars (`*.db-journal`, `*.sqlite-journal`, and `*.sqlite3-journal`) were not ignored, although WAL/SHM sidecars were. These files may contain transient database pages, so the patterns were added on the integration branch in commit `e377a244e91f586ca4f5c225f32a6197b8bb22d0`.
- This is a repository hygiene change only; no database, token, speech setting, course content, production service, or deployment was touched. CI for the new commit is pending at the time of this note.
- Quota review confirmed the current tests cover atomic reservation, daily limit, persistence, and basic refund. A future deeper change to reservation/refund identity should only be made with a concrete design and regression coverage; do not claim duplicate-refund idempotency is currently guaranteed.
