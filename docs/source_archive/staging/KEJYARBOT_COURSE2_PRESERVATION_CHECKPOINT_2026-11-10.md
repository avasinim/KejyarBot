# KejyarBot Course 2 — Preservation and recovery checkpoint

**Checkpoint date:** 2026-11-10  
**Repository:** `avasinim/KejyarBot`  
**Preservation branch:** `archive/preservation-audit-2026-11-10`  
**Policy:** append-only staging; `main` remains read-only; no runtime activation or deployment.

## Purpose
This checkpoint records the current recoverable state of the Course 2 review work so the work can be resumed after the current ChatGPT session or local system is shut down. The authoritative persisted copy is the Git history on the named archive branch. This checkpoint is an index and recovery guide, not a replacement for the underlying files or Git history.

## Current work products

| Artifact | Repository path | Last known commit or blob SHA |
|---|---|---|
| 62-question answer-key structural verification report | `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62Q_ANSWER_KEY_STRUCTURAL_VERIFICATION_2026-11-10.md` | commit `5f4d49e3e5a650434eae15790e47749e649a012f` |
| Global consistency audit, including section 22 | `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_GLOBAL_CONSISTENCY_AUDIT_2026-11-10.md` | commit `27a725c8e53496280c81703dc13f100d217d86d0` (later appended below) |
| Runtime migration plan | `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62Q_RUNTIME_MIGRATION_PLAN_2026-11-10.md` | retained on archive branch; fetch current branch version before editing |
| Runtime linkage audit | `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RUNTIME_LINKAGE_AUDIT_2026-11-10.md` | retained on archive branch; fetch current branch version before editing |
| Pedagogical/answer-validity review | `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62Q_PEDAGOGICAL_REVIEW_2026-11-10.md` | commit `2a94d52dc6b4405b2cbbc46774d1b36a001734fe`; blob `f1b8111233298524508c8dcdd705b5d53ab19929` |
| Reviewed Course 2 lesson draft | `course_data/latin_course_2_reviewed_draft_2026-11-10.md` | blob `abc88219e2a0e249883e8d62c5117a9b3aaa3108` (verified unchanged) |
| Reviewed Course 2 answer key | `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md` | blob `879e1525e720bdc25b8f6e896de3e388801238d0` (verified unchanged) |

## Verified protected files
- `latin_course_runtime.py` blob: `7139aec3d585919baac65f93c2630a519c995e04` — unchanged in this work.
- Reviewed lesson draft blob: `abc88219e2a0e249883e8d62c5117a9b3aaa3108` — unchanged.
- Reviewed answer-key blob: `879e1525e720bdc25b8f6e896de3e388801238d0` — unchanged.
- The 62-question structural report was fetched after creation and its key validation statement was present.
- The pedagogical review was fetched after creation and its content was present.
- The global audit was fetched after append and section 23 was present.

## Review findings preserved
- Course 2 contains 62 quiz questions: Lessons 1–7 have five each, Lesson 8 has seven, Lessons 9–12 have five each.
- The answer key has 62 corresponding rows; structural comparison found no missing/orphan/duplicate rows, absent option references, normalized answer-text mismatches, question numbering gaps/repeats, or duplicate option texts.
- The structural check does not prove the academic correctness of every answer.
- The pedagogical pass found no keyed answer contradicting the corresponding reviewed lesson's stated rule/example; it is limited to the staged text and is not a full independent peer review of every primary-source page.
- Remaining next step: distractor-quality and Kurdish orthography/context audit, followed by a separate append-only report.

## Resume/recovery procedure
1. Open repository `avasinim/KejyarBot` and select branch `archive/preservation-audit-2026-11-10`.
2. Read this checkpoint first, then the global consistency audit and the individual structural, pedagogical, linkage, and migration reports listed above.
3. Fetch the current versions of the lesson draft and answer-key draft from the archive branch; compare their blob SHAs with the protected SHAs recorded here before any further work.
4. Continue by creating a new dated, append-only staging report for distractor quality and orthography. Append its summary to the global audit; do not rewrite prior reports.
5. Keep `main` read-only. Do not modify runtime, active manifests, DB, Botkeep, Telegram, or deploy/activate unless the user gives explicit authorization.
6. Before any future runtime integration, separately review and update the test assumptions recorded in the migration plan. Tests and CI have not been run as part of this review.

