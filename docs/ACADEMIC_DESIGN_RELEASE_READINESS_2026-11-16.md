# Academic, pedagogical, and learner-interface release readiness — 2026-11-16

Branch: `fix/latin-course1-duplicate-note-2026-11-16`
Purpose: consolidate the current source-backed content and presentation state before any production activation or Telegram acceptance test.
This is an audit and release gate, not scientific approval of every lesson.

## Executive decision

**Do not promote all catalogued courses to academically approved status.** The runtime catalogue currently marks six course entries as `active`, but this field means the course route is present in the bot; it does not mean every lesson has passed scientific/editorial review. Keep the existing lesson-level review gates and Beta boundaries intact.

A controlled Telegram smoke test is a separate engineering check. It can verify menus, lesson delivery, pagination, callbacks, progress isolation, and media delivery; it cannot certify linguistic accuracy.

## Current course state

| Course | Content inventory | Review evidence | Release interpretation |
|---|---|---|---|
| 1 — Arami/Sorani orthography foundations | 21 lessons; user-supplied source texts preserved; reader/practice/assessment routes enabled in text mode | Lesson 1 has a dedicated interaction bank (5 practice + 5 assessment); Lesson 5 has a dedicated reader/interaction flow; remaining lessons use the shared source reader and lesson-scoped question bank. The manifest marks the sources as user-supplied and generally preserves them without scientific edits. | Existing course route may be smoke-tested as implemented. Do not rewrite owner-supplied wording or claim external academic validation. Check each source/quiz pair against the owner's supplied text. |
| 2 — Daily conversation | 42 lessons, 306 dialogue turns, 87 MCQs; vocabulary, exercises, comprehension, role-play for each lesson | All 42 remain `draft_editorial_review`. Lesson 2 origin/residence mismatch was corrected to ask residence when the answer states residence. | Runtime route exists; editorial/naturalness review is still required before calling the course final. |
| 3 — Unified orthography | 66 lessons, 201 MCQs; source book/page references, exercises and quizzes | All 66 remain `draft_editorial_review`. Structural audit confirms numbering and quiz metadata only, not sentence-level source fidelity. | Keep text-only presentation; no lesson images/infographics. Do not call the course scientifically approved. |
| 4 — Grammar | 50 lessons | Lessons 1–30 have qualified scientific review notes; Lesson 31 is an internal cross-lesson synthesis without external source mapping; Lessons 32–50 are owner-review Beta drafts. Beta lessons have no structured quiz or official rewards. | Preserve official/Beta separation. Resolve owner terminology choices before normalization. |
| 5 — Kurmanji Latin orthography | 12 lessons, 60 questions | Source-aligned draft; all content remains `draft_editorial_review`. Parser validates five MCQs per lesson and exact answer-key alignment. | Do not promote to academically approved until page-by-page source and native-language review is complete. |
| 6 — Kurmanji Latin grammar foundations | 12 lessons, 60 questions | Source-aligned draft; all content remains `draft_editorial_review`. Source book explicitly omits several grammar domains, so it is a foundations course, not a complete grammar. | Keep scope accurately described; Lesson 12 numeral-adjective vs numeral distinction remains unresolved against the source. |

## High-priority scientific/editorial issues

### Course 1
- Preserve the user's supplied text exactly where its manifest says immutable; do not silently import an external source or normalize examples.
- Keep distinctions among grapheme, phoneme, vowel/consonant, and orthographic symbol explicit.
- The supplied source texts and practice/assessment banks must be checked lesson-by-lesson against each other. Existing activation metadata proves the Telegram route is wired, not independent academic validation.
- Keep the eight-vowel explanation for Lesson 1 as owner-confirmed; do not replace it with an external count without explicit review.

### Course 2
- Review each dialogue for natural Sorani syntax, register, speaker consistency, and pragmatic appropriateness; a structurally valid dialogue may still sound translated or unnatural.
- Ensure every MCQ tests the lesson's stated communicative function, not merely memorization of one phrase.
- Role-play tasks should specify a realistic communicative goal and an observable completion condition.
- Keep the known Lesson 2 residence/origin correction; continue checking similar semantic mismatches between question and reply.

