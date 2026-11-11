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

## Checkpoint update — Lesson 12 distractor and rationale quality audit (2026-11-11)

- New audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_DISTRACTOR_AND_RATIONALE_QUALITY_AUDIT_2026-11-11.md`, verified blob SHA `7d90ba45aa64d7518b8c93d91c80eb76490cbd10`.
- The five-question key remains **B / C / A / B / C**; no key-letter contradiction found.
- Q4's distractors `di bin pronav de` and `di bin lêker de` are weak/nonparallel and need a future approved, language-editor-reviewed redesign. Q2 has the strongest category contrast; Q1/Q3/Q5 remain usable but uneven in distractor difficulty.
- All five current key rationales are generic assertions; the audit supplies item-specific draft explanations, not approved key text. Q3's `rengdêra jmarîn` form remains unresolved.
- No protected lesson, quiz, option, key, runtime, parser, test, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks were performed; `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.

## Checkpoint update — Lesson 12 Kurmanji orthography and wording audit (2026-11-11)

- New verified audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_QUIZ_KURMANJI_ORTHOGRAPHY_AND_WORDING_AUDIT_2026-11-11.md`, blob SHA `47329d8c24c0a5f854495434f4612f38fbb9d2eb`.
- No unequivocal character-level spelling error was established from the staged text alone. Q1 has capitalization/answer-shape inconsistency and an open terminology query over `kiryar`; Q3's `rengdêra jmarîn` remains unresolved. Q4 A/C are surface-syntactically parallel but semantically weak; B has a different answer shape. Q5 options are not perfectly parallel in semantic type.
- The audit corrects Section 43's overbroad statement: Q4 A/C are parallel in surface syntax; their problem is category meaning and mismatch against B, not A-vs-C syntax.
- No protected course or runtime content changed; no tests/CI or live runtime checks were performed. `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.

## Checkpoint update — Lesson 12 quiz parallelism and rationale audit (2026-11-11)

- New verified audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_QUIZ_PARALLELISM_AND_RATIONALE_ALIGNMENT_AUDIT_2026-11-11.md`, blob SHA `f076c4878192fd8cfdc4cf0b2c7384142a14341b`.
- Q2 is the most parallel option set. Q1 mixes clause/fragment forms and capitalization; Q4 A/C are surface-parallel but semantically weak, while B has a different answer shape; Q5 mixes category labels with an example-description. Q3's category contrast is acceptable but uneven.
- New unresolved terminology flag: Q1 `kiryarê` vs master register `kirar`. Do not normalize or substitute `kirde` without source/editor ruling.
- Item-specific answer rationales are drafted in the audit only; no key text changed. Current key remains **B / C / A / B / C**.
- No protected lesson, quiz, key, runtime, parser, tests, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks occurred; `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — Lesson 12 learning-objective and assessment alignment (2026-11-11)

- New verified audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_LEARNING_OBJECTIVE_ASSESSMENT_ALIGNMENT_AUDIT_2026-11-11.md`, blob SHA `c90ca1fee11df39f200fd7222ac0bfb284baf883`.
- The five current key answers align with the concepts they test; no key contradiction was found. The quiz samples only a subset of the lesson objectives: it does not directly test the six-class taxonomy as a whole, adjective degrees, adjective/pronoun distinction, or the interrogative, indefinite, and possessive classes.
- The quiz is best characterized as a short end-of-lesson checkpoint, not a representative assessment of all objectives. Xebata 1's `nîv roj` needs a teacher-facing answer criterion; Xebata 3 should model the expressed-noun vs independent numeral distinction.
- Recommendations are audit-only. No lesson, exercise, quiz, key, runtime, parser, tests, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks occurred; `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — Lesson 12 exercise teacher rubric (2026-11-11)

