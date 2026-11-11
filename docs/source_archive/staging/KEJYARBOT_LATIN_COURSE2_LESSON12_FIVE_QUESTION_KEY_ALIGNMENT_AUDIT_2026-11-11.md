# Course 2 Lesson 12 — five-question quiz and answer-key alignment audit

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** read-only verification; no quiz or key edits applied.

## Sources and scope

- Reviewed Lesson 12 draft: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Reviewed answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`, blob SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.
- Direct source page-image review: `KEJYARBOT_LATIN_COURSE2_LESSON12_PAGE_IMAGE_REVIEW_2026-11-10.md`, blob SHA `c712dd136e36154e5314efc65e9f7eef8c9cf4ab`, pp.89–100, §§119–152.
- Terminology adjudication: `KEJYARBOT_LATIN_COURSE2_LESSON12_TERMINOLOGY_ADJUDICATION_2026-11-11.md`, blob SHA `833c34339eb6ae80de339e0d1b7c42b5fa65960b`.

The five question stems, options, answer letters, and answer-text entries were compared against the reviewed lesson's definitions/examples and the page-image review. This is a content/key alignment audit, not a runtime test or independent linguistic peer review.

## Item-by-item result

| Item | Key | Intended concept | Alignment result |
|---|---|---|---|
| Q1 | B | Adjective describes a characteristic/property of a noun | B is the only lesson-aligned option. The stem is a deliberately simplified introductory definition; add a qualification to the lesson definition that descriptive adjectives can also be predicative or substantivized (source §§124–127). This does not invalidate B in the current question's basic framing. |
| Q2 | C | `mezin` in `hespê mezin` is a descriptive adjective | Directly supported by the lesson's descriptive-adjective examples and class definition. |
| Q3 | A | `sê` in `sê mal` is a numeral adjective | Concept and key letter are correct: the noun is expressed and the numeral modifies its quantity. The label text `rengdêra jmarîn` remains a Kurdish morphology/editorial open item against heading `rengdêrên jmarîn` and explanatory singular `rengdêrê jmarîn`. Do not change A or silently normalize its text pending Kurmanji editor review. |
| Q4 | B | Numeral is presented as an independent grammatical class in the adopted course framework | Matches Lesson 12 §8. Preserve the scope marker “Li gorî vê rêbazê” because this is the course's adopted analysis, not a claim that all grammatical traditions classify numerals identically. |
| Q5 | C | `nîv` is an example of a numeral | Supported by the numeral section and source §§146–148, which separately discuss `nîv`, `nîvî`, and `nîvekî). The question asks what `nîv` is used as in the numeral section; C is aligned. |

## Answer-key integrity and rationale quality

- Key letters in the reviewed answer key are Q1=B, Q2=C, Q3=A, Q4=B, Q5=C.
- The answer texts correspond to the keyed option meanings.
- The current rationale column repeats a generic sentence (“according to the question and options”) rather than explaining the grammar. This is not a key mismatch, but it is pedagogically weak. A future approved patch should replace generic rationales with one-sentence reasons:
  - Q1: B states the basic function of an adjective in the lesson's introductory framework.
  - Q2: `mezin` describes the noun `hesp`.
  - Q3: `sê` gives the quantity of the expressed noun `mal`.
  - Q4: the course explicitly teaches `jmarnav` as a separate class.
  - Q5: `nîv` is explicitly listed and discussed in the numeral section.
- This rationale improvement is a proposal only; no answer-key file was changed.

## Disposition

**No keyed-answer contradiction found.** Four items are fully aligned at the concept/label level (Q1, Q2, Q4, Q5); Q3 is conceptually correct but its Kurdish answer-label morphology remains unresolved. No key-letter changes are recommended.

## Preservation boundary

No lesson, quiz, answer key, source-aligned file, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was modified. No tests/CI or live runtime checks were performed. All work remains on `archive/preservation-audit-2026-11-10`; `main` is read-only. GitHub archive history is the persisted record, not a separate ZIP/off-site backup.
