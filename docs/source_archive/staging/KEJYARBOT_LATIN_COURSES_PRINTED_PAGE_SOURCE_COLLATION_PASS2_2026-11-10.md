# Latin Courses 1–2 — printed-page source collation, pass 2
Date: 2026-11-10
Branch: `archive/preservation-audit-2026-11-10`
Primary source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002, ISBN 91-89687-04-3.
Accessible scan used for page-image inspection: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf

## 1. Why this pass matters

The earlier source audit relied partly on extracted text/OCR and listed several spelling questions as unresolved. This pass found an accessible scan whose printed pages can be inspected as images. The following decisions are grounded in the printed page images, not guessed from OCR.

## 2. Confirmed correction applied to the separate reviewed draft

### Course 2, Lesson 2 — proper-name spelling

Printed p.51, §37, the proper-name examples end with `Cemşîd, Ferezende`. The reviewed draft had `Cemşîd, Ferazende`.

- Correct source form: `Ferezende`
- Previous reviewed-draft form: `Ferazende`
- Action: corrected the single occurrence in `course_data/latin_course_2_reviewed_draft_2026-11-10.md` on this archive branch only.
- Verified after fetch: `Ferezende` present; `Ferazende` absent.
- Update commit: `02106f3629eb1a2f9616ed908e6edfdfb80dfb7c`
- New file SHA: `ee6e8f243bc6a0155f0c9765482c28e5621b2bd2`

Printed p.51 also confirms `Cemşîd` with the current reviewed-draft spelling. No change needed for that name.

## 3. Course 2 — source forms and classifications confirmed

### Printed p.52, §§39–41: grammatical gender lists

The page explicitly lists `Herekol` in the feminine grammatical-gender list. The reviewed draft preserves that classification. This is a source grammatical classification, not a claim about biological sex or geography.

The same page confirms the source forms in the lists:
- Masculine examples include `Cemşîd`, `Ferat`, `Xurşîd`, `kevir`.
- Feminine examples include `Sînemxan`, `Herekol`, `Hezarom`, `Kurdistan`.

Current reviewed draft spellings for these examples match the printed page. No edits needed in Lesson 3.

### Printed p.87, §§114–118: possessive pronouns

The page heading is `Pronavên xwemalîn`; the section describes forms built from a demonstrative/possessive element and another pronoun, and includes the paradigms `yê min`, `ya min`, `yên min`, etc. The reviewed draft's spelling `xwemalîn` is confirmed. Its distinction between possessive pronouns and possessive adjectives is pedagogical exposition consistent with the source structure.

### Printed p.94, §§134–136: numeral adjectives

The printed page explicitly states the two classes of numeral adjectives: `jmarîn` and `rêzîn`. It distinguishes cardinal quantity forms before the noun from ordinal forms after the noun. Therefore the reviewed draft's spelling `rêzîn` is confirmed; the alternative OCR hypothesis `razîn` is not supported by the page image.

### Printed p.97, §§141–145: `jmarnav`

The printed page confirms:
- two broad groups: `jmarnavên binavkirî` and `jmarnavên nebinavkirî`;
- four subgroups of definite numerals: `bingehîn`, `rêzîn`, `birewîn`, `komelîn`;
- indefinite examples include `gelek`, `hindik`, `pir`, `bêtir`, `zehf`.

The reviewed draft's forms `rêzîn`, `birewîn`, `komelîn`, and `bêtir` match the printed page. Keep `rêzîn` as a term in both adjective and numeral-pronoun sections, while keeping the two grammatical categories distinct.

## 4. Course 1 — printed source collation

### Printed p.11: alphabet and vowel inventory

The page image confirms:
- the 31-letter alphabet inventory;
- eight vowel letters: `a, e, ê, i, î, o, u, û`;
- short-vowel group `e, i, u`;
- long-vowel group `a, ê, î, o, û`.

The displayed source examples include:
- short: `der, şer, ser`; `kin, din, bin`; `kurd, kur, kul`;
- long: `av, sar, bar`; `dêr, şêr, mêr`; `tîr, zîv, şîv`; `dor, sor, kor`; `kûr, şûr, dûr`.

The reviewed Course 1 Lessons 4–7 preserve the source's short/long groupings. Many lesson examples are additional teaching examples, not verbatim source examples. In future revisions, label source examples and supplementary examples separately wherever a lesson's provenance could otherwise imply that every word was printed by Celadet.

### Printed p.12: consonant inventory and sample words

The page confirms 23 consonant letters and includes source examples for:
- X: `xanî, xwarin, xar`
- Y: `yar, yek, yarî`
- Z: `zor, zabit, nafiz`

The current Lesson 9 includes additional words such as `xizan`, `xort`, `çiya`, `zozan`, and `zîv`. These are supplementary teaching examples, not the three-word source lists on p.12. They are not automatically errors, but the lesson should not imply that every one is a verbatim source example. The source classifies Y within the consonant inventory.

