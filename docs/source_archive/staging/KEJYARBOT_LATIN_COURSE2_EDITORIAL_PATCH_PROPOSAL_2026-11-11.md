# Course 2 — proposed editorial patch (approval pending)

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** proposal only — not applied to the reviewed lesson or quiz files  
**Base reviewed quiz SHA:** `abc88219e2a0e249883e8d62c5117a9b3aaa3108`  
**Base reviewed answer-key SHA:** `879e1525e720bdc25b8f6e896de3e388801238d0`

## Purpose and preservation rule

This proposal turns the findings in `KEJYARBOT_LATIN_COURSE2_62Q_DISTRACTOR_ORTHOGRAPHY_REVIEW_2026-11-11.md` into concrete suggested edits. It is a review artifact only. It does not change either base file, the source-aligned originals, runtime, tests, manifests, database, Botkeep, Telegram, or deployment state.

If approved, apply the edits only to a new dated append-only reviewed-draft/patch artifact. Preserve the current reviewed files and answer key unchanged as the baseline. Then run the structural quiz/key comparison again and document the resulting new blob SHAs.

## A. Lesson 6 — Question 3 terminology

**Current stem**

`Di `hespê beza` de bireser çi ye?`

**Proposed stem**

`Di koma navdêrî `hespê beza` de, kîjan hêman `bireserê navdêrê` ye?`

**Options and key:** retain the current options and keyed answer `beza`, subject to rechecking the sentence against the lesson text.

**Reason:** the lesson distinguishes the noun modifier `bireserê navdêrê` from the sentence-role term `bireser`. The question should use the full term and avoid undoing that distinction.

## B. Lesson 8 — Question 5 distractors

**Current stem**

`-ên û -ine ma yek in?`

**Proposed stem**

`Ma veqetandeka binavkirî ya gelemjimar `-ên` û veqetandeka nebinavkirî `-ine` heman erkê hene?`

**Proposed options**

- A) Erê, her du formên binavkirî ne.
- B) Erê, her du formên nebinavkirî ne.
- C) Na, erkên wan cuda ne.

**Key:** C.

**Reason:** A and B are parallel, recognizable confusions between the definite and indefinite paradigms. The current “erê / her tim” alternatives are near-duplicates and do not test a useful grammatical misconception. Confirm the revised wording against the precise terminology in Lesson 8 before approval.

## C. Lesson 10 — Question 1 object context

**Current stem**

`Kîjan yek ji pronavên bireser e?`

**Proposed stem**

`Di hevoka dema niha de `Tu ___ dibînî`, kîjan pronav li cihê bireserê tê?`

**Proposed options**

- A) `te`
- B) `min`
- C) `me`

**Key:** B (`min`).

**Reason:** the lesson explicitly cautions that forms such as `min` do not have an invariant subject/object role; the clause construction determines the role. The sentence frame makes the intended direct-object function observable rather than attributing a permanent role to the form.

## D. Lesson 10 — Question 2 object context

**Current stem**

`Forma bireserî ya `ew` mê çi ye?`

**Proposed stem**

`Di hevoka dema niha de `Ez ___ dibînim`, kîjan form ji bo pronavê kesê sêyem yekjimar a mê wek bireser tê?`

**Proposed options**

- A) `wî`
- B) `ew`
- C) `wê`

**Key:** C (`wê`).

**Reason:** `wê` also occurs as an inflected agent in past-transitive clauses. A present-tense direct-object frame removes that potential confusion and tests the intended form in context.

## E. Lesson 8 — three mixed-script explanatory lines

The following are proposed full-line replacements for the three affected lines in the reviewed lesson draft. They should be checked against the cited source section before any approved patch is produced.

**Draft line 290 — proposed replacement**

`Ji ber vê yekê formên tewandî divê ji formên netewandî yên `-ek/-ek/-in` cuda bên fêrkirin.`

**Draft line 292 — proposed replacement**

`Dema ku ji yekê zêdetir bireser bi navdêrê ve girêdayî bin û ew bireser tevde navdêr û peyhev bireserên hev bin, her yek ji wan li gorî mêjer û zayenda xwe veqetandekeke cuda werdigire. Ev hûrgilî di vê dersê de wek rêgezeke pêşketî hatiye pêşkêşkirin, ne wek bingehê destpêkê.`

**Draft line 294 — proposed replacement**

`Nîşe: `-ek/-ek/-in`, `-ekî/-eke/-ine` û `-î/-e/-en` sê komên formên cuda ne; divê her yek li gorî şert û erkê xwe were bikaranîn. Ev form ji veqetandekên binavkirî `ê/a/ên` cuda ne.`

