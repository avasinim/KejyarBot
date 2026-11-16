# Course 4 Lessons 32–50 and learner-interface review — 2026-11-16

Branch: `fix/latin-course1-duplicate-note-2026-11-16`
Scope: editorial, scientific-risk, runtime-gating, pagination, and menu review. This is not final academic approval.

## 1. Verified course state

- Course 4 contains 50 ordered lesson IDs (`grammar_01` through `grammar_50`) in the lesson source, curriculum plan, and `courses.json`.
- Lessons 32–50 (19 lessons) are explicitly `owner_review_pending_expanded_draft`.
- Those 19 lessons have no structured quiz; their preserved Markdown drafts are rendered for Beta reading.
- The Beta policy is limited to Course 4 lesson numbers 32–50 with matching IDs and the exact pending-review status. Beta completion is recorded separately and does not grant XP, coins, chests, badges, or official completion.
- Course 4's description in `courses.json` explicitly tells learners that lessons 32–50 are under owner review and have no official quiz/rewards until approval.
- Existing tests cover the 50-lesson sequence, the 19 draft gates, Beta progress isolation, Telegram-safe page lengths, preservation of rendered text order, and page navigation. This is evidence of structural/runtime safeguards, not proof that every linguistic claim or example is correct.

## 2. Scientific and pedagogical observations from the remaining lessons

### Lesson 32 — sentence foundations
The draft makes a useful and necessary distinction between phrase structure (Noun Phrase / Verb Phrase) and grammatical function (Subject / Predicate). It also distinguishes grammatical Subject from semantic Agent and warns that imperative subjects may be unexpressed. Preserve these distinctions in later lessons; do not reduce Subject to “the person who performs the action.”

### Lessons 33–36 — clause functions and sentence constituents
These lessons must be reviewed as a connected sequence: Subject, Predicate, copular constructions, Object, Complement, and Adjunct are not interchangeable labels. The existing Course 4 terminology audit also records the unresolved use of `بکەر` versus `بابەت`; this review does not silently normalize it.

### Lessons 37–38 — sentence types and clause relations
The drafts distinguish simple, compound, complex, and compound-complex sentences by clause structure rather than sentence length or raw verb count. They also distinguish coordination from subordination and warn that words such as `بۆیە`, `هێشتا`, and `کەوایە` cannot all be labelled conjunctions without examining their syntactic role. Keep the distinction, but validate every Sorani example for naturalness and clause boundaries with a competent speaker/editor before approval.

### Lessons 39–46 — extended syntax sequence
The remaining sequence should be checked for dependency and terminology consistency across clause structure, argument functions, word order, topic/focus, and related sentence-level phenomena. In particular, examples that rely on omitted subjects, fronted objects, clitic marking, or dialect-sensitive word order need explicit context and a source or native-speaker validation note. Do not infer a universal Sorani rule from one constructed example.

### Lessons 47–50 — restored source drafts
These are preserved as Markdown source drafts, not as final approved structured lessons. Lesson 50 contains a capstone-style grammatical data-analysis project. Keep the project clearly labelled as a proposed learning activity until the source text, examples, assessment rubric, and terminology have been reviewed. Do not create official quizzes or rewards for these drafts by inference.

## 3. Learner-interface review

### Existing strengths
- Course catalogues are paginated and show lesson numbers, progress/access states, and navigation.
- Beta and pending-review states are visually distinguished from unlocked and completed lessons.
- Course 4 lesson reading uses academic pagination with a Telegram-safe character limit; navigation and the completion action appear only on the final page.
- Reopening a reading page does not resend the lesson image.
- The main menu provides academic lesson search, reducing the need to browse every course page.

### Concrete menu issue to address
The generic course catalogue currently places a separate lesson number before the title, while many lesson titles themselves begin with `وانەی N:`. The button builder then truncates the title to 20 characters. This duplicates the lesson number and can hide the actual topic in the visible button label (especially for Course 4's long titles).

**Recommended presentation correction:** remove the redundant `وانەی N:` prefix from the displayed button title before truncation, retain the stable number shown by the menu, and preserve the full original title in the lesson page. This is presentation-only; lesson IDs, callbacks, sequence, progress records, and content must not change.

A future improvement may use a one-column layout or adaptive row widths for long academic titles, but it should be validated on Telegram clients before replacing the current compact two-column layout.

## 4. Safe next actions

1. Fix the duplicated lesson-number prefix in catalogue labels and add regression tests for Sorani and Latin course titles.
2. Continue source-based review of Lessons 32–50, beginning with Lessons 33–36 and then checking 37–46 as a connected syntax sequence.
3. Verify the exact source and naturalness of every dialect-sensitive example before changing scientific content.
4. Only after review, update approval metadata and quiz availability through a separately reviewed change; do not promote drafts automatically.

## 5. Safety and scope

This audit did not modify lesson content, lesson order, images, credentials, production runtime, SQLite data, or deployment settings. No merge, production deployment, or restart was performed. CI for the current PR head has not been verified; no test success is claimed.

## 6. Catalogue-label fix (implemented in the review branch)

The catalogue label builder now removes a leading numbered lesson prefix in Sorani (`وانەی N:`) and Kurmanji Latin (`Ders N:`) before applying the existing 20-character display limit. The number remains visible in the catalogue's dedicated number field; the complete lesson title and all lesson records remain unchanged. A regression test covers both title forms, a title without a prefix, and unchanged callback IDs.

Implementation commits:
- `efd1605bbedd6080d744e14277d0e3b3675ba2f0` — display-only fix
- `ab3e5848d0d57889eae0fd87d00cfa0184f1f8ae` — regression test

CI workflow runs for the test commit were not returned by GitHub at the time of this update; the test is committed but not yet reported as passing.
