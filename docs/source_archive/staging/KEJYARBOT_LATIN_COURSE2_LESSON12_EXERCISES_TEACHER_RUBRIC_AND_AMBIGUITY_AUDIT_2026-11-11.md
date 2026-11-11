# Course 2 Lesson 12 — exercise teacher rubric and ambiguity audit

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** teacher-facing proposal only; no lesson or exercise wording changed.

## Evidence and scope

Reviewed the staged Course 2 Lesson 12 exercise text and source-aligned version. The exercise sequence contains:
- Xebata 1: classify 13 noun groups/forms as adjective type or `jmarnav`.
- Xebata 2: write one additional example for each adjective type.
- Xebata 3: explain the difference between numeral adjective and `jmarnav` in one sentence.

The lesson teaches six adjective classes: descriptive (`wesfîn`), demonstrative (`îşarkî`), numeral (`jmarîn`), interrogative (`pirsiyarkî`), indefinite (`nebinavkirî`), and possessive (`xwemalîn`). It separately presents `jmarnav` in the adopted course framework.

## 1. Xebata 1 — provisional teacher rubric

The following is a proposed marking guide, not a claim that every item has only one possible analysis in all grammatical frameworks.

| Item | Provisional expected classification | Teaching reason / caution |
|---|---|---|
| `hespê mezin` | `mezin`: descriptive adjective (`wesfîn`) | Describes the quality/size of the expressed noun `hesp`. |
| `ev keçik` | `ev`: demonstrative adjective (`îşarkî`) | Modifies the expressed noun; contrast with independent `Ev hat.` |
| `sê mal` | `sê`: numeral adjective (`rengdêra jmarîn`) | Numeral directly modifies the expressed noun `mal`. |
| `kîjan mirov` | `kîjan`: interrogative adjective (`pirsiyarkî`) | Asks which person and modifies `mirov`. |
| `hin çiya` | `hin`: indefinite adjective (`nebinavkirî`) | Indicates an unspecified quantity/group of mountains. |
| `hespê min` | `min`: possessive adjective (`xwemalîn`) in the course's noun-modifier analysis | Expresses possession/association with the noun; distinguish this use from independent `yê min`. |
| `mehînên te` | `te`: possessive modifier (`xwemalîn`) | Possessive relation to the expressed plural noun; verify the intended inflection/idiom with a Kurmanji editor. |
| `kurên van` | **Needs teacher clarification** | `van` follows the noun and may be read as an independent demonstrative/genitive possessor (“sons of these [people/things]”), not straightforwardly as an adjective modifying `kur`. Do not force it into `îşarkî` without the intended syntax/context. |
| `tu mirov` | `tu`: indefinite adjective (`nebinavkirî`) in the intended “any/no particular person” reading | Provide a sentence context; isolated `tu` may invite alternative readings. |
| `gelek fêkî` | `gelek`: indefinite/quantifying adjective (`nebinavkirî`) | Indicates an unspecified large quantity. |
| `vî hespî` | `vî`: demonstrative modifier (`îşarkî`), oblique form | The case form is contextual; the phrase alone does not explain why oblique is selected. |
| `van hespan` | `van`: demonstrative modifier (`îşarkî`), oblique plural form | Same issue: teacher key should state the relevant oblique context or simply test recognition of the demonstrative form. |
| `nîv roj` | **Ambiguous without a declared analysis level** | `nîv` is introduced among `jmarnav` examples, but here it modifies an expressed noun. The rubric must state whether learners classify lexical class (`jmarnav`) or phrase-level function (numeral modifier/adjective). Do not mark either framework-based answer wrong until the course owner chooses the intended criterion. |

### Xebata 1 marking recommendation

Use two columns in the teacher key: (a) target word/form and (b) category **plus one-line reason**. For `kurên van` and `nîv roj`, accept no single fixed key until the syntax/context and classification level are clarified. Add a sentence context for `tu mirov`, `vî hespî`, and `van hespan` if the purpose is to assess interpretation rather than memorization of labels.

## 2. Xebata 2 — coverage and success criteria

Current instruction: write one additional example for every adjective type.

