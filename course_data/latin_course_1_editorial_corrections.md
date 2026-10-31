# چاکسازیی دەقی کۆرسی ١ — Bingehên Rastnivîsîna Kurdî ya Latînî
Status: editorial patch list for Course 1's 12 lesson slots, based on the user-supplied/recovered lesson texts and Part I of Celadet Alî Bedir-Xan (2002). These are corrections to apply to the Latin Course 1 master copy; they do not modify the separate Sorani 22-lesson course.

## Source
Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002, Part I: “Elfabêya kurdî”, printed pp. 11–34.
The book identifies 31 letters and 8 vowels; short vowels are `e, i, u`; long vowels are `a, ê, î, o, û`. The V/W section gives contrastive examples on pp. 16–17.

## Source-level verification update — printed page 11

A direct check of the digital edition's printed p. 11 confirms the eight-vowel inventory and supplies compact example sets for each target vowel. Printed p. 39 further explains that the short/long division is not merely a matter of stretching the same sound: the vowel groups also differ in sound quality and articulation position. Lessons 4–5 now state this explicitly, without claiming that each vowel forms a simple duration-only pair. Page 11 supplies these compact example sets:
- Short E: `der, şer, ser`.
- Short I: `kin, din, bin`.
- Short U: `kurd, kur, kul`.
- Long A: `av, sar, bar`.
- Long Ê: `dêr, şêr, mêr`.
- Long Î: `tîr, zîv, şîv`.
- Long O: `dor, sor, kor`.
- Long Û: `kûr, şûr, dûr`.

The current source-aligned branch copies for Lessons 4–5 include these source-attested examples in the appropriate vowel groups. The user supplied both complete lesson texts earlier; keep those original messages as the reference and do not ask for them again. The branch copies are editorial working copies and should not be described as newly invented lessons. Regression tests assert that these examples remain in the correct short/long lesson and that `bûk` and `şûştin` are not placed under short U.

## Confirmed corrections

### Lesson 1 — Elfabeya Kurdî
- Keep the 31-letter alphabet and the eight-vowel split.
- The letter table currently uses `jin` for both I and J. It is technically a word containing both letters, but pedagogically duplicates one example. Use `kin` for I (also supported as a short-I example in the source) and retain `jin` for J.
- The corrected draft now explicitly says that `kin` begins with K and contains I medially, while `jin` begins with J and also contains I medially. This avoids implying that short I normally begins Kurmanji words; the source discusses its restricted initial/final distribution on printed p. 39.
- Add I to the vowel-identification exercise if the current exercise set omits it.
- Keep the source distinction between written letter and spoken sound; do not imply that each written letter is itself a vowel/consonant sound without explaining the levels.

### Lesson 4 — Dengdêrên Kin: E, I, U
- In the U list, remove `bûk` and `şûştin`: both contain `û`, not `u`.
- Keep them in the long-vowel lesson under Û.
- Short-U examples may include `gur, kur, gund, xurt, kulîlk`. The source treats `tu` (and `du`) as exceptional forms in its discussion; label `tu` as a source-noted exception rather than using it as an unqualified typical example.
- E examples from the recovered lesson: `ez, ev, yek, deng, kes, heval, mezin, şert`.
- I examples: `kin, dil, pir, nivîs, birîn, hilbijartin, kirin, biçûk`. Check each item by its sound and not merely by visual letter presence.

### Lesson 5 — Dengdêrên Dirêj: A, Ê, Î, O, Û
- For O, replace unverified `zoro` with the source's contrastive examples `dor, sor, kor`, unless a Kurmanji dictionary and the course's designated source verify `zoro` in the intended sense.
- Preserve the distinction between vowel length and vowel quality. The source does not license reducing every short/long pair to duration alone.
- Existing A examples: `av, bav, mal, dar, zarok, bajar, çav`.
- Existing Ê examples: `êvar, pênc, sê, mêrik, hêvî, çêkirin`.
- Existing Î examples: `îro, pîr, nîv, hêvî, jîn, şîr, xwîn`.
- Existing Û examples: `dûr, bûk, bû, dû, mû`. `xwîn` contains Î, not Û; move it to the Î examples and check each exercise's actual vowel target.

### Lesson 6 — Cudahiyên Dengên I û Î
- Keep the contrast as two distinct letters/sounds; the diacritic in `Î` is part of the letter.
- The current contrast table includes `jin` as an I example; that is valid because I occurs inside the word. Do not claim it is invalid. Use `kin` or `dil` as an additional clear example.
- Avoid describing all listed words as minimal pairs; most are contrastive examples, not meaning-matched minimal pairs.

### Lesson 7 — Cudahiyên Dengên U û Û
- Keep `bûk` and `şûştin` exclusively in the Û group; the recovered lesson already notes that `bûk` has Û. `xwîn` contains Î, not Û, and must not be listed as a Û example.
- Explain that the source treats U and Û as distinct vowel qualities and not merely as one sound written short/long.
- Keep the source examples for U and Û separate; do not let an exercise place `bûn`, `xwîn`, or `dûr` under U.