## Explicit non-actions and limitations
- No runtime code, active manifest, database, Botkeep bot, Telegram bot, or deployment was modified or activated.
- No automated test suite or CI job was run.
- No claim is made that live Botkeep runtime state or external backups were inspected.
- GitHub's persistent commit history on this archive branch is the saved project record. This checkpoint does not claim to create a separate downloadable ZIP or an independent off-site backup.

## Latest relevant commit chain
- Structural report creation: `5f4d49e3e5a650434eae15790e47749e649a012f`.
- Global audit section 22: `27a725c8e53496280c81703dc13f100d217d86d0`.
- Pedagogical report creation: `2a94d52dc6b4405b2cbbc46774d1b36a001734fe`.
- Global audit section 23: `6de2b70043d358d36eb62c3c82c734d8e2b39cff`.

## Checkpoint update — 2026-11-11

### New completed work
- **Distractor-quality and Kurdish orthography review:** `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62Q_DISTRACTOR_ORTHOGRAPHY_REVIEW_2026-11-11.md`
  - Creation commit: `ec1353ec640e42990cccc2de52ebf412268a567d`
  - Current report blob SHA: `f42a72b2936b6075281c6e932419837b92239dae`
- **Global audit section 25:** appended to `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_GLOBAL_CONSISTENCY_AUDIT_2026-11-10.md`
  - Commit: `2d418ec3858cc93fc0ca135fd0eb67f048fef005`
  - Current global-audit blob SHA: `43ec935393f18fc199cd68fb13afd983b087a150`

### Findings to carry forward
- All 62 quiz questions were reviewed. Most stems and distractors are acceptable for the course's beginner level.
- Recommended wording refinements, not yet applied: Lesson 6 Q3 (restore `bireserê navdêrê`); Lesson 8 Q5 (replace weak near-duplicate distractors); Lesson 10 Q1–Q2 (add explicit sentence/tense context for object forms).
- Three mixed-script lines were found in Lesson 8 prose of the reviewed lesson draft (lines 290, 292, 294). Rewrite those lines wholly in Kurmanji Latin in a separate approved patch.
- The reviewed quiz blob remains `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; the reviewed answer-key blob remains `879e1525e720bdc25b8f6e896de3e388801238d0`. No edits were made to either artifact in this review.

### Resume point
The 62-question structural, pedagogical, and distractor/orthography review stages are now documented. The next safe task is to prepare a **separate proposed editorial patch** for the four targeted quiz refinements and three Lesson 8 mixed-script lines, preserving the reviewed drafts unchanged until the patch is separately approved. After any approved patch, re-run the 62-question/key structural comparison and update the audit/checkpoint. Do not integrate into runtime or deploy without explicit authorization.

### Verification and boundaries
The new report, global audit append, and this checkpoint update are to be fetched and checked after commit. All work remains on `archive/preservation-audit-2026-11-10`; `main` remains read-only. No tests/CI, runtime, Botkeep, Telegram, manifest, DB, or deployment action was performed. No separate ZIP/off-site backup is claimed; the GitHub archive branch and commit history remain the persisted project record.


## Checkpoint update — proposed editorial patch prepared (2026-11-11)

- Proposal: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_EDITORIAL_PATCH_PROPOSAL_2026-11-11.md`
  - Initial creation commit: `c81af46f19cb499116977a148b4193e73e652fee`
  - Wording refinement commit: `706b0a52978117695608222e2315b217817daa50`
  - Latest proposal blob SHA: `e2c9238cb36b6792ddc3b49ba260c49d6d2a5c6f`
- Global audit section 26 appended:
  - Commit: `0dc16deeed398304a2589ec174fafa9ee77d5202`
  - Latest global-audit blob SHA: `605e637156ed700139a0c08c8bf61a9f4fde0ddb`

