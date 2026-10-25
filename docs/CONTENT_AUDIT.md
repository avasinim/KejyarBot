# KejyarBot lesson and quiz content audit

Branch reviewed: `fix/kejyarbot-stability-2026-10-25`

## Checks completed

- `lessons.json` contains six non-empty lesson records, numbered 1–6.
- `learning_path.json` matches the six lesson titles and their intended order.
- `quiz.json` contains quiz sets for all six lessons.
- Each quiz question has non-empty text, at least two unique answer options, and an answer that matches one of those options.
- The automated content tests check lesson-specific practice sections, example dialogues, the lesson-6 quiz path, and the existence and RTL structure of the six infographic assets.
- The currently observed CI runs for commit `3e91a6b7679c41951461ff39f8310acccd132eaf` passed:
  - https://github.com/avasinim/KejyarBot/actions/runs/40195442921
  - https://github.com/avasinim/KejyarBot/actions/runs/40195446238

## Items deliberately not changed

- Lesson 2 states that the Sorani Kurdish alphabet has 34 letters, while the lesson presents a sample of letters rather than a complete alphabet table. The claim and the exact inventory/order should be checked against the selected edition of Diako Hashemi's `پوختەی ڕێنووس و خاڵبەندی` before changing either the number or the examples.
- Some spellings in lesson and quiz text need source-based orthographic review. The exact edition and relevant pages have not yet been verified, so no speculative global replacement or application of Avasin Code was made.
- Quiz coverage is introductory and checks basic recall; passing structural tests does not prove the linguistic accuracy or completeness of the teaching material.

## Next review steps

1. Identify the exact PDF edition to use as the orthographic source.
2. Read the relevant pages for alphabet inventory/order and the spelling rules being applied.
3. Compare lesson text, quiz wording, and infographic labels with those pages.
4. Make only evidence-backed corrections and add regression tests for confirmed rules.

## Safety boundary

This audit is documentation only. It does not change `main`, production bot settings, production databases, migrations, or prerecorded audio assets. KejyarBot's orthography remains separate from Avasin Code.