- New verified audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_EXERCISES_TEACHER_RUBRIC_AND_AMBIGUITY_AUDIT_2026-11-11.md`, blob SHA `6abe7c8440175b0f5f50781b1ee6f4456b54a4fc`.
- Xebata 1 provisional classifications are documented. `kurên van` and `nîv roj` are intentionally left unresolved pending syntax/category decisions; `mehînên te` needs Kurmanji review; `tu mirov` and oblique demonstratives need context for interpretation-based marking.
- Xebata 2's implied six-example requirement and proposed marking criteria are documented. Xebata 3 has a scoped model answer contrasting `sê mal` with independent `jmarnav` use.
- All content is teacher-facing proposal only. No lesson/exercise/quiz/key/runtime/parser/tests/manifest/DB/Botkeep/Telegram/deployment files changed. No tests/CI or live runtime checks occurred; `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — Lesson 12 source-to-terminology alignment (2026-11-11)

- New audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_SOURCE_TO_TERMINOLOGY_ALIGNMENT_AUDIT_2026-11-11.md`, verified blob SHA `017faf373f704a08eb77f5be7a45b75ea1ece828`.
- Global consistency audit Section 48 appended; verified global audit blob SHA: `90db4ec8a3c24cb8e49c6e4f8edb66c9441e1091`.
- The six adjective classes remain unchanged; ordinal `rêzîn` is treated as a subtype within numeral adjectives, not a seventh class. The audit distinguishes word class, subclass, syntactic function, and surface form.
- Clarified lesson-internal readings for exercise items: `nîv roj` = `jmarnav` used before an expressed noun (with a modifying/quantifying phrase function); `kurên van` is listed by the lesson under possessive examples and provisionally belongs to `xwemalîn`, subject to Kurmanji editor review.
- Predicative/substantivized adjective uses and source/course terminology mappings are recorded. Q3's `rengdêra jmarîn` vs `rengdêrê jmarîn` remains unresolved.
- Audit-only. No learner-facing files, terminology register, runtime, parser, tests, manifest, DB, Botkeep, Telegram, or deployment files changed. No tests/CI or live runtime checks occurred; `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup.


## Checkpoint update — terminology register Lesson 12 boundary addendum (2026-11-11)

- Master terminology register addendum appended and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_MASTER_TERMINOLOGY_REGISTER_2026-11-11.md`, blob SHA `494546c6e94504806b7f073c98e3e5a21ad0d194`.
- The addendum preserves the six top-level adjective classes, treats `rêzîn` as a numeral-adjective subtype, separates lexical class from syntactic function and surface form, and records the lesson-internal readings of `nîv roj` and `kurên van`.
- This is provisional course-internal guidance, not a final external standard; Kurmanji editor review remains needed for detailed syntax/idiomaticity and Q3 morphology.
- No learner-facing lesson, exercise, quiz, answer key, runtime, parser, tests, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks occurred; `main` remains read-only.


## Checkpoint update — Lesson 12 exercise rubric reconciliation (2026-11-11)

- Teacher-rubric addendum appended and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_EXERCISES_TEACHER_RUBRIC_AND_AMBIGUITY_AUDIT_2026-11-11.md`, blob SHA `c7b7a3fe4ca131cdecab3a7db59330d400146f86`.
- Global consistency audit Section 49 appended and verified: blob SHA `dd922dda8f7e571652f4ea1f201554cae707fc9a`.
- Updated teacher guidance: `kurên van` follows the lesson's `xwemalîn` example list (editor review remains); `nîv roj` is `jmarnav` in the lesson taxonomy, with its noun-phrase function recorded separately.
- Xebata 2 and Xebata 3 marking criteria now distinguish class/subclass/function/surface form. Q3 singular label morphology remains open.
- Audit-only. No learner-facing content, quiz/key, runtime, parser, tests, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks occurred; `main` remains read-only.


## Checkpoint update — complete 13-item Lesson 12 exercise audit (2026-11-11)

