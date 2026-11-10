# Course 4 — Lesson 5 book-addendum / runtime reconciliation (2026-11-10)

## Sources checked

- Runtime: `course_data/grammar_course4_lessons.json` on `main`; blob SHA `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`.
- Lesson: `grammar_05`, `وانەی ٥: ناو لە ڕووی ناوەرۆک، ناسینەوە و پێکهاتەوە`.
- Library research supplement: `KEJYAR_COURSE4_LESSON05_BOOK_ADDENDUM.md`.
- Book reference recorded in the addendum: سەعید کەرەمی، *وشەناسیی زمانی کوردی*، بەشی 6-1 و خشتەی 6-1، چاپی لاپەڕەکانی 154–157؛ بەشی حەوتەم «لێکدان»، نزیکەی لاپەڕەکانی 175–187.

## Runtime baseline

| Section | Current count |
|---|---:|
| Key points | 12 |
| Examples | 6 |
| Activities | 3 |
| Exercises | 5 |
| Comprehension | 10 |
| Quiz | 8 |
| Appendix | 7 |

The current runtime already distinguishes semantic/reference classifications from word structure, defines simple/derived/compound nouns, uses `جوانی` and `ئازادی` as derived examples, includes `دەستنوێژ` as a compound example, and warns against relying on spelling or word length alone.

## Reconciliation finding

The book addendum provides useful details not fully represented in the current appendix:

1. The derivational patterns in Table 6-1, including noun-forming suffixes and examples for profession, agent, container, place and abstract-noun formations.
2. A clear test for distinguishing productive derivational affixes from restricted forms: identifiable base and derivative, repeated comparable function, semantic fit, and evidence from actual use.
3. Compound patterns beyond noun+noun, including coordinate compounds, head/modifier compounds and compounds containing a verbal root.
4. A source boundary: the book's derivation/compounding sections do not directly establish the lesson's broader concrete/abstract or common/proper classifications. Those owner-authored parts remain, but must not be attributed to the book.

Because the addendum explicitly cautions that the book's examples retain their source forms and must not be automatically transferred into Sorani lesson forms, the patch records them as book examples with a dialect/source qualification.

## Append-only patch prepared

- File: `docs/source_archive/staging/grammar_05_append_only_patch.json`
- Commit: `3bf3e598ae691abb239c69eedef3a7a0b57b7d33`
- Patch type: `append_only`
- Target: `grammar_05`
- Additions: 4 appendix strings only.
- All existing lesson sections and items are preserved.
- Patch status: prepared and archived; not applied to runtime.

The patch and its package/README were uploaded to:

- `/KejyarBot/Course4_Archive/grammar_05_append_only_patch.json`
- `/KejyarBot/Course4_Archive/grammar_05_append_only_package.zip`
- `/KejyarBot/Course4_Archive/README_KU_PATCH05_2026-11-10.md`

Local integrity checks:
- Patch JSON parsed successfully.
- Exactly 4 appendix additions were present.
- ZIP integrity test passed.
- Patch SHA-256: `a856ed9a7e901f794a5a47e5c874c7b09597cf5c589fda1d5e27a232d3e3ba91`.
- Package ZIP SHA-256: `25f5b96568131c390594b345fb6f86f625c4d3924b83801fcf1dc2e87ebbb48d`.

## Operational boundary

No changes were made to `main`, runtime JSON, Botkeep, SQLite, Railway, production deployment or Telegram. This patch is archival only and is not active in the bot.

## Next step

Continue the book-addendum/runtime reconciliation for Lesson 6. Preserve the lesson's existing content and use only source-backed additions.