It implicitly requires six examples, but does not state the count or quality criteria. Proposed teacher rubric:
1. Six examples, one for each of the six named classes.
2. Each example includes an expressed noun, so the adjective's modifying role is visible.
3. The target form is marked and the class named.
4. Examples are original and not copied from the lesson list.
5. Demonstrative, interrogative, indefinite, and possessive examples must be used attributively with a noun, not as independent pronouns.
6. For descriptive adjectives, an ordinary quality/property example is sufficient; degree formation is not required unless separately requested.

This clarifies marking without requiring a change to learner-facing wording. A future wording revision could explicitly say “six examples, one for each class,” but it remains unapproved.

## 3. Xebata 3 — one-sentence distinction rubric

A complete one-sentence response should contain both sides of the contrast:
- Numeral adjective: a number modifies an expressed noun, e.g. `sê mal`.
- `jmarnav`: in the course's adopted taxonomy, a numeral is presented as an independent grammatical class/use rather than as an adjective attached to an expressed noun.

Proposed model answer:
`Di “sê mal” de “sê” navdêra “mal” diyar dike û rengdêra jmarîn e; lê jmarnav di vê rêbazê de wek beşeke serbixwe tê pêşkêşkirin.`

This preserves the scope marker `di vê rêbazê de`; it does not claim that all linguistic frameworks classify numerals identically. A Kurmanji editor should review the sentence's idiomaticity before adoption.

Suggested marking: 1 point for identifying the expressed noun relation in the first clause; 1 point for identifying the independent class/use in the second clause; 1 point for making the contrast explicit and correctly scoped to the course framework.

## 4. Decisions needed before any learner-facing edit

1. Decide the intended syntactic reading of `kurên van`; as written, it is not a clean attributive demonstrative example.
2. Decide whether `nîv roj` is being classified by lexical category or by its modifying function in the noun phrase.
3. Add teacher context for `tu mirov` and oblique demonstratives if interpretation is assessed.
4. Confirm `mehînên te` idiomaticity and morphology with a Kurmanji editor.
5. Decide whether Xebata 2 explicitly requires six examples.
6. Have a Kurmanji editor review the proposed Xebata 3 model answer.

## 5. Preservation and disposition

- These are provisional teacher-facing classifications; flagged forms are intentionally left unresolved.
- No learner-facing wording, source lesson, exercise, quiz, answer key, or key letter was modified.
- No runtime, parser, tests, manifest, database, Botkeep, Telegram, or deployment file was changed.
- No tests/CI or live runtime checks were performed. `main` remains read-only.
- Work remains on `archive/preservation-audit-2026-11-10`. GitHub archive history is not a separate ZIP/off-site backup.


## Addendum — revised exercise adjudication after source-to-terminology cross-check (2026-11-11)

**This addendum supersedes only the provisional dispositions for `kurên van` and `nîv roj` in section 1 above.** The original audit is retained as an append-only record of the earlier uncertainty.

### A. Stable classification language for the teacher key

Use the six top-level class labels exactly as the lesson does:

- `wesfîn` — descriptive
- `îşarkî` — demonstrative
- `jmarîn` — numeral
- `pirsiyarkî` — interrogative
- `nebinavkirî` — indefinite
- `xwemalîn` — possessive

Keep the levels distinct in every answer: (1) word class, (2) subclass, (3) syntactic function/use, and (4) surface form. The six labels are the course taxonomy; `rêzîn` is an ordinal subtype within numeral adjectives, not a seventh top-level class. Adjectives may also be predicative or substantivized, so “an expressed noun is present” is a diagnostic for attributive use, not a universal definition of every adjective.

### B. Xebata 1 — updated rows

| Item | Course-intended classification | Required explanation / marking note |
|---|---|---|
| `kurên van` | `van`: possessive element under `xwemalîn`, following the lesson's explicit example list | The lesson itself places `kurên van` and `keçên wan` in its possessive-adjective examples. Do not mark it as `îşarkî` solely because the surface form resembles a demonstrative. Precise syntax and idiomaticity remain flagged for Kurmanji editor review; avoid using it as a high-stakes diagnostic until reviewed. |
| `nîv roj` | `nîv`: `jmarnav` under the lesson's own lexical taxonomy | State the second level too: in this noun phrase it quantifies/modifies the expressed noun `roj`. Do not relabel it as one of the six adjective subclasses merely because it has a noun-modifying phrase function. |

