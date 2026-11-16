# Kurmanji Latin Course 2 — Lessons 1–12 editorial recheck (2026-11-16)

Status: **structural and internal-consistency review; not final academic approval**.
Branch: `fix/latin-course1-duplicate-note-2026-11-16`.
Source document: `course_data/latin_course_2_source_aligned_lessons_01_12.md`.
Answer key: `course_data/latin_course_2_quiz_answer_key_draft.md`.
Runtime loader: `latin_course_runtime.py`.

## Verified structure

- The source document has exactly 12 ordered lesson headings (1–12).
- The runtime loader requires 12 lessons for this course, each with five parsed MCQs.
- The answer key contains 60 unique lesson/question rows (five for each lesson).
- The loader checks that each key's answer letter and answer text match the corresponding option in the lesson; it rejects missing rows, duplicate options, non-contiguous option labels, and wrong answer text.
- All lesson content remains `draft_editorial_review`; these checks do not certify the linguistic correctness of the source analysis or examples.
- Course 2 remains source-separated from Course 1; its loader reads the Part II document, not a concatenated master.

## Corrections already recorded on this branch

1. Course 1 Lesson 2's exact duplicated editorial note was reduced to one occurrence; a regression test guards this.
2. Course 2's noun `mehîn` was normalized to preserve the long-vowel letter `î` in 28 source-document occurrences and the single corresponding answer-key occurrence; a regression test guards the spelling.

## Lesson-level review observations

### Lesson 4–5: number and oblique forms

The lessons explicitly distinguish the non-oblique plural `hespin` from oblique `hespan`, and distinguish `mehînin` from oblique `mehînan`. The examples and quiz are internally aligned after the `mehîn` spelling correction. Keep number and oblique case separate; do not generalize one ending as the universal plural marker.

### Lesson 11: the two uses of `ko`

The lesson and quiz distinguish the relative pronoun in `Yê ko hat bira yê min bû` from the conjunction in `Min got ko ez nayêm`. The answer key records the latter as `gihanek`. A runtime regression test checks this distinction. Do not collapse the two functions into one label.

### Lesson 12: adjectives and numerals

The lesson presents six adjective classes, including numeral adjectives, and then gives `jmarnav` a separate section as an independent category. Its quiz likewise calls `sê` in `sê mal` a `rengdêra jmarîn`, while describing `jmarnav` as a separate part of speech and using `nîv` as an example.

This may reflect a distinction in the source's grammatical framework, but the boundary between `rengdêrên jmarîn` and `jmarnav` should be checked against the exact source pages before approval. No automatic rewrite is safe: it could erase a source-specific distinction or create a contradiction. Keep Lesson 12 in editorial review until that mapping is explicit.

## Remaining review work

1. Compare each lesson's terminology and examples with the corresponding printed pages of Part II (pp. 37–100); structural checks alone do not establish source fidelity.
2. Resolve the Lesson 12 distinction between numeral adjectives and numerals using the source's own definitions and examples.
3. Review the Kurmanji terminology for gender, number, case, oblique forms, ezafe, pronouns and verbal morphology as one connected sequence.
4. Check every MCQ for one unambiguously correct answer in the intended grammatical framework, not merely a matching answer-key row.
5. Keep all lessons in draft status until source-based and linguistic review is complete.

## Safety and scope

This review did not change production runtime behavior, Telegram credentials, SQLite data, deployment configuration, image assets, lesson order, or user progress. No deployment or merge was performed. CI for the current PR head has not been verified; no test success is claimed.
