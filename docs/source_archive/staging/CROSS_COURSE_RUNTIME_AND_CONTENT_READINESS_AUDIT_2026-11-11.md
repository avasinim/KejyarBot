# Cross-course runtime and content readiness audit
## 2026-11-11 | Append-only | Candidate ref: botkeep-menu-clean-2026-11-09

### Catalogue inventory
The candidate `courses.json` registers:
- Arami Course 1 (`arami_orthography_foundations`): 21 lessons, active.
- Daily Conversation Course 2 (`daily_conversation`): 42 lessons, active.
- Unified Orthography Course 3 (`unified_orthography`): 66 lessons, active.
- Grammar Course 4 (`grammar`): 50 lessons, active with beta gates.
- Kurmanji Latin Orthography Course 1: 12 lessons, active in catalogue.
- Kurmanji Latin Grammar Course 2: 12 lessons, active in catalogue.
- Legacy orthography_basic: retired and replaced by Arami Course 1.

### Arami Course 1
- Dedicated Telegram module exists: `arami_course1_telegram.py`.
- Manifest requires exactly 21 lessons and validates lesson numbering.
- Lesson 1 has dedicated presentation and interaction bank: 5 practice + 5 assessment questions.
- Lesson 2–21 use a shared source reader / lesson-scoped practice and assessment architecture.
- Manifest marks Lesson 2 as source-review-pending and user-source immutable; its separate source texts must not be merged without owner direction.
- A 21-lesson catalogue registration is not equivalent to proof that all 21 source texts, question banks, and reward/completion flows have passed end-to-end tests.
- No evidence in this audit that Arami Course 1 data was changed by PR #125; its module appears in the PR diff and requires regression testing.

### Daily Conversation Course 2
- Four data files contain lesson ranges 01–06, 07–30, 31–36, and 37–42 (42 lessons total).
- Inspected sample records show `review_status: draft_editorial_review`; review findings remain on some lessons.
- Course catalogue marks the course active, but lesson records are still draft editorial review. This is a release/readiness mismatch that must be reconciled before describing all 42 lessons as academically approved.
- Dialogue, vocabulary, exercises, quiz, comprehension, and role-play fields are present in inspected records; full record-by-record content validation and Telegram flow regression remain required.

### Unified Orthography Course 3
- One data file `unified_orthography_lessons_01_66.json` contains 66 lessons.
- Course catalogue marks it active.
- This audit did not yet complete a full per-lesson review-status, quiz-bank, source-alignment, and end-to-end runtime validation. Do not infer full readiness from lesson count or catalogue status.
- PR #140 is a separate draft for Course 3 lessons 67–68; it is not part of the 66-lesson catalogue and must not be promoted with the current release.

### Kurmanji Latin courses
- Catalogue registers 12 lessons in each of two Latin courses.
- `latin_courses_manifest_draft.json` labels both course manifests as draft, despite catalogue status active.
- Source-aligned lesson documents and review/answer-key drafts exist in `course_data`, but the draft manifest and content status need reconciliation before release.
- The 2026-11-11 archive branch contains preservation PRs #142–#144; these are archive records, not evidence of runtime activation.

### Runtime isolation / regression gates
- `course_runtime.py` uses namespaced lesson IDs for new courses and preserves legacy Course 1 keys.
- It provides ordered unlock checks and filters catalogue lessons to loaded lesson data.
- Before promotion, run end-to-end tests for each course's lesson loading, locked/unlocked sequencing, quiz submission, progress persistence, badges/rewards, and cross-course ID isolation.
- Explicitly test retired `orthography_basic` handling and ensure existing legacy progress is not renamed or lost.
- Test the exact release candidate with the preserved Botkeep test DB only in a disposable copy; do not migrate the live DB during audit.

### Release blockers / non-actions
- Resolve Course 4 Lesson 13 status/gate inconsistency in the separate finding.
- Reconcile active catalogue flags with draft/source-review-pending lesson/manifest statuses for Courses 1, 2, and Latin courses.
- Complete full record-level Course 3 and Course 2 audits.
- Botkeep Node17 staging recovery confirmation remains required before any import/restore/deploy attempt.
- Rotate the exposed Telegram token before further user-facing tests.
- No merge, deployment, Botkeep import/restore/restart, Railway activation, database write, or live course change was performed during this audit.
