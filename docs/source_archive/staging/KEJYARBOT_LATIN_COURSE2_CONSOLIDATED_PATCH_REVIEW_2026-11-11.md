# Course 2 — consolidated editorial patch review and handoff

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** consolidated proposal only — approval pending; nothing applied  
**Reviewed quiz baseline SHA:** `abc88219e2a0e249883e8d62c5117a9b3aaa3108`  
**Reviewed answer-key baseline SHA:** `879e1525e720bdc25b8f6e896de3e388801238d0`  
**Runtime baseline SHA:** `7139aec3d585919baac65f93c2630a519c995e04`

## 1. Why this handoff exists

The detailed editorial proposal accumulated several append-only correction notes while the Lesson 8 source pages were being adjudicated. Some historical notes contradict later findings. This file consolidates only the currently operative interpretation and proposed wording, so the next review does not accidentally act on superseded text. The historical records remain intact.

**Controlling Lesson 8 source interpretation:** §68 is the final-noun agreement rule; §69 is the separate construction in which each linked complement receives its own determiner according to its own gender and number; §70 gives oblique forms `-ekî/-ekê/-ina` for the stated object environment. The last page-image adjudication in the editorial proposal, the page-image review addendum, global audit §30, and the preservation checkpoint are authoritative. Earlier contradictory notes in the append-only history are superseded.

## 2. Operative proposed quiz edits

These are the four proposed stem/option changes, preserving the currently keyed answers:

### Lesson 6, Q3
- Stem: `Di koma navdêrî `hespê beza` de, kîjan hêman `bireserê navdêrê` ye?`
- Keep current options and key A (`beza`).
- Reason: use the full noun-modifier term, not the ambiguous shortened `bireser`, which elsewhere denotes clause-level object.

### Lesson 8, Q5
- Stem: `Ma veqetandeka binavkirî ya gelemjimar `-ên` û veqetandeka nebinavkirî `-ine` heman erkê hene?`
- A) Erê, her du formên binavkirî ne.
- B) Erê, her du formên nebinavkirî ne.
- C) Na, erkên wan cuda ne.
- Key C.
- Reason: the options test two distinct confusions between the definite and indefinite plural paradigms.

### Lesson 10, Q1
- Stem: `Di hevoka dema niha de `Tu ___ dibînî`, kîjan pronav li cihê bireserê tê?`
- A) `te`; B) `min`; C) `me`.
- Key B (`min`).
- Reason: §86 gives the exact present-tense frame `tu min dibînî`; the frame, not the pronoun form alone, identifies the object role.

### Lesson 10, Q2
- Stem: `Di hevoka dema niha de `Tu ___ dibînî`, kîjan form ji bo pronavê kesê sêyem yekjimar a mê wek bireser tê?`
- A) `wî`; B) `ew`; C) `wê`.
- Key C (`wê`).
- Reason: §86 gives the exact frame `tu wê dibînî`, avoiding confusion with `wê` as an inflected agent in past-transitive clauses.

## 3. Operative proposed Lesson 8 explanatory-line replacements

The following are proposal text only. They do not replace the reviewed baseline until explicit approval.

**Reviewed draft line 290 — proposed replacement**

`Ji ber vê yekê formên tewandî divê ji formên netewandî yên `-ek/-ek/-in` cuda bên fêrkirin.`

The source distinction is between uninflected `-ek/-ek/-in` and oblique inflected forms `-ekî/-ekê/-ina` in the stated object environment (§70).

**Reviewed draft line 292 — proposed replacement**

`Dema ku ji yekê zêdetir bireser bi navdêrê ve girêdayî bin û ew bireser tevde navdêr û peyhev bireserên hev bin, her yek ji wan li gorî mêjer û zayenda xwe veqetandekeke cuda werdigire. Ev hûrgilî di vê dersê de wek rêgezeke pêşketî hatiye pêşkêşkirin, ne wek bingehê destpêkê.`

Source rule (§69): in the described construction, each linked complement receives its own determiner according to its own gender and number. Do not substitute §68's final-noun agreement rule here.

**Reviewed draft line 294 — proposed replacement**

`Nîşe: `-ek/-ek/-in`, `-ekî/-eke/-ine` û `-î/-e/-en` sê komên formên cuda ne; divê her yek li gorî şert û erkê xwe were bikaranîn. Ev form ji veqetandekên binavkirî `ê/a/ên` cuda ne.`