All other rows in the original table remain provisional as previously stated. In particular, retain the context caveats for `tu mirov`, `vî hespî`, and `van hespan`, and the Kurmanji morphology/idiomaticity review for `mehînên te`.

### C. Xebata 2 — six-class coverage without category/function conflation

The six-example criterion remains: one original noun phrase for each of the six named adjective classes. Ask learners to underline the target modifier, identify its class, and show the noun it modifies. For the numeral-adjective example, require a stated noun (e.g. course pattern `sê mal)); do not use an independent `jmarnav` as a substitute. This is a proposed marking interpretation; learner-facing instruction has not been changed.

### D. Xebata 3 — sharpened marking rubric

The model answer remains:

`Di “sê mal” de “sê” navdêra “mal” diyar dike û rengdêra jmarîn e; lê jmarnav di vê rêbazê de wek beşeke serbixwe tê pêşkêşkirin.`

Mark separately for:
1. recognizing that `sê` modifies the expressed noun `mal`;
2. naming its course class as numeral adjective (`jmarîn`);
3. stating that `jmarnav` is presented as a separate/independent class in this course framework.

The sentence is explicitly scoped to the adopted course taxonomy, not claimed as a universal analysis across all linguistic frameworks. Kurmanji copy-edit remains necessary before adoption.

### E. Editorial hold points

- Keep `rengdêra jmarîn` (quiz Q3 option) vs `rengdêrê jmarîn` (singular explanatory prose) unresolved pending a Kurmanji editor's decision; preserve plural class heading `rengdêrên jmarîn`.
- Do not globally normalize source/course crosswalks: `wesfîn` ↔ source `çilobûn û çawabûnê`; `xwemalîn` ↔ `destdaniyê/xwedîtiyê`; `rêzîn` ↔ `rêzda`; source comparison records `jmarda` for adjective numerals.
- These are teacher-facing rubric clarifications only. No learner-facing wording, source lesson, quiz, answer key, or runtime file is changed by this addendum.


## Addendum — all 13 Xebata 1 items: class, function, form, and context audit (2026-11-11)

This is a teacher-facing audit of the complete exercise list in the reviewed Lesson 12 source (blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`). It distinguishes the course-intended category from phrase function and surface morphology. It is not a universal grammar ruling and does not alter learner-facing material.

### Full 13-item adjudication

