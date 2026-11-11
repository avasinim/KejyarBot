# Course 2 — Early-lessons rationale targeted source recheck
**Date:** 2026-11-11  
**Status:** Audit record only; proposals remain unapproved and unapplied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## Scope
A fresh row-level comparison was made for the following proposed rationale items: L1 Q2; L2 Q2; L3 Q5; L4 Q2 and Q5; L5 Q1. Each was compared against the exact quiz stem/options, the relevant lesson explanation/examples, the proposed rationale wording (including superseding errata), and the reviewed answer-key row.

Verified source files:
- `course_data/latin_course_2_reviewed_draft_2026-11-10.md` — blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`
- `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md` — blob SHA `879e1525e720bdc25b8f6e896de3e388801238d0`
- `course_data/latin_course_2_source_aligned_lessons_01_12.md` — source-aligned reference, fetched from the archive branch during this pass.
- Base rationale proposal and refinement patch were fetched at their latest branch versions; superseding wording was applied when judging the proposal, not written back to the source files.

## Row findings

### L1 Q2 — four listed basic elements (key B)
The stem asks for the count of basic language elements. The lesson enumerates four: `tîp`, `kît`, `bêje`, and `komek`. It separately describes `qiset` as formed by sequencing groups, rather than listing it as a fifth member of that four-item inventory. The refined rationale preserves this distinction and matches the stem/key. **No correction identified.**

### L2 Q2 — `hesp` as common noun (key C)
The lesson's taxonomy distinguishes `hevenav` (common noun) from `serenav` (proper noun), and `hesp` is the generic animal name rather than a uniquely named person/place/thing. The refined rationale explains the keyed class and the relevant contrast. **No correction identified.**

### L3 Q5 — grammatical gender of inanimate nouns (key C)
The lesson explicitly says that inanimate things can have grammatical gender and that grammatical gender need not correspond to biological sex. The rationale accurately frames this as a property of the noun's grammatical classification, not as a biological claim. **No correction identified.**

### L4 Q2 and Q5 — indefinite plural paradigm (key C for both)
The lesson explicitly gives `hespek/hespin` as singular/plural in its particular indefinite paradigm and warns that `hespan` is an inflected form, not the same plural marker. The current corrected Q5 wording now says “ji forma yekjimara `hespek`” (rather than the earlier awkward comparative construction) and contrasts `hespin` with inflected `hespan`. The Q2 refinement correctly limits `-in` to this paradigm and does not generalize it to all Kurmanji plural nouns. **No further correction identified.**

### L5 Q1 — definition of inflection (key B)
The lesson defines `tewang` as form change according to grammatical role and conditions, and explicitly distinguishes it from number. It also warns that the simple “object is inflected” rule has exceptions in transitive past clauses: agent, object, tense/aspect construction and verb transitivity must be read together. The refined rationale appropriately avoids reducing inflection to word order and names the relevant grammatical and phonological conditions. The reference to tense and verb type is supported by the lesson's §56 note. **No correction identified.**

## Outcome
- Rows freshly rechecked in this pass: **6** (two rows in Lesson 4).
- New concrete key/rationale contradiction found: **0**.
- New proposal wording correction required: **0**.
- Existing corrections retained: L1 Q1 uses `qaydeyên`; L4 Q5 uses the corrected comparative phrase; L6 Q5 uses `rengdêra xwemalîn`, not `pronavê xwemalî`.
- This is a source-and-stem alignment check, not an independent native-speaker copy-edit or certification of the course's linguistic framework.
- No lesson, quiz, answer-key, runtime, parser, manifest, database, Botkeep, Telegram, deployment, test, or CI file was changed or run.
- No proposal was approved or applied. `main` remains read-only. The archive branch is not an independent offsite/ZIP backup; none is claimed.
