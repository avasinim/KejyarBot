# Latin Courses 1–2 — lesson sequence and prerequisite audit
Date: 2026-11-10
Branch: `archive/preservation-audit-2026-11-10`

## Scope and preservation

This is a separate editorial audit note based on the two reviewed drafts:
- `course_data/latin_course_1_reviewed_draft_2026-11-10.md`
- `course_data/latin_course_2_reviewed_draft_2026-11-10.md`

The pass checks lesson order, prerequisite flow, repeated concepts, transitions, and scope boundaries. It does not alter either reviewed draft, quiz, answer key, original source file, runtime, database, Botkeep, Telegram, or deployment. The `main` branch remains read-only. This is a first structural pass, not a final certification of every example or every learning outcome.

## 1. Course 1 — alphabet and Latin-script foundations

### Current sequence observed

1. Whole alphabet and letter-case inventory (31 letters; 8 vowels / 23 other letters).
2. Alphabet order and marked Kurdish letters.
3. Vowels versus consonant letters.
4. Short-vowel group: E, I, U.
5. Long-vowel group: A, Ê, Î, O, Û.
6. I / Î contrast.
7. U / Û contrast.
8. V / W contrast.
9. X, Y, Z.
10. Speech sound versus written letter.
11. Counts in the source's letter-frequency table.
12. General alphabet review.

### Sequence strengths

- The inventory and alphabet order come before individual letter groups; this is a sound whole-to-part progression.
- The vowel/consonant classification is introduced before short/long vowel group practice.
- The short and long vowel groups precede the focused I/Î and U/Û contrasts, so learners encounter the categories before the minimal contrasts.
- The V/W contrast follows the vowel sequence and the X/Y/Z lesson then completes coverage of the less familiar consonant letters.
- The final lesson revisits the complete 31-letter system after the focused lessons, functioning as consolidation.
- Lesson 11's source-table work is correctly framed as reading raw source counts rather than treating them as universal frequency percentages.

### Sequence risks / proposed editorial actions

1. **Lesson 10's sound-versus-letter distinction arrives relatively late.** Learners already meet words, vowel sounds, and V/W sound contrasts in earlier lessons. This is not a factual error: the later placement can work as a conceptual synthesis. Add a short anticipatory sentence in Lesson 1 or 3 that says the course initially uses letter labels for learning the alphabet and will later distinguish written letters from speech sounds explicitly. Do not move or rewrite the full Lesson 10 without reviewing its source examples.
2. **Lesson 8 and Lesson 9 are contrast/coverage lessons, but their bridge could be clearer.** Add a one-sentence transition explaining that after vowel contrasts, the course returns to consonant letters whose forms or sounds may be unfamiliar. This is an editorial bridge only.
3. **Lesson 11 is a change of task type.** It moves from identifying and distinguishing letters to interpreting a historical/source table. Keep it as an enrichment/application lesson, and label the task explicitly as “reading the source table,” not as a universal statement about present-day Kurdish frequency.
4. **Lesson 12 repeats several earlier outcomes.** This repetition is useful as retrieval practice, not automatically redundant. Ensure its questions require learners to combine classifications and contrasts rather than simply repeat Lesson 1 facts. This is a future assessment enhancement, not a reason to delete content.

No lesson-order reversal is recommended in Course 1 during this pass.

## 2. Course 2 — grammar foundations and categories

### Current sequence observed

1. Grammar and language elements: tîp → kît → bêje → komek.
2. Nouns: common and proper nouns.
3. Grammatical gender.
4. Number.
5. Noun inflection / case (tewang).
6. Noun modifiers (bireser).
7. Definite suffixes.
8. Indefinite suffixes.
9. Personal pronouns and agent forms.
10. Object pronouns and reciprocal/reflexive-related forms.
11. Demonstrative, relative, and interrogative pronouns.
12. Adjectives and numeral pronouns.

### Sequence strengths

- The course starts with language structure, then moves to the noun as a central grammatical category.
- Gender and number precede case/inflection, giving learners core noun properties before they encounter inflected forms.
- Noun modifiers are introduced before definiteness suffixes; this gives a broad phrase-level view before more specific noun marking.
- Personal pronouns and agent forms precede object-pronoun forms, allowing the latter to build on the personal-pronoun paradigm.
- The distinction between pronouns and noun modifiers is explicitly signposted in Lesson 6, which helps prevent category confusion.
- Lesson 11's relative `ko` and conjunction `ko` distinction is a useful late-course contrast after the personal-pronoun lessons.