The proposal contains exact candidate stems/options and replacement text for the three mixed-script Lesson 8 lines. **It is not an applied patch.** The two reviewed base artifacts remain unchanged at their protected blob SHAs. Do not create a revised quiz/lesson/key patch until the proposal is explicitly approved. After approval, create a new dated append-only artifact and re-run the 62-row structural comparison.

All changes remain confined to the archive branch. `main` is read-only. No runtime, test execution, manifest, DB, Botkeep, Telegram, or deployment action occurred. GitHub archive-branch history remains the persisted record; no separate ZIP/off-site backup is claimed.


## Checkpoint update — answer-key rationale proposal (2026-11-11)

- Companion proposal: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_ANSWER_KEY_PATCH_PROPOSAL_2026-11-11.md`
  - Creation commit: `43c248d19b347f33568763cbcf2cc5a45ff641a8`
- Global audit section 27 appended:
  - Commit: `2f790434789dd0a1bf0e939494a4777d8d94ab9f`
  - Latest global-audit blob SHA: `18e66c27d90c4599afdba9b7445a6809ab57cc7f`

The companion proposal supplies four matching rationale entries for L6 Q3, L8 Q5, L10 Q1, and L10 Q2. It is proposal-only and must not be applied until the related quiz/lesson proposal receives explicit approval. The base quiz SHA remains `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; the base answer-key SHA remains `879e1525e720bdc25b8f6e896de3e388801238d0`.

No runtime, tests/CI, manifest, DB, Botkeep, Telegram, or deployment action occurred. All writes remain on the archive branch; `main` remains read-only. No separate ZIP/off-site backup is claimed.


## Checkpoint update — Lesson 8 §69 source correction (2026-11-11)

A primary-source recheck of Celadet Alî Bedir-Xan, printed pp.66–68, §§67–70, caught and corrected a substantive error in the proposed replacement for Lesson 8 reviewed-draft line 292. Section 69 requires each linked complement/modifier to receive its own suffix according to its own gender and number; the earlier proposal incorrectly said the final component determines the suffix.

- Editorial proposal: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_EDITORIAL_PATCH_PROPOSAL_2026-11-11.md`
  - Corrected blob SHA: `061127ddf7fec01b4df5e43066053010bac0fe10`
  - Update commit: `aae7ae016821d1e11b5c9697d7ec479a65a7fea2`
  - Verified after update; remains proposal-only and unapplied.
- Global audit section 28 appended and verified:
  - Blob SHA: `b3f8b4a649b4388c5cbb0fd74a7b0e363facdf61`
  - Update commit: `4daf9763400d5818809f00934f286e37c660b67a`

The reviewed lesson draft remains at SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; the reviewed answer key remains at SHA `879e1525e720bdc25b8f6e896de3e388801238d0`. Neither was edited. No runtime, tests/CI, manifest, database, Botkeep, Telegram, or deployment action occurred. `main` remains read-only. GitHub archive-branch history remains the persisted project record; no separate ZIP/off-site backup is claimed.


## Checkpoint update — final Lesson 8 §§68–70 page-image adjudication (2026-11-11)

A final visual reinspection distinguishes the adjacent source rules and resolves the temporary reversal in the proposed line 292 wording:
- §68 (printed p.66): when several nouns are linked by one complement, the determiner is selected according to the final noun's gender.
- §69 (printed pp.66–67): when several complements are linked in the described noun group, each complement receives its own determiner according to its own number and gender.
- §70 (printed pp.67–68): the uninflected `-ek/-ek/-in` forms take oblique forms `-ekî/-ekê/-ina` in the stated object construction.

The earlier §28 claim that §69 gives each element its own suffix was correct. A temporary later revision incorrectly conflated §68 with §69; the latest proposal now restores the correct §69 wording and explicitly distinguishes both rules. It also uses `formên netewandî` for the uninflected forms in the proposed line 290.

- Current editorial proposal blob SHA: `2a468ec504434d6e98d5c31f86061f47f61c4b68` (verified after update; proposal-only).
- Global audit section 29 blob SHA: `28b23564f3f47e567e62166599c2392d6c687f8e` (verified).
- The reviewed lesson base remains `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; the reviewed answer key remains `879e1525e720bdc25b8f6e896de3e388801238d0`.

