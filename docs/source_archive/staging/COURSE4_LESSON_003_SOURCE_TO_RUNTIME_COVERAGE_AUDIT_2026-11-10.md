# Course 4 — Lesson 3 source-to-runtime coverage audit (2026-11-10)

## Purpose and preservation rule

This is an append-only audit record. It does not replace the owner-supplied source, the current runtime lesson, or any earlier review. The owner source remains preserved unchanged in:

- `docs/source_archive/COURSE4_LESSON_03_NAME_SOURCE_AND_AUDIT_2026-11-07.md`
- Source file blob SHA on `main`: `d91b5aeba634516a783f946d51264fd8116bc879`

The owner-supplied noun lesson material is the opening source section, ending immediately before the archived review text beginning “ئەم دەقە وەک ماددەی سەرچاوەی وانەی «ناو»”. The same file also contains later review notes and progress history; those later notes are not to be mistaken for the owner's raw lesson text.

## Runtime snapshot checked

- Branch: `main`
- File: `course_data/grammar_course4_lessons.json`
- Runtime JSON blob SHA: `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`
- Lesson ID: `grammar_03`
- Title: `وانەی ٣: پێناسە و تایبەتمەندییەکانی ناو`
- Review status: `scientific_review_complete_with_qualified_notes`

Current structured inventory:

| Section | Count |
|---|---:|
| Key points | 35 |
| Examples | 15 |
| Activities | 3 |
| Exercises | 5 |
| Comprehension items | 10 |
| Quiz questions | 8 |
| Appendix items | 30 |

## Source-to-runtime coverage

The core subject matter from the owner source is represented in the current lesson, with scientific distinctions and qualifications:

1. **Definition and identification of nouns:** noun as a word class, identified through form, grammatical behaviour, distribution and meaning—not merely by naming visible objects.
2. **Reference and semantic groupings:** common/proper nouns, collective nouns, and concrete/abstract or conceptual nouns.
3. **Grammatical categories:** absolute, indefinite and definite forms; singular and plural; the distinction between definiteness and number.
4. **Gender:** the source's natural-sex examples are not taught as a productive grammatical-gender system. The runtime explicitly distinguishes natural gender from grammatical gender in Sorani.
5. **Word structure:** simple, derived and compound nouns; derivational morphology; compounds are not classified by spacing or joined spelling alone.
6. **Nominal morphology:** the roles and limits of `-ێک`, `-ەکە`, `-ان`, `-ەکان`, and the need to account for vowel-final stems and dialect variation.
7. **Compound formation and linkers:** evidence-backed discussion of `-ە-` and `-و-`, with a distinction between lexical compounds, ordinary coordination and phonological linking.
8. **Sentence function:** noun class is kept separate from syntactic function such as subject or object.

The runtime examples include evidence-backed cases such as `گوڵەباخ`, `گاکێوی`, `ئاسنگەر`, and `کچۆڵە`. The appendix retains source references and qualifications for these analyses.

## Material retained as qualified source evidence, not promoted to general rules

The owner source also contains lists and analyses that should remain visible in the source archive, but should not be taught as unrestricted standard Sorani rules without stronger dictionary, corpus or dialect-specific evidence. The current appendix records these limitations, including:

- echo formations / `ئیتباع` and the individual pairs supplied in the source;
- sound-symbolic nouns and proposed analyses such as `بۆڕەبۆڕ`, `قۆڕەقۆڕ` and `تەپەتەپ`;
- the broad diminutive-suffix list, distinguishing genuine derivational suffixes from the indefinite marker `-ێک`;
- `-ەمەنی` examples and the proposed plural markers `-ات`, `-هات`, `-ها`;
- `-گەل/-گال`, whose distribution must be identified by dialect and construction;
- the supplied candidate interfix examples that have not all been independently validated.

This is a deliberate evidence qualification, not deletion of the owner's material: the original list remains intact in the raw source archive, while the lesson appendix explains why unverified forms are not presented as universal rules.

## Scope boundaries preserved

The source also discusses infinitival nominalization and compound verbs. These are not expanded as if they were ordinary noun subclasses in Lesson 3. The runtime preserves explicit scope notes directing the related material to the relevant later lessons (compound verbs in Lesson 30, infinitival nominalization in Lesson 31, and verbal derivation in Lesson 29).

## Quiz and exercise integrity checks

A structural check of the current Lesson 3 quiz confirmed:

- all 8 questions have non-empty question text;
- each question has exactly 4 options;
- all answer indices are within the available options;
- all 8 questions have non-empty explanations;
- correct-answer positions are balanced exactly: 2 each in option positions 1, 2, 3 and 4.

The 3 activities, 5 exercises and 10 comprehension items are present in the runtime object. This is a structural and topical consistency check, not a claim of independent specialist approval of every linguistic analysis.

## Decision

- No missing core topic or evidence-backed correction was identified that justifies creating a new Lesson 3 append-only patch at this checkpoint.
- No empty, duplicate or backdated patch is to be created.
- The 2026-11-07 owner source remains unchanged.
- The current runtime lesson on `main` remains unchanged by this audit.
- This audit was written only to the preservation branch; no Botkeep, SQLite, Railway, production runtime or Telegram state was changed.

## Next audit step

Continue with a source-item-level reconciliation of the remaining owner examples and their corresponding appendix qualifications. Any future addition must cite the exact source item and supporting linguistic evidence, and must be appended without deleting or rewriting the existing lesson material.