### Lesson 8 — Cudahiyên Dengên V û W
- Correct the recovered table entry `zivistan | destpêk` to `zivistan | navîn`: the word begins with Z but contains V medially. Retain it as a V-containing word; do not classify V as initial in this example.
- Use the source's contrastive examples: `dev/dew`, `vir/wîr`, `ava/awa`, `evî/ewî`.
- Keep reliable position examples: V in `ve` (initial), `nivîs` (medial), `av` (final); W in `welat`, `wêne` (initial), `law` (final).
- Preserve the recovered sorting exercise because `zivistan` does contain V medially. Add the source's contrastive pairs `dev/dew`, `vir/wîr`, `ava/awa`, and `evî/ewî` as supplementary examples, not as meaning-equivalent pairs.

### Lesson 9 — Herfên Taybet di Elfabeya Kurdî de
- Keep the current title “Herfên Taybet di Elfabeya Kurdî de”: it describes the lesson's focus on marked letters. Do not relabel it “Dengdarên Taybet”, because Ê, Î and Û are vowels.
- Explain that this lesson groups marked letters for orthographic practice, not a single phonological class: Ç and Ş are consonants; Ê, Î and Û are vowels.
- Correct the malformed exercise `U / Ûr` to `U / Û` and identify `dûr` as the target word. Move `xwîn` from the Û examples to the Î examples; `xwîn` contains Î, not Û.
- Avoid repeating Lesson 2's entire explanation; focus on accurate recognition, typing, and preserving the diacritics in actual words.

### Lesson 10 — Têkiliya Deng û Herfê
- Ground the explanation in Part I, pp. 13–15: writing represents language sounds, but spelling is a system and not every phonetic variation gets its own separate letter.
- Keep the distinction accessible: a sound is heard/spoken; a letter is a written symbol. Do not claim a perfect one-to-one mapping for every accent or pronunciation.

### Lesson 11 — Bingehên Nivîsandina Rast
- Keep as a pedagogical synthesis of the alphabet and orthography principles, not as a verbatim chapter title from the book.
- Check every spelling example in its sentence context. A form that is valid in another variety or has another meaning must not be labelled universally wrong.
- Ensure the quiz tests the rule taught in this lesson rather than only repeating a letter-recognition question.

### Lesson 12 — Xwendin û Nivîsandina Pratîk
- Keep it as the review/practice lesson for Lessons 1–11; its five-question quiz exists in the recovered draft and must not be mistakenly marked absent.
- Correct `Ev pirtûk a min e` to `Ev pirtûka min e`. The ezafe linker belongs attached to the noun in this construction; compare the source's attached forms such as `xencera min` (Part II, p. 61).
- In the fill-in word bank, use `dibistanê` for the sentence `Zarok di ______ de ne`, so the oblique/locative form is supplied correctly.
- Check that each reading passage and quiz item uses only distinctions taught earlier in the course.

## Release gates
- The user supplied the complete texts of Lessons 4–5 in the conversation. The current branch files are source-aligned editorial working copies; preserve the user-provided wording and quiz option order as the authority during reconciliation. Do not request that the user resend the lessons.
- Add explicit answer keys and lesson-specific explanations to all quizzes; no quiz is ready for runtime until its options and key are verified.
- Preserve original Kurmanji Latin forms and do not apply the Avasin Academy Arabic-script orthography rules.
- Do not merge these drafts into a runtime course until course IDs, progress isolation, quiz handlers, and offline tests are added and passed.


## Editorial cleanup — Lesson 6

The recovered Lesson 6 contained a few accidental Sorani/Arabic-script fragments inside its explanatory note and practice instructions. These were converted to clear Kurmanji Latin wording without changing the lesson's target contrast, word list, or quiz options. A regression test now rejects Arabic-script characters anywhere in this Latin-course lesson. The remaining vowel-pair table is explicitly described as a recognition aid, not as a list of minimal pairs or synonymous pairs.


## Recovery update — Lessons 8, 9 and 12

The exact original bodies for Course 1 Lessons 8, 9 and 12 were recovered from `Pasted markdown(3).md` and restored to `latin_course_1_lessons_08_09_recovered_draft.md` and `latin_course_1_lesson_12_recovered_draft.md`. The older rewritten drafts are marked superseded. Lesson 8 keeps the original content but corrects the V position in `zivistan` from initial to medial and adds the source's V/W contrast examples. Lesson 9 preserves the original quiz option order, moves `xwîn` to the Î group and repairs `U / Ûr`. Lesson 12 preserves the original reading and quiz sequence, correcting the ezafe spelling and supplying the inflected `dibistanê` form in its exercise word bank. Regression tests now verify the restored option order and exact keys.
