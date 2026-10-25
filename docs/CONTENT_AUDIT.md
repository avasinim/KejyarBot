# KejyarBot lesson and quiz content audit

Branch reviewed: `fix/kejyarbot-stability-2026-10-25`

## Checks completed

- `lessons.json` contains six non-empty lesson records, numbered 1–6.
- `learning_path.json` matches the six lesson titles and their intended order.
- `quiz.json` contains quiz sets for all six lessons.
- Each quiz question has non-empty text, at least two unique answer options, and an answer that matches one of those options.
- The automated content tests check lesson-specific practice sections, example dialogues, the lesson-6 quiz path, and the existence and RTL structure of the six infographic assets.
- A regression test now checks that six letter/word examples shown in the lesson-2 alphabet infographic also occur in lesson 2: `ب — باوک`, `پ — پیاو`, `چ — چاو`, `ڕ — ڕۆژ`, `ش — شاخ`, and `گ — گوڵ`.
- The currently observed CI runs for commit `3e91a6b7679c41951461ff39f8310acccd132eaf` passed:
  - https://github.com/avasinim/KejyarBot/actions/runs/40195442921
  - https://github.com/avasinim/KejyarBot/actions/runs/40195446238

## Latest verification

- The infographic-example regression test was added in commit `a9d870d63397454e7e387f9aa8a38ac8dd5514b5` and re-read from the branch.
- CI run #244 passed for that commit: https://github.com/avasinim/KejyarBot/actions/runs/40195984360 . This confirms the automated checks passed; it does not establish source-level orthographic correctness.
- The documentation update itself was also checked by CI runs #246 and #247; both passed for commit `6ddd91e3cbef61b71d5f08575bf807b06e92703c`: https://github.com/avasinim/KejyarBot/actions/runs/40196071449 and https://github.com/avasinim/KejyarBot/actions/runs/40196074868.

## Expanded vocabulary and example policy

- The Diako Hashemi book is a reference for orthography and punctuation, not the exclusive source or limit for lesson vocabulary, example sentences, dialogues, or exercises.
- Expand teaching examples using appropriate Kurdish dictionaries, other Kurdish-language textbooks and linguistic references, literature, and natural everyday dialogue where suitable.
- New illustrative sentences and practice items may be authored directly when pedagogically useful; do not present invented examples as quotations or attribute them to a source.
- Keep source-sensitive claims (such as alphabet inventory/order or prescriptive spelling rules) distinct from ordinary illustrative examples. Verify claims against suitable references, and record source details when a factual linguistic claim depends on them.
- Prioritize varied examples, clear meaning, natural usage, gradual difficulty, and useful repetition without duplicating quiz question text within the same lesson.
- Keep KejyarBot spelling policy separate from Avasin Code.

## Items deliberately not changed

- Lesson 2 states that the Sorani Kurdish alphabet has 34 letters, while the lesson presents a sample of letters rather than a complete alphabet table. The claim and the exact inventory/order should be checked against the selected edition of Diako Hashemi's `پوختەی ڕێنووس و خاڵبەندی` before changing either the number or the examples.
- Some spellings in lesson and quiz text need source-based orthographic review. The exact edition and relevant pages have not yet been verified, so no speculative global replacement or application of Avasin Code was made.
- Quiz coverage is introductory and checks basic recall; passing structural tests does not prove the linguistic accuracy or completeness of the teaching material.

## Source edition selected for the next pass

- The working reference is now the **third updated edition dated 16 August 2024**, linked from the preparer's website: https://diyako.yageyziman.com/wp-content/uploads/2024/08/Puxtey_Renus_U_Xallbendi_Weshani_3_New.pdf .
- Kurdipedia's record lists several editions, including 90-page PDF versions from 2022 and 2024: https://www.kurdipedia.org/default.aspx?lng=1&q=20211004184500395359 .
- The PDF's title page identifies it as the third updated edition. Its relevant rule pages still need to be read and compared before changing any lesson, quiz, or infographic wording.

## Next review steps

1. Inspect the selected edition's relevant pages for alphabet inventory/order and spelling rules.
2. Compare lesson text, quiz wording, and infographic labels against those pages.
3. Make only evidence-backed corrections and add regression tests for confirmed rules.

## Safety boundary

This audit is documentation only. It does not change `main`, production bot settings, production databases, migrations, or prerecorded audio assets. KejyarBot's orthography remains separate from Avasin Code.
