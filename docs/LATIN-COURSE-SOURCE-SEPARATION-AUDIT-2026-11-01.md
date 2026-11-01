# KejyarBot — Latin course source separation audit
Date: 2026-11-01
Branch: audit/latin-courses-source-review-2026-11-01

## The two designated source books are distinct

### Course 1 — Bingehên Rastnivîsîna Kurmancî ya Latînî
Designated Course 1 source recovered in the user's Library:
- Dr. Efrasîyab Şikofteh, *Rê zimanê Kurmancî*.
- The title page gives the author and identifies the book as a Kurmanji grammar.
- The preface explicitly says the book teaches reading and writing Kurmanji in the North Khorasan Kurmanji dialect.
- The contents list Lesson 1, “Alfabê ya zimanê kurmancî” (printed p. 11) and Lesson 2, “Alfabê ya kurmancî bi dîtina dengnasînê” (contents list: printed p. 44).
- The alphabet section states that the Kurmanji alphabet has 31 letters (printed p. 12). Its following pages provide letter-specific examples and sentences (e.g. printed pp. 13–28).
- Printed p. 29 explicitly lists 8 vowel letters and 23 consonants, matching the 31-letter inventory. It uses the course-specific terms `tîpên dengdar` for vowel letters and `tîpên bêdeng` for consonants; printed p. 46 identifies `W` and `Y` as semivowels (`nîvdeng`). Printed pp. 45–46 divide vowels into 3 short (`E, I, U`) and 5 long (`A, Ê, Î, O, Û`). Printed pp. 56–60 provide letter-specific phonetic descriptions and distributions.

### Course 2 — Bingehên Gramera Kurmancî
Source:
- Celadet Alî Bedir-Xan, *Elfabêya Kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002.
- Course 2 uses Part II, “Bingehên gramera kurdmancî” (printed p. 37 onward).
- Celadet's book is the designated source for Course 2 only; it is not used as the source for Course 1.

## Corrections made on this isolated branch

1. Identified Course 1's distinct source as Dr. Efrasîyab Şikofteh's *Rê zimanê Kurmancî* (Havîn 2010), Ders 1 (printed pp. 11–43) and Ders 2 (from printed p. 44). This is a different book from Course 2's Celadet source.
2. Updated the source separation index in `course_data/latin_courses_master_draft.md`.
3. Updated Course 1 source metadata in the runtime and catalogue to Şikofteh's book. The book identity is established from the Library PDF. Source checks and corrections are recorded below; a final human-level linguistic proofread of every dialect form and exercise remains outstanding.
4. Removed the previous incorrect Celadet Part I attribution from Course 1 metadata. Course 2 remains exclusively attributed to Celadet's Part II.
5. Standardized the `🤖 کەژیار — KejyarBot@` footer in all 12 lessons of each Latin course.
6. Fixed the runtime quiz parser so the KejyarBot footer is not appended to the final answer option in lessons where the quiz is the final section.

## Source checks and remaining audit

