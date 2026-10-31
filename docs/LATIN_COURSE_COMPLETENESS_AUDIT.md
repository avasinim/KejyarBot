# Latin Courses — Content Completeness and Release Gate

**Checked:** 2026-10-31  
**Branch:** `work/latin-courses-source-alignment-2026-10-31`  
**Status:** runtime integration active on this isolated work branch; production bot/deployment untouched. The lesson texts remain editorially reviewed drafts pending final text verification and independent native-speaker review.

## Scope separation

The bot's two Latin courses are distinct:
- **Course 1:** Kurmanji Latin orthography, sourced from Part I, *Elfabêya kurdî*, pp. 11–34.
- **Course 2:** Kurmanji grammar, sourced from Part II, *Bingehên gramera kurdmancî*, pp. 37–100.

Do not substitute the separate Sorani/Arabic-script 22-lesson `orthography_foundations.json` course for either Latin course. Do not apply Avasin Academy Arabic-script orthography rules to these bot courses.

## Course 1 — 12 lessons

| Lesson | Draft status in this branch | Quiz/key status |
|---:|---|---|
| 1 | Corrected draft present | Separate key; exact option test |
| 2 | Recovered draft restored from `Pasted text(1).txt` | Five options restored; master key matches exact option text |
| 3 | Recovered draft restored from `Pasted text(1).txt` | Five options restored; master key matches exact option text |
| 4 | User-provided full lesson text confirmed in conversation; current branch copy is source-aligned; final line-by-line reconciliation remains editorial work | Separate key; exact option test |
| 5 | User-provided full lesson text confirmed in conversation; current branch copy is source-aligned; final line-by-line reconciliation remains editorial work | Separate key; exact option test |
| 6 | Recovered draft restored from `Pasted text(1).txt` (brand casing/layout normalized) | Five options restored; master key matches exact option text |
| 7 | Corrected draft present | Separate key; exact option test |
| 8 | Recovered from `Pasted markdown(3).md`; V position corrected and source contrasts added | Key matches original option order; exact option test |
| 9 | Recovered from `Pasted markdown(3).md`; `xwîn` moved to Î and malformed exercise corrected | Key follows original option order; exact option test |
| 10 | Corrected draft present | Separate key; exact option test |
| 11 | Corrected draft present | Separate key; exact option test |
| 12 | Recovered from `Pasted markdown(3).md`; ezafe and locative word-bank forms corrected | Key matches original quiz options; exact option test |

**Recovery completed:** Lessons 2, 3, and 6 have been restored from the user's Library file `Pasted text(1).txt`; Lessons 8, 9 and 12 have been restored from `Pasted markdown(3).md`. Their original teaching text and quiz option order were recovered; the master answer-key entries were corrected to match the exact selected option text. Lesson 6 received only Markdown/layout and brand-casing normalization. Lessons 8 and 9 preserve the recovered original quiz option order; Lesson 12 preserves its original quiz and reading sequence with two minimal corrections. Lessons 4 and 5 were supplied in full in the conversation. Their current branch copies are source-aligned; preserve the user-provided wording as the reference and do not ask the user to resend them.

## Course 2 — 12 lessons

- One source-aligned 12-lesson draft is present. The user supplied the full texts for Lessons 1–3 in the conversation; the current branch copies are editorially source-aligned and must be checked against those user messages, not treated as invented originals. Do not ask the user to resend the texts. Lesson 1 was checked against printed pp. 37–38: the source's four elements are Tîp, Kît, Bêje, and Komek; Qiset is described as arising from the sequence of Komek units, not as a fifth item in that list. The lesson's grammar definition, Kurmanji-language introduction, source examples, quiz, and key were aligned accordingly. Lesson 9 now explicitly includes the source's three-way pronoun gender distinction (nêr, mê, nêtar), including the neutral use of ew, and has a regression guard.
- Lessons 4–12 are editorially revised from recovered lesson material.
- Lesson 12: the expanded six-category draft is now selected and copied into the canonical 12-lesson master. The former baseline section was replaced; the separate replacement file is retained only as an editorial snapshot. The consolidated master key was aligned to the selected quiz options and is regression-tested. Do not load the snapshot as a second lesson.
- The consolidated key must match the exact quiz options in the selected lesson draft. The current canonical Course 2 Lesson 1 quiz and key are source-aligned and regression-tested. The user supplied the original lesson texts for Lessons 1–3 in the conversation; do not request them again. The branch copies are source-aligned working versions, not a claim of byte-for-byte transcript restoration.

