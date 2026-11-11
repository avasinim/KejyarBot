# Course 2 — 62-question distractor-quality and Kurdish orthography review

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Reviewed quiz blob:** `abc88219e2a0e249883e8d62c5117a9b3aaa3108`  
**Reviewed answer-key blob:** `879e1525e720bdc25b8f6e896de3e388801238d0`  
**Scope:** read-only editorial review of the staged Course 2 quiz and lesson text. No lesson, quiz, answer-key, runtime, manifest, database, Botkeep, Telegram, or deployment file was changed.

## 1. Review method and limits

All 62 quiz questions across Lessons 1–12 were reviewed against the corresponding lesson's definitions, examples, terminology, and keyed answer. The review assessed: (a) whether each distractor represents a recognizable misconception or contrast; (b) whether the stem gives enough grammatical context to make one answer clearly best; (c) whether distractors are parallel and non-duplicative; and (d) consistency of Kurmanji Latin orthography and terminology in the staged lesson text.

This is an editorial quality pass, not a new primary-source collation, dialect survey, psychometric item analysis, or runtime test. No learner-response data is available, so distractor performance cannot be measured empirically. The reviewed artifacts remain staging drafts.

## 2. Overall result

- **62/62 questions reviewed.**
- Most items have one answer supported by the lesson and distractors that test a relevant contrast.
- No evidence was found in this pass of a second correct option in the 62 items as currently keyed.
- Three questions need wording/terminology attention before any future approval: **Lesson 6 Q3**, **Lesson 10 Q1**, and **Lesson 10 Q2**.
- **Lesson 8 Q5** has weak, non-parallel distractors and should be improved.
- A script scan of the Latin-course lesson draft found **three unintended mixed-script lines** in Lesson 8's explanatory prose. The Kurdish-Arabic-script course header and bot signatures are intentional and were not counted as errors.
- No answer letter is recommended to change on the evidence reviewed. The proposed changes are stem/distractor refinements only, subject to separate approval.

## 3. Item-by-item distractor review

| Lesson | Questions | Result |
|---:|---:|---|
| 1 | Q1–Q5 | Acceptable. Options distinguish grammar from phonetic/word-structure subsets, written sign from speech sound, meaningful word from syllable/group, and group-combination from letter/syllable repetition. Beginner-level recall is appropriate here. |
| 2 | Q1–Q5 | Acceptable. Distractors contrast noun with verb/adjective, common with proper noun, and the intended general-name function. The examples `Ferzane`, `Kejyar`, and `Argesh` are marked in the lesson as added teaching examples. |
| 3 | Q1–Q5 | Acceptable. The alternatives test the two-gender inventory and grammatical rather than biological gender. Some count questions are simple recall, but they are not ambiguous. |
| 4 | Q1–Q5 | Acceptable. The alternatives test number, singular/plural forms, and the distinction between inflection and number. `hespin` is keyed consistently with the lesson's indefinite plural example. |
| 5 | Q1–Q5 | Acceptable. The tense and noun-gender/number conditions in Q2–Q4 are sufficiently restricted; the distractors represent plausible wrong forms or wrong grammatical categories. Preserve the present-tense wording. |
| 6 | Q1–Q2, Q4–Q5 | Acceptable. The alternatives test noun modification versus sentence function, identify the head noun, and distinguish a noun modifier from pronoun/verb categories. |
| 6 | Q3 | **Revise stem terminology.** The current stem asks “Di `hespê beza` de bireser çi ye?” The lesson explicitly distinguishes `bireserê navdêrê` (noun modifier) from sentence-role `bireser` (object). The abbreviated `bireser` reintroduces the ambiguity the lesson warns against. Recommended stem: “Di koma navdêrî `hespê beza` de, kîjan hêman `bireserê navdêrê` ye?” Keep the keyed option `beza` unless source review indicates otherwise. |
| 7 | Q1–Q5 | Acceptable. The three suffixes are tested within the definite-determiner paradigm, and the stems explicitly identify that system. |
| 8 | Q1–Q4, Q6–Q7 | Acceptable with ordinary beginner-level recall. The items distinguish indefinite from definite forms, the three suffix environments, and the oblique paradigm. Retain the distinction between `-ine` and `-ên`. |
| 8 | Q5 | **Improve distractors.** The current options “erê”, “her tim”, and “na, erkên wan cuda ne” make A and B near-duplicate affirmative responses; “her tim” is not a useful grammatical misconception. Keep C as the keyed answer, but replace A/B with parallel, concept-based confusions—for example, one claiming both are definite forms and another claiming both are the same indefinite paradigm. Ensure neither replacement can be read as correct. |
| 9 | Q1–Q5 | Acceptable. The agent forms are consistently framed within past transitive clauses in Q1–Q4; Q5 checks the second-person plural form against other persons. |
| 10 | Q1 | **Add sentence context.** The current stem asks “Kîjan yek ji pronavên bireser e?” and keys `min`. The lesson itself warns that forms such as `min` are not permanently subject or object: their clause role depends on construction. Without a sentence, this wording can be read as assigning `min` an invariant object role. Recommended: ask which form fills the object slot in a concrete present-tense sentence, e.g. “Di hevoka dema niha de `Tu ___ dibînî`, kîjan pronav li cihê bireserê tê?” Then retain `min` as the answer if the intended sentence is verified. |
| 10 | Q2 | **Specify the construction.** “Forma bireserî ya `ew` mê çi ye?” keys `wê`, but `wê` also appears as the inflected agent in past-transitive clauses elsewhere in the course. Add a concrete object context (for example, the present-tense frame `Ez ___ dibînim`) or explicitly state the relevant object paradigm. Retain `wê` only after the stem's intended construction is explicit. |
| 10 | Q3–Q5 | Acceptable. The reciprocal forms, object role in `Wan ew xwar`, and source-limited “du an sê kes” definition are aligned with the lesson. Do not broaden the reciprocal scope without fresh source verification. |
| 11 | Q1–Q5 | Acceptable. The items distinguish demonstrative, relative, and interrogative forms; Q4's full sentence disambiguates conjunction `ko` from relative `ko`. |
| 12 | Q1–Q5 | Acceptable. The items distinguish descriptive adjectives, numeral adjectives, and the separately taught numeral category. The stem on `nîv` is supported by the lesson's own examples. |