### Course 3
- Keep the written wordmark «کەژیار» first, followed by lesson number/title; use consistent section hierarchy: objective, key points, examples, exercises, comprehension, quiz.
- Preserve right-to-left ordering and Kurdish punctuation in Telegram; validate actual split/pagination boundaries and avoid separating a question from its options.
- Clearly distinguish examples quoted/adapted from the fourth edition of «پوختەی ڕێنووس و خاڵبەندی» from newly authored practice examples.
- Human review remains open for Lesson 1 compound-word scope; Lesson 35's U+200C treatment; Lessons 51–62 source examples versus supplementary examples; and the specificity/usefulness of practical tasks.
- No images or infographics are required or approved for this course.

### Course 4
- Preserve phrase structure versus grammatical function; Subject must not be reduced to semantic Agent.
- Keep Subject, Predicate, Object, Complement, and Adjunct distinct; distinguish sentence types by communicative purpose from sentence types by clause structure.
- Validate Sorani examples involving omitted subjects, fronted objects, clitics, and dialect-sensitive word order with a competent native-language reviewer and source evidence.
- Owner decisions remain open for Enclitic (`پاشبەستە` / `پاشنووس`), Noun Phrase (`گرێی ناوی` / `گروپی ناوی`), and Subject (`بکەر` / `بابەت`). Do not mass-replace these.
- Lessons 32–50 remain Beta only, with no official quiz or rewards until approved.

### Courses 5–6
- Verify every Kurmanji example against the exact cited printed page, preserving the distinction between non-oblique and oblique forms and between different grammatical functions.
- Resolve Course 6 Lesson 12's numeral adjective versus numeral category boundary from the source's own definitions; do not guess.
- Keep Course 6 labelled as grammar foundations because the cited source omits verbs, adverbs, prepositions, syntax, and other domains.

## Presentation and Telegram UX release checklist

- [ ] Every course menu button exposes the lesson topic without a duplicated lesson-number prefix.
- [ ] Full lesson title remains visible on the lesson page even when the menu label is truncated.
- [ ] Kurdish Arabic-script and Kurmanji Latin-script text retain correct direction, punctuation, diacritics, and glyphs.
- [ ] Headings and section order are consistent within each course, while preserving source-specific structures.
- [ ] Long lessons split at safe paragraph/list/question boundaries; options and explanations remain attached to their question.
- [ ] Back/next/catalogue callbacks preserve the correct course, lesson, page, and learner progress.
- [ ] Text-only lessons remain fully usable when optional media is absent.
- [ ] Only the approved seven PNG assets are packaged; no audio, PDF, JPG, or legacy SVG is added to runtime.
- [ ] No Course 3 image or infographic is created or attached.
- [ ] A Telegram smoke test records exact course, lesson, page, callback, and expected result; visual appearance is checked on desktop and mobile Telegram.

## Activation and deployment gates

1. Do not change `review_status` or `curriculum_state` merely because a course has `status: active` in `courses.json`.
2. Do not promote Course 2 or Course 3 to scientifically approved status while all lessons remain in editorial review.
3. Keep Course 4 Lessons 32–50 in Beta; do not add official quizzes, XP, coins, chests, badges, or official completion.
4. Keep Latin courses as source-aligned drafts until source-page and linguistic review is complete.
5. PR #161 is still Draft and not merged/deployed. The Altare app has `AUTO_UPDATE=0`; repository commits do not by themselves update the live bot.
6. The project owner has explicitly confirmed that the bot is empty and no learners have used it. There is no learner database to recover, migrate, or preserve for this activation; do not spend time on learner-data restoration or request learner records.
7. A fresh empty SQLite database created by the normal startup path is acceptable for this first activation. The only database-related check is that the bot can initialize its own empty database at the intended writable runtime path; this is not a blocker requiring a recovery workflow.
8. After the approved revision is on the deployment branch and runtime files/configuration are verified, the owner can perform one controlled restart and a limited Telegram smoke test. No existing learner records are at risk because none exist. Do not test destructive operations against future real learner accounts.

## Verification boundary

This document consolidates repository records and current branch metadata. It does not claim that all lesson examples have been scientifically checked, that all course designs have been visually tested on Telegram clients, that the current PR is deployed, or that Altare's persistent SQLite database has been recovered and verified.

No production runtime, SQLite database, Telegram credential, Altare setting, schedule, start, or restart was changed for this audit.


## Owner clarification — learner-data scope (2026-11-16)
The project owner explicitly corrected the earlier operational assumption: KejyarBot is an empty/new bot and has never been used by learners. There are no learner records that need backup, migration, restoration, or preservation before first activation. Any prior release checklist that treated recovery of an existing learner database as a hard gate does not apply to this first activation. This clarification changes only the release checklist; it does not authorize touching unrelated database files or making production changes without the owner's requested restart/deploy sequence.