## Regression protection added

The manifest test suite now checks that per-lesson quiz keys have unique question IDs and cover the complete expected 1–5 set, rather than accepting a correct total row count that could conceal a missing lesson/question and a duplicate. The Course 1 master answer key now contains all 60 question rows across all 12 lessons; a regression test verifies complete coverage, uniqueness, and agreement with the selected per-lesson key files. It checks the Course 1 Lessons 4–5 selected key against their selected options, preserves the recovered original option order for Lessons 8–9, and verifies the recovered Lesson 12 key. A master-pack test checks all 24 lesson slots and five quiz questions per lesson.

## Release blockers

- [x] Restore Course 1 Lessons 2, 3, 6, 8, 9 and 12 from recovered source files, record provenance, and verify their quiz keys.
- [x] Reconcile the Course 1 master key into 60 unique rows (five per lesson); cross-check the consolidated rows against the selected per-lesson keys, while the existing lesson tests verify answer text against the quiz options.
- [x] Select the expanded Course 2 Lesson 12 version, copy it into the master, align the consolidated key, and mark the snapshot as non-runtime.
- [x] Complete assistant-led linguistic/source review of all 24 lessons; add source-based examples and regression guards where needed. Independent native-speaker review remains recommended before runtime activation.
- [x] Add a lossless Markdown runtime parser for the 24 selected lessons and their 120 answer-key-verified quiz questions.
- [x] Render Markdown lesson tables as readable Telegram rows while preserving every header/cell value; add a regression test for the table renderer.
- [x] Remove stray Markdown horizontal separators and the recovered `<text>` wrapper from Telegram lesson output; add a regression test.
- [x] Register both Latin courses as active only on this isolated work branch; add namespaced lesson IDs and progress-unlocking isolation tests.
- [x] Run branch CI: 177 tests passed, including compileall, parser/runtime smoke tests, and Telegram table-rendering regression checks.
- [ ] Complete independent native-speaker review and final text reconciliation before production release.
- [ ] Preserve the existing voice workflow; keep dynamic speech disabled.
- [ ] Do not modify `main`, production bot/token/database, or deploy without explicit user approval.


## Course 1 vowel classification source check

The user-supplied texts for Lessons 4–5 were checked against Celadet Alî Bedir-Xan, *Elfabêya kurdî*, printed p. 11: the book states that Kurdish has eight vowels and classifies them by duration into short vowels **e, i, u** and long vowels **a, ê, î, o, û**. The current branch copies include the source examples in the corresponding vowel groups and explain the duration-based classification without suggesting the two groups are identical sounds that only differ in length. The regression test guards the two exact vowel sets and the corrected explanation.

Source: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 Lesson 1 source-alignment check

Checked against Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 37–38 (PDF lines around the start of Part II). The lesson now preserves:
- Grammar as the totality of rules for correct speaking and writing.
- The book's short introduction to Kurmanji as the language of the Kurmanji people.
- The four listed language elements: **Tîp → Kît → Bêje → Komek**.
- **Qiset** as the result of successive combinations of **Komek**, not as a fifth item in the four-element list.
- The source's examples (Par ez çûbûm Rewanê, Îro dinya sar e, Gundê me di navbera du avan de ye) without the earlier malformed Parêz transcription.

The five-question quiz and its answer key were revised together; a regression test now checks the four-element sequence, the qiset distinction, and exact key-to-option text. The user supplied the full Lesson 1 text in the conversation. This source-alignment pass corrects the current branch copy; it does not require the user to resend anything.

Source: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 Lesson 9 source-alignment check