## 4. Orthography and script findings

A Unicode-script scan of the reviewed Latin-course lesson draft (`course_data/latin_course_2_reviewed_draft_2026-11-10.md`, 651 lines, blob SHA above) found three lines in Lesson 8's Latin explanatory prose that mix Latin Kurmanji with Persian/Arabic-script fragments:

- **Line 290:** `formên serەکی yên` — the word `serەکی` is mixed-script. Use a consistent Kurmanji Latin form such as `sereke` in the phrase `formên sereke yên ...`.
- **Line 292:** the sentence beginning `Dema zêتر لە yek pêvek...` contains multiple Arabic-script fragments (including `zêتر`, `لە`, `گرێدرا`, `پێکهاتە`, `وەک`, and `نەک`). Rewrite the whole sentence in Kurmanji Latin rather than transliterating fragments one by one.
- **Line 294:** `Sê pêکهاتەy` and the remainder of the sentence contain mixed-script fragments. Rewrite the whole note in consistent Kurmanji Latin; preserve its intended meaning that the three suffix patterns are distinct and are not interchangeable.

The two Kurdish-Arabic-script introductory lines and the twelve `کەژیار` bot-signature lines are intentional; they are not Latin-course orthography errors.

Other orthographic consistency observations:
- Preserve diacritics and letters in established forms, including `î, ê, ş, ç, x, û`; do not normalize them to unaccented ASCII.
- Keep grammatical forms visually distinct and consistently backticked: `-ek/-ek/-in`, `-ekî/-eke/-ine`, `-î/-e/-en`, `-ekî/-ekê/-ina`, and definite `-ê/-a/-ên`.
- Keep the terminology distinction `bireserê navdêrê` versus sentence-role `bireser` throughout the lesson and quiz.
- Preserve `ko` as the course's chosen form in this source scope; do not silently substitute `ku` without an explicit source/standardization decision.
- Capitalization at sentence starts and within tables should be normalized in a later copy-edit pass, but no capitalization-only issue was judged to alter an answer in this review.

## 5. Recommended editorial patch queue (not applied)

1. Lesson 6 Q3: restore the full term `bireserê navdêrê` in the stem.
2. Lesson 8 Q5: replace the two weak affirmative distractors with parallel, paradigm-based misconceptions; keep the correct answer concept unchanged.
3. Lesson 10 Q1–Q2: add explicit sentence/tense context so object function is not confused with the past-transitive agent/object alternation.
4. Lesson 8 explanatory prose, lines 290, 292, 294: rewrite the three mixed-script lines in consistent Kurmanji Latin.
5. Conduct a final terminology/orthography sweep after the above changes and re-run the structural comparison of quiz and key.

These are recommendations only. The reviewed quiz, answer key, source-aligned originals, runtime, tests, manifests, database, Botkeep, and Telegram were not modified. No tests or CI were run. No runtime, live-bot, or deployment status is claimed.

## 6. Preservation note

This report is a new append-only staging artifact on `archive/preservation-audit-2026-11-10`. It does not replace prior structural or pedagogical reports. The reviewed lesson and answer-key blob SHAs were rechecked before this review and remain the versions identified above. The original content and all prior commits remain preserved in Git history.