No base lesson, answer key, runtime, tests/CI, manifest, DB, Botkeep, Telegram, or deployment state was changed. `main` remains read-only. The GitHub archive branch remains the persisted project record; no independent ZIP/off-site backup is claimed.


## Checkpoint update — definitive Lesson 8 lines 290, 292 and 294 review (2026-11-11)

Direct inspection of the original source page images confirms:
- §68: final-noun agreement when several nouns are linked by one complement.
- §69: each linked complement in the specified multi-complement construction receives its own determiner according to its own gender and number.
- §70: uninflected -ek/-ek/-in forms inflect as -ekî/-ekê/-ina in the stated object environment.

The proposed line 290 uses formên netewandî accurately for the uninflected forms; line 292 preserves §69's own-form-for-each-complement rule; line 294 separates the three indefinite environments from the definite forms -ê/-a/-ên and removes mixed-script fragments. This is the controlling source-based interpretation. Earlier contradictory intermediate summaries are superseded by the latest addenda in the proposal and page-image review note.

- Page-image review current blob SHA: 0eaa37c517fdaf244b48cc69f953400393ab0812.
- Editorial proposal current blob SHA: a8e5d3fed8591c81b33f3b411a7d851ee3891224.
- Global audit section 30 is being appended in the same work sequence.

All reviewed lesson, answer-key, and runtime baselines remain unchanged. No tests/CI, runtime, manifest, database, Botkeep, Telegram, or deployment action occurred. `main` remains read-only. The proposal remains unapplied; no independent ZIP/off-site backup is claimed.


## Checkpoint update — four proposed quiz edits source-verified (2026-11-11)

Primary-source cross-check supports all four proposed revisions:
- L6 Q3: §59–60, exact example `hespê beza`; `beza` is the noun complement and the full term `bireserê navdêrê` avoids ambiguity.
- L8 Q5: §§63 and 66–67 distinguish definite `-ên` from indefinite `-ine`; proposed A/B are distinct false conflations and C is correct.
- L10 Q1: §86 explicitly gives `tu min dibînî`.
- L10 Q2: §86 explicitly gives `tu wê dibînî`; the proposal stem was changed to use that exact frame.

The proposed key letters remain A/C/B/C. The current option order supports these keys. Editorial proposal SHA: `7ce8709d4847cc9fde265d198c69a0d694610787`; answer-key rationale proposal SHA: `79b39c8fb499f45c61445f640dc268f32c05eecb`. Both were fetched and verified after updates. They remain unapproved and unapplied.

The reviewed lesson baseline remains `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; reviewed answer-key baseline remains `879e1525e720bdc25b8f6e896de3e388801238d0`; runtime baseline remains `7139aec3d585919baac65f93c2630a519c995e04`. No tests/CI, runtime, manifest, database, Botkeep, Telegram, or deployment operation occurred. `main` remains read-only.


## Checkpoint update — consolidated patch review handoff (2026-11-11)

A single operative handoff has been created and fetched back successfully:
`docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_CONSOLIDATED_PATCH_REVIEW_2026-11-11.md`

Verified blob SHA: `ccd2ed2ead0783354699c2df5db26ba8fac8ca6d`.

It consolidates the four proposed quiz edits and the three proposed Lesson 8 prose-line replacements, records the controlling §§68–70 interpretation, and clearly labels all changes as unapproved and unapplied. It also flags a remaining language-editor pass for the exact Kurmanji Latin syntax/terminology of the prose replacements, particularly line 292. The baseline reviewed lesson, quiz, answer key and runtime remain unchanged. Tests/CI were not run; runtime was not tested live; no deployment or Botkeep/Telegram operation occurred. `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup.


## Checkpoint update — Lesson 8 §69 terminology candidate (2026-11-11)

The consolidated handoff now contains a language-editor candidate for line 292 that uses the course's precise term `bireserên navdêrê` rather than the potentially ambiguous bare `bireser`. The candidate is explicitly proposal-only and requires final language-editor review. It does not alter the source-based rule: each linked modifier receives its own determiner according to its own gender and number (§69), distinct from §68's final-noun agreement rule.

