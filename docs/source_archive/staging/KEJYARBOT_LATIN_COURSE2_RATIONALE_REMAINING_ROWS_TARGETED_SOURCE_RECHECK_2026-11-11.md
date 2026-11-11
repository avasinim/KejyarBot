# Course 2 — Remaining proposed rationale rows targeted source recheck
**Date:** 2026-11-11  
**Status:** Audit record only; proposal wording remains unapproved and unapplied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## Scope and inputs
Fresh exact-row comparison of 16 proposed rationales against the reviewed quiz stems/options, lesson definitions/examples, and current answer-key rows:
- L5 Q1/Q5
- L6 Q1–Q4
- L9 Q5
- L10 Q1/Q3/Q4/Q5
- L11 Q1/Q3/Q5
- L12 Q2/Q4

Lesson source: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`. Base rationale proposal fetched at SHA `ccdd1fea505fa354d9c043dd0c010f8fe84faf2a`. Answer key fetched at SHA `879e1525e720bdc25b8f6e896de3e388801238d0`. The superseding L6 Q5 possessive-modifier correction was preserved and not reverted.

## Row findings

### Lesson 5 — inflection
- **Q1 (B):** The stem asks for the definition of `tewang`; the lesson defines it as a change in a word/noun form according to grammatical role and conditions. The rationale's contrast with colour and question is responsive to the distractors and correctly ties the concept to clause role and conditions. **No correction identified.**
- **Q5 (C):** The lesson explicitly warns that not all nouns inflect in the same way and lists gender, number, final sounds and clause structure as conditioning factors, including exceptions. The rationale captures this non-uniformity. **No correction identified.**

### Lesson 6 — noun-attached modifier
- **Q1 (B):** The lesson defines `bireserê navdêrê` as an element/phrase that describes, specifies or adds information about a noun. The rationale matches the definition and distinguishes it from clause-level subject/object role and inflection. **No correction identified.**
- **Q2 (C):** In `ev keçik`, the noun/head is `keçik`; `ev` is the pre-nominal determiner/modifier. This is stated in the lesson's grammatical note. The rationale matches the keyed answer.
- **Q3 (A):** In `hespê beza`, `beza` is the noun-attached descriptive/qualifying element; the lesson explicitly uses this as a post-nominal example and distinguishes it from clause-level `bireser`. The rationale identifies the right constituent and preserves that terminology distinction.
- **Q4 (B):** The lesson supplies both pre-nominal examples (`ev keçik`, `çar xanî`) and post-nominal examples (`hespê beza`, `xencera min`). The rationale accurately states both positions.

### Lesson 9 — second-person plural pronoun
- **Q5 (A):** The lesson identifies `hon` as the second-person plural personal pronoun. The other options `min` and `wan` belong to different person/number forms. The rationale matches the table and the stem. **No correction identified.**

### Lesson 10 — object pronouns and reciprocal forms
- **Q1 (B):** The lesson lists `min, te, wî, wê, me, we, wan` in the object-pronoun forms table, while explicitly warning that a form's table label does not determine its clause role in every sentence. The rationale preserves this form-versus-role distinction. **No correction identified.**
- **Q3 (A):** The lesson gives `hev` and `êk` as the two basic reciprocal-pronoun forms and notes the regional use of `êk`. The rationale matches the inventory and avoids extending the regional note beyond the lesson.
- **Q4 (B):** In `Wan ew xwar`, `ew` stands for the thing eaten and is the direct object; `wan` is the inflected agent. The lesson explicitly analyses this construction. The rationale matches the stem and key.
- **Q5 (B):** The lesson's §90 framing limits its basic definition/examples to two or three people acting in relation to one another. The rationale explicitly scopes the answer to the course/source framing rather than claiming a universal limit for all languages or reciprocal constructions.

### Lesson 11 — demonstrative and interrogative pronouns
- **Q1 (B):** The lesson gives `ev/ew` as the basic demonstrative-pronoun pair and contrasts them with personal pronouns and interrogatives. The rationale also preserves the near/far or discourse-reference distinction.
- **Q3 (A):** The lesson deliberately retains `ko` as the course's traditional relative-pronoun form and explicitly says this does not make `ku` wrong in all standards/dialects. The rationale's scope limitation is accurate.
- **Q5 (C):** The lesson defines `kîjan` as selecting/identifying a person or thing among alternatives. The rationale matches that function and the distractors.

### Lesson 12 — adjective and numeral
- **Q2 (C):** In `hespê mezin`, `mezin` describes the quality of the noun `hesp`; the lesson places this under qualitative adjectives. The rationale is supported by the explicit example.
- **Q4 (B):** The lesson explicitly presents `jmarnav` as a separate grammatical class in this teaching framework, distinct from a numeral adjective used with a noun. The rationale is properly scoped to the lesson's selected classification.

## Outcome and limits
- Rows checked in this pass: **16**.
- New concrete stem/key/source contradiction: **0**.
- New proposal wording correction: **0**.
- The earlier superseding L6 Q5 correction remains mandatory: `min` in `xencera min` is `rengdêra xwemalîn`, not `pronavê xwemalî`.
- This tranche does not independently copy-edit all 45 proposed rationales at native-speaker level, nor does it settle held L1 Q4, L12 Q1 or L12 Q3.
- No lesson, quiz, answer-key, runtime, parser, manifest, database, Botkeep, Telegram, deployment, test or CI file was changed or run. No proposal was approved/applied. `main` remains read-only. The archive branch is not an independent ZIP/offsite backup; none is claimed.