The pronoun section in printed pp. 71–73 distinguishes three grammatical genders for pronouns: masculine, feminine, and neuter. The recovered Course 2 Lesson 9 draft previously listed only masculine and feminine third-person singular rows. It now adds the neuter row and explains that wî is masculine, wê feminine, and the remaining personal forms are treated as neuter in the source's classification. The quiz's existing masculine agent-form question remains unchanged. A regression test guards the presence of all three categories and the forms ew, wî, and wê.

Source: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 pronoun completeness — source pages 76–89

A second pass against the source table of contents and printed pp. 76–89 found that the 12-lesson draft did not yet teach every pronoun class named by Bedir-Xan. The missing coverage is now added without changing the Latin-course boundary or importing Course 1 material:

- Lesson 10 adds **Pronavên lihevxistî** (printed pp. 79–81), including the source's preposition-pronoun combinations `jê`, `lê`, `pê`, `tê` and compound forms such as `jev/jêk` and `pev/pêk`. The caution about not duplicating a preposition already contained in a fused form is included. It also teaches reflexive `xwe` (printed pp. 76–77; distinct from the **Pronavên xwemalîn** section on printed p. 87) and the singular neuter pronoun `ê` (printed p. 77), with examples and a distinction from plural `wan`.
- Lesson 11 adds **Pronavên nebinavkirî** (printed pp. 86–87), with source-grounded examples such as `yek`, `her yek`, `kes`, `tu kes`, `her kes`, `tişttek`, `hin`, `hinek`, `çend`, `hemî`, `gişt`, and `gelek`.
- Lesson 11 distinguishes two separate source categories: **demonstrative pronouns of the qerse form** `yê/ya/yên` (printed pp. 81–83), and **Pronavên xwemalîn** (possessive pronouns, printed pp. 87–89). The demonstrative section uses `Yê ko hat bira yê min bû`, `Yên ko hatin bira yên min bûn`, and `Ya ko hat dotmama min bû`, explaining the relative `ko`. The possessive section explains the two-pronoun structure and gives `yê min`, `ya min`, `yên min`, and `destmalên min — yên min`. These forms are not simply reflexive `xwe`.
- A regression test guards the new source categories and examples.

Source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 76–89. The six broad pronoun classes are listed on printed p. 72; the separate lihevxistî section begins on printed p. 79. Source PDF: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf

This is an editorial source-alignment completion, not a claim that the new explanatory prose is a verbatim transcription of the book.


## Course 2 Lesson 12 — ordinal numeral adjectives

The source's printed pp. 94–95 explicitly divides **rengdêrên jmarîn** into cardinal and ordinal forms. The Lesson 12 draft previously showed cardinal examples (`sê mal`, `çar xanî`, `deh bizin`) but omitted the ordinal class. It now explains that ordinal forms indicate a noun's sequence and normally follow the noun, with source-grounded examples such as `stûna çaran`, `a pêncan`, and `ê heftan`. A regression assertion guards this distinction and examples.

Source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 94–95. Source PDF: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 Lessons 4–8 — number, noun inflection and determiners

A source-level recheck of printed pp. 55–70 identified a key pedagogical boundary that needed to be made explicit:

- **Lesson 4 — Mêjer (pp. 55–56):** the plural examples now follow the source pairs `Mîr hat/Mîr hatin`, `Ev mehin e/Ev mehin in`, `Min mehin dît/Min mehin dîtin`, and `Ez mehinê dibînim/Ez mehînan dibînim`. The lesson explicitly warns that `hespan` and `mehînan` in the cited examples are oblique/inflected forms, not a general plural suffix. It keeps `hespek/hespin` as the source's indefinite singular/plural pair rather than generalizing it to all nouns.
- **Lesson 5 — Tewanga navdêran (pp. 57–60):** the lesson now contrasts subject forms (`Hesp hat`, `Mehin hat`) with object forms (`Ez hespî dibînim`, `Ez mehinê dibînim`) and plural object forms (`Ez hespan dibînim`, `Ez mehînan dibînim`). It adds the source's exceptions for masculine nouns without `e/a` and the alternative forms the source accepts for some masculine nouns containing `e/a`. The source's singular/plural changes `maseyan → masan` and `çiyayan → çiyan` are also represented. These are taught as source-specific patterns, not as a universal rule for every noun.
- **Lesson 7 — definite determiners (pp. 62–64):** retains `ê/a/ên` and adds their use before adjectives when the noun is omitted, with the source's `ê gewir`, `a sor`, and `ên sor` patterns.
- **Lesson 8 — indefinite determiners (pp. 63–70):** distinguishes `-ek/-ek/-in` after a noun without a following descriptor from `-ekî/-eke/-ine` when a descriptor follows. It now notes the additional forms that appear in oblique environments (`-ekî/-ekê/-ina`) instead of presenting the two basic rows as exhaustive.