Consolidated handoff current blob SHA: `c648fae070f10691ebcb754b772544af0a343ff8`. No base lesson, quiz, key, runtime, manifest, database, Botkeep, Telegram, or deployment file changed. Tests/CI not run; `main` remains read-only.


## Checkpoint update — full 12-lesson terminology and orthography audit (2026-11-11)

- New append-only report: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_12LESSON_TERMINOLOGY_ORTHOGRAPHY_AUDIT_2026-11-11.md`
- Verified report blob SHA: `d727d0d2c49109f254eacc954ce22206054e568f`
- Global audit section 34 appended; commit `60c85e2f85a8afde08d9b9c518658e2babeecf42`, blob SHA `fd72d2f8b5c2e3aa756aa721670825709b8a65c8`.

The report covers all 12 lesson sections in the reviewed 651-line draft. Main follow-ups: language-editor decision on `rengdêrê/rengdêra jmarîn`; glossary distinction for broad `pêvek` versus specific `veqetandek`; review of Lesson 6's paired `pêşnavdêr/bireser` label; retain the contextual distinction of `bireserê navdêrê` versus clause-level `bireser`, and source-aware `ko/ku`; and keep the three Lesson 8 mixed-script lines pending approval of the existing proposal.

The report is audit-only. Reviewed lesson SHA remains `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; answer-key SHA remains `879e1525e720bdc25b8f6e896de3e388801238d0`; runtime SHA remains `7139aec3d585919baac65f93c2630a519c995e04`. No tests/CI, runtime, manifest, DB, Botkeep, Telegram, or deployment operation occurred. `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — master terminology register created (2026-11-11)

- Register: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_MASTER_TERMINOLOGY_REGISTER_2026-11-11.md`
- Verified register blob SHA: `08423c8bf0a44f5b3b5efe28f531a41f81b5fed8`
- Global audit section 35 appended; commit `24b9a232df79aaadc440e928f8c5e5316694817f`, blob SHA `0ec4bdd0f87cc381167268ce792c7d9adeb01ec4`.

The register consolidates the working terminology and semantic boundaries for all 12 Course 2 lessons. It is an editorial navigation baseline, not an external standard. It records the outstanding language-editor decisions for Lesson 12 `rengdêrê/rengdêra jmarîn`, the `pêvek/veqetandek` glossary distinction, Lesson 6's paired label, and Lesson 8's proposal-only mixed-script replacements. No source lesson or reviewed base was modified.

Protected baselines remain: reviewed lesson `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; reviewed answer key `879e1525e720bdc25b8f6e896de3e388801238d0`; runtime `7139aec3d585919baac65f93c2630a519c995e04`. No tests/CI, runtime, manifest, database, Botkeep, Telegram, or deployment action occurred. `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup.


## Checkpoint update — 62-question lesson/quiz terminology cross-check (2026-11-11)

