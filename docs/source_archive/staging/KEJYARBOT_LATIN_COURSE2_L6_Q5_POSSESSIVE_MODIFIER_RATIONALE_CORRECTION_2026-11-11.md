# Course 2 — Lesson 6 Q5 possessive-modifier rationale correction
**Date:** 2026-11-11  
**Status:** Editorial correction proposal; not approved or applied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## 1. Finding

The original 44-row proposal for L6 Q5 says that `min` in `xencera min` expresses possession / a postnominal element. The later refinement patch changes this to:

> Di koma xencera min de min pronavê xwemalî ye ku têkiliya xwedîtiyê ya navdêrê diyar dike.

This refined label is not consistent with the reviewed course taxonomy.

## 2. Exact course evidence

The reviewed Lesson 6 draft:
- lists `xencera min` as a postnominal example of `bireserê navdêrê`;
- keys L6 Q5 as C, `bireserê navdêrê`.

The reviewed Lesson 12 draft:
- labels `hespê min`, `mehînên te`, `kitêba vî`, etc. as examples of **`rengdêrên xwemalîn`** (possessive adjectives);
- distinguishes those noun-modifying forms from **`pronavên xwemalîn`**, which are formed from `yê/ya/yên` plus a personal pronoun and replace an understood noun/group;
- explicitly says that `yê min` / `yên min` as pronouns are different from `hespê min` as a possessive adjective.

Therefore, in `xencera min`, `min` is not a `pronavê xwemalî` under the course's own Lesson 11–12 terminology. It is the possessive modifier in an expressed noun phrase, aligned with the Lesson 12 category `rengdêra xwemalîn`.

## 3. Corrected proposed wording

Replace only the L6 Q5 rationale proposal in the refinement patch with:

> Di koma `xencera min` de `min` rengdêra xwemalîn e ku têkiliya xwedîtiyê ya navdêrê `xencera` diyar dike. Tevahiya komê komeke navdêrî ye; `min` li vir ne pronavê xwemalî ye ku li şûna navdêrekê bisekine.

A more concise version, if the editorial style avoids repeating the noun-class label:

> Di koma `xencera min` de `min` hêmaneke xwemalîn e ku xwedîtiya `xencera` diyar dike. Ji ber ku navdêr `xencera` eşkere ye, `min` li vir rengdêra xwemalîn e, ne pronavê xwemalî.

The first version is preferred because it uses the course's explicit class label and makes the pronoun/adjective contrast clear.

## 4. Terminology boundary

- `rengdêrên xwemalîn`: possessive adjectives modifying an expressed noun, e.g. `hespê min`, `xencera min`.
- `pronavên xwemalîn`: possessive pronouns such as `yê min`, `ya min`, `yên min), which replace an understood noun/group.
- `bireserê navdêrê`: the broader noun-attached modifier function taught in Lesson 6. The possessive adjective `min` realizes that function in `xencera min`.

Do not use `pronavê xwemalî` as a generic name for every possessive-looking form.

## 5. Impact and preservation

- This corrects a terminology error in a proposal only.
- L6 Q5 key C remains unchanged.
- No lesson, quiz, answer-key, runtime, parser, manifest, database, Botkeep, Telegram or deployment file was changed.
- No tests/CI, runtime checks, learner-response analysis or psychometric validation was performed.
- `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup; no separate backup is claimed.
