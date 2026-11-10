# Course 4 — Lesson 4 book-addendum / runtime reconciliation (2026-11-10)

## Sources checked

- Runtime: `course_data/grammar_course4_lessons.json` on `main`; blob SHA `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`.
- Lesson: `grammar_04`, `وانەی ٤: ناو لە ڕووی ژمارە و ڕەگەزەوە`.
- Library research supplement: `KEJYAR_COURSE4_LESSON04_BOOK_ADDENDUM.md`.
- Book reference recorded in the addendum: سەعید کەرەمی، *وشەناسیی زمانی کوردی*، بەشی 5-1-1 «ژمارە»، چاپی لاپەڕەکانی 129–131؛ هەروەها 5-1-2 «ناسراوەتی».

## Runtime baseline

| Section | Current count |
|---|---:|
| Key points | 9 |
| Examples | 6 |
| Activities | 3 |
| Exercises | 5 |
| Comprehension | 10 |
| Quiz | 8 |
| Appendix | 6 |

The runtime already covers the core distinction between grammatical number and numeral, the common Sorani plural marker `ـان`, definite plural `ـەکان`, the demonstrative plural construction `ئەو ئەسپانە`, vowel-final stem linking, and natural versus grammatical gender.

## Reconciliation finding

The book addendum contains additional source-backed distinctions not explicitly recorded in the current six appendix items:

1. The book's restricted/borrowed plural markers `ـات` and `ـەها`, with examples such as `کوردستان-ات`, `عێراق-ات`, `هەورامان-ات`, `ساڵ-ەها` and `دەرد-ەها`. These must not be generalized as productive standard Sorani suffixes.
2. The book's analysis of `=گەل` as a clitic rather than an ordinary, unrestricted plural suffix, with dialect-sensitive distribution.
3. The book's examples showing that `ـان` does not attach mechanically to every noun stem, and that noun type, definiteness and demonstrative structure must be considered together.

The existing runtime already covers the main contrast between `ئەسپەکان` and `ئەو ئەسپانە`; the new supplement therefore avoids duplicating that explanation and concentrates on the three under-recorded details above. The addendum does not provide new evidence for expanding the lesson's gender rules, so no gender rule is added.

## Append-only patch prepared

A new archival patch was created:

- `docs/source_archive/staging/grammar_04_append_only_patch.json`
- Commit: `01a7285416e6e54a55910cf785720ddb78441a34`
- Patch type: `append_only`
- Target: `grammar_04`
- Additions: 3 appendix strings only.
- Existing key points, examples, activities, exercises, comprehension items, quiz and appendix entries are preserved.
- Patch status: prepared and archived; not applied to runtime.

The same patch and its package/README were uploaded to the Library folder:

- `/KejyarBot/Course4_Archive/grammar_04_append_only_patch.json`
- `/KejyarBot/Course4_Archive/grammar_04_append_only_package.zip`
- `/KejyarBot/Course4_Archive/README_KU_PATCH04_2026-11-10.md`

Local integrity checks before upload:
- Patch JSON parsed successfully.
- Exactly 3 appendix additions were present.
- ZIP integrity test passed.
- Patch SHA-256: `85a9136c3fa5e1926e9a046d0c4b9d1c1d9a9839d1b59943a87126470ceec2d6`.
- Package ZIP SHA-256: `4c01c89af349c43c139c650661d2e339e4ee49dab10ca4120f9586749f162359`.

## Operational boundary

No changes were made to `main`, runtime JSON, Botkeep, SQLite, Railway, production deployment or Telegram. The patch is an archival supplement and is not active in the bot. The earlier baseline decision that Lessons 3–7 did not require patches is retained as a historical checkpoint; this Lesson 4 patch is a newly justified addition based on the subsequently reconciled book addendum.

## Next step

Continue the same source-to-runtime reconciliation for Lesson 5, using its book addendum and current `grammar_05` runtime entry. Only evidence-backed additions should be prepared, and all changes must remain append-only.
