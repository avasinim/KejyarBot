# COURSE 3 — LESSONS 67–68 RELEASE READINESS GATE
Date: 2026-11-10
Branch: \`work/course3-lessons67-68-practice-archive-2026-11-10\`
PR: #140 — Draft, open, unmerged.
Status: operational readiness snapshot; this is not a production activation request.

## 1. Readiness matrix

| Workstream | Current evidence | Status | Release requirement |
|---|---|---|---|
| Source preservation | Original source file for Lessons 1–66 unchanged; original 66 lesson objects preserved in candidate | PASS | Reconfirm blob hash and 66-object equality on final integration commit |
| Candidate structure | Candidate dataset and manifest contain Lessons 1–68; Lessons 67–68 remain draft editorial review / candidate only | PASS (candidate) | Final schema and manifest validation after any accepted revision |
| Practice package | 18 activities, 20 exercises, 24 comprehension prompts across Lessons 67–68 | PASS (package exists) | Integrate only the specialist-approved remediation version |
| Practice traceability | 62/62 audit IDs have matching proposal references; no missing or extra IDs | PASS (coverage only) | Content correctness still requires specialist review |
| Original MCQ preservation | Original 24 questions and answer keys remain unchanged | PASS | Preserve original records in archive even after any replacement |
| Proposed MCQ V2 | 19 questions; 9 for Lesson 67 and 10 for Lesson 68; 19/19 answer keys match; answer positions A=4, B=8, C=7 | PASS (internal QA) | Specialist review of script, dialect, answer uniqueness, difficulty and distractors |
| Scientific evidence | Haig (2018) and Ahmadi (2021) used with dialect and manuscript caveats | PARTIAL | Verify exact Kurdish-script forms and held lexical/morphological examples in authoritative Sorani sources |
| Runtime integration | Branch-local runtime candidate and Course 3 count 68 are prepared; no production deployment | PARTIAL | After academic sign-off, integrate accepted practice/quiz revisions and run all adapters/pagination tests |
| Automated CI | Latest run for commit \`395f6873aa73557396da404467cdfa157daf8c35\` succeeded | PASS (repository CI) | Rerun on the final exact integration commit |
| Host smoke test | No Botkeep/Telegram host smoke test has been completed for this candidate | BLOCKED | Botkeep must confirm infrastructure safe; then run a controlled non-destructive host test |
| Botkeep infrastructure | Prior Botkeep status showed infrastructure operation failure and server offline; support review/retry required | BLOCKED / status must be rechecked | Obtain explicit support confirmation before any resume, retry, sync, restart or deployment |
| Human academic review | No independent Sorani specialist sign-off recorded | BLOCKED | Obtain documented review of both lessons and all scored questions |
| Production release | PR #140 remains Draft and unmerged; no production action performed | NOT RELEASE-READY | All above gates must pass; explicit authorization required before merge/deploy |

## 2. Verified package counts
- Lesson 67: 8 activities, 10 exercises, 12 comprehension items, 12 original MCQs.
- Lesson 68: 10 activities, 10 exercises, 12 comprehension items, 12 original MCQs.
- V2 scored proposal: 9 + 10 = 19 MCQs.
- Practice audit coverage: 62/62 identifiers represented in the proposed remediation document.
- Original quiz: 24 items and original answer keys remain archived and unmodified.

## 3. Non-negotiable release controls
1. Do not treat branch-local Course 3 status \`active\` as production activation.
2. Do not merge PR #140 while it remains Draft and the academic/host gates are blocked.
3. Do not press Botkeep Resume, Cancel/restore, retry sync, change startup command, database, token, or restart server before Botkeep support confirms backend safety.
4. Do not score any item marked HOLD or turn an OPEN TASK into an auto-graded item without a source-backed rubric.
5. Keep original lesson text, source 1–66, original 24 MCQs, answer keys and prior append-only artifacts preserved.
6. Re-run full compile, unit tests, schema, adapters, pagination, answer-index and candidate manifest checks on the exact final commit.

## 4. Next safe sequence
1. Continue dialect-specific source verification for held forms and exact Sorani-script examples.
2. Obtain independent specialist review; record each accepted/rejected suggestion in a new append-only addendum.
3. Prepare a new candidate snapshot incorporating only approved practice/quiz changes; retain all previous snapshots.
4. Run exact-commit automated tests and non-destructive host smoke test only after Botkeep support clearance.
5. Keep PR Draft until all blockers are cleared; request explicit release authorization before any production change.

## 5. Preservation
This readiness file is documentation-only. It does not alter lesson data, the candidate, runtime, PR merge state, Botkeep settings, Telegram, database, tokens or production services.


## 6. Evidence and quiz proposal update — V3
- New source evidence follow-up added: «ڕەشەبا» is attested in two Central Kurdish dictionary records for lexical meaning, but its internal segmentation remains HOLD.
- Ahmadi (2021), Rules 7.9–7.10, explicitly documents Sorani past-progressive negation with ne- and de-/e- in intransitive and transitive examples. This supports the general pattern, but does not validate the exact Kurdish-script lesson example «نەدەنووسی»; that exact form remains HOLD pending dialect/person/stem review.
- V3 quiz proposal created with 19 questions (9 + 10). Its Q10 tests the source-attested sequence ne- before de- in the intransitive past-progressive example; it does not present that example as a direct equivalent of «نەدەنووسی».
- V3 answer key check: 19 questions / 19 answers / 19 key entries, all matching; answer positions A=4, B=8, C=7.
- V3 remains proposal-only. Human Sorani specialist review and Botkeep host-safety clearance remain blocked release gates.
