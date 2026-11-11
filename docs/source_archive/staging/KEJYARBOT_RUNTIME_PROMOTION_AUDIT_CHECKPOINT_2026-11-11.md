# KejyarBot — runtime promotion audit checkpoint
## 2026-11-11 | Append-only preservation record

### Scope
Read-only audit of GitHub source state and Botkeep test runtime evidence. This checkpoint does not authorize or perform merge, import, restore, redeploy, restart, database migration, token change, or production activation.

### Botkeep test runtime
- User screenshot on 2026-11-11 showed runtime output repeatedly calling Telegram `getUpdates` and receiving `HTTP/1.1 200 OK`.
- This confirms Telegram API connectivity for the currently running Botkeep test runtime at the screenshot time; it does not prove the latest GitHub candidate is deployed, nor does it prove lesson, quiz, reward, and progress flows.
- Botkeep support incident #a1a7aa05 previously reported the Node17 staging/import issue and advised against another import/restore workaround until infrastructure recovery is confirmed.
- Do not retry the failed import/restore or use destructive Botkeep controls as a deployment workaround.
- The Telegram bot token appeared in the user's console screenshot. Treat it as exposed and rotate it before further public/user-facing testing. Never record the token in this repository.

### GitHub candidate status verified 2026-11-11
- PR #125, “Harden academic course menus, lesson access, and pagination”: OPEN, not merged; base `botkeep-runtime-2026-11-09`, head `botkeep-menu-clean-2026-11-09`, head SHA `c41fc186e8e2482de336d297c3b7dd9758356e08`; 186 commits, 194 changed files. Three relevant workflows on this exact head completed successfully (Python checks, Course 4 beta review safety, orthography course structure). Successful CI is not deployment approval.
- PR #129, 50-lesson Course 4 beta runtime/manifest work: merged into the PR #125 working branch, not into main or Botkeep runtime. The 50-lesson candidate permits lessons 32–50 for beta/read-only progression only.
- PR #128, append-only scientific reconciliation for Course 4 lessons 16–50: merged into the PR #125 working branch, not into main or Botkeep runtime. It records 44 quiz review findings; source quiz records remain preserved.
- PR #140, Course 3 lessons 67–68 runtime candidate: OPEN and DRAFT, based on `audit/course3-diako-20261110`; do not include in the current Botkeep test promotion.
- PRs #142, #143, and #144 were merged into `archive/preservation-audit-2026-11-10`; they preserve Latin Course 2 quiz/orthography review material and are not Botkeep runtime deployment changes.
- PR #141 remains Railway-specific and is not the current hosting target.

### Course 4 activation and review gates
- Candidate Course 4 catalogue has 50 lessons (`grammar_01` through `grammar_50`).
- Lessons 32–50 remain `owner_review_pending_expanded_draft`, beta/read-only; no structured quiz, official completion, XP, coins, chest, or badge rewards are enabled for those pending lessons.
- Lesson 13 has a source-mapping/review gate; do not bypass its quiz/reward eligibility checks unless its review status is explicitly cleared in the source.
- Candidate quiz bank contains 248 questions for lessons 1–31. Internal review records note remaining source/answer-quality work; structural CI alone is not proof of scholarly correctness.
- The 142-field reversible “بەستێن” patch was tested against a local copy and regression-checked, but the canonical Course 4 JSON was not rewritten by that patch. Do not represent it as already applied to runtime.
- Lesson 48 expanded V3 is a separate draft; its Sorani dialect examples and terminology still require owner/native-speaker and scientific review. It is not the approved runtime lesson.
- Preserve original lesson text, original quiz banks, snapshots, answer keys, and append-only review history.

### Promotion safety decision
- Current Botkeep runtime is not proven to contain the work in PR #125; the support-reported last applied revision was `bdd08e6`, and the failed import did not deploy commit `54723763dbef9278cdefbeeb425e00cb84e3cc1b`.
- PR #125 is a candidate working branch, not a release artifact. Before any promotion, produce a clean release manifest separating runtime-ready code/data from review-only drafts and appendices; run the full suite on the exact release commit; validate database compatibility/migrations and backup restore in a safe isolated copy; obtain Botkeep confirmation that Node17 staging is healthy; rotate the exposed Telegram token and update the environment securely.
- Test bot remains the only authorized target. Main bot must retain its separate token and database and must not be activated as part of this test promotion.
- No merge, deployment, Botkeep import, restore, restart, Railway activation, or database write was performed for this checkpoint.

### Next safe work
1. Build a file-level release manifest from the exact PR #125 head, marking each changed file as runtime code, runtime data, test, archival evidence, or review-only draft.
2. Verify every included runtime data file against the lesson/quiz gates above; exclude unapproved drafts from official quiz/reward paths.
3. Run and record full tests against the exact proposed release commit and perform read-only SQLite schema/compatibility checks against the preserved test backup.
4. Wait for Botkeep support confirmation of staging recovery before attempting any import or deployment operation.
5. Only after these gates, prepare a separate, explicit test-bot promotion step; do not promote to main bot.

This record is append-only. It records source-reported and tool-verified states separately and does not claim that any candidate has been deployed.