- Full 13-row teacher-facing audit appended and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_EXERCISES_TEACHER_RUBRIC_AND_AMBIGUITY_AUDIT_2026-11-11.md`, blob SHA `99694a86c9457e3b5a296d105209b5175b24a25b`.
- Global consistency audit Section 50 appended and verified: blob SHA `7adc1886654751a138392a40152741c74bbe4393`.
- The matrix distinguishes course-intended class from phrase function, morphology, and context. `tu mirov` requires context; `hespê min` and `mehînên te` require careful possessive/pronoun terminology and Kurmanji editor review; `kurên van` remains the lesson-intended `xwemalîn` item pending syntax/idiomaticity review; `nîv roj` remains `jmarnav` with modifying phrase function stated separately.
- No learner-facing lesson, exercise, quiz, answer key, runtime, parser, tests, manifest, DB, Botkeep, Telegram, or deployment file changed. No tests/CI or live runtime checks occurred; `main` remains read-only.


## Checkpoint update — Lesson 12 Xebata 2 and Xebata 3 audit (2026-11-11)

- Teacher-facing audit appended and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_EXERCISES_TEACHER_RUBRIC_AND_AMBIGUITY_AUDIT_2026-11-11.md`, blob SHA `4d3937cbc49dd4ca28e860fdd36a78cb579e05c3`.
- Global consistency audit Section 51 appended and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_GLOBAL_CONSISTENCY_AUDIT_2026-11-10.md`, blob SHA `a9b5edfecdc6982d8f471efbe7039bd7d37c108e`.
- Xebata 2 rubric specifies six top-level adjective classes, one new noun-containing example per class; `rêzîn` remains a subtype within `jmarîn`, not a seventh class.
- Xebata 3 rubric distinguishes numeral-adjective use with an expressed noun from independent/substantive `jmarnav` use and records a provisional one-sentence model response. Kurmanji copy-edit and the existing singular morphology query remain open.
- No learner-facing content or protected runtime/deployment files changed. No tests/CI or live runtime checks occurred; `main` remains read-only. No independent ZIP/off-site backup was created or verified.


## Checkpoint update — Lesson 12 internal definition/example consistency audit (2026-11-11)

- New teacher-facing audit created and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_INTERNAL_DEFINITION_EXAMPLE_CONSISTENCY_AUDIT_2026-11-11.md`, blob SHA `6488333dfc374f7ba3fa36240cdf1ebc019c9d4c`.
- Master terminology register addendum and global consistency audit Section 52 record the course-taxonomy caveat and the distinctions among lexical class, phrase function, and surface form.
- Main open issues: broad opening definition; context-sensitive demonstrative/interrogative/quantifier forms; mixed possessor morphology (especially `kitêba vî`); `nîv roj` lexical-vs-phrase analysis; case context in numeral examples; ellipsis context for ordinal forms.
- No learner-facing or protected runtime/deployment files changed. No tests/CI or live runtime checks occurred; `main` remains read-only. No independent ZIP/off-site backup is claimed.


## Checkpoint update — Course 2 cross-lesson terminology chain (2026-11-11)

- Cross-lesson terminology audit created and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_CROSS_LESSON_TERMINOLOGY_CHAIN_AUDIT_2026-11-11.md`, blob SHA `178b0fb99da312265e27172208635a0221a9ef2b`.
- Master terminology register updated to record the core distinctions and unresolved labels; global consistency audit Section 53 appended.
- No learner-facing lesson/exercise/quiz/key or protected runtime/parser/tests/manifest/database/Botkeep/Telegram/deployment files changed. No tests/CI or live runtime checks occurred; `main` remains read-only. No independent ZIP/off-site backup is claimed.


## Checkpoint update — Course 2 62-question terminology audit (2026-11-11)

- 62-item terminology audit created and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62_QUESTION_TERMINOLOGY_AUDIT_2026-11-11.md`, blob SHA `1cd41f566c4896450a4bd93b93cf0b75af9288f3`.
- Confirmed 62 quiz items and 62 answer-key rows. Master terminology register updated; global consistency audit Section 54 appended.
- No quiz/key or learner-facing content was edited. No tests/CI or runtime checks occurred; `main` remains read-only. No independent ZIP/off-site backup is claimed.


## Checkpoint update — 62-question distractor quality audit (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62_QUESTION_DISTRACTOR_QUALITY_AUDIT_2026-11-11.md`, SHA `92e83ee006cf388f5b31b726deb7c3c493c28719`.
- All 62 questions and options reviewed. Critical open issue: Lesson 10 Q2 `forma bireserî` vs keyed `wê`; high-priority wording risk: Lesson 6 Q3's bare `bireser`.
- Master terminology register updated and global audit Section 55 appended. No quiz/key edits or runtime changes; no tests/CI or learner-response analysis. `main` remains read-only; no independent ZIP/off-site backup is claimed.


