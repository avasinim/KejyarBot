# Course 2 — Lesson 6 / Lesson 8 modifier terminology clarification
**Date:** 2026-11-11  
**Status:** Append-only editorial clarification; proposed wording only, not approved/applied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## 1. Verified source wording

The source-aligned lesson file `course_data/latin_course_2_source_aligned_lessons_01_12.md` (SHA `19090077a11dc9d7211987e958e560b328fcd3d6`) contains these relevant formulations:

- **Lesson 6** defines `bireserê navdêrê` as a word or group of words that describes, specifies, or adds information to a noun. It gives postnominal examples `hespê beza`, `mehinên spehî`, and `xencera min`. Its quiz L6 Q3 asks “Di `hespê beza` de bireser çi ye?” and keys `beza`.
- **Lesson 8** labels its first indefinite-suffix environment “Piştî navdêrê, bê bireser” and describes the contrasting environment as “Dema bireser/rengdêr li pey were”. Its quiz L8 Q2 uses “bê bireser” for `hespek hat`; L8 Q3 asks for the plural indefinite form “bê bireser”.
- Elsewhere in the course, especially Lesson 10, `bireser` also denotes the clause-level object. The cross-lesson terminology register explicitly warns against shortening `bireserê navdêrê` to bare `bireser`.

## 2. Corrected diagnosis

The previous explanation-to-option audit identified L8 Q3 as a possible stem/construct mismatch. This clarification narrows that finding:

- L8 Q3 is consistent with the *local* Lesson 8 contrast and heading: the intended distinction is whether a descriptive element follows the noun.
- However, the term `bireser` is overloaded across the course. Lesson 6 uses the full compound for a noun-attached modifier, while Lesson 10 uses the bare term for a clause-level object. Lesson 8's shortened `bê bireser` therefore creates a cross-lesson ambiguity even though it matches its own local section wording.
- This is a course terminology consistency issue, not evidence that the §66/§67 grammatical contrast or the keyed answer `-in` is necessarily wrong.

## 3. Proposed editorial wording — not applied

To make the two environments explicit without changing the grammatical content:

- Lesson 8 subsection heading: replace “Piştî navdêrê, bê bireser” with **“Piştî navdêrê, bê hêmaneke raveker”** (or another exact term approved by the Kurmanji editor).
- Lesson 8 contrasting heading: use **“Dema hêmaneke raveker li pey navdêrê were”** consistently, instead of the compressed “bireser/rengdêr”.
- L8 Q2: consider “`hespek hat` di çi rewşê de ye?” with option C rephrased as “bê hêmaneke raveker a li pey navdêrê”.
- L8 Q3: consider “Forma gelemjimara nebinavkirî ya bê hêmaneke raveker a li pey navdêrê çi ye?” Key remains A (`-in`) in this proposal.
- L6 Q3: replace bare “bireser” in the stem with the full category: “Di koma `hespê beza` de kîjan hêman `bireserê navdêrê` ye?” Key remains A (`beza`).
- L6 rationale must retain `bireserê navdêrê`; it should not imply that the abbreviated stem was already unambiguous.

These are wording proposals only. Do not globally replace every occurrence of `bireser`: clause-level object terminology in Lesson 10 must remain distinct.

## 4. Decision boundary

This note does not adjudicate the underlying grammar beyond the stated source-aligned lesson text. A Kurmanji editor should approve the preferred equivalent of “postnominal descriptive element” before any learner-facing copy is changed. Preserve the suffix paradigm, examples, keys and original content until explicit approval.

No lesson, quiz, answer-key, runtime, parser, manifest, database, Botkeep, Telegram or deployment file was changed. No tests/CI, runtime checks, learner-response analysis or psychometric validation was performed. `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup; no separate backup is claimed.


## 5. Item-specific rationale proposals

The current reviewed answer key still gives only a generic confirmation for L6 Q3 and L8 Q3. The following concise explanations are proposed for editorial review; they are not applied.

**L6 Q3 — Key A (`beza`):**

> Di koma `hespê beza` de `beza` navdêrê `hesp` rave dike û agahiyek li ser wê zêde dike; ji ber vê yekê `bireserê navdêrê` ye. `hesp` serê koma navdêrî ye, ne bireserê navdêrê.

This explains why `beza` is the modifier and `hesp` is the head, while retaining the full technical term.

**L8 Q3 — Key A (`-in`):**

> Di paradigmaya §66 de, dema hêmaneke raveker li pey navdêrê nayê, `-in` forma gelemjimara nebinavkirî ye: `hespin` / `mehînin`. `-ên` veqetandeka binavkirî ye, lê `-a` di vê paradigmaya gelemjimara nebinavkirî de nîşana rast nîne. Dema hêmaneke raveker li pey navdêrê were, paradigma ya §67 formên cuda, wek `-ine`, bikar tîne.

This explanation aligns with the actual option set A `-in`, B `-ên`, C `-a`, and the §66/§67 distinction. It should be paired with the proposed explicit stem wording in Section 3 so that “bê bireser” does not carry an unintended clause-level reading.

The exact Kurdish wording remains subject to editorial review. No key letter or source text has been changed.