- The 31-letter alphabet count in Course 1 Lesson 1 agrees with Şikofteh (printed pp. 12, 29).
- Course 1 Lesson 2's C, I and Ş examples were replaced with `cêran`, `dil` and `şîr`, which are directly attested in the designated book's alphabet examples (printed pp. 14 and 18).
- Replaced the Lesson 1 example for `I` (`kin`) with `dil`, which appears in Şikofteh's I-letter examples (printed p. 18).
- Removed three imported Bedir-Xan source notes from Course 1 Lessons 4, 6, and 7 and replaced them with source-based explanations based on the designated Şikofteh book (printed pp. 45–46, 56–60). Course 1 no longer cites the Course 2 book inside its lesson bodies.
- Corrected Course 1 Lesson 8 to distinguish `V` (consonant) from `W` and `Y` (semivowels), following Şikofteh's phonetic section (printed p. 46).
- Clarified Course 1 Lesson 3's taxonomy: Şikofteh's printed p. 29 groups the 23 non-vowel letters as `bêdeng`, while the phonetic classification (printed p. 51) distinguishes `W` and `Y` as semivowels. The lesson now states both levels explicitly instead of defining all 23 as airflow-obstructing consonants.
- Changed Course 1's vowel/consonant terminology to match Şikofteh (`dengdar` for vowels, `bêdeng` for consonants, `nîvdeng` for semivowels). Course 2 retains its separate Celadet-based terminology; the two systems are not blended.
- Şikofteh's alphabet pages give concrete dialect-specific words and sentences. The Lesson 1 I-vowel example was changed from `kin` to `dil`, which appears among the examples visible on printed p. 18 (`bivir, bizin, dil, hêstir, hingiv, zivistan`). This is a direct match to the designated Course 1 source.
- The designated Course 1 PDF provides a comparison map for Course 1's lesson sequence: Lessons 1–3 use the alphabet inventory and letter list (printed pp. 12–29); Lessons 4–7 use the short/long vowel classification and letter descriptions (pp. 45–60); Lessons 8–10 use the consonant/semivowel and sound-letter descriptions (pp. 46, 60); Lesson 11 uses the spelling rules for adjacent vowels and repeated letters (p. 61); Lesson 12 uses syllable division and examples (p. 62). Lessons still require a final human-level linguistic proofread for every dialect form and exercise.
- The source has an internal numerical inconsistency: printed p. 46 says there are 32 consonants, while printed p. 29 gives the 8-vowel + 23-consonant inventory that totals 31 letters. The draft follows the internally consistent 31/8/23 count from p. 29 and does not repeat the apparent p. 46 error.
- Rebuilt Course 1 Lessons 11–12 against the designated Şikofteh book's printed pp. 61–62: Lesson 11 now teaches vowel separation and repeated-letter spelling rules; Lesson 12 teaches syllable structure and division. The corresponding 10 quiz answer-key rows were updated.
- KejyarBot footer branding (`🤖 کەژیار — KejyarBot@`) has now been standardized across all 12 lessons in both Latin course documents. Editorial provenance blocks are retained outside learner text and the runtime loader strips them from lesson bodies.
- Removed explicit author/book citations from learner-facing text in both Latin courses; source identities and editorial notes remain in the source documents and this audit.
- Course 1's 60-question answer key matches its lesson options structurally. The source book is identified; the remaining work is a line-by-line linguistic proofread of examples and explanations.
- Course 2's source page map is confirmed against the PDF contents and body: nouns/hevenav/serenav p. 51; gender p. 52; number pp. 55–56; tewang pp. 57–60; noun modifiers p. 61; definite/indefinite determiners pp. 62–67; pronouns pp. 71–87; adjectives pp. 89–95; numerals pp. 97–100.
- Compared Course 2's noun, gender, number, tewang and determiner examples against the PDF. In Lessons 4 and 8, corrected the feminine indefinite forms `mehinik/mehinin/mehinine` to `mehînek/mehînin/mehînine`, matching the printed p. 64–65 examples and the distinction between `-ek/-in` and `-eke/-ine` patterns.
- Course 2 pronoun checks: `hon` is the source's second-person plural form; `wî/wê` are masculine/feminine third-person object forms; `hev/êk` are reciprocal pronouns (printed pp. 72–78). The lesson does not introduce unsupported `hevdu` forms; it notes that `êk` is especially used in Central Kurdistan.
- Course 2 Lesson 11 correctly separates relative pronoun `ko` (printed p. 83) from conjunction `ko` (printed p. 84); they have different functions and must not be merged.
- Course 2 Lesson 12 follows the source's separate adjective and numeral sections (pp. 89–100). The grammar section itself states that it is incomplete and omits verbs, adverbs, prepositions and syntax; the bot course does not claim to teach those omitted topics.
- No Course 1 material was imported into Course 2.
- Final static validation mirroring the runtime quiz parser checked all 24 lessons: Course 1 = 60 questions / 60 matching answer keys; Course 2 = 60 questions / 60 matching answer keys; 120/120 total. All 24 lessons have the KejyarBot footer and no provenance note leaks into the lesson body. This was a content/parser simulation, not a GitHub Actions or local Python test run.