This separates three indefinite-determiner environments (§§66–68) from the definite forms. It also removes the unintended Kurdish-Arabic-script fragments from the Latin-script prose.

## 4. Source cross-check status

- L6 Q3: §59–60 includes `hespê beza`; the noun modifier is `beza`.
- L8 Q5: §§63 and 66–67 distinguish definite `-ên` from indefinite `-ine`.
- L8 lines 290/292/294: original page images were inspected; the §68/§69 distinction and §70 oblique paradigm are recorded in the page-image review addendum and global audit §30.
- L10 Q1/Q2: §86 explicitly supplies `tu min dibînî` and `tu wê dibînî`.
- Proposed key sequence remains A / C / B / C. Option order in the reviewed quiz was checked against those proposed letters.

**Remaining editorial caution:** source-rule correctness is verified, but the exact Kurmanji Latin phrasing of the three explanatory-line replacements—especially the terminology and syntax in line 292—should receive a final language-editor pass before approval. This is not a reason to alter the source interpretation.

## 5. Approval and preservation gates

No changes have been applied to the reviewed lesson/quiz baseline, answer-key baseline, runtime, tests, manifest, database, Botkeep, Telegram, or deployment.

After explicit approval only:
1. Create new dated append-only lesson/quiz and answer-key patch artifacts; never overwrite the baselines.
2. Apply only the approved changes above.
3. Recheck all four answer letters and exact answer texts against the final option order.
4. Re-parse all 62 questions and 62 answer-key rows; verify missing/orphan/duplicate rows, valid option labels, and normalized answer-text matches.
5. Re-scan the complete Latin-script draft for unintended mixed-script text and terminology drift.
6. Append fresh SHAs and verification results to the global audit and checkpoint.
7. Keep runtime and deployment untouched unless separately authorized.

Tests/CI have not been run. Runtime behavior has not been tested live. The archive branch and GitHub commit history are not an independent ZIP/off-site backup. `main` remains read-only.


## 6. Language-editor refinement candidate for Lesson 8 line 292 (2026-11-11)

The original source §69 uses the term `bireser` for the elements attached to the noun in this construction. In this course, however, `bireser` also appears in clause-level object terminology, while Lesson 6 has already established the more precise phrase `bireserê navdêrê`. To reduce that potential ambiguity without changing the source rule, a clearer candidate sentence for final language-editor review is:

`Dema ku ji yekê zêdetir bireserên navdêrê bi navdêrê ve girêdayî bin û ew bireser bi hev re komeke navdêrî pêk bînin, her yek ji wan li gorî mêjer û zayenda xwe veqetandeka cuda werdigire.`

This is a wording candidate, not a source quotation and not an approved replacement. It preserves the source's §69 rule: each linked modifier receives its own determiner according to its own gender and number. It avoids suggesting that the final noun alone controls all forms (the separate §68 rule). The original proposed line remains available in section 3; a language editor should choose between the source-close wording and this clearer course-terminology wording before approval.

Source image check: printed p.66 shows §68's final-noun rule followed by the opening of §69; printed p.67 continues §69's examples and begins §70. The source text at §69 explicitly says that each of the linked `bireser` elements receives a distinct determiner according to its own number and gender. See the PDF page images and extracted text.


## 7. Controlling update — include Lesson 8 Q3 and refresh proposal pointers (2026-11-11)

This section is the current operative queue and supersedes the four-item-only scope in section 2 and any earlier stale blob pointers in this handoff.

### Complete proposed quiz queue (five items)

1. **L6 Q3:** use the full term `bireserê navdêrê`; keep A (`beza`).
2. **L8 Q3:** replace the ambiguous `bê bireser` with `bê pêvekeke raveker li pey navdêrê` in the stem; retain A (`-in`). The exact proposed stem is in the current editorial proposal.
3. **L8 Q5:** use the expanded definite/indefinite contrast stem and distinct A/B misconception distractors; keep C.
4. **L10 Q1:** use `Tu ___ dibînî`; keep B (`min`).
5. **L10 Q2:** use `Tu ___ dibînî`; keep C (`wê`).

The corresponding answer-key rationale proposal currently contains four rationale rows (L6 Q3, L8 Q5, L10 Q1–Q2). L8 Q3 retains its existing answer A and should receive a matching rationale only in a future dated key copy if the quiz edit is approved. No key file has been changed.