| # | Exercise form | Course-intended class / label | Function and form observation | Disposition |
|---:|---|---|---|---|
| 1 | `hespê mezin` | `mezin`: `wesfîn` | Postnominal descriptive modifier in an ezafe-linked noun phrase; describes `hesp`. | **Stable for course key.** |
| 2 | `ev keçik` | `ev`: `îşarkî` | Demonstrative modifier with an expressed feminine singular noun; compare independent `Ev hat.` | **Stable for course key.** |
| 3 | `sê mal` | `sê`: `jmarîn` (numeral adjective) | Cardinal numeral modifies the expressed noun `mal`; the noun's form is the relevant phrase context. | **Stable for course key.** |
| 4 | `kîjan mirov` | `kîjan`: `pirsiyarkî` | Interrogative determiner/modifier before an expressed noun. The sentence context determines whether the whole phrase asks “which person”. | **Stable for course key.** |
| 5 | `hin çiya` | `hin`: `nebinavkirî` | Indefinite/quantifying modifier before an expressed plural noun. | **Stable within course taxonomy.** |
| 6 | `hespê min` | `min`: `xwemalîn`, in the lesson's adopted analysis | Possessive relation follows the noun through the ezafe construction; `min` is the oblique personal-pronoun form. Do not describe it as an ordinary inflecting adjective without qualification. | **Course key may use `xwemalîn`; terminology/editor review needed** on whether to call the element a possessive modifier, pronoun, or possessive construction. |
| 7 | `mehînên te` | `te`: intended `xwemalîn` | Possessive relation to the expressed plural noun; `te` is an oblique personal-pronoun form. Number/ezafe agreement and idiomaticity need a fluent Kurmanji review. | **Provisional; hold as diagnostic until editor review.** |
| 8 | `kurên van` | `van`: intended `xwemalîn`, explicitly listed by the lesson | The source lesson itself groups this form with possessive examples. Surface `van` also has demonstrative uses elsewhere, so the answer key must state the intended possessive construction rather than infer class from form alone. Exact syntax/idiomaticity needs editor review. | **Provisional course-intended answer; not a high-stakes item pending review.** |
| 9 | `tu mirov` | `tu`: intended `nebinavkirî` | The isolated phrase is context-sensitive: `tu` can be read as the second-person singular pronoun in other environments. The intended indefinite reading must be demonstrated by a full sentence or discourse context. | **Do not use as a stand-alone diagnostic; add context or accept only with stated intended reading.** |
| 10 | `gelek fêkî` | `gelek`: `nebinavkirî` in the lesson | Indefinite quantity/degree modifier before the expressed noun. It can also be used pronominally in other sentence positions, as the lesson itself notes. | **Stable for this attributive phrase; context needed for other uses.** |
| 11 | `vî hespî` | `vî`: `îşarkî`, oblique masculine singular form | Demonstrative form accompanies `hesp); the oblique case is not explained by the two-word fragment alone. | **Class stable; add a governing sentence/context if testing case selection.** |
| 12 | `van hespan` | `van`: `îşarkî`, oblique plural form | Demonstrative form accompanies the plural noun; oblique environment is not recoverable from the fragment alone. | **Class stable; add a governing sentence/context if testing case selection.** |
| 13 | `nîv roj` | `nîv`: `jmarnav) under the lesson's lexical taxonomy | The lesson specifically preserves `nîv` before a noun. In this phrase it quantifies/modifies expressed `roj`; that phrase function does not convert the course lexical label into one of the six adjective subclasses. | **Course-intended answer: `jmarnav`; state function separately.** |

### What the exercise currently tests—and what it does not

- It can test recognition of the six course adjective subclasses and the course's separate `jmarnav` category.
- It does **not** consistently test sentence-level interpretation: several prompts are fragments, not full clauses.
- It mixes clear attributive examples (`hespê mezin`, `ev keçik`, `sê mal`, `kîjan mirov`, `hin çiya`, `gelek fêkî`) with possessive ezafe constructions and oblique demonstrative forms whose full syntax is not shown.
- It should not simultaneously grade category recognition, case selection, and idiomaticity when the prompt supplies no governing context.
- In particular, `tu mirov`, `mehînên te`, and `kurên van` should be held from high-stakes use until context and Kurmanji editorial review settle their intended reading.

### Teacher-key format recommended for all 13 rows

Use four explicit fields: (1) target word/form, (2) course class, (3) phrase/sentence function, and (4) context or editorial caveat. Where the lesson's own taxonomy supplies the intended label, mark it as “course-intended” rather than presenting it as a universally agreed grammatical category.

### No-edit disposition

This addendum is an audit-only classification matrix. It does not change the 13 learner prompts, lesson source, quiz, answer key, key letters, runtime, parser, tests, manifest, database, Botkeep, Telegram, or deployment. No tests/CI or live runtime checks were performed. `main` remains read-only; GitHub archive history is not an independent ZIP/off-site backup.


## Addendum — Xebata 2 and Xebata 3 coverage and marking audit (2026-11-11)

### Source reviewed