## Safety / release boundary

- This branch was created from `fix/course3-latin-finalization-2026-11-01`.
- No edits were made to `main`, production data, production bot, Botkeep, live runtime, or deployment.
- No PR was created or merged.
- Dynamic speech remains disabled.
- This audit is editorial and source-provenance work; it does not claim runtime activation or deployment.


## Kurmanji Latin language validation

- Both canonical lesson documents contain 12 lesson sections each.
- All learner-facing explanations, examples, exercises, questions and answer options are written in Kurmanji using the Latin alphabet. The only non-Latin-script content in the lesson bodies is the agreed Kejyar mascot signature `کەژیار`.
- Both 60-row answer-key documents now use Kurmanji Latin for their headings, answer explanations and editorial notes; no Sorani or Persian script remains in either answer key.
- Updated the runtime manifest, catalogue and runtime loader so the source identity for each course is identical across all three places; the bot's startup metadata check can compare them without a false mismatch.
- Updated the regression tests to assert the separate Şikofteh and Celadet sources and to reject Arabic-script content in learner lessons and answer keys (except the Kejyar mascot signature).
- Course 1 follows the North Khorasan Kurmanji language scope of Şikofteh's book. Course 2 follows the separate Kurmanji grammar scope of Celadet's Part II. Do not transfer rules, terms or examples between these books.

## Additional source corrections — 2026-11-01

- **Course 1, Lesson 11:** the Şikofteh source, printed p. 61, describes two vowels (dengdêr) meeting inside a word or across a word boundary/suffix, and the insertion of y, w or h between them. The lesson had incorrectly called these consonants (dengdar). The lesson title, explanation, exercises, quiz wording and summary now consistently use dengdêr. The examples gî + an → gîyan, du + emîn → duwemîn, dirêj + î → dirêjahî/dirêjayî, and çîya + ê → çîyayê are retained from the source. The source also treats repeated-letter reduction as a separate orthographic point on the same printed page.
- **Course 2, Lesson 9:** Celadet Part II, printed pp. 71–73, distinguishes neuter personal pronouns from the agent forms. The personal-pronoun list includes neuter ew, but the agent-form table maps third-person singular to wî/wê; it does not provide a separate neuter agent form ew. The lesson table now leaves that cell unassigned (—) and explains the distinction rather than inventing ew → ew.
- **Course 2, Lessons 10–11:** verified against Celadet Part II, printed pp. 77–84. The reciprocal forms hev/êk (with êk identified by Celadet as described by Celadet with the source wording `li nîvrohelatê Kurdistanê` (the directional term is retained literally pending an independently verified translation)), the compound pronoun forms jê/lê/pê/tê and jev/jêk, lev/lêk, pev/pêk, tev/têk, the two demonstrative sets ev/ew and yê/ya/yên, and the distinction between relative-pronoun ko and conjunction ko are supported by the source.
- Regression tests were added for the Course 1 vowel-contact terminology and the Course 2 neuter-agent distinction.

- **Course 1, Lesson 8:** Şikofteh, printed p. 46, treats `W` and `Y` as semivowels, while `xw`, `kw` and `gw` are treated separately as `pevdeng` clusters. The lesson now explicitly distinguishes these categories and uses `xew` (where W is final) rather than `xwarin` (where W belongs to the `xw` cluster) as the W-position example.
- A regression test now protects the distinction between the W semivowel and `pevdeng` clusters.

- **Course 2, Lesson 10:** corrected the regional note for reciprocal `êk`: Celadet's printed p. 78 describes the regional usage with the wording `li nîvrohelatê Kurdistanê`; the source wording is retained literally rather than imposing an uncertain English/Sorani directional translation. Added a regression test for this source-specific distinction.
