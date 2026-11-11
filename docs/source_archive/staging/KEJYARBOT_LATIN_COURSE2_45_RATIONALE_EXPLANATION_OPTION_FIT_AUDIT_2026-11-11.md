# Course 2 — 45 rationale explanation-to-option fit audit
**Date:** 2026-11-11  
**Status:** Editorial audit only; no proposals approved or applied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## 1. Scope and sources

This pass checks whether the proposed rationale text explains the keyed option in the actual quiz context, whether its terminology matches the stem/options, and whether it gives enough contrast to make the answer educationally useful. It is not a fresh source-page audit or a validation of all underlying answer keys.

Reviewed:
- Base 44-rationale proposal, SHA `133c9105a9a3315ceed3d5e2d84d69bf1d472b28`.
- Rationale refinement patch, SHA `a38d463ab2683762d879a45a21678602aaa280ab`.
- Reviewed quiz/lesson draft, SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Reviewed answer key, SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.

The base set has 44 items; the patch refines 11 of those and adds L10 Q2. Thus 45 distinct items have proposed rationale wording. This audit covers those proposed rows and records the held items separately.

## 2. Overall result

- The proposed rationales generally identify the intended concept and keyed option.
- No new key-letter mismatch was found in the prior 44/44 mapping verification.
- The main risk is not answer-letter association but **construct/term alignment**: one question uses `bireser` where the explanation and lesson paradigm require the notion “a postnominal descriptive element/modifier”; these are not interchangeable.
- Several explanations are correct but remain answer-confirmation rather than full distractor analysis. That is acceptable for a concise key only if the editorial goal is a short explanation; it does not satisfy a stronger “explain why alternatives are wrong” standard in every row.
- Some proposed rationales include broad explanatory material not explicitly represented by the options. These should be kept carefully scoped to the course's stated framework.

## 3. Priority findings

### P1 — L8 Q3: stem terminology does not match the rule explained

**Quiz stem:** “Forma gelemjimar a nebinavkirî ya bê bireser çi ye?”  
**Key:** A, `-in`.  
**Proposed rationale:** says that §66 uses `-in` when no `pêvekeke raveker` follows the noun, and distinguishes it from definite `-ên` and inflected forms.

The rationale is about the presence or absence of a postnominal descriptive element/modifier, not about the clause-level object (`bireser`). In the course's controlled terminology, bare `bireser` elsewhere means clause-level object, while `bireserê navdêrê` is a noun-attached modifier. Therefore the stem's `bê bireser` can lead learners to answer a different question from the one the rationale explains.

**Recommendation:** hold the rationale from certification until the stem is reviewed. If the intended contrast is §66 versus §67, revise the stem to name the absence of a postnominal descriptive element using the exact course-approved term, rather than `bê bireser`. Do not silently change the stem or key in this audit.

### P2 — L1 Q1: terminology drift from the keyed answer text

**Keyed option:** “tevahiya qaydeyên rastaxaftin û rastnivîsandina ziman”.  
**Proposal:** “tevahiya rêzikên rastaxaftin û rastnivîsandina ziman”.

The meaning is close, but the proposal replaces the option's `qaydeyên` with `rêzikên`. Since the explanation is intended to reinforce a controlled course vocabulary, retain the exact lexical head from the keyed answer unless the course glossary explicitly prefers `rêzik`.

**Recommendation:** prefer `Gramêr tevahiya qaydeyên rastaxaftin û rastnivîsandina ziman e.` Then contrast A and C as narrower domains, without introducing a near-synonym.

### P2 — L6 Q3: good concept distinction, but explanation must not imply that option wording is already adequate

**Stem:** asks what the `bireser` is in `hespê beza`; keyed option A is `beza`.  
**Proposal:** correctly calls it `bireserê navdêrê` and distinguishes it from clause-level `bireser`.

The rationale repairs the conceptual ambiguity, but the option/stem still use bare `bireser`. A learner may reasonably interpret that as the clause-level object term already taught elsewhere.

**Recommendation:** retain the full term `bireserê navdêrê` in the explanation and flag the stem/option wording for an editorial consistency decision. Do not shorten the explanation to bare `bireser`.

### P2 — L5 Q1: avoid defining inflection by “position” alone

The refinement correctly broadens the explanation to grammatical role and sentence conditions, but its first version's phrase “erk û cihê wê” can be read as making word order itself the definition. Keep the refined version's explicit role, tense/transitivity, gender/number and phonological-condition qualifications; describe position as a possible contextual cue, not the definition.

### P3 — L1 Q2: make the counting scope explicit

