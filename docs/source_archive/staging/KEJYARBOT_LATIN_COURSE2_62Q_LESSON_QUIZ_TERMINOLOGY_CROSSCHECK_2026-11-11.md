# Course 2 — 62-question lesson/quiz terminology cross-check

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** read-only audit; all proposed edits remain unapplied.

## 1. Scope and baselines

This pass compares every quiz stem and option in the reviewed 12-lesson draft with its lesson explanation, the reviewed answer-key entry/rationale, and the master terminology register.

- Reviewed lesson + embedded quiz: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`
  - blob SHA: `abc88219e2a0e249883e8d62c5117a9b3aaa3108`
- Reviewed answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`
  - blob SHA: `879e1525e720bdc25b8f6e896de3e388801238d0`
- Master terminology register:
  - blob SHA: `08423c8bf0a44f5b3b5efe28f531a41f81b5fed8`

Coverage is 62 questions: Lessons 1–7 and 9–12 have five each; Lesson 8 has seven. The reviewed key contains 62 corresponding rows. The earlier structural verification found no missing, orphaned, duplicated, or answer-text-mismatched key rows. This pass is a terminology/teaching-alignment review, not a fresh runtime test or psychometric assessment.

## 2. Lesson-by-lesson result

| Lesson | Questions checked | Cross-check result |
|---:|---:|---|
| 1 | Q1–Q5 | Aligned: `gramêr`, the four course units, `tîp` as written sign (not sound), `bêje`, and `qiset` as broader discourse are consistent with the lesson's distinctions. |
| 2 | Q1–Q5 | Aligned: `navdêr`, `hevenav`, and `serenav` are used consistently; the added names are explicitly identified as teaching examples. |
| 3 | Q1–Q5 | Aligned: the two grammatical genders and the `dar` meaning distinction follow the lesson; grammatical gender is not confused with biological sex. |
| 4 | Q1–Q5 | Aligned: `mêjer`, `yekjimar`, `gelemjimar`, and the example `hespin` match the stated indefinite paradigm. |
| 5 | Q1–Q5 | Aligned: `tewang` is distinguished from number; Q2–Q4 explicitly restrict the noun forms to the present-tense examples, consistent with the lesson's warning about past transitive clauses. |
| 6 | Q1–Q5 | Q1, Q2, Q4, Q5 align. **Q3 needs the already-proposed terminology repair:** it says bare `bireser` for `beza` in `hespê beza`, while the lesson calls this a `bireserê navdêrê`. The bare form risks confusion with clause-level object `bireser`. |
| 7 | Q1–Q5 | Aligned: all three definite forms `-ê/-a/-ên` are identified within the definite-determiner paradigm and are not conflated with noun inflection. |
| 8 | Q1–Q7 | Q1, Q2, Q4, Q6, Q7 align with the stated indefinite paradigms and environments. **Q3 needs more exact wording:** `bê bireser` is not the lesson's label for the §66 environment, which is “without a following descriptive/modifying element after the noun”; the bare term `bireser` is also used for clause-level object. Prefer a stem that repeats the lesson's precise condition, e.g. `bê pêvekeke raveker li pey navdêrê`. **Q5** retains the previously identified weak, near-duplicate affirmative distractors; the proposal to replace A/B while retaining C remains pending. |
| 9 | Q1–Q5 | Aligned: the agent forms `min/te/wî/me` are explicitly limited to past transitive clauses; `hon` is retained as the source form. |
| 10 | Q1–Q5 | Q3–Q5 align, including the source-limited reciprocal scope and the contextual object in `Wan ew xwar`. **Q1–Q2 need the already-proposed sentence frames:** the current stems risk treating `min` and `wê` as invariant object forms. The source-supported present-tense frames `Tu min dibînî` and `Tu wê dibînî` make the syntactic role observable. |
| 11 | Q1–Q5 | Aligned: `ko` as relative form in Q3 is kept distinct from `ko` as conjunction in the full sentence in Q4. No global `ko/ku` substitution is recommended. |
| 12 | Q1–Q5 | Q1, Q2, Q4, Q5 align with the lesson's adjective/numeral distinction. **Q3 is pending terminology adjudication:** `rengdêra jmarîn` is used in the quiz/key, while the lesson's source-category heading and register preserve `rengdêrên jmarîn`; the lesson prose also varies between singular/construct forms. Do not normalize until a Kurmanji language editor confirms the intended singular/construct form. |

## 3. Consolidated findings and proposed queue

### A. Question wording that should be revised in a future dated patch

1. **L6 Q3 — full noun-modifier term.** Use `bireserê navdêrê` in the stem, not bare `bireser`. The existing proposed wording is:
   `Di koma navdêrî `hespê beza` de, kîjan hêman `bireserê navdêrê` ye?`
   Keep answer A (`beza`) unless a separate source-based reason emerges.
2. **L8 Q3 — name the §66 environment.** Replace `bê bireser` with the lesson's exact condition, such as `bê pêvekeke raveker li pey navdêrê`. This avoids confusion between absence of a following modifier and the clause-level object role.
3. **L8 Q5 — improve distractor quality.** The current A/B options are near-duplicate affirmative answers. The existing proposal uses two distinct false conflations (both definite / both indefinite) and retains C as the only correct answer. This remains pending.
4. **L10 Q1–Q2 — expose syntactic context.** Use the source-backed frames `Tu min dibînî` and `Tu wê dibînî`, respectively. The proposed answer letters remain B and C in the current proposed option order.

### B. Terminology decision — do not auto-edit

- **L12 Q3:** the form `rengdêra jmarîn` needs a language-editor decision against the source heading `rengdêrên jmarîn` and the reviewed lesson's singular/construct variation. The concept is correctly distinguished from `jmarnav`; the open issue is the preferred Kurdish grammatical form of the label.
- **L6 lesson glossary:** the paired label `pêşnavdêr/bireser` remains unresolved in the lesson/register. The quiz cross-check does not authorize collapsing it into a single category.
- **L8 lesson prose:** the base draft still contains mixed-script lines 290, 292, and 294. In addition, its current line 292 summary needs to preserve the source distinction between §68's final-noun agreement and §69's each-linked-complement rule. The source-checked replacement is already in the proposal, not in the protected lesson base.
- **`pêvek` / `veqetandek`:** preserve the current broad/specific distinction until the glossary definition is approved; no blanket substitution.
- **`ko` / `ku`:** preserve source- and function-specific usage; no global spelling normalization.

## 4. Answer-key and preservation status

- The reviewed answer-key baseline remains 62 rows and is unchanged.
- Existing key letters for the proposed edits remain L6 Q3=A, L8 Q5=C, L10 Q1=B, L10 Q2=C. The proposed wording edits do not authorize changing these letters; revalidate against the final option order if a future patch is approved.
- No lesson, embedded quiz, answer key, source-aligned original, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was changed.
- This audit is append-only and does not approve or apply any proposed edits.
- No tests/CI were run, no live runtime was checked, and no deployment was performed. `main` remains read-only.
- GitHub archive branch history is the persisted project record; this is not a separate ZIP or independent off-site backup.

## 5. Next safe action

Prepare a new dated patch copy only after the wording is reviewed, including L8 Q3 alongside the already-proposed L6/L8/L10 changes. Keep all current baselines untouched, then rerun the 62-question/key structural comparison and a terminology/script scan on the new copy.
