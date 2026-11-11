# Course 4 — Basten Non-Quiz Temporary Patch and Regression (Round 63)
Date: 2026-11-10
Branch: `botkeep-menu-clean-2026-11-09`
Source file: `course_data/grammar_course4_lessons.json`
Verified source SHA before and after temporary-copy test: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
Previous review: `COURSE4_BASTEN_NONQUIZ_PHRASE_CONTEXT_REVIEW_ROUND62_2026-11-10.md`

## Purpose
Resolve the two held whole-sentence cases from Round62 and test the 26 non-quiz phrase proposals on an in-memory temporary copy. This is a review/regression artifact only. The repository source JSON remains unchanged.

## Manual resolutions
1. **Lesson 9 — `key_points[10]`:** revised both parts coherently:
   - `لە سیاقێکی تایبەتدا` → `لە بەستێنێکی تایبەتدا`
   - `بەبێ سیاق و ڕستەی نموونەیی` → `بەبێ بەستێن و ڕستەی نموونەیی`
   This keeps the sentence's requirement for contextual and example-sentence evidence without leaving a mixed legacy term.
2. **Lesson 27 — `key_points[8]`:** revised both sides of the contrast:
   - `لە سیاقێکدا` → `لە بەستێنێکدا`
   - `لە سیاقێکی دیکەدا` → `لە بەستێنێکی دیکەدا`
   The sentence now consistently contrasts two usage contexts.
3. **Lesson 12 — `appendix[2]`:** in the same targeted field, the closing phrase `سیاقی ڕستە` was also revised to `بەستێنی ڕستە`, so the field contains no leftover instance of the legacy term. This is a local consistency completion, not an additional target path.

## Temporary-copy regression results
- Target paths processed: **26** (the 26 non-quiz paths from Round60).
- Lesson records before/after: **50 / 50**.
- Lesson IDs and order: unchanged.
- Recursive JSON shape (object keys, array lengths, primitive types): unchanged.
- Quiz objects: byte-for-byte JSON-equivalent before/after; **248** structured quiz records retained.
- Quiz options, answer values, answer indices, and explanations: untouched.
- Residual `سیاق` occurrences in the 26 revised fields: **0**.
- No source file write was performed; all substitutions occurred on an in-memory temporary copy.

## Exact path register
| Lesson | Path | Result |
|---:|---|---|
| 3 | `key_points[12]` | Accept; whole phrase changed |
| 3 | `appendix[17]` | Accept; whole phrase changed |
| 5 | `key_points[1]` | Accept; whole phrase changed |
| 7 | `examples[1][1]` | Accept; whole phrase changed |
| 8 | `key_points[7]` | Accept; whole phrase changed |
| 8 | `exercises[4]` | Accept; whole phrase changed |
| 9 | `key_points[0]` | Accept; whole phrase changed |
| 9 | `key_points[10]` | Manual whole-sentence resolution; both context phrases aligned |
| 9 | `examples[4][1]` | Accept; whole phrase changed |
| 10 | `examples[3][1]` | Accept; whole phrase changed |
| 11 | `examples[2][1]` | Accept; whole phrase changed |
| 12 | `examples[1][1]` | Accept; whole phrase changed |
| 12 | `appendix[2]` | Accept; context phrase and closing sentence phrase aligned |
| 13 | `key_points[5]` | Accept; whole phrase changed |
| 15 | `key_points[1]` | Accept; whole phrase changed |
| 15 | `key_points[9]` | Accept; whole phrase changed |
| 15 | `appendix[1]` | Accept; whole phrase changed |
| 16 | `objective` | Accept; whole phrase changed |
| 16 | `comprehension[0]` | Accept; whole phrase changed |
| 17 | `key_points[1]` | Accept; whole phrase changed |
| 21 | `key_points[3]` | Accept; whole phrase changed |
| 21 | `activities[1]` | Accept; whole phrase changed |
| 23 | `appendix[5]` | Accept; whole phrase changed |
| 26 | `key_points[2]` | Accept; whole phrase changed |
| 27 | `key_points[8]` | Manual whole-sentence resolution; both sides of contrast aligned |
| 31 | `comprehension[0]` | Accept; whole phrase changed |

## Interpretation limits
The regression confirms structural and quiz integrity for the temporary text substitutions. It does not establish dialect-wide validity of every grammatical claim or lexical example. Lesson9's regional numeral examples remain evidence-limited; Lesson27's interjection forms still require natural-speech evidence across speakers/regions. The term substitution must not be used to erase distinctions among linguistic context, real-world situation (`بارودۆخ`), and adjacent textual environment (`دەوروبەری دەق`).

## Change control
- This file is append-only review evidence.
- No raw lesson JSON, quizzes, answers, runtime manifest, database, Botkeep, or Telegram data was changed.
- No merge or deployment was performed.
- The temporary patch is eligible for a later separately reviewed reversible patch; it is not yet applied to the course source.
