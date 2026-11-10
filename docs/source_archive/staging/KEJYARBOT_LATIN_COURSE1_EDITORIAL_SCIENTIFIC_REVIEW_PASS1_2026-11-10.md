# KejyarBot — Latin Course 1 editorial and scientific review (Pass 1)

Date: 2026-11-10
Repository: avasinim/KejyarBot
Reviewed branch: main (read-only)
Scope: Course 1, `course_data/latin_course_1_source_aligned_lessons_01_12.md`, its Course 1 answer key and related source-correction note.
Source boundary: Celadet Alî Bedir-Xan, Part I, “Elfabêya kurdî”, printed pages 11–36 (Nefel, Stockholm, 2002).

## Safety and change status
- Read-only review of the main branch.
- This note is append-only on `archive/preservation-audit-2026-11-10`.
- No lesson text, answer key, runtime code, manifest, `courses.json`, `lessons.json`, Botkeep, database, or deployment was modified.
- Findings below are editorial flags, not silent corrections. Original lesson content remains preserved.

## Confirmed editorial / orthographic findings

1. **Lesson 2 — duplicated explanatory note:** The paragraph beginning “Têbînî: Celadet di Beşa I de alfabeyê...” appears twice consecutively. Remove one copy in a future reviewed patch; this is a clear duplication, not a content change.
2. **Lesson 2 — inconsistent terminology:** The lesson alternates between “herfên taybet” and “herfên nîşankirî” for Ç, Ê, Î, Ş, Û. Choose one teaching label and define it once; retain the precise individual letter names thereafter.
3. **Lesson 5 — capitalization:** “Aşxane” is capitalized in the middle of a word-example table. Unless it is deliberately sentence-initial or a proper name, normalize to lowercase “aşxane”.
4. **Lesson 9 — likely spelling errors in examples:** “yêk” should be checked against the intended Kurmanji form “yek”; “çîya” should be checked against “çiya”. These appear in both example and exercise/test contexts, so a correction must update all occurrences consistently.
5. **Lesson 4 — punctuation/capitalization:** “Baldar be” begins a note without bold formatting or punctuation consistency relative to neighboring notes. Editorial normalization needed.
6. **Lesson 2 — repetition in learning design:** The lesson covers alphabet order, special letters, uppercase/lowercase, and letter pairs; section 3 repeats its explanatory note. Review the sequence after removing duplication so it does not over-teach the same point.

## Scientific / pedagogical review flags

1. **Short/long vowel classification:** Lessons 4–7 and 12 present E/I/U as short and A/Ê/Î/O/Û as long. This is attributed to Celadet Part I pp. 24–30. The distinction is explained as involving both duration and articulation, not merely stretching one vowel. Preserve that qualification. A final phonetic review should compare every example with the exact source table and avoid describing this as a universal or dialect-invariant phonetic law.
2. **Lesson 5 — example “avis”:** The form is unclear in this context and is not established by the currently inspected audit evidence as a valid example of A. Do not silently retain it as an authoritative lexical example; verify against the source or replace with a transparent, attested example.
3. **Lesson 9 — Y classification:** The course follows Celadet's alphabet inventory in counting W, X, Y, Z among 23 consonant letters. Keep the distinction between an alphabetic letter-class inventory and more detailed phonetic description explicit; do not imply that every letter has identical phonetic behavior.
4. **Lesson 11 — frequency tables:** The lesson gives raw counts from source pp. 33–34. It correctly warns that these are counts from the source's corpus/table, not universal frequencies. Add sample/corpus context only if the source itself supports it; do not convert raw counts into percentages without the denominator.
5. **Lesson 10 — sound vs. letter:** The conceptual distinction is sound, but examples should be described as orthographic contrasts, not as proof that writing represents every phonetic variation in speech.

## Question and answer-key spot checks

- Course 1 master key contains 60 rows (12 lessons × 5 questions), and the prior source audit reports exact answer-text/option matching for these rows.
- Spot-checked Lesson 1, 2, 5, 6, 7, 8, 9, 10, 11 and 12 questions against their displayed options and corresponding individual/master answer-key entries. No clear wrong answer letter was identified in this spot check.
- Lesson 2 Q4: only “Ç / ç” is a matching uppercase/lowercase pair among its options.
- Lesson 5 and 6 I/Î, U/Û items are internally consistent in the inspected questions.
- Lesson 9 Q5's intended answer (“Dengdar e”) matches the lesson's own classification, but its example spelling “çîya” should be normalized/verified.
- Lesson 12 Q4's intended answer is four words (“Ez / kurmancî / hîn / dibim”).

## Scope and unresolved work
- This pass covers Course 1's source-aligned lesson document and selected key artifacts; it is not a full source-line-by-line collation of every example against a page image.
- Course 2 (Part II grammar) has not yet been reviewed in this pass.
- The current runtime loader and draft manifest describe two separate 12-lesson Latin courses, but the manifest is marked draft; no claim is made here that either Latin course is active in the live Botkeep bot.
- Next review: continue Course 1 lesson-by-lesson through all remaining examples and all quiz distractors, then conduct a separate Course 2 grammar review against Part II. Keep both parts strictly source-separated.