The rationale says there are four basic elements in the lesson's sequence and that `qiset` is not a fifth item in that list. This is appropriate only as a statement about the course's enumerated hierarchy, not a universal claim that discourse/speech has no structural status. Keep the phrase “di vê rêza çaran de” or equivalent.

### P3 — L4 Q2/Q5: preserve the paradigm boundary and corrected wording

The explanations appropriately restrict `-in` to the taught indefinite paradigm and distinguish `hespin` from oblique `hespan`. The refinement patch's appended erratum corrects the awkward L4 Q5 phrase. Use the erratum wording, not the earlier sentence with “hespek-a yekjimar”.

### P3 — L10 Q1/Q2: form and syntactic role must remain distinct

The refined L10 Q1 and added L10 Q2 explanations appropriately caution that `min`/`wê` may be inflected agents in transitive past clauses even though the paradigm table classifies these forms in the object-pronoun set. Keep this distinction explicit; do not generalize from form label to clause function.

## 4. Rows that are adequate as concise explanations, with limits

- **L2 Q1–Q5:** the proposals identify noun naming, common noun vs proper name, and the examples. Most do not discuss every distractor, but the core contrast is adequate.
- **L3 Q1–Q5:** the grammatical-gender scope and lexical classifications are appropriately bounded to the course list/examples.
- **L4 Q1/Q3/Q4:** the explanations distinguish number from inflection and identify the singular example; concise distractor commentary is adequate.
- **L5 Q5:** appropriately states that nouns do not all inflect identically and points to gender, number, final sounds and construction.
- **L6 Q1/Q2/Q4/Q5:** explanations distinguish noun-attached modification from clause roles and identify head/modifier relationships; L6 Q3 remains flagged above.
- **L7 Q1/Q5:** correctly distinguishes definite suffixes and the plural form in the example. L7 Q2–Q4 retain existing specific rationales in the key and are outside the 44-row rewrite set.
- **L8 Q1/Q2/Q5:** generally distinguish indefinite marking, the §66/§67 environments, and definite `-ên` vs indefinite `-ine`. L8 Q3 remains flagged above; Q4/Q6/Q7 have existing non-generic rationales.
- **L9 Q5:** correctly identifies `hon` as second-person plural; the remaining L9 Q1–Q4 already have item-specific key rationales.
- **L10 Q3/Q4/Q5:** appropriately explain reciprocal forms, clause roles, and the course/source scope of the two/three-participant description.
- **L11 Q1/Q2/Q3/Q5:** preserve the course's pronoun distinctions and avoid claiming `ku` is universally wrong. L11 Q4 already has an item-specific rationale.
- **L12 Q2/Q4/Q5:** distinguish descriptive adjective, the course's independent `jmarnav` class, and the lexical-class vs phrase-function analysis of `nîv roj`.

These are judgments of explanation-to-option fit, not independent linguistic certification of every answer.

## 5. Held items

- **L10 Q2:** source §86 adjudication now supports the form/role distinction and the key C (`wê`); the rationale is eligible for editorial wording review. The question stem still merits scrutiny because its “forma bireserî” wording can be misunderstood unless the paradigm-vs-role distinction is explicit.
- **L12 Q1:** remains held for the adjective-definition scope and options; do not draft a rationale that treats the introductory definition as exhaustive.
- **L12 Q3:** remains held for `rengdêra jmarîn` vs `rengdêrê jmarîn`.
- **L1 Q4:** separate spelling/notation hold `kîtê/kitê`; the existing key rationale is not part of the generic-rationale rewrite set.

## 6. Recommended editorial sequence

1. Resolve L8 Q3 stem terminology against the §66 paradigm and controlled distinction between `bireser` and `bireserê navdêrê`.
2. Standardize L1 Q1 on the keyed option's `qaydeyên`.
3. Decide whether L6 Q3 stem/option should explicitly say `bireserê navdêrê`; keep the full term in the rationale meanwhile.
4. Accept the L4 Q5 erratum as the only proposed wording in that row.
5. Retain L5 and L10 form/function qualifications.
6. Only after these editorial decisions, conduct a final copy-edit of the 45 rationale rows as a single coherent answer-key style.

## 7. Preservation and validation boundary

No lesson, quiz, answer-key, source transcription, runtime, parser, manifest, database, Botkeep, Telegram or deployment file was modified. No proposal was approved or applied. No tests/CI, runtime checks, learner-response analysis or psychometric validation was performed. `main` remains read-only. Work is confined to `archive/preservation-audit-2026-11-10`. GitHub archive history is not an independent ZIP/off-site backup; no separate backup is claimed.