Regression tests now guard the key source examples and ensure the lessons keep number separate from oblique inflection, and definite forms separate from indefinite forms. Quiz answer-key option text remains unchanged and is checked against all 60 Course 2 questions.

Source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 55–70. Source PDF: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf

These are editorially expanded explanations of the cited grammar, not verbatim reproductions of the book.


### Correction: source taxonomy for `xwe`, `yê/ya/yên`, and possessive pronouns
The source treats `xwe` on printed pp. 76–77 as a neuter pronoun that can represent both genders and both numbers; it is not the section titled **Pronavên xwemalîn**. The forms `yê/ya/yên` are introduced separately on pp. 81–83 as demonstrative pronouns of the qerse form, always functioning as subjects and followed by relative `ko` in the examples. The actual **Pronavên xwemalîn** section begins on p. 87 (body text) and explains possessive pronouns formed from a remote demonstrative plus a personal pronoun, e.g. `yê min`, `ya min`, `yên min`. Lesson 11 now teaches these three distinctions separately, and regression tests guard the corrected taxonomy.


## Course 2 Lesson 12 — fuller adjective paradigms

A further comparison with printed pp. 91–96 expanded Lesson 12 beyond single introductory examples. The demonstrative-adjective section now includes source forms for masculine and feminine nouns in singular/plural oblique contexts (`vî hespî/van hespan`, `wî hespî/wan hespan`, `vê mehinê/van mehinan`, `wê mehinê/wan mehinan`) and explains agreement and the source's option to mark only the final noun in some coordinated noun groups. The cardinal numeral section adds subject/object contrasts (`deh mirov hatin/deh mirovan got`, `çel mirov hatin/çel mirovan got`); the interrogative section adds `kîjan mirov` and `çend` examples; the indefinite adjective section now includes the source's `tu`, `her`, `herçî`, `filan`, `gelek`, `hemî`, `hevqas`, and `çend`; and the possessive adjective section now demonstrates forms across genders and numbers (`hespê min`, `mehinên te`, `kitêba vî`, `qelemên wê`, `xaniyê me`, `çiyayê we`, `kurên van`, `keçên wan`). New assertions guard these source examples.

Source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 91–96. Source PDF: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 1 follow-up — source examples and text consistency (2026-10-31)

- A direct check of Celadet Alî Bedir-Xan's printed p. 11 confirms the short-vowel examples `der/şer/ser`, `kin/din/bin`, `kurd/kur/kul`, and long-vowel examples `av/sar/bar`, `dêr/şêr/mêr`, `tîr/zîv/şîv`, `dor/sor/kor`, `kûr/şûr/dûr`. The current Course 1 Lesson 4–5 editorial copies include these examples in the corresponding vowel groups. The user supplied both complete lesson texts earlier; preserve those original texts as the reference and do not request them again.
- The current Lesson 4–5 copies keep `bûk` and `şûştin` under long `Û`, not short `U`; tests guard that boundary and the exact quiz answer-key mappings.
- Lesson 6 had accidental Sorani-script fragments in its explanatory note and exercise instructions. These have been normalized into Kurmanji Latin prose without changing the recovered example list or quiz choices. A test now rejects Arabic-script characters in that lesson.
- The source PDF's printed p. 11 also supports the distinction between the eight vowel letters and their short/long grouping. See Part I, printed p. 11: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 1 Lesson 12 — practice sentence agreement

