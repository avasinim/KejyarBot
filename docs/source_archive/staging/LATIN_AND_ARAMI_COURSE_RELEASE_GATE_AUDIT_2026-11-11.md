# Latin and Arami course release-gate audit
## 2026-11-11 | Append-only source-backed finding
Candidate inspected: `botkeep-menu-clean-2026-11-09`

### Kurmanji Latin Courses 1 and 2
- `latin_course_runtime.py:load_latin_courses()` loads 12 lessons per course and five quiz questions per lesson, validates contiguous numbering, exactly 60 answer-key rows per course, unique option labels/options, and answer-key-to-source-option agreement.
- The loader explicitly sets every generated lesson record to `review_status=draft_editorial_review`.
- `course_data/latin_courses_manifest_draft.json` sets both course manifests to `status=draft`.
- However, the main `courses.json` catalogue registers both course IDs as `active`; startup validation requires them active and loaded. This is a direct catalogue-vs-source-manifest mismatch.
- `bot.py:lesson_is_pending_review()` recognizes only the exact Course 4 status `owner_review_pending_expanded_draft`; `lesson_quiz_is_available()` does not block Latin `draft_editorial_review`.
- `quiz_requires_submission()` explicitly includes both Latin course IDs. Their quizzes therefore use the standard interactive quiz path if the course is catalogue-active.
- The lesson completion path and quiz result path use ordinary reward functions for non-beta lessons. No general editorial-draft reward gate is present.
- Structural parsing and answer-key consistency are useful safeguards but do not certify the Latin source interpretation, Kurdish orthography, morphology, or dialect suitability.
- Release blocker: keep both Latin courses hidden/read-only until explicit owner/editorial approval, or define and test a beta-without-rewards policy. Do not silently change manifest status or academic review status.

### Arami Course 1
- Manifest declares 21 lessons, all marked `user_supplied_immutable` for their source provenance.
- Lesson 1 has a dedicated source content record and validated practice/assessment bank; Lesson 5 has separate runtime helpers and interaction bank.
- Manifest statuses for Lessons 2–4, 6–13, and 17–21 are `source_review_pending`; Lessons 14–16 are received/preserved statuses rather than explicit academic approval.
- The runtime loader's manifest checks lesson count, unique IDs, source path containment, source file presence, and question-bank structural/evidence requirements for the banks it loads. It does not turn a received source into academic approval.
- The inspected manifest maps Lesson IDs 17–21 to filenames whose embedded source numbers appear to be 16–20 respectively (e.g. ID 17 points to `...lesson_16_v_source.md`, ID 18 to `...lesson_17_he_e_source.md`, ID 19 to `...lesson_18_k_g_mukriani_source.md`, ID 20 to `...lesson_19_cluster_source.md`, ID 21 to `...lesson_20_syllable_cluster_source.md`). This may be intentional legacy numbering or a mapping defect; verify file headings and content before changing anything.
- The startup validation inspects the dedicated Lesson 1 and Lesson 5 interaction assets and manifest shape; it does not establish full academic approval or fully interactive assessment coverage for all 21 lessons.
- Release blocker: preserve all user-supplied source unchanged; verify ID-to-source mapping, and explicitly distinguish delivered/read-only lessons from approved interactive lessons. Do not activate source-review-pending content as reward-bearing learning.

### Cross-course conclusions
- Course catalogue `active` is not a sufficient release-readiness signal.
- For all unapproved statuses, policy must be enforced at lesson opening, quiz start/submission, finish callback, progress persistence and reward issuance; UI-only hiding is insufficient.
- Maintain independent namespaced lesson IDs and progress ledgers; no migration or renaming of existing learner records during this audit.

### Non-actions
No source text, manifest, runtime code, quiz, reward logic, DB, Botkeep configuration, or course activation was changed. No merge, deploy, import, restore, restart, or Railway activation was performed.