### Sequence risks / proposed editorial actions

1. **Lesson 6 uses demonstrative forms before Lesson 11 formally teaches demonstrative pronouns.** Lesson 6 already lists `ev keçik`, `van zarokan`, and explains that `ev/ew` can function differently when standing alone. This is a legitimate preview, but it creates a dependency. Add a short cross-reference in Lesson 6: “Here `ev/ew` are shown as noun modifiers; their standalone pronoun use is treated in Lesson 11.” Preserve the current examples and do not move the full Lesson 11 content.
2. **Lesson 7–8 depend on gender, number, and case distinctions.** The order supports this, but the transition into definite/indefinite suffixes should explicitly remind learners that suffix selection and noun inflection are related but distinct operations. The current draft already begins to distinguish them; retain and reinforce that contrast with one paired example only if source verification supports it.
3. **Lesson 9's “forma kirarî/agent” is conceptually demanding.** The course has already introduced case and number, but the transition should remind learners that these are pronoun forms used in specific clause structures, not a second set of unrelated personal pronouns. Keep Celadet's terminology and explain the function without renaming the category.
4. **Lesson 10 combines object pronouns with reciprocal forms.** These are related in the source's pronoun section but may represent distinct subskills. Add explicit subheadings and a brief “what changes from Lesson 9” bridge; do not split or reorder until the source's section structure and quiz dependencies are checked.
5. **Lesson 11 groups several pronoun subcategories.** The breadth is high. Keep the source sequence, but make the internal hierarchy visible: demonstrative forms; relative `ko`; interrogative and indefinite forms; possessive forms. Ensure each subsection has a distinct example and does not imply that every listed form behaves identically.
6. **Lesson 12 is the broadest lesson.** It contains six adjective classes, degrees of comparison, and a separate `jmarnav` category with subgroups. The separation is linguistically important and already stated, but the combined scope risks cognitive overload. Preserve it for now; consider splitting into two lessons only after confirming the original course architecture, lesson numbering, quiz mappings, and source coverage. Do not split the runtime or change the 12-lesson structure in this audit.
7. **Cross-course terminology boundary:** Course 1 uses `herf` in the alphabet teaching context while Course 2 follows the source's `tîp` terminology for written signs. Do not globally normalize one into the other. A compact glossary note can explain the different instructional contexts.

## 3. Cross-course continuity

- Course 1 establishes alphabetic letter categories and introduces the distinction between written sign and speech sound; Course 2 begins with the written/linguistic building blocks. The courses should be presented as related but independent source parts, not as if Course 2 were a continuation of every phonetic claim in Course 1.
- Course 1's `dengdêr/dengdar` inventory labels should not be silently converted into a modern phonetic taxonomy in Course 2.
- The shared use of forms such as `ev/ew`, `deng`, and `tîp/herf` should be accompanied by context-specific definitions where necessary.
- Course 1 Lesson 12 is a cumulative alphabet review; Course 2 Lesson 12 is a new grammar-category lesson, not a cumulative review. Avoid describing the two final lessons as equivalent in pedagogical function.

## 4. Priority queue

### Priority A — low-risk editorial bridges
1. Add the `ev/ew` preview-to-Lesson-11 cross-reference in Course 2 Lesson 6.
2. Add a one-sentence sound/letter preview in Course 1 Lesson 1 or 3, while leaving Lesson 10 as the full explanation.
3. Add a transition before Course 2 Lesson 7 clarifying the difference between noun inflection and definiteness marking.
4. Add internal subheadings/transition sentences in Course 2 Lessons 10–11 without changing source terminology.

### Priority B — review before any structural change
1. Evaluate whether Course 2 Lesson 12 should remain integrated or be divided; do not change numbering or quizzes without a full dependency map.
2. Review Course 1 Lesson 12 quiz for transfer/application rather than simple recall.
3. Verify every transition example against the printed source before inserting new linguistic examples.

## 5. What this pass does not establish

- It does not certify that every lesson example is source-exact.
- It does not prove that all learning outcomes are measurable or that all distractors are optimal.
- It does not establish runtime, Botkeep, Telegram, database, or deployment status.
- It does not authorize any change to the active course data.

## 6. Next audit step

Build a lesson-dependency matrix for all 24 lessons. For each lesson, map: prerequisite concepts, concepts first introduced, concepts previewed for later, repeated concepts, quiz coverage, and source section/page. Then implement only low-risk explanatory bridges in a separate reviewed draft, preserving all original lesson and quiz content and verifying every changed file by fetching it again from the archive branch.
