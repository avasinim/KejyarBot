# Course 4 — Non-quiz Whole-Phrase Basten Review (Round 62)
Date: 2026-11-10
Branch: `botkeep-menu-clean-2026-11-09`
Source path: `course_data/grammar_course4_lessons.json`
Source SHA verified before review: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
Round60 proposal SHA: `1316073488bf38f022d7044cb3415c457640ebeb`

## Scope and result
- Reviewed all 26 non-quiz paths from the 35-entry Round60 shortlist.
- 24 paths: the proposed whole-phrase substitution is contextually and grammatically acceptable as a terminology-only proposal.
- 2 paths: held for manual whole-sentence revision because the proposed local replacement leaves a mixed or incomplete use of the legacy term.
- No source JSON was edited. No quiz path was in scope. No answer key, runtime, database, Botkeep, Telegram, deployment, or merge action was taken.

## Path-by-path decisions

| Round60 item | Lesson / exact path | Decision | Review note |
|---:|---|---|---|
| 1 | 3 · `key_points[12]` | Accept proposal | The phrase refers to the semantic/pragmatic conditions under which a bare noun may express an indefinite/general quantity; `بەستێن` is appropriate. |
| 2 | 3 · `appendix[17]` | Accept proposal | Classification of lexical items is explicitly said not to be identical in every usage context; the replacement preserves this meaning. |
| 3 | 5 · `key_points[1]` | Accept proposal | The noun's abstract/concrete interpretation is context-dependent; `بە پێی بەستێن` is appropriate. |
| 4 | 7 · `examples[1][1]` | Accept proposal | The note describes a context-sensitive relational adjective example; no semantic shift detected. |
| 6 | 8 · `key_points[7]` | Accept proposal | Gradability of absolute/ classifying adjectives is context-sensitive; replacement is suitable. |
| 7 | 8 · `exercises[4]` | Accept proposal | The exercise asks learners to judge natural gradability in an ordinary usage context; the phrase remains grammatical. |
| 9 | 9 · `key_points[0]` | Accept proposal | Independent use of numerals is conditioned by context; replacement preserves the intended linguistic sense. |
| 10 | 9 · `key_points[10]` | Hold — manual revision | The first phrase can become `لە بەستێنێکی تایبەتدا`, but the same sentence later retains `بەبێ سیاق`. This leaves terminology inconsistent and the second phrase should be revised in the same sentence. Suggested wording for review: `بەبێ بەستێنی بەکارهێنان و ڕستەی نموونەیی`. Do not apply automatically; check the intended examples and dialect evidence before final wording. |
| 11 | 9 · `examples[4][1]` | Accept proposal | The grammatical category of the final element in compounds is said to depend on use context; replacement is semantically apt. |
| 12 | 10 · `examples[3][1]` | Accept proposal | The pronoun `ئەو` is resolved by its antecedent in the preceding discourse; `بەستێن` is appropriate here. |
| 15 | 11 · `examples[2][1]` | Accept proposal | The possessive reading of `ـیان` is explicitly contrasted with the transitive-past subject marking analysis; the context phrase is apt. |
| 16 | 12 · `examples[1][1]` | Accept proposal | The sentence's two readings (subject clitic vs possessive clitic) are distinguished through context; replacement preserves the contrast. |
| 17 | 12 · `appendix[2]` | Accept proposal | Same two-reading ambiguity is explicitly tied to the sentence's intended meaning and context; replacement is appropriate. |
| 18 | 13 · `key_points[5]` | Accept proposal | The interpretation of `دەـ` as present, habitual/repeated, or future depends on context; replacement is appropriate. |
| 20 | 15 · `key_points[1]` | Accept proposal | The past continuous/habitual form may describe ongoing or repeated past events in a particular context; replacement is appropriate. |
| 21 | 15 · `key_points[9]` | Accept proposal | The distinction between simple and perfect past is not invariant across contexts; replacement preserves the claim. |
| 22 | 15 · `appendix[1]` | Accept proposal | The interpretation of `دەخوێند` as flow, habit, or repetition is context-dependent; replacement is suitable. |
| 23 | 16 · `objective` | Accept proposal | The objective concerns interpreting present/future readings of the `دەـ` form through context; replacement is apt. |
| 24 | 16 · `comprehension[0]` | Accept proposal | Duplicates the same objective wording; the same decision applies. |
| 26 | 17 · `key_points[1]` | Accept proposal | The addressee and generalized-instruction readings of imperative forms are usage-context dependent; replacement is suitable. |
| 27 | 21 · `key_points[3]` | Accept proposal | The syntactic function of a locative element is context-dependent; replacement is suitable. |
| 28 | 21 · `activities[1]` | Accept proposal | The activity asks learners to evaluate competing analyses in context; replacement is suitable. |
| 30 | 23 · `appendix[5]` | Accept proposal | The form and syntactic arrangement of the coordinated negation may vary with context; replacement is suitable. |
| 31 | 26 · `key_points[2]` | Accept proposal | The diagnostics for discourse particles are explicitly defeasible and context-sensitive; replacement is suitable. |
| 32 | 27 · `key_points[8]` | Hold — manual revision | The proposal changes only the first `لە سیاقێکدا` but leaves `لە سیاقێکی دیکەدا` in the same contrastive sentence. Revise the pair together, e.g. `لە بەستێنێکدا ... و لە بەستێنێکی دیکەدا`, after checking that the examples really contrast two usage contexts. |
| 34 | 31 · `comprehension[0]` | Accept proposal | The final statement denies that every infinitive is a regular noun in every usage context; replacement is suitable. |

## Held items — required before any source patch
1. **Lesson 9 — `key_points[10]`:** resolve both `لە سیاقێکی تایبەتدا` and `بەبێ سیاق` in one coherent sentence. The suggested wording above is provisional, not an approved source edit.
2. **Lesson 27 — `key_points[8]`:** revise both sides of the contrast consistently (`بەستێنێک` / `بەستێنێکی دیکە`) rather than replacing only one occurrence.

## Terminology boundary
This review treats `بەستێن` as the linguistic context of interpretation/use. It does not authorize blanket replacement of semantic compounds or of references that actually mean a real-world situation (`بارودۆخ`) or adjacent textual material (`دەوروبەری دەق`). Each such case requires a concept-level decision.

## Integrity and change control
- Source SHA at review start: `fd8dfbde7e6937841214cacac653ef10d0c6097d`.
- This report records review decisions only; no source file was written or rewritten.
- Round60's nine quiz paths remain governed by the separate Round61 quiz semantic/answer-integrity review.
- The 24 accepted items are proposals eligible for a later reversible patch and regression test, not a claim of final dialect-wide validation.
- The two held items must not be auto-applied.
- No PR merge, deployment, Botkeep or Telegram operation was performed.