## Checkpoint update — 62-question orthography and formatting audit (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62_QUESTION_ORTHOGRAPHY_FORMATTING_AUDIT_2026-11-11.md`, SHA `6478e42c7231732ae1bf9ea5cba45ff9ae4636ff`.
- Confirmed 62 questions and 62 answer-key rows. Main open editorial spelling item: L1 Q4 rationale `kîtê/kitê`; L12 quiz heading/layout/capitalization differs from earlier lessons.
- Master terminology register updated and global audit Section 56 appended. No learner-facing changes or key edits; no parser/test/runtime verification. `main` remains read-only; no separate ZIP/off-site backup is claimed.


## Checkpoint update — 62-question answer-key rationale specificity and source-support audit (2026-11-11)

- Audit created and verified: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62_ANSWER_KEY_RATIONALE_SPECIFICITY_SOURCE_SUPPORT_AUDIT_2026-11-11.md`, blob SHA `fc1e91a3435fcd89c551efc51a5bdb476393e210`.
- Verified 62 quiz items and 62 key rows. 47 rationales (75.8%) are generic confirmations; 15 contain item-specific explanations. The audit provides a complete 62-row review.
- Stronger existing rationales: L5 Q2–Q4, L8 Q6–Q7, L11 Q4. Repeated but useful paradigms: L7 Q2–Q4 and L9 Q1–Q4.
- Priority holds: L10 Q2 (`wê` agent vs stem's object-form label), L12 Q1 adjective-definition scope, L12 Q3 `rengdêra/rengdêrê jmarîn`, L1 Q4 `kîtê/kitê`. L6 Q3 must retain the full noun-attached modifier distinction.
- No quiz, key, rationale or lesson text was edited. No tests/CI, live runtime checks, learner-response or psychometric analysis occurred. `main` remains read-only; GitHub archive history is not a separate ZIP/off-site backup.


## Checkpoint update — 44 proposed answer-key rationale rewrites (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_44_PROPOSED_ANSWER_KEY_RATIONALE_REWRITES_2026-11-11.md`, SHA `04931e2bc674c6a0d842a74b41e20f82e440f3d5`; exact proposal-row count: 44.
- Draft covers generic-rationale items across Lessons 1–12. Three generic items remain on hold (L10 Q2, L12 Q1, L12 Q3); L1 Q4 remains a separate spelling/notation hold.
- L6 Q3 wording retains `bireserê navdêrê` and avoids the ambiguous bare term `bireser`.
- No answer-key or lesson edits; proposals are not approved or learner-facing. No runtime/parser/manifest/database/Botkeep/Telegram/deployment changes, tests/CI, or psychometric/learner-response analysis.
- `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup; no separate backup is claimed.


### Checkpoint addendum — rationale proposal alignment verification (2026-11-11)

- Updated proposal artifact: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_44_PROPOSED_ANSWER_KEY_RATIONALE_REWRITES_2026-11-11.md`, verified SHA `133c9105a9a3315ceed3d5e2d84d69bf1d472b28`.
- Confirmed 44/44 proposed rationale rows map to the existing answer-key option letter; zero missing mappings and zero mismatches.
- Mapping validation is not linguistic certification. All proposals remain unapproved; no key/quiz/lesson or runtime changes.


## Checkpoint update — linguistic/source review of 44 rationale proposals (2026-11-11)

- Audit: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_44_RATIONALE_PROPOSALS_LINGUISTIC_SOURCE_ALIGNMENT_AUDIT_2026-11-11.md`, verified SHA `d1275daeedd8e7576524f30d71d1eb6276795ada`.
- All 44 proposals were compared with the reviewed lesson draft and corresponding quiz/key items. Overall alignment is good; ten precision refinements are recorded for editorial review.
- Holds remain: L10 Q2, L12 Q1, L12 Q3; L1 Q4 is a separate spelling/notation hold.
- This is not fresh inspection of every original book page and does not constitute approval. No key, quiz, lesson, runtime, parser, manifest, database, Botkeep, Telegram or deployment changes; no tests/CI, learner-response or psychometric analysis.
- `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup; none is claimed.


## Checkpoint — held rationale source adjudication (2026-11-11)