- New append-only report: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62Q_LESSON_QUIZ_TERMINOLOGY_CROSSCHECK_2026-11-11.md`
- Verified report blob SHA: `e5e7b67bcc98504d0fd39b7da8a348ba8bee7350`
- Global audit Section 36 appended in commit `698c2466ffadd7728cca14e0000b7935dc4afa9d`.

All 62 questions across 12 lessons were cross-checked against lesson terminology and the 62-row reviewed answer key. New exact follow-ups: L8 Q3 should use the §66 condition `bê pêvekeke raveker li pey navdêrê` rather than ambiguous `bê bireser`; L6 Q3 retains the full term `bireserê navdêrê`; L8 Q5 and L10 Q1–Q2 remain covered by the existing proposal; L12 Q3 remains pending a language-editor decision on `rengdêra jmarîn` versus the source category heading `rengdêrên jmarîn`. No content edits were applied.

Protected lesson SHA remains `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; answer-key SHA remains `879e1525e720bdc25b8f6e896de3e388801238d0`. No tests/CI, runtime, manifest, DB, Botkeep, Telegram, or deployment operation occurred. `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup.


## Checkpoint update — Lesson 8 Q3 proposal added (2026-11-11)

The editorial patch proposal now includes a proposal-only Lesson 8 Q3 stem refinement: use `bê pêvekeke raveker li pey navdêrê` to name the §66 environment, rather than the ambiguous `bê bireser`; retain `-in` (A) in the current option order. Proposal blob SHA verified: `11b6c6c055a149283f2b4275da15922e28d1f82d`. The proposal is not applied to the protected quiz/lesson or answer key. The 62-question cross-check report remains `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62Q_LESSON_QUIZ_TERMINOLOGY_CROSSCHECK_2026-11-11.md` (SHA `e5e7b67bcc98504d0fd39b7da8a348ba8bee7350`). No runtime/deployment/test actions occurred; `main` remains read-only.


## Checkpoint update — consolidated five-item proposal handoff (2026-11-11)

- Consolidated handoff: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_CONSOLIDATED_PATCH_REVIEW_2026-11-11.md`, blob SHA `31efd8edba0aca2820ebe9b53d8eec424746b83e`.
- Answer-key rationale proposal addendum: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_ANSWER_KEY_PATCH_PROPOSAL_2026-11-11.md`, blob SHA `3e202d34739d6f55d2b079e8d0a6c38b1ddcb1ff`.

The handoff now includes five proposed quiz items: L6 Q3, L8 Q3, L8 Q5, L10 Q1 and L10 Q2, plus the three Lesson 8 explanatory-line candidates. The key rationale proposal includes a draft rationale for L8 Q3 but remains proposal-only. No base quiz/key or lesson content was changed. All proposals require explicit approval; the outstanding language-editor decisions remain clearly recorded. No tests/CI, live runtime, manifest, DB, Botkeep, Telegram, or deployment action occurred. `main` remains read-only; GitHub history is not an independent off-site backup.


## Checkpoint update — five-item option/key alignment (2026-11-11)

The current option order and protected answer-key rows were rechecked for all five proposed edits. Confirmed sequence: **A / A / C / B / C** (L6 Q3, L8 Q3, L8 Q5, L10 Q1, L10 Q2). Exact options and answer texts are in section 8 of the consolidated handoff, blob SHA `565481fe4b5a8346e8c5c5d312e16056e09da37b`. This is not approval of the proposed wording; no quiz, lesson, or answer-key base file was modified.

No tests/CI, live runtime, manifest, DB, Botkeep, Telegram, or deployment action occurred. `main` remains read-only.


## Checkpoint update — Lesson 8 line 292 supersession guard (2026-11-11)

The consolidated handoff now explicitly marks the earlier line 292 wording in section 3 as non-operative and not approved. The later section 6 candidate using `bireserên navdêrê` is also pending language-editor review; neither should be applied. The §68/§69 source distinction remains verified. Current handoff blob SHA: `73cf22bbd2280e4d9dcf79ea88e494b22e7ed7fc`. Protected base files remain unchanged.


## Checkpoint update — Lesson 12 terminology adjudication (2026-11-11)

- New note: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_TERMINOLOGY_ADJUDICATION_2026-11-11.md`, verified blob SHA `833c34339eb6ae80de339e0d1b7c42b5fa65960b`.
- Master terminology register has an append-only adjudication addendum; update commit `4c7578d4d0f5f46155a8c3b2aea7e605c4745102`.
- The working preference is to retain `rengdêrên jmarîn` as plural class label and provisionally use `rengdêrê jmarîn` in singular prose. Quiz Q3's `rengdêra jmarîn` remains unresolved pending a Kurmanji editor's grammatical judgment in that exact context. This is not a final grammar ruling because the primary Lesson 12 source page image was not reopened.

No base lesson/quiz/key edits were made; all proposals remain unapproved. No tests/CI, runtime, manifest, DB, Botkeep, Telegram, or deployment action occurred. `main` remains read-only.


## Checkpoint update — Lesson 6 terminology adjudication (2026-11-11)

