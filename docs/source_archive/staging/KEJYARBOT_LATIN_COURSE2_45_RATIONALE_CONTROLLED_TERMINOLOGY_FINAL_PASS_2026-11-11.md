# Course 2 — Controlled terminology final pass for 45 rationale proposals
**Date:** 2026-11-11  
**Status:** Editorial audit only; no wording approved or applied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## 1. Scope

Cross-checked the 44-row base proposal and its 11-row refinement / L10 Q2 addition against:
- reviewed Course 2 lessons and quiz options;
- reviewed 62-row answer key;
- master terminology register;
- cross-lesson terminology chain audit;
- held-item source adjudication;
- L6/L8 modifier clarification and L6 Q5 possessive-modifier correction.

This pass focuses on exact controlled labels, not a new grammar/source-page adjudication.

## 2. Findings

### P1 — L6 Q5: possessive adjective vs possessive pronoun

The refinement patch had called `min` in `xencera min` a `pronavê xwemalî`. The course itself distinguishes:
- `rengdêrên xwemalîn`: possessive adjectives modifying an expressed noun, e.g. `hespê min`;
- `pronavên xwemalîn`: forms such as `yê min/ya min/yên min` replacing an understood noun/group.

The correction is documented in:
`KEJYARBOT_LATIN_COURSE2_L6_Q5_POSSESSIVE_MODIFIER_RATIONALE_CORRECTION_2026-11-11.md`, SHA `f9ec5ed10da96c889393b9ab1502e648b937d380`.

**Controlled form for L6 Q5 proposal:** `min` is `rengdêra xwemalîn` in `xencera min`, while the whole construction is an instance of the broader Lesson 6 noun-attached modifier function `bireserê navdêrê`.

### P2 — L1 Q1: retain the keyed term

The keyed option uses `qaydeyên rastaxaftin û rastnivîsandina ziman`; the first proposal uses `rêzikên`. These are near-synonymous in broad meaning, but the course's answer-specific rationale should echo the exact keyed lexical head unless the glossary/editor explicitly authorizes a change.

**Preferred proposal wording:**
> Gramêr tevahiya qaydeyên rastaxaftin û rastnivîsandina ziman e. Vebijarka A tenê aliyê deng û derxistina dengên ziman digire, û C jî tenê avakirina peyvan; her du jî ji pênaseya firehtir a dersê tengtir in.

### P2 — L6 Q3 and L8 Q2/Q3: preserve phrase-level distinctions

- L6 Q3 must retain full `bireserê navdêrê` in its rationale; bare `bireser` can be read as clause-level object elsewhere in the course.
- L8's local `bê bireser` follows its own §66/§67 section wording, but cross-lesson it is ambiguous. The terminology clarification proposes “`bê hêmaneke raveker li pey navdêrê`” (pending editorial approval). This does not invalidate key `-in`.
- Do not globally replace clause-level `bireser` in Lessons 9–10 or `pronavên bireser`.

### Stable distinctions confirmed in the proposal set

- `mêjer` vs `tewang`: number vs inflection.
- `kirar` / `bireser`: clause roles, with construction-sensitive form/role mapping.
- `forma kirarî` / actual clause role: do not infer syntactic role from paradigm label alone (`min`, `wê`).
- `veqetandek` / `pêvek`: specific determiner label vs broader affix term; preserve the register's review status.
- `rengdêr` / `bireserê navdêrê`: word class vs broader noun-attached function.
- `rengdêrê jmarîn` / `jmarnav`: numeral adjective with noun vs independent numeral class.
- `ko` relative-pronoun use vs conjunction use: preserve the separate Lesson 11 question contexts; do not claim `ku` universally wrong.

## 3. Held items remain held

- L1 Q4: `kîtê/kitê` orthographic status unresolved.
- L10 Q2: source supports the paradigm form `wê`; rationale must preserve form-vs-role distinction; wording review remains.
- L12 Q1: adjective definition scope requires lesson/quiz review.
- L12 Q3: `rengdêra jmarîn` vs `rengdêrê jmarîn` unresolved.

## 4. Consolidated disposition

1. Apply the L6 Q5 terminology correction to the proposal patch only when preparing a clean editorial draft; do not leave the superseded `pronavê xwemalî` wording as the active recommendation.
2. Use `qaydeyên` in L1 Q1 rationale to match the keyed option.
3. Retain full `bireserê navdêrê` for L6 Q3 and the cross-lesson caution for L8.
4. Preserve all unresolved items without manufacturing a ruling.
5. Before any answer-key update, perform a single final native-Kurmanji copy-edit over all 45 proposed rationales, then compare each against the exact stem, option text and key row once more.

## 5. Validation and preservation

This pass is a controlled-terminology audit of staged documents. It does not independently certify all 45 rationales or every key. No lesson, quiz, answer-key, source transcription, runtime, parser, manifest, database, Botkeep, Telegram or deployment file was changed. No tests/CI, runtime checks, learner-response analysis or psychometric validation was performed. No proposal was approved/applied. `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup; no separate backup is claimed.
