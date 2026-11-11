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