- New note: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON6_PRENOMINAL_MODIFIER_ADJUDICATION_2026-11-11.md`, blob SHA `9bcb2af635e61a5a78945c5cb17031f634cd8331`.
- Master terminology register addendum commit: `d34de2a3a6b2655cef7b9435cbaac43ad97feee8`.
- Global consistency audit addendum commit: `17c26ec4d5058cd488eaf9caade687975f996a80`.
- Finding: `pêşnavdêr/bireser` is an unexplained slash-pair; distinguish pre-nominal position from noun-modifying function and from clause-level object `bireser`. Verify the technical sense of `pêşnavdêr` against the primary source before final wording.

No lesson, quiz, answer key, or runtime changes; all proposals remain unapproved. No tests/CI or live runtime check occurred. `main` remains read-only.


## Checkpoint update — Lessons 7–8 `pêvek` / `veqetandek` adjudication (2026-11-11)

- New append-only adjudication: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSONS7_8_PEKVEK_VEQETANDEK_ADJUDICATION_2026-11-11.md`, verified blob SHA `ffac88211e309ede86159e8132d5e0d73c8c5be9`.
- Master terminology register addendum: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_MASTER_TERMINOLOGY_REGISTER_2026-11-11.md`, verified blob SHA `a0268a554d8e5650bab7c8b20aa52537c4a628bc`.
- Global consistency audit section 37 appended: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_GLOBAL_CONSISTENCY_AUDIT_2026-11-10.md`, update commit `38d20d35266132d62cfc83074f232e9e4cf4bdb4`, new blob SHA `835a12be4ba0eecabb7bf16ae87a367809dafc77`.

Working ruling: `pêvek` is the broad affix/suffix term; `veqetandek` is the course-specific label for the definite/indefinite noun-determining paradigms in Lessons 7–8. Keep `veqetandeka binavkirî` and `veqetandeka nebinavkirî` stable. `pêveka raveker` is descriptive wording for a particular modifier-following environment, not evidence of synonymy. Avoid global replacement. This internal course distinction still requires Kurmanji language-editor confirmation before it is promoted as a formal glossary definition; §§61–67 primary-source pages were not independently reopened in this pass.

No source-aligned lesson, reviewed lesson, quiz, answer key, runtime, manifest, database, Botkeep, Telegram, or deployment file was changed. No tests/CI were run; no live runtime or Botkeep state was inspected. All work remains on `archive/preservation-audit-2026-11-10`; `main` remains read-only. GitHub archive history is the persisted project record, not a separate ZIP/off-site backup.


## Checkpoint refinement — source-verified `veqetandek` vs `pêvek` distinction (2026-11-11)

A further source-page review refined the Lesson 7–8 adjudication: §61 defines `veqetandek` as the grammatical determiner category/function (a small word before or after a noun that identifies/limits reference), not inherently as a suffix. Lesson 7 includes both post-nominal attached `-ê/-a/-ên` and shortened pre-adjectival `ê/a/ên` forms when the noun is understood/omitted. Lesson 8's indefinite forms vary by syntactic environment. `pêvek` remains the broader morphological term for affix/suffix and may describe a bound realization, but is not the category label.

- Focused adjudication refinement latest blob SHA: `a3b9e85c8f8d78a1dfe3d14767834ef06f86c967`.
- Master terminology register latest blob SHA: `98c6c52a34e3f9733e208bad8d230808e9b9779b`.
- Global audit section 38 latest blob SHA: `8ef98cc4b3a200d7fa4a8ba91c4f495001c9ad86`.
- Source page-image evidence: Lessons 6–7 review blob `6ff6e84792bc13f5835010401bfab89acd446295`; Lesson 8 review blob `0eaa37c517fdaf244b48cc69f953400393ab0812`.

This refinement supersedes only the earlier too-narrow phrase implying that all determiners are suffix-like. No lesson, quiz, answer key, runtime, manifest, database, Botkeep, Telegram, or deployment file was changed. No tests/CI or live runtime check occurred. `main` remains read-only; GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — Lessons 6, 8 and 12 modifier/adjective/object adjudication (2026-11-11)