### Printed pp.16–17: V/W distinction

The printed page 17 contains the contrast pairs:
- `kevan / kewandin`
- `dev / dew`
- `vir / wîr`
- `ava / awa`
- `evî / ewî`

The reviewed Lesson 8 includes the latter four pairs and explicitly says they are contrast examples, not synonymous words. This is consistent with the source. No correction needed.

### Printed pp.33–34: letter-distribution tables

The Lesson 11 selected values were checked against the page images:
- p.33 general table: `e = 2200`, `i = 1800`, `a = 1500`, `n = 1300`, `r = 1100`, `ê = 1000`, `d = 840`, `î = 700`, `b = 650`, `k = 650`.
- p.33 word-initial table: `k = 417`, `s = 292`, `d = 282`, `t = 275`, `m = 259`, `u = 0`.
- p.34 compares four regional/dialect columns: Bakur, Başûr, Rojavayê bakurê (Palo), and Rojavayê bakurê (Siwerek).

The current Lesson 11 selected figures match the source images. The draft correctly warns that these are source-table counts, not percentages or universal normalized frequencies. No data correction needed in this pass.

## 5. Still unresolved / next source-image pass

1. Course 1 Lesson 4–7: identify which supplementary examples are intended as source quotations versus teacher-added examples, and label them consistently. Do not remove valid teaching examples.
2. Course 1 Lesson 9: preserve source examples (`xanî/xwarin/xar`, `yar/yek/yarî`, `zor/zabit/nafiz`) distinctly from supplementary examples.
3. Course 2 Lesson 2: only `Ferezende` was corrected in this pass. Continue exact page-image collation for all proper-name examples before normalizing any other diacritics.
4. Any unresolved OCR variant must remain marked unresolved until the printed image itself is checked; do not infer the correct form from OCR alone.

## 6. Preservation boundary

This pass changed exactly one spelling in the separate Course 2 reviewed draft: `Ferazende` → `Ferezende`. The correction was fetched and verified. No original source file, quiz, answer key, `main`, active manifest, runtime, database, Botkeep bot, Telegram bot or deployment was changed. The archive note itself is append-only. No test suite or live runtime verification is claimed.


## 7. Additional printed-page check — Course 2, Lesson 5

Printed p.59, §57, shows the three source variants as:
- `Soro kevirî tavêje.`
- `Soro kêvir tavêje.`
- `Soro kevir tavêje.`

The reviewed draft had incorrectly split the second form as `Soro kê vir tavêje.`. The printed page image confirms that `kêvir` is one word. The separate reviewed draft was corrected to `Soro kêvir tavêje.`, then fetched again and verified.

- Update commit: `c1ad3eb52eb79631bd25459d43fbd5f2dbc58f3b`
- New Course 2 reviewed-draft SHA: `693a58e214e63d04035dbc6419ca3c367cc273c0`

**Audit-history correction:** the earlier source-audit note's transcription of the second variant also contained the same space error. Treat the printed p.59 image as authoritative; the prior text transcription is superseded for this example.

## 8. Updated preservation boundary

This pass has made exactly two verified spelling/transcription corrections in the separate Course 2 reviewed draft:
1. `Ferazende` → `Ferezende` (printed p.51).
2. `Soro kê vir tavêje` → `Soro kêvir tavêje` (printed p.59).

No original source, quiz, master answer key, `main`, active manifest, runtime, database, Botkeep bot, Telegram bot or deployment was changed.


## 9. Additional printed-page check — Course 2, Lessons 6–8

Printed pp.61–68 were inspected as page images.

- **p.61, §§59–60:** confirms the pre-noun modifier examples `ev keçik`, `kîjan mirov`, `çar xanî`, `hin çiya`, `çend kitêb`, `deh bizin`, `van zarokan`, and post-noun examples including `hespê beza`, `mehîna spehî`, `xencera min`. Current Lesson 6 preserves the core examples and the singular `mehîna spehî`.
- **p.62, §63:** confirms definite suffix forms `ê`, `a`, `ên`; feminine singular example `Mehîna Cemşîd`.
- **p.63, §63–64:** the plural source example is `mehînên Cemşîd` (with `î` in the noun stem). The reviewed Lesson 7 had `mehinên Cemşîd`; corrected it to `mehînên Cemşîd` and verified by fetching the updated file.
- **pp.64–65, §§65–67:** confirms indefinite suffix patterns `ek, ek, in` and `ekî, eke, ine`, with masculine singular, feminine singular and plural distributions as represented in Lesson 8.
- **p.66, §68:** confirms the patterns `î, e, en` before adjectives in the described indefinite constructions. The reviewed draft does not silently merge these with the post-noun suffix patterns.