- Reviewed draft: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`, Lesson 12 lines 525–625.
- Source-aligned lesson collection: `course_data/latin_course_2_source_aligned_lessons_01_12.md`, blob SHA `19090077a11dc9d7211987e958e560b328fcd3d6`.
- The exercise wording is preserved exactly in the reviewed draft:
  - Xebata 2: “Ji bo her cureya rengdêrê yek nimûneya din binivîse.”
  - Xebata 3: “Rengdêrê jmarîn ji jmarnav cuda bike û bi yek hevokê cudahiya wan rave bike.”

### Xebata 2 — six-class coverage and marking rule

The prompt is underspecified: “her cureya rengdêrê” does not explicitly state the number of examples, identify the six top-level classes, or say that each example must contain an expressed noun. In context, the intended criterion should be six new examples, one for each top-level class:

1. `wesfîn`
2. `îşarkî`
3. `jmarîn`
4. `pirsiyarkî`
5. `nebinavkirî`
6. `xwemalîn`

Do not count `rêzîn` as a seventh top-level class: in this course it is an ordinal subtype discussed within `jmarîn`. A learner may choose an ordinal example for the `jmarîn` row if the noun is expressed and the ordinal relationship is clear, but that does not create an additional class row.

Recommended teacher marking protocol (audit recommendation, not learner-facing revision):

- Require six examples total, one per class, and require a noun to be expressed in each phrase so that the target is demonstrably used attributively in the course's teaching framework.
- Mark each row on four dimensions: (a) target word/form is identifiable; (b) intended class is correct; (c) the noun is expressed; (d) the phrase is grammatically well formed and meaningfully interpretable.
- Do not accept a bare numeral as a numeral-adjective example when the task is specifically testing `jmarîn`; distinguish `sê mal` from independent/substantive `jmarnav` use.
- Do not mark a correct class label wrong merely because the learner uses a different valid lexical example. Conversely, a correct-looking label does not rescue a phrase whose syntax or meaning is unclear.
- Avoid double-counting a single example for two classes. If a form is context-sensitive (especially possessive or demonstrative forms), request a complete phrase or sentence rather than infer the intended reading from the isolated form.
- The lesson's source examples may be used as teaching references, but Xebata 2 asks for “nimûneya din” (another example); exact copying of the lesson's listed examples should not earn full originality credit.

The current prompt does not specify whether examples must be phrases or full sentences. For a low-stakes practice task, well-formed noun phrases can suffice; where case, agreement, or a context-sensitive reading is being assessed, require a sentence that supplies the governing context. Do not silently impose sentence-level case testing on the current wording.

### Xebata 3 — conceptual distinction and model response

The task asks for one sentence. The core distinction in the lesson is relational/function-based, not merely a difference in the numeral's written form:

- `rengdêra jmarîn`: a numeral/ordinal functioning with an expressed noun and specifying its number or order (e.g. `sê mal`, `stûna çaran`).
- `jmarnav`: the separate numeral category in the lesson's adopted taxonomy, used independently/substantively rather than directly modifying an expressed noun.

A compact provisional model response, retained for teacher use and pending Kurmanji copy-edit:

`Di “sê mal” de “sê” navdêra “mal” diyar dike û rengdêra jmarîn e; lê jmarnav di vê rêbazê de wek beşeke serbixwe tê pêşkêşkirin.`

Mark the response for three required ideas: (1) the numeral-adjective example has an expressed noun; (2) the numeral specifies that noun; (3) `jmarnav` is presented separately/independently in the course framework. The answer should not claim that every numeral form is inherently an adjective or inherently a `jmarnav`; syntactic use and relation to an expressed noun determine the intended course distinction.

The model response is a single sentence with coordinated clauses, so it meets the prompt's “one sentence” constraint. Accept an equivalent accurate sentence; do not require verbatim reproduction. If a learner gives only definitions without an example or without the expressed-noun contrast, mark the distinction incomplete.

### Editorial and scope cautions

- Preserve the exercise's exact phrase `Rengdêrê jmarîn` in this audit. The singular morphology remains an open editorial query against `rengdêra jmarîn` in the quiz and `rengdêrên jmarîn` as the plural class heading. No normalization is authorized here.
- The exercise is a practice prompt, not a full assessment of all six classes unless the teacher applies the six-row rubric above.
- The six-class framework is course-internal. This audit does not claim that the same labels or boundaries are universal across all Kurmanji grammatical traditions.
- These are teacher-facing clarifications only. No learner-facing exercise, lesson, quiz, answer key, terminology register, runtime, parser, tests, manifest, database, Botkeep bot, Telegram bot, or deployment file was changed. No tests/CI or live runtime checks were performed. `main` remains read-only; the archive branch is not an independent ZIP/off-site backup.