- New append-only adjudication: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSONS6_8_12_MODIFIER_ADJECTIVE_OBJECT_ADJUDICATION_2026-11-11.md`, verified blob SHA `b245160ce26b27d6bc1adeb8416708febc722824`.
- Master terminology register addendum verified blob SHA: `bcae04276e7946d4874a2df1a062636f99a946c3`.
- Global consistency audit section 39 verified blob SHA: `0367e14204d552f6f0b46d5d5d68424ef938547d`.

Working distinction: `bireserê navdêrê` is the broad syntactic noun-attached modifier/complement function; `rengdêr` is the adjective word class; bare `bireser` is the clause-level object role. For `ev keçik`, Lesson 12's internal taxonomy supports demonstrative adjective/modifier; for `Ev hat.`, independent demonstrative pronoun. Lesson 6's `pêşnavdêr/bireser` slash-pair and Lesson 8's `bireser/rengdêr` shorthand remain editorial clarification targets, not silently corrected text. Lesson 12 page images were not reopened in this pass; that taxonomy is internally checked against the staged source-aligned text.

No source-aligned lesson, reviewed lesson, quiz, answer key, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was changed. No tests/CI or live runtime checks were performed. Work remains on `archive/preservation-audit-2026-11-10`; `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — Lesson 12 source-grounded category boundaries (2026-11-11)

- Added source-grounded adjudication: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_SOURCE_GROUNDED_ADJECTIVE_PRONOUN_NUMERAL_ADJUDICATION_2026-11-11.md`, verified blob SHA `d6baeceb8981b661cdac7f10d4a42257db431a86`.
- The reconciliation uses recorded page-image reviews: Lesson 12 pp.89–100, §§119–152 (blob `c712dd136e36154e5314efc65e9f7eef8c9cf4ab`), and pronoun sections pp.71–88, §§72–118 (blob `db629ed41eeb8783a09b662c75b838a90cd43ca6`).
- Category depends on syntactic function: demonstrative/possessive forms can be adjective-like with an expressed noun or pronominal when replacing one; numeral adjective modifies a stated noun, while `jmarnav` is independently/substantively used in the course's adopted framework. Source labels and course teaching labels must be mapped explicitly. Descriptive adjectives may be predicative or substantivized.
- Lesson 12 quiz Q3 form `rengdêra jmarîn` remains unresolved against prose `rengdêrê jmarîn`; do not silently normalize.

No lesson, exercise, quiz, answer key, source-aligned text, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks performed. Archive branch only; `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — Lesson 12 adjective-class/function boundary review (2026-11-11)

- New audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_ADJECTIVE_CLASS_FUNCTION_BOUNDARY_REVIEW_2026-11-11.md`, verified blob SHA `d76164ef5c2bbad97d63c4b10058cad6a415e931`.
- The source-grounded review records that descriptive adjectives can be predicative or substantivized (source §§124–127); the opening definition should be qualified rather than treating an expressed adjacent noun as mandatory.
- Preserve the six adjective classes while separating word class from syntactic function. Demonstrative, possessive, interrogative, and indefinite forms may be adjective-like with an expressed noun or pronominal when they stand independently; numeral adjective modifies an expressed noun while `jmarnav` is independent/substantive in the course's adopted framework.
- Map course terminology to source wording explicitly at first mention: `wesfîn` ↔ `çilobûn û çawabûnê`; `xwemalîn` ↔ `destdaniyê/xwedîtiyê`; `rêzîn` ↔ `rêzda`.
- Lesson 12 Q3 `rengdêra jmarîn` remains unresolved; no automatic normalization.

No lesson, exercise, quiz, answer key, runtime, parser, test, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks occurred. `main` remains read-only; GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — Lesson 12 five-question quiz/key audit (2026-11-11)

- Audit file: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_FIVE_QUESTION_KEY_ALIGNMENT_AUDIT_2026-11-11.md`, verified blob SHA `464b2c284dbff250f979aa03a091d10eaf49350d`.
- Compared all five question stems/options and answer-key rows with the reviewed lesson and direct source page-image review §§119–152.
- No keyed-answer contradiction found; current answer sequence **B / C / A / B / C** remains correct at the concept level.
- Q3's concept is correct, but `rengdêra jmarîn` remains an unresolved morphology/editorial form. No automatic normalization.
- The generic answer-key rationales are pedagogically weak; item-specific explanations are recommended for a future approved patch only.
- No lesson, quiz, answer key, runtime, parser, test, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks occurred; `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.