- Adjudication note: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_HELD_RATIONALE_ITEMS_SOURCE_ADJUDICATION_2026-11-11.md`, verified SHA `c985701ac40e326519713f1c91440687f5e26c43`.
- L10 Q2 no longer treated as a demonstrated source contradiction: §86 supports `wê` as the feminine form in the direct-object paradigm, while clause role can switch in transitive past constructions. Editorial wording clarification recommended; no answer-key change.
- L12 Q1 still needs an authorized scope clarification for predicative/substantivized adjectives; L12 Q3 morphology and L1 Q4 spelling remain unresolved.
- No lesson/quiz/key/runtime/deployment changes, no tests/CI. Archive branch only; main read-only; no separate offsite backup claimed.


## Checkpoint — rationale refinement patch (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_REFINEMENT_PATCH_2026-11-11.md`, blob SHA `2b82d52cd10ef336ccc2455eb7455e21746d9cd4`.
- Patch records 11 refinements to existing rationale proposals plus a source-adjudicated proposed rationale for L10 Q2. The answer remains C (`wê`); rationale distinguishes its paradigm form from its clause role in a transitive past sentence.
- 45 rationale items now have proposed wording across the 44-row base proposal and this delta patch. L12 Q1 and Q3 remain withheld; L1 Q4 notation issue remains open. None approved or applied.
- No lesson, quiz, key, runtime, parser, manifest, database, Botkeep, Telegram or deployment changes; no tests/CI. `main` read-only; GitHub archive is not a separate ZIP/off-site backup.


## Checkpoint — 45 rationale mapping verification (2026-11-11)

- Verification note: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_45_RATIONALE_PROPOSALS_KEY_MAPPING_VERIFICATION_2026-11-11.md`, SHA `6d38e27867915d62dab0fd78140a346e4a67bbaa`.
- Confirmed 44/44 base rationale rows map to the reviewed answer-key rows, with zero missing mappings and zero key-letter mismatches. The refinement patch contributes one additional distinct rationale, L10 Q2 (C / `wê`); its other 11 table rows refine items already in the base set. Total distinct proposed items: 45.
- This is mapping validation only, not linguistic certification or approval. L12 Q1/Q3 remain held; L1 Q4 notation remains open. No lesson, quiz, answer key, runtime or deployment changes; no tests/CI. `main` read-only; no separate offsite backup claimed.


## Checkpoint — explanation-to-option fit audit (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_45_RATIONALE_EXPLANATION_OPTION_FIT_AUDIT_2026-11-11.md`, SHA `5e83fa49f311ff979dc63ea35d5bd6500fa2a8e4`.
- Flagged L8 Q3 as P1: the stem's `bê bireser` does not match the §66 condition described in the rationale (no postnominal descriptive element); this conflates bare clause-level `bireser` with a noun-attached modifier. Requires editorial decision before certifying the rationale.
- Flagged L1 Q1 lexical drift (`qaydeyên` in keyed option vs `rêzikên` in proposal) and L6 Q3 bare `bireser` in stem/options despite full `bireserê navdêrê` rationale. Also retained L5 tewang scope and L10 form/role cautions.
- No proposal approved/applied; no learner-facing or protected files changed; no tests/CI/runtime/deployment. `main` read-only; no separate offsite backup claimed.


## Checkpoint — Lesson 6 / Lesson 8 terminology clarification (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_L6_L8_MODIFIER_TERMINOLOGY_CLARIFICATION_2026-11-11.md`, SHA `5ab9adcaf4a05d30618b16de3dd9ee3f17f90e18`.
- Important refinement: L8 Q3's local “bê bireser” follows the Lesson 8 section's own contrast, so do not label its key wrong on this basis. The ambiguity is cross-lesson: noun-attached `bireserê navdêrê` (L6) versus clause-level `bireser` (L10). Proposed explicit modifier wording in L8 and full compound in L6 Q3 stem, pending editor approval.
- No lesson/quiz/key edits, approval or application. No tests/CI/runtime/deployment; `main` read-only; no separate offsite backup claimed.

- Follow-up rationale proposals for L6 Q3 and L8 Q3 were appended to the clarification artifact, latest SHA `ffc5cea44282a08d32f390bd204c4bcaf6c267ae`. These explain the keyed forms but remain editorial proposals; no quiz/key content changed.