### Current artifact pointers

- Editorial proposal, including the new L8 Q3 candidate: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_EDITORIAL_PATCH_PROPOSAL_2026-11-11.md`, blob SHA `11b6c6c055a149283f2b4275da15922e28d1f82d`.
- Answer-key rationale proposal: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_ANSWER_KEY_PATCH_PROPOSAL_2026-11-11.md`, blob SHA `79b39c8fb499f45c61445f640dc268f32c05eecb` (its older related-proposal pointer is corrected in an addendum to that file).
- Full 62-question terminology cross-check: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_62Q_LESSON_QUIZ_TERMINOLOGY_CROSSCHECK_2026-11-11.md`, blob SHA `e5e7b67bcc98504d0fd39b7da8a348ba8bee7350`.

### Remaining language-editor decisions

- Review the exact Kurmanji Latin phrasing of Lesson 8 explanatory line 292; the source rule is settled, but the wording candidate must not be mistaken for a source quotation.
- Decide the preferred Lesson 12 label form around `rengdêrê/rengdêra jmarîn` against the source heading `rengdêrên jmarîn`.
- Resolve the Lesson 6 paired glossary label `pêşnavdêr/bireser` without collapsing the established noun-modifier / clause-object distinction.

### Preservation and approval gate

All five quiz edits and all three Lesson 8 prose replacements remain proposals only. The reviewed lesson/quiz baseline and answer-key baseline remain unchanged. Do not create a revised patch copy or modify the baseline until explicit approval. If approved, create new dated append-only copies, include the L8 Q3 rationale, and rerun the full 62-question/key, terminology, and script checks. No runtime, parser, manifest, database, Botkeep, Telegram, tests/CI, or deployment action is authorized by this handoff. `main` remains read-only.


## 8. Exact five-item option/key cross-check (2026-11-11)

The five proposed stems were compared against the protected reviewed quiz's current option order and the protected 62-row answer key. The baseline answer text and key letters align with the proposed edits; no option reorder is needed for the current proposal.

| Item | Proposed stem / options | Current key and answer text |
|---|---|---|
| L6 Q3 | Stem from §2 above. A) `beza`; B) `hesp`; C) `hespê`. | A — `beza` |
| L8 Q3 | `Di rewşa bê pêvekeke raveker li pey navdêrê de, forma gelemjimar a veqetandeka nebinavkirî çi ye?` A) `-in`; B) `-ên`; C) `-a`. | A — `-in` |
| L8 Q5 | Stem/options in §2 above: A) both definite; B) both indefinite; C) `Na, erkên wan cuda ne.` | C — `na, erkên wan cuda ne` |
| L10 Q1 | Stem in §2 above. A) `te`; B) `min`; C) `me`. | B — `min` |
| L10 Q2 | Stem in §2 above. A) `wî`; B) `ew`; C) `wê`. | C — `wê` |

The proposed key sequence is therefore **A / A / C / B / C** in the order L6 Q3, L8 Q3, L8 Q5, L10 Q1, L10 Q2. This confirms only the current option/key alignment. It does not independently certify the linguistic quality of the wording, approve any change, or alter the answer-key baseline. The new L8 Q3 rationale candidate is recorded in the separate answer-key proposal.

Source baseline SHAs used for this comparison: reviewed quiz/lesson `abc88219e2a0e249883e8d62c5117a9b3aaa3108`; reviewed answer key `879e1525e720bdc25b8f6e896de3e388801238d0`. All source files remain unchanged.


## 9. Explicit supersession note — Lesson 8 line 292 (2026-11-11)

To prevent an older wording from being applied accidentally: **do not treat the line 292 sentence printed in section 3 as approved or operative copy.** It is an earlier proposal draft and requires language-editor correction. Section 6 contains the later course-terminology candidate using `bireserên navdêrê`; that candidate is still pending final Kurmanji syntax review and is not approved either.

The source rule itself is settled by the page-image adjudication: §68 concerns agreement with the final noun in its construction; §69 is distinct and assigns each linked complement its own determiner according to its own gender and number. Any future approved line must express §69 without importing §68's final-noun rule. Until a language editor approves the exact wording, retain the protected base and do not apply either candidate.
