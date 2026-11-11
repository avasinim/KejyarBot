# Course 2 Lesson 12 — Kurmanji orthography and wording audit of the five-question quiz

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** read-only linguistic/editorial audit; no protected wording changed.

## Scope and limits

Reviewed the five stems and all fifteen options in Lesson 12 of `course_data/latin_course_2_reviewed_draft_2026-11-10.md` (blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`), and compared terminology with the reviewed lesson and the existing terminology adjudications. This pass checks internal orthographic consistency, morphology visible in the text, wording, and syntactic parallelism. It is not a substitute for a native Kurmanji copy-edit against the exact printed edition; where a form depends on dialect/editorial convention, it is marked open rather than silently corrected.

## Findings by item

### Q1

Stem: `Rengdêr çi dike?`

- The stem is concise and understandable.
- Option B begins with lowercase `taybetmendî`, while A begins with uppercase `Têkiliya` and C with uppercase `Kes`. This is a visible capitalization inconsistency. If options are sentence fragments, one consistent policy should be selected (normally lowercase fragments); if full sentences, all should be capitalized and punctuated consistently. This is formatting/editorial consistency, not a key error.
- A (`Têkiliya navdêrê bi lêkerê re diyar dike`) is semantically broad and could be read as a syntactic relation description. It is not a precise definition of adjective, but its wording is not simply meaningless. A future editor could make the contrast more explicit; no replacement is authorized here.
- C (`Kes û hejmarê lêkerê li gorî kiryarê diguherîne`) points toward person/number agreement. The term `kiryar` should be checked against the course's intended term for the controller/subject (possibly `kirde` in the course's terminology); do not replace it without checking the glossary and source usage. The wording also deserves a Kurmanji editor's review for idiomaticity.
- B is a noun-phrase fragment while A and C are finite clauses. This makes the correct option visually and syntactically easier to identify. A future patch should make all three options the same grammatical shape (all concise definitions or all parallel fragments).

### Q2

Stem: `mezin di hespê mezin de çi ye?`

- The example `hespê mezin` is internally consistent with the lesson's descriptive-adjective explanation.
- Options `jmarnav`, `pronav`, and `rengdêra wesfîn` are all category labels, so their grammatical shape is reasonably parallel.
- The phrase `rengdêra wesfîn` should be retained as the established current course wording pending the broader singular/plural terminology ruling; do not infer its correctness or incorrectness from Q3 alone.
- No clear spelling error is established in this item. Capitalization style should follow the chosen global option policy.

### Q3

Stem: `sê di sê mal de çi ye?`

- The example is clear: `sê` modifies the expressed noun `mal`.
- Options A and B use `rengdêra ...`, while C is the bare category label `daçek`; this is a mild parallelism difference, though category labels can legitimately differ in morphology.
- The open form `rengdêra jmarîn` must remain unresolved. The lesson heading has `rengdêrên jmarîn`, while the explanatory singular has `rengdêrê jmarîn`. These forms are not interchangeable by assumption. A Kurmanji editor should decide the intended singular label in this exact option context.
- Do not change `jmarîn` to another source variant merely to imitate the source's terminology: the course has adopted its own stable label, and the source/course crosswalk is documented separately.

### Q4

Stem: `Li gorî vê rêbazê, jmarnav di çi awayî de tê pêşkêşkirin?`

- The scope phrase `Li gorî vê rêbazê` is important and should remain.
- A (`di bin pronav de`) and C (`di bin lêker de`) are syntactically parallel to each other: both use the frame `di bin X de`. The earlier distractor audit's phrase “not parallel” was therefore too broad if read as a claim about their surface syntax.
- The real weakness is semantic/category fit: “under a pronoun” and “under a verb” are not meaningful competing classifications for the course's question about whether `jmarnav` is taught as an independent grammatical class. They are grammatical-looking phrases, but weak conceptual alternatives.
- B (`wek beşeke serbixwe`) is a phrase, whereas A/C are locative/prepositional phrases. The forms are not fully parallel as answers to “di çi awayî de”; this is an answer-shape mismatch, not an A-vs-C syntactic mismatch.
- A future approved revision should make all three options answer the same question in the same grammatical form, and should use plausible competing classifications. Do not invent or apply new wording in this audit.

### Q5

Stem: `nîv di beşa jmarnavan de ji bo çi tê bikaranîn?`

- The stem is clear and the answer C (`nimûneyeke jmarnav`) is supported by the lesson's numeral subsection.
- A (`rengdêra wesfîn`) and B (`pronavê kesîn`) are category phrases, while C is a phrase meaning “an example of a numeral”. They are understandable but not perfectly parallel in semantic type: A/B name a category; C names an example's role. The stem asks what `nîv` is used as, so C remains intelligible, but a future editor could make all options category labels or all explanatory descriptions.
- `jmarnavan` in the stem is the plural oblique form used by the lesson in this context; no correction is proposed without the course's declension paradigm review.

## Cross-item orthographic and editorial consistency

1. **Capitalization:** Q1 mixes initial uppercase and lowercase option starts. Other items mostly use lowercase category labels. Adopt one policy for fragments and apply consistently.
2. **Punctuation:** The options are unpunctuated fragments/labels, which is acceptable if consistent. Do not add periods to only some options.
3. **Answer shape:** Q1 mixes a noun phrase with finite clauses; Q4 mixes locative phrases with a predicative/complement phrase; Q5 mixes category labels with an example-description. These differences can cue the key independently of grammar knowledge.
4. **Terminology:** Preserve `rengdêr`, `rengdêrên`, `rengdêra`, `rengdêrê`, `wesfîn`, `jmarîn`, `jmarnav`, and `pronav` as separate recorded forms pending editorial adjudication; do not normalize morphology by visual similarity.
5. **Potential lexical choice:** Q1's `kiryar` requires cross-check against the project's controlled term for grammatical subject/controller. Treat this as a terminology query, not a confirmed typo.
6. **Orthographic evidence:** No unequivocal character-level misspelling (such as a missing diacritic) is established by this text-only comparison. A final copy-edit should compare the exact source edition and the project's Kurmanji spelling policy.

## Recommended future editorial order (approval required)

1. Resolve the Q3 singular label with a Kurmanji editor.
2. Confirm Q1 `kiryar` against the controlled grammar glossary.
3. Standardize capitalization and answer-shape across all options.
4. Redesign Q4 distractors as plausible, same-form grammatical classifications.
5. Consider making Q5 options semantically parallel.
6. Re-run key alignment after any approved wording change; preserve the current key letters unless a substantive concept change requires review.

## Correction to the previous distractor audit

The earlier audit's description of Q4 A and C as “not parallel” needs precision. A and C are parallel in surface syntax (`di bin X de`), but they are weak and semantically ill-fitting category alternatives; the answer set as a whole also mixes those phrases with B's `wek beşeke serbixwe`. This correction does not change the key or authorize an edit.

## Preservation boundary

No question, option, answer, rationale, lesson, source-aligned file, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was changed. No tests/CI or live runtime checks were performed. `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.