## Checkpoint — L6 Q5 possessive terminology correction (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_L6_Q5_POSSESSIVE_MODIFIER_RATIONALE_CORRECTION_2026-11-11.md`, SHA `f9ec5ed10da96c889393b9ab1502e648b937d380`.
- Corrected a proposal-level terminology error: `min` in `xencera min` is a possessive adjective (`rengdêra xwemalîn`) modifying an expressed noun, not a possessive pronoun (`pronavê xwemalî`) replacing a noun. The latter category applies to forms such as `yê min/ya min/yên min`.
- L6 Q5 key C unchanged. No lesson, quiz, answer-key or runtime edits; no tests/CI/deployment. `main` read-only; no separate offsite backup claimed.


## Checkpoint — controlled terminology final pass (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_45_RATIONALE_CONTROLLED_TERMINOLOGY_FINAL_PASS_2026-11-11.md`, SHA `7f912cbca35233b18df7281c3d685fead169f0ed`.
- Two proposal-level corrections: L6 Q5 `min` in `xencera min` is `rengdêra xwemalîn` (possessive adjective), not `pronavê xwemalî`; L1 Q1 should use `qaydeyên` to match the keyed option.
- No learner-facing/key/lesson/runtime changes; no tests/CI/deployment. `main` read-only; no separate offsite backup claimed.


## Checkpoint — targeted rationale recheck (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_45_RATIONALE_TARGETED_STEM_OPTION_RECHECK_2026-11-11.md`, SHA `47db0bc21ffc740e9c275ab4e2385057753a67eb`.
- Rechecked L8 Q2/Q3 against the quiz and §66/§67; key `-in` remains locally supported while cross-lesson bare `bireser` ambiguity remains. Rechecked L9/L10 form-vs-role, L11 `ko` uses, and L12 Q5 class/function distinction; no new correction found in these selected rows.
- Appended corrected L1 Q1 and L6 Q5 wording to the base 44-row proposal; latest SHA `ccdd1fea505fa354d9c043dd0c010f8fe84faf2a`.
- L1 Q4, L12 Q1 and L12 Q3 remain held. No learner-facing/source/key/runtime changes, no tests/CI/deployment. `main` read-only; no separate offsite backup claimed.



## Checkpoint — early-lessons rationale source recheck (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_EARLY_LESSONS_TARGETED_SOURCE_RECHECK_2026-11-11.md`, SHA `02e8d8db530136ab7e1c2a941e437b5a5f9209d8`.
- Rechecked six rows: L1 Q2, L2 Q2, L3 Q5, L4 Q2/Q5 and L5 Q1. No new key/rationale contradiction or proposal correction was found. L4 `hespek/hespin` remains distinct from inflected `hespan`; L5 Q1's tense/verb-type caveat is grounded in §56.
- This is a targeted tranche, not full independent copy-edit of all 45 items. Held items and proposal-only status remain unchanged. No lesson/key/runtime/deployment changes or tests/CI. `main` read-only; no separate offsite backup claimed.



## Checkpoint — Lessons 2–4 rationale source recheck (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_LESSONS2_4_TARGETED_SOURCE_RECHECK_2026-11-11.md`, SHA `892c51ee24499b7cc696eae367b9314bbe016db7`.
- Ten rows checked (L2 Q1/Q3/Q4/Q5; L3 Q1–Q4; L4 Q1/Q3); no new mismatch or wording correction. L3 `dar` sense distinction and L4 `mehînek` singular paradigm are preserved accurately.
- No lesson/key/runtime/deployment changes or tests/CI. Proposals remain unapproved/unapplied; `main` read-only; no separate offsite backup claimed.



## Checkpoint — Lessons 7–8 rationale source recheck (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_LESSONS7_8_TARGETED_SOURCE_RECHECK_2026-11-11.md`, SHA `0ca63c1a261032d17c859d36a760e8132bfd8759`.
- Four rows checked (L7 Q1/Q5; L8 Q1/Q5); no new correction. Definite suffix inventory, indefinite definition, and §67 `-ine` distribution align with the course draft.
- No source/key/runtime/deployment changes or tests/CI; proposals remain unapproved/unapplied. `main` read-only; no separate offsite backup claimed.



