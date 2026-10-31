# چاکسازیی دەقی کۆرسی ١ — Bingehên Rastnivîsîna Kurdî ya Latînî
Status: editorial patch list based on the recovered 12-lesson drafts and Part I of Celadet Alî Bedir-Xan (2002). These are corrections to apply to the Latin Course 1 master copy; they do not modify the separate Sorani 22-lesson course.

## Source
Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002, Part I: “Elfabêya kurdî”, printed pp. 11–34.
The book identifies 31 letters and 8 vowels; short vowels are `e, i, u`; long vowels are `a, ê, î, o, û`. The V/W section gives contrastive examples on pp. 16–17.

## Confirmed corrections

### Lesson 1 — Elfabeya Kurdî
- Keep the 31-letter alphabet and the eight-vowel split.
- The letter table currently uses `jin` for both I and J. It is technically a word containing both letters, but pedagogically duplicates one example. Use `kin` for I (also supported as a short-I example in the source) and retain `jin` for J.
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
- Existing Î examples: `îro, pîr, nîv, hêvî, jîn, şîr`.
- Existing Û examples: `dûr, bûk, bû, dû, mû, xwîn`. Verify the actual vowel target in each exercise before finalizing.

### Lesson 6 — Cudahiyên Dengên I û Î
- Keep the contrast as two distinct letters/sounds; the diacritic in `Î` is part of the letter.
- The current contrast table includes `jin` as an I example; that is valid because I occurs inside the word. Do not claim it is invalid. Use `kin` or `dil` as an additional clear example.
- Avoid describing all listed words as minimal pairs; most are contrastive examples, not meaning-matched minimal pairs.

### Lesson 7 — Cudahiyên Dengên U û Û
- Keep `bûk` and `şûştin` exclusively in the Û group; the recovered lesson already notes that `bûk` has Û.
- Explain that the source treats U and Û as distinct vowel qualities and not merely as one sound written short/long.
- Keep the source examples for U and Û separate; do not let an exercise place `bûn`, `xwîn`, or `dûr` under U.

### Lesson 8 — Cudahiyên Dengên V û W
- Correct the table entry `zivistan | destpêk`: the word begins with Z and has no V. Remove it from the V-at-word-start list.
- Use the source's contrastive examples: `dev/dew`, `vir/wîr`, `ava/awa`, `evî/ewî`.
- Keep reliable position examples: V in `ve` (initial), `nivîs` (medial), `av` (final); W in `welat`, `wêne` (initial), `law` (final).
- Rebuild the sorting exercise so every item actually contains the target letter. Do not include `zivistan` in the V/W sorting set.

### Lesson 9 — Herfên Taybet di Elfabeya Kurdî de
- Keep the current title “Herfên Taybet di Elfabeya Kurdî de”: it describes the lesson's focus on marked letters. Do not relabel it “Dengdarên Taybet”, because Ê, Î and Û are vowels.
- Explain that this lesson groups marked letters for orthographic practice, not a single phonological class: Ç and Ş are consonants; Ê, Î and Û are vowels.
- Correct the malformed exercise `U / Ûr` to `U / Û` in the word `dûr`.
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
- Check that each reading passage and quiz item uses only distinctions taught earlier in the course.

## Release gates
- The exact text of Lessons 4–5 was confirmed in prior conversation but was not restored verbatim in the recovered master file. Their content above is an editorial correction record, not a claim of verbatim restoration.
- Add explicit answer keys and lesson-specific explanations to all quizzes; no quiz is ready for runtime until its options and key are verified.
- Preserve original Kurmanji Latin forms and do not apply the Avasin Academy Arabic-script orthography rules.
- Do not merge these drafts into a runtime course until course IDs, progress isolation, quiz handlers, and offline tests are added and passed.
