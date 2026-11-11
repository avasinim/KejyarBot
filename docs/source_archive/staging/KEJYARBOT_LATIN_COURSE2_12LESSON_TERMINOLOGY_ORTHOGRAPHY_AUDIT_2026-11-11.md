# Course 2 — 12-lesson terminology and orthography consistency audit

**Date:** 2026-11-11  
**Repository:** `avasinim/KejyarBot`  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** audit findings only; no lesson, quiz, answer-key, or runtime edits applied  
**Reviewed base:** `course_data/latin_course_2_reviewed_draft_2026-11-10.md`  
**Reviewed base blob SHA:** `abc88219e2a0e249883e8d62c5117a9b3aaa3108`  
**Scope:** all 12 lesson sections in the reviewed Course 2 Kurmanji Latin draft

## 1. Method and limits

The complete 651-line reviewed draft was fetched from the archive branch and segmented by its twelve lesson headings. A terminology occurrence scan was run for the principal grammar terms, followed by contextual inspection of the relevant passages. The scan is a consistency triage, not a complete linguistic proofread or an independent review against every source page. Counts are occurrence indicators, not quality scores. Source-specific terminology and distinctions must not be flattened merely to make spelling uniform.

The base file was fetched at the SHA above. This audit does not alter it.

## 2. Stable distinctions to preserve

### 2.1 `bireserê navdêrê` versus clause-level `bireser`

Lesson 6 explicitly distinguishes the noun-attached modifier/complement (`bireserê navdêrê`, e.g. `hespê beza`) from the sentence role of direct object (`bireser`), and connects this distinction to the pronoun lessons. Lesson 10 uses `pronavên bireser` for pronouns taking the object role. This distinction is pedagogically important and should remain explicit in future revisions.

**Action:** retain the full phrase `bireserê navdêrê` wherever the noun-modifier concept is meant; use `bireser` alone only where the clause role is intended and context makes that clear. Lesson 6 Q3's proposed wording refinement is already captured in the consolidated patch handoff and remains unapplied.

### 2.2 `veqetandek` versus `pêvek`

Lessons 7–8 use `veqetandek` for the definite/indefinite determiner suffix patterns. Elsewhere `pêvek` is used more broadly for attached morphological material (including plural/indefinite morphology and comparative `-tir`). Lesson 8's existing explanatory prose also uses both terms in the same discussion.

This may be a useful broad-term/specific-term distinction, not necessarily an error. The current draft does not provide one concise terminology rule that makes the scope of both terms explicit to learners.

**Action:** add a glossary/editorial note defining `pêvek` as the broad morphological term and `veqetandek` as the course's specific label for the determiner forms, if that distinction matches the intended grammar framework. Do not replace every occurrence of one with the other mechanically.

### 2.3 Pronoun form versus syntactic function

Lessons 9–11 repeatedly warn that forms such as `min/te/wî/wê/me/we/wan` do not have an invariant agent/subject or object role. The role depends on tense, verb transitivity, and clause structure. Lesson 6 similarly distinguishes the same visible forms as modifiers from standalone demonstrative pronouns according to their syntactic environment.

**Action:** preserve these contextual explanations in any shortening or quiz revision. Do not classify a pronoun solely from its surface form.

### 2.4 `ko` and `ku`

Lesson 11 explicitly teaches `ko` in the source-specific relative/conjunction examples and contrasts it with `ku`. The wider explanatory prose also contains ordinary `ku` in subordinate clauses. This is not a global typo pattern that can safely be normalized by search-and-replace.

**Action:** retain `ko` in the source-scoped examples and preserve `ku` where it functions as the ordinary subordinating conjunction in the explanatory Kurmanji. Any standardization must be source- and function-aware.

## 3. Confirmed editorial consistency issues

### 3.1 Lesson 12: two forms for “numeral adjective”

The same lesson uses both `rengdêrê jmarîn` and `rengdêra jmarîn` (including in the explanatory paragraph and exercise/test wording). The intended grammatical construction and preferred headword form should be checked once by a Kurmanji language editor, then normalized consistently within Lesson 12 and the course glossary.

**Status:** confirmed within-file variation; preferred form not adjudicated by this scan. No automatic replacement is proposed.

### 3.2 Lesson 8: mixed-script explanatory lines remain in the base

The reviewed base still contains mixed Kurdish Arabic/Latin script in lines 290, 292, and 294. Earlier review identified these as requiring complete Kurmanji Latin rewrites. The current consolidated patch handoff contains candidate replacements and the source-based distinction between §§68–70, but it remains proposal-only.

**Status:** confirmed unresolved in the protected base. Do not mistake proposed text for an applied correction.

### 3.3 Lesson 6: `pêşnavdêr/bireser` wording needs glossary alignment

Lesson 6 uses the combined label `pêşnavdêr/bireser` for `ev` in `ev keçik`, while the surrounding explanation focuses on the modifier's function and later distinguishes standalone demonstrative pronouns. This may reflect two terminology traditions or a pedagogical gloss, but the slash construction is not defined as a stable course term elsewhere in the scan.

**Action:** language-editor review should decide whether to retain the paired gloss, choose one preferred label, or explain the distinction in the glossary. Do not silently delete either concept.

## 4. Cross-course terminology inventory observations

- Lessons 1–2 establish `tîp`, `kît`, `bêje`, `komek`, `qiset`, `hevenav`, and `serenav`. Lesson 1 explicitly treats `qiset` as a larger construction formed from groups, not as a fifth item in the four-part basic list; preserve that distinction.
- Lessons 3–5 establish grammatical gender (`zayend`), number (`mêjer`), and inflection (`tewang`) as separate concepts. Lesson 5 warns that the general present-tense object pattern must not be generalized to past transitive clauses; retain the tense/transitivity qualification.
- Lessons 7–8 distinguish definite forms `-ê/-a/-ên`, indefinite paradigms `-ek/-ek/-in`, `-ekî/-eke/-ine`, and the pre-adjective forms `-î/-e/-en`, plus the stated oblique forms `-ekî/-ekê/-ina`. These paradigms must not be collapsed.
- Lessons 9–11 distinguish personal, object, reciprocal, compound, reflexive, demonstrative, relative, and interrogative pronouns. Similar surface forms do not establish identical function.
- Lesson 12 treats `jmarnav` as a separate grammatical class in its adopted framework and contrasts it with `rengdêrê/rengdêra jmarîn`. Preserve that distinction pending a source/terminology review; do not recategorize the class based on surface examples alone.

## 5. Proposed action queue (not applied)

1. Have a Kurmanji language editor adjudicate the preferred form of `rengdêrê/rengdêra jmarîn` and normalize only after decision.
2. Define the broad/specific relationship between `pêvek` and `veqetandek` in the glossary, without mechanical substitution.
3. Review the Lesson 6 paired label `pêşnavdêr/bireser` for clarity and alignment with the rest of the course.
4. Keep the Lesson 8 lines 290/292/294 candidate patch pending explicit approval and language-editor review, especially line 292.
5. Retain the contextual distinctions for `bireser`, pronoun roles, `ko/ku`, and the Lesson 7–8 suffix paradigms.
6. After any separately approved patch, rerun the full 12-lesson terminology scan and the 62-question/62-key structural comparison.

## 6. Preservation and non-actions

- No edits were made to the reviewed lesson base, quiz, answer key, source-aligned originals, runtime, tests, active manifest, database, Botkeep, Telegram, or deployment.
- No tests or CI were run; no live runtime state was checked.
- All audit work is confined to the archive branch. `main` remains read-only.
- GitHub archive-branch history is the persisted project record; this report does not claim a separate ZIP or independent off-site backup.