## Checkpoint — Lesson 1 Q3/Q5 rationale source recheck (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_LESSON1_Q3_Q5_RECHECK_2026-11-11.md`, SHA `dfce471ab619202c8f4b307216b649be1de36ffb`.
- Two rows checked: L1 Q3 (`tîp` as written sign, not speech sound) and L1 Q5 (`qiset` formed from `komek` units). Both align; no correction. L1 Q4 remains held.
- No source/key/runtime/deployment changes or tests/CI; `main` read-only; no separate offsite backup claimed.



## Checkpoint — Remaining proposed rationale rows source recheck (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_REMAINING_ROWS_TARGETED_SOURCE_RECHECK_2026-11-11.md`, SHA `bca455a18d0ad6d58d9c4b89dc3f2d327d23a4f7`.
- Sixteen rows checked across Lessons 5, 6, 9, 10, 11 and 12; no new stem/key/source contradiction or proposal correction. Superseding L6 Q5 possessive-adjective wording retained.
- L1 Q4, L12 Q1 and L12 Q3 remain held. No lesson/key/runtime/deployment changes or tests/CI; proposals remain unapproved/unapplied. `main` read-only; no separate offsite backup claimed.


## Checkpoint — Held items exact-stem boundary check (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_HELD_ITEMS_EXACT_STEM_FINAL_BOUNDARY_CHECK_2026-11-11.md`, SHA `2c0337b672f234e93dfe28a9319224c9a128cdc2`.
- L1 Q4 key B remains supported; spelling note `kîtê/kitê` held. L12 Q1 key B remains plausible but needs a non-absolute rationale scope. L12 Q3 category is clear but exact compound morphology remains unresolved. No answer-key change authorized or made.
- No lesson/key/runtime/deployment changes or tests/CI. Holds remain; `main` read-only; no separate offsite backup claimed.


## Checkpoint — Final base-proposal row check (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_L4_Q4_FINAL_ROW_CHECK_2026-11-11.md`, SHA `a56aab12447dcccdaa6add266ee855821cedfd6d`.
- L4 Q4 is aligned: `mêjer` marks singular/plural quantity; `tewang` changes word form according to grammatical role and clause structure. Key B remains supported; no correction.
- Targeted exact stem-option-key-source coverage of the 44 base proposal rows is now complete; L10 Q2 is the separately added 45th rationale and was checked separately. This is not a full native-Kurmanji editorial certification. L1 Q4, L12 Q1 and L12 Q3 remain held.
- No lesson/key/runtime/deployment changes or tests/CI. Proposals remain unapproved/unapplied; `main` read-only; no separate offsite backup claimed.


## Checkpoint — Consolidated 45-item editorial review pack (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_CONSOLIDATED_45_RATIONALE_EDITORIAL_REVIEW_PACK_2026-11-11.md`, SHA `177faaaa5260879bf4b2211474dede013f8d002c`.
- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_CONSOLIDATED_45_PACK_KEY_ALIGNMENT_VERIFICATION_2026-11-11.md`, SHA `3bca6cd89bda8186c8ed52c9b6b2553c7d6093d5`.
- Consolidated pack contains 45 rationale rows (44 base + L10 Q2), with current superseding corrections. A fresh parse confirms 45/45 key-letter matches, no missing rows or duplicates. This validates mapping only, not linguistic correctness.
- L1 Q4, L12 Q1 and L12 Q3 remain held; L10 Q2 needs editorial clarity review. No native-speaker certification, tests/CI, runtime or deployment. No lesson/key changes; `main` read-only; no separate offsite backup claimed.


## Checkpoint — Editorial preflight of consolidated 45 rationales (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_45_RATIONALES_EDITORIAL_PREFLIGHT_2026-11-11.md`, SHA `70e075aaddf5848aee1598e6f59c3e4251a455a5`.
- Three proposed clarity refinements flagged for native-editor review: L2 Q2, L11 Q2 and L10 Q2. Remaining 42 rows had no new concrete correction established in this screening pass.
- L1 Q4, L12 Q1 and L12 Q3 remain held. All proposals remain unapproved/unapplied; no learner-facing or runtime changes and no tests/CI. `main` read-only; no separate offsite backup claimed.