## F. Required validation if approved

1. Preserve the two base reviewed artifacts and create a new dated patch copy; do not overwrite either base file.
2. Apply only the approved wording changes. Do not change answer letters unless a separate source-based reason is recorded.
3. Update the corresponding answer-key rationales so they explain the new context and terminology; keep the 62-row coverage intact.
4. Re-parse all 12 lesson quizzes and the key. Confirm 62 questions, 62 key rows, no missing/orphan/duplicate rows, valid option labels, and exact normalized answer-text matches.
5. Re-scan the full lesson draft for unintended mixed-script fragments and terminology consistency.
6. Append the new report and verification results to the global audit and preservation checkpoint.
7. Keep runtime and deployment untouched unless separately authorized. Tests/CI remain unexecuted unless explicitly run in a later authorized task.

## Approval boundary

No proposed edit in this file has been applied. A separate explicit approval is required before creating the revised lesson/quiz/key patch artifact. The archive branch remains the only writable branch for this work; `main` remains read-only.


## Source-verification correction — Lesson 8, §69 (2026-11-11)

A direct recheck of Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, printed pp.66–67, §§67–70, found that the earlier proposed replacement for reviewed-draft line 292 repeated an inaccurate interpretation. Section 69 says that when more than one complement/modifier is attached in a linked noun group, **each** such element receives its own suffix according to its own gender and number. It does not state that only the final component determines the suffix. The proposed replacement above has therefore been corrected to express separate inflection for each element. The reviewed base lesson remains unchanged; this is still a proposal-only wording update.

Source locator: printed p.67, §69; the preceding paradigms are §67 (printed p.66), §68 (printed p.66), and §70 (printed pp.67–68). The source PDF is the 2002 Nefel edition, ISBN 91-89687-04-3. The current source wording was checked against the PDF text and the original page image context; the source's §69 examples include the coordinated forms on printed pp.67–68.


## Source-verification correction — Lesson 8, §§69–70 (2026-11-11, superseding prior correction)

A direct inspection of the source PDF text and page image at printed pp.66–68 corrects the immediately preceding §69 note in this proposal. That previous note was mistaken: §69 does **not** say that every linked element receives its own suffix. It says that when several complements/modifiers form one linked noun group, the determiner is selected according to the gender and number of the **final noun** in that group. The corrected proposed line 292 above now reflects that source rule. The earlier audit section 28 and checkpoint entry describing separate suffixes for every element must be treated as superseded by this correction; a new audit/checkpoint addendum records the reversal.

The same source check also clarifies line 290: §70 contrasts the uninflected forms `-ek/-ek/-in` with their oblique inflected forms `-ekî/-ekê/-ina`. The proposal therefore uses `formên netewandî` (uninflected forms), not the vague `formên bingehîn`. The reviewed base lesson remains unchanged. This file remains proposal-only.

Primary-source locator: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed p.67, §69 (PDF page index 66), and printed pp.67–68, §70 (PDF page indices 66–67). In §69 the source explicitly states that the determiner is applied according to the gender of the final noun; §70 lists `-ekî/-ekê/-ina` as inflected forms. The printed examples support these distinctions.


## Page-image adjudication — distinguish §68 from §69 (2026-11-11; supersedes the immediately preceding correction)

The immediately preceding correction incorrectly transferred the rule at the end of §68 to §69. Direct inspection of the original page images resolves the distinction:

- **§68, printed p.66:** its concluding note says that where several nouns are linked by one complement, the determiner is selected according to the gender of the final noun. This is the final-noun agreement rule.
- **§69, printed pp.66–67:** a separate construction is introduced when more than one complement is attached to a noun and the complements themselves form a linked noun sequence. The text says that each one receives a distinct determiner according to its own number and gender. The examples continue on printed p.67.
- **§70, printed pp.67–68:** the uninflected forms `-ek/-ek/-in` take oblique forms `-ekî/-ekê/-ina` in the stated object environment.

Accordingly, the proposed line 292 above correctly expresses the §69 rule: each linked complement receives its own form according to its own gender and number. The previous proposed wording about the final noun belongs only to §68 and must not replace §69. Line 290 also remains clarified as `formên netewandî` for the uninflected `-ek/-ek/-in` forms, in contrast with the oblique forms in §70.

Evidence: the original PDF page image for printed p.66 shows the §68 final-noun note and the opening of §69 separately; the image for printed p.67 continues §69's examples and then begins §70. See the cited source pages and the page-image review note. The reviewed base lesson remains unchanged; this artifact remains proposal-only.