Lesson 7 correction:
- Update commit: `0ebcfc4f9e0942f80da76c7f3458b85b2bd411d5`
- New Course 2 reviewed-draft SHA: `e3700d373b8606fe6ed1b51080e3e8437d107cc6`

**Pending rather than guessed:** Lesson 4 uses `mehin` in its own singular/plural teaching pair, and Lesson 12 contains supplementary `mehinên ...` examples. Their exact intended morphology/spelling should be compared against the relevant full printed examples before making a blanket normalization. This pass changed only the exact Lesson 7 form directly attested on p.63.

## 10. Updated correction inventory

The separate Course 2 reviewed draft now has three verified corrections from printed-page inspection:
1. `Ferazende` → `Ferezende` (p.51).
2. `Soro kê vir tavêje` → `Soro kêvir tavêje` (p.59).
3. `mehinên Cemşîd` → `mehînên Cemşîd` (p.63).

Each correction was fetched and verified after update. All other uncertain `mehin/mehîn` occurrences remain unchanged pending a more exact source-context comparison.


## 11. Consistent plural spelling in Course 2, Lesson 12

Printed p.63 gives the plural source form `mehînên Cemşîd`. Applying the same plural stem spelling to the reviewed draft's parallel plural noun phrases, the two Lesson 12 examples `mehinên spehî` and `mehinên te` were normalized to `mehînên spehî` and `mehînên te`. The third occurrence in Lesson 7 was already corrected in §9.

This correction is limited to the plural form `mehînên`. The separate forms `mehinê` / `mehinan` in demonstrative examples have not been globally changed: printed p.93 itself shows `vê mehinê / van mehinan`, so those forms must remain distinct.

- Update commit: `dd16456a3750bb9b96b56724be4424a136aa360c`
- New Course 2 reviewed-draft SHA: `bf5e790f7c70169aa463e7bbdf8a289665784127`

The pending note in §9 remains: Course 2 Lesson 4's standalone `mehin` paradigm still needs its own context-specific collation; no blanket normalization was applied to it.


## 12. Printed-page collation — Course 2, Lessons 10–12

Printed pp.76–84 and pp.90–100 were inspected.

### Lessons 10–11

- **p.76, §§86–87:** confirms object-pronoun forms `min, te, wî, wê, me, we, wan`, their role alternation in transitive past clauses, and reflexive `xwe`. The reviewed Lesson 10's central contrasts and examples are source-aligned.
- **p.77, §90:** confirms reciprocal pronouns `hev, êk` and the regional note for `êk`.
- **p.79, §§91–93:** confirms compound pronouns `jê, lê, pê, tê` and the corresponding preposition/pronoun constructions. The reviewed Lesson 10 keeps these forms and does not collapse them into ordinary independent pronouns.
- **p.81, §§94–96:** confirms demonstrative pronouns `ev/ew` and the two source classes, near/far and `yê/ya/yên`.
- **p.83, §99:** confirms relative `ko` and its position after the relevant noun/pronoun phrase.
- **p.84, §§100–102:** confirms the distinct conjunction `ko` and interrogative forms `kî, kê, çi, çî`. The reviewed Lesson 11's distinction between relative-pronoun `ko` and conjunction `ko` is source-aligned.

No additional source-spelling correction was justified for Lessons 10–11 in this pass.

### Lesson 12

- **p.90, §§124–126:** confirms descriptive adjective behavior and examples such as `reş`, `spehî`, `bilind`; the reviewed lesson's adjective-class framework is consistent with the source.
- **p.91, §128:** confirms the descriptive adjective comparison sequence, including `beza` and `bezatir`; the lesson's basic/comparative/superlative teaching distinction is appropriate.
- **p.93, §§131–133:** confirms demonstrative adjective forms including `vî hespî / van hespan`, `wî hespî / wan hespan`, `vê mehinê / van mehinan`, `wê mehinê / wan mehinan`. These exact `mehinê/mehinan` spellings are preserved in the reviewed lesson; do not apply the plural `mehînên` normalization to these different inflected forms.
- **p.95, §139:** confirms the heading and category `Rengdêrên xwemalîn`, and explains that these possessive adjectives follow nouns and show possession. The reviewed lesson distinguishes them from possessive pronouns.
- **p.98, §148:** confirms the special `nîv` inflection when used independently, including `nîvî` and `nîvekî`, and contrasts it with `nîv` before another numeral or noun.
- **p.99, §149:** confirms the independent `yekê` form and examples such as `ji yekê`, `bîst û yekê`; the reviewed lesson's `yekê` form is supported.
- **p.100, §152:** confirms `hezar` can take `-î` when used independently (`hezarî`) and behaves differently when combined with another numeral. The reviewed lesson's summary is source-aligned.

No further spelling change was made to Lesson 12 in this subpass.