A final pedagogical pass found that the fill-in sentence `Zarok di ______ de ne` paired with the bare word-bank item `dibistan`, which would produce an incomplete locative form. The exercise now uses `Zarok li ______ ne` with the correctly inflected bank item `dibistanê`. A regression test guards the word-bank form and sentence pattern. This is a small language-quality correction; it does not add a new grammar lesson or alter the five-question quiz.


## Consolidated 24-lesson master pack and recovery correction

`course_data/latin_courses_master_draft.md` consolidates all 24 selected lessons in their authoritative order. The user confirmed that five complete lesson texts were already supplied in the conversation (Course 1 Lessons 4–5 and Course 2 Lessons 1–3); their provenance is explicitly recorded in the master pack. Do not ask the user to resend them. The branch copies are source-aligned working versions, and the exact original wording remains the reference when reconciling any final transcription differences. A regression test checks all 24 lesson headings, order, provenance tags and five quiz questions per lesson. The master pack is now loaded on this isolated work branch through `latin_course_runtime.py`; it remains editorial content and production activation/deployment has not been performed.


## Final microcopy and exercise pass

- Course 1 Lesson 12: the alphabet count introduction now uses the grammatical form `Di alfabeyê de 31 herf hene`; the recovered quiz and exercise order remain unchanged.
- Course 2 Lesson 11: the indefinite-pronoun example is normalized to `Her kes dibêje` (the present-tense prefix remains attached to the verb). A regression assertion rejects the split form `Her kes di bêje`.
- These language-level edits are retained as editorial history; the two courses are now wired into runtime only on the isolated work branch. Production remains unchanged.


## Course 2 Lessons 2–3 — noun taxonomy and grammatical gender source pass

A direct review of Celadet Alî Bedir-Xan, *Bingehên gramera kurdmancî*, printed pp. 51–52, expanded the examples in the two opening noun lessons to use the book's own lists. Lesson 2 now includes the source's proper-name examples (`Sado`, `Bêlan`, `Herekol`, `Hevind`, `Sîpan`, `Xabûr`, `Hindistan`, `Hezro`, `Kerevan`, `Zîn`, `Dêrgul`, `Kurdistan`, `Agirî`, `Cemşîd`, `Ferazende`). Lesson 3 now uses the source's masculine and feminine noun lists and retains the semantic contrast for `dar`: plant/tree = feminine (`vê darê`), wood/log = masculine (`vî darî`). Automated tests guard the added source examples, the two `dar` forms, and the Kurmanji-Latin-only script boundary.

This is a source-alignment edit to the editorial content, not a claim of verbatim transcription. The lesson order and course separation are unchanged; branch runtime loading is isolated from production.

Source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 51–52. PDF: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 Kurmanji Latin-script normalization

All lesson headings and structural labels in `latin_course_2_source_aligned_lessons_01_12.md` now use Kurmanji Latin forms (`Ders`, `Armanc`, `Naverok`, `Xebat`, `Kuis`, `Têbînîyên çavkaniyê`). Sorani-script labels and prose were removed from the course file; the master pack now contains 24 lesson headings in Latin script and no Arabic-script characters in either Latin course. A regression assertion enforces the script boundary across both courses.


## Five user-supplied lesson texts — handling rule

The five full lesson texts have already been provided by the user in the conversation. Their lesson slots are Course 1 Lessons 4 and 5, and Course 2 Lessons 1, 2 and 3. The master pack records these five as user-provided. Continue using the existing conversation text and branch copies; never ask the user to paste or upload them again. Keep exact user wording as the reference, and record any source-alignment correction separately rather than silently rewriting the original.


## Course 2 Lesson 10 — terminology spelling correction

The section heading and references for the fused pronoun class are standardized as **Pronavên lihevxistî**, matching the source's printed heading on pp. 79–81. A regression test asserts the corrected form and rejects the former transposition typo `lihevxisitî`.



## Course 2 Lesson 1 — source terminology consistency

The opening grammar lesson now uses the source's exact four-element label **Komek** consistently in the definition, example label, exercise and learning sequence (`Tîp → Kît → Bêje → Komek`). The `Bêje` definition no longer narrows the category to names of people, animals or things; the lesson's examples include the source's non-noun forms `spehî`, `gotin` and `were`. Regression assertions guard the four source labels and this broader definition.