## Checkpoint — Editorial refinements E1–E3 source recheck (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_EDITORIAL_REFINEMENT_E1_E3_SOURCE_RECHECK_2026-11-11.md`, SHA `b5456386a9fd56320eff4e0c8176a8a24433e39f`.
- Source recheck confirms the three clarity refinements for L2 Q2, L11 Q2 and L10 Q2; suggested wording is recorded for qualified editor review only. The answer keys remain unchanged (C).
- This was a focused review of the three flagged items, not a re-adjudication of all 45 rows or native-speaker certification. L1 Q4, L12 Q1 and L12 Q3 remain held.
- No learner-facing, lesson, quiz, answer-key, runtime or deployment files changed; no tests/CI or live runtime checks. `main` read-only; archive branch is not an independent ZIP/offsite backup.


## Checkpoint — Lesson 8 Q3 “bê bireser” terminology boundary (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON8_Q3_BIRESER_TERMINOLOGY_BOUNDARY_RECHECK_2026-11-11.md`, SHA `5c90a8c46cc5ea6758a77c2d045dad6f68fdbfd2`.
- L8 Q3 stem uses “bê bireser”, whereas source §66 says no descriptive/qualifying element follows the noun. This risks conflating `bireserê navdêrê` (L6 noun-complement term) and clause-object `bireser` (L9–10). Key A (`-in`) remains supported; stem refinement is proposed but not applied.
- New review hold added for L8 Q3. Existing L1 Q4, L12 Q1 and L12 Q3 remain open. No lesson/key/runtime/deployment changes or tests/CI. `main` read-only; archive branch is not an independent ZIP/offsite backup.


## Checkpoint — Lesson 10 Q1 paradigm label vs clause role (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON10_Q1_OBJECT_PRONOUN_FORM_VS_CLAUSE_ROLE_RECHECK_2026-11-11.md`, SHA `a639fa4783ecaf31d535b6ca0ed9e43166b1f30c`.
- L10 Q1 key B (`min`) is supported as a member of the course's named paradigm, but the stem wording may be read as syntactic-object function. Lesson examples explicitly distinguish paradigm form from actual clause role. Alternative wording and hold recorded; no key or lesson change.
- New hold L10 Q1 added. Existing L1 Q4, L8 Q3, L12 Q1 and L12 Q3 remain open. No tests/CI or runtime/deployment changes. `main` read-only; archive branch is not an independent ZIP/offsite backup.


## Checkpoint — Lesson 12 Q1 scope and Q3 label morphology (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON12_Q1_Q3_SCOPE_AND_MORPHOLOGY_RECHECK_2026-11-11.md`, SHA `b54353948d19b933b62ddf4cf5a2e04ee0d0b714`.
- L12 Q1: key B remains supported for the wesfîn subtype, but the broad stem asks about the whole adjective class; proposed narrowing the stem to `Rengdêra wesfîn çi dike?`. Hold remains.
- L12 Q3: key A and numeral-adjective category supported by `sê mal`; singular option-label inflection remains unresolved pending native-Kurmanji review. Hold remains.
- Open holds now: L1 Q4, L8 Q3, L10 Q1, L12 Q1, L12 Q3. No tests/CI or runtime/deployment changes. `main` read-only; archive branch is not an independent ZIP/offsite backup.


## Checkpoint — Lesson 6 Q3/Q4 “bireser” term boundary (2026-11-11)

- Created and verified `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_LESSON6_Q3_Q4_BIRESER_TERM_BOUNDARY_RECHECK_2026-11-11.md`, SHA `0788cb3a644cdc3b32c08ee3de4872bb5dc7c7cb`.
- L6 Q3 and Q4 omit `ê navdêrê` from the term although Lesson 6 explicitly warns bare `bireser` can be confused with Lesson 10 clause object. Keys A and B remain supported; stem clarifications proposed, not applied.
- New holds: L6 Q3 and L6 Q4. Current open holds: L1 Q4, L6 Q3, L6 Q4, L8 Q3, L10 Q1, L12 Q1, L12 Q3. No tests/CI or runtime/deployment changes. `main` read-only; archive branch is not an independent ZIP/offsite backup.
