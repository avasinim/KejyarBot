# Course 2 Latin — Lessons 6, 8 and 12: noun modifier, adjective, and object terminology adjudication

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** source-aligned internal adjudication; editorial proposals only; no lesson, quiz, or key edits authorized or applied.

## Question

How should the course distinguish `bireserê navdêrê`, `rengdêr`, and bare `bireser`, especially where Lesson 6 labels `ev` in `ev keçik` as `pêşnavdêr/bireser` and Lesson 8 refers to a following `bireser/rengdêr`?

## Evidence from the staged course

Source-aligned file: `course_data/latin_course_2_source_aligned_lessons_01_12.md`, blob SHA `19090077a11dc9d7211987e958e560b328fcd3d6`.

### 1. Lesson 6 — `bireserê navdêrê` is a syntactic function/construction

Lesson 6 defines `bireserê navdêrê` as a word or group of words that describes, specifies, or adds information to a noun, and says it can occur before or after that noun. Examples include:
- pre-nominal: `ev keçik`, `kîjan mirov`, `çar xanî`, `hin çiya`, `çend kitêb`, `deh bizin`, `van zarokan`;
- post-nominal: `hespê beza`, `mehinên spehî`, `xencera min`, and nested noun groups such as `xencera xulamê min`.

These examples do not all belong to one word class. They include demonstrative, interrogative, numeral, indefinite, descriptive-adjective, and possessive/genitive-like material. Therefore, `bireserê navdêrê` is the broader noun-attached modifier/complement function in this course, not a synonym for the lexical class `rengdêr`.

### 2. Lesson 12 — `rengdêr` is a word class

Lesson 12 explicitly organizes adjectives into classes, including:
- `rengdêrên wesfîn` (descriptive adjectives);
- `rengdêrên îşarkî` (demonstrative adjectives);
- `rengdêrên jmarîn` (numeral adjectives);
- `rengdêrên pirsiyarkî` (interrogative adjectives);
- `rengdêrên nebinavkirî` (indefinite adjectives);
- `rengdêrên xwemalîn` (possessive adjectives).

It separately distinguishes independent pronouns from adjectives modifying an expressed noun. In particular, the course itself identifies demonstrative forms as adjective-like when they directly specify a noun, but as demonstrative pronouns when they stand independently.

### 3. Bare `bireser` — clause-level object role

Lessons 2 and 10 use bare `bireser` for the object role in a clause, including object-pronoun contexts. This is not the noun-attached modifier construction of Lesson 6. Where the noun-modifying construction is intended, retain the full phrase `bireserê navdêrê` to avoid ambiguity.

### 4. Lesson 8 — broad modifier vs adjective

Lesson 8's phrase `bireser/rengdêr` for material following a noun is too compressed to serve as a stable taxonomy. The form choice is tied to a following complement/modifier environment, but not every possible complement of a noun is necessarily an adjective. The lesson should distinguish the broader syntactic environment from the narrower adjective class. This is especially important because its inflectional paradigms are conditioned by the construction, not simply by the label `rengdêr`.

## Adjudication

Use three distinct levels:

| Term | Course-level meaning | Editorial rule |
|---|---|---|
| `bireserê navdêrê` | Broad syntactic noun-attached modifier/complement function | Keep the full term where the broader construction is meant; do not treat it as a word class |
| `rengdêr` | Adjective, a lexical/grammatical word class | Use for adjective subclasses; it can realize a noun-modifying function but does not cover every noun complement |
| `bireser` | Clause-level object role in the course's syntactic explanations | Do not use bare form as shorthand for `bireserê navdêrê` |

For the specific examples:
- `ev keçik`: classify `ev` as a demonstrative adjective/modifier (`rengdêra îşarkî` in the course's Lesson 12 framework) because it modifies an expressed noun.
- `Ev hat.`: classify `Ev` as an independent demonstrative pronoun.
- `mehinên spehî`: `spehî` is a descriptive adjective within the broader noun-modifying construction.
- `xencera min` and nested genitive-like examples: noun-attached possessive/genitive material; do not relabel every such element as an adjective without checking the source's taxonomy.
- `hespê beza`: retain `bireserê navdêrê` as the broad construction label; do not call `beza` a clause-level object.

## Specific editorial recommendations

1. Remove or explain the unresolved slash-pair `pêşnavdêr/bireser` in Lesson 6 only through a separately approved patch. The source-aligned course itself later classifies noun-modifying demonstratives under `rengdêrên îşarkî`; that is the most internally consistent provisional label for `ev` in `ev keçik`.
2. Preserve the broader Lesson 6 heading/definition `bireserê navdêrê`, but clarify that it is a syntactic function/construction that can be realized by different word classes or phrases.
3. In Lesson 8, avoid presenting `bireser/rengdêr` as a pair of interchangeable labels. Prefer a broad phrase such as “complement or modifier following the noun”; name `rengdêr` only when the following element is specifically an adjective.
4. Keep bare `bireser` reserved for clause-level object function in explanations where ambiguity is possible.
5. Keep the independent-pronoun contrast explicit: classify by syntactic use, not by the surface form `ev/ew` alone.

## Limits

- This ruling is internally supported by the staged Lessons 6, 8 and 12, not a claim that all Kurdish grammar traditions use these labels identically.
- The primary-source page images for Lesson 12 were not reopened in this pass; the Lesson 12 taxonomy is currently checked against the source-aligned staged text.
- The direct page-image review for Lesson 6 §§59–60 (printed p.61) is documented in `KEJYARBOT_LATIN_COURSE2_LESSONS6_7_PAGE_IMAGE_REVIEW_2026-11-10.md`, blob SHA `6ff6e84792bc13f5835010401bfab89acd446295`.
- Lesson 8 source-page review §§65–71 (printed pp.63–68) is documented in `KEJYARBOT_LATIN_COURSE2_LESSON8_PAGE_IMAGE_REVIEW_2026-11-10.md`, blob SHA `0eaa37c517fdaf244b48cc69f953400393ab0812`.
- The precise technical sense of `pêşnavdêr` has not been confirmed against the primary source; do not assert a definitive replacement solely from its surface morphology.

## Preservation

No source-aligned lesson, reviewed lesson, quiz, answer key, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was changed. This is an append-only staging note. No tests/CI or live runtime checks were performed. All work remains on `archive/preservation-audit-2026-11-10`; `main` remains read-only.
