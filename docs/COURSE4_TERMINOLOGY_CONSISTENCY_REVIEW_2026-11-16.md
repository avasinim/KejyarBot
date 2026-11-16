# Course 4 terminology consistency review — 2026-11-16

Branch: `fix/latin-course1-duplicate-note-2026-11-16`
Scope: terminology audit across the 50-lesson grammar course; this is an editorial consistency review, not final scientific approval.

## Definite correction applied

### Lesson 29 — Inflection

The quiz used `لەچۆنایەتی` three times where the intended technical term is `گەردان` (Inflection). The lesson's own definition and terminology appendix already use `گەردان`; the quiz now uses the same term. No concept, answer, or lesson sequence was changed.

## Owner decisions deliberately left open

These conflicts recur in the course and should not be normalized by guesswork:

1. **Enclitic:** Lesson 11's explanatory text uses `پاشبەستە`, while its appendix uses `پاشنووس`; Lessons 12 and 13 also use `پاشنووس`. Lesson 13 explicitly distinguishes an enclitic from a suffix and lists `Enclitic = پاشنووس`. The choice between `پاشبەستە` and `پاشنووس` needs an owner-approved canonical form and a consistent derivative form for proclitic.
2. **Noun Phrase:** `گرێی ناوی` is used in Lessons 3, 22–25, 31–34 and especially 47; Lesson 31 also uses `گروپی ناوی`. These may be synonyms, but one canonical course term should be selected before broad replacement.
3. **Subject:** `بکەر` is used consistently for Subject in Lessons 32–34 and elsewhere. Lesson 31 sometimes calls a nominalized constituent `بابەتی ڕستە` (sentence subject). It is unclear whether `بابەت` is intended as a separate syntactic label or is an inconsistent translation of Subject. Do not replace it automatically until the owner confirms the intended distinction.
4. **Inflection:** The established term in Lesson 29 is `گەردان`; only the three erroneous quiz occurrences of `لەچۆنایەتی` were corrected. No wider synonym sweep was performed.

## Cross-lesson observations

- Lessons 11–13 discuss clitics, enclitics, suffixes, person marking and subject marking. The distinction between a clitic and an affix is explained, but the Kurdish label for Enclitic is not stable.
- Lessons 31–34 distinguish phrase structure (Noun Phrase / Verb Phrase) from grammatical functions (Subject / Predicate). That distinction should remain explicit when the owner chooses the canonical Noun Phrase label.
- Lesson 31 uses `بابەت` in its subject-of-sentence examples while Lessons 32–34 use `بکەر` for Subject. This needs a deliberate terminology decision, not an unreviewed find-and-replace.

## Review status and safety

- Course 4 still has 50 lessons; no lesson was deleted or reordered.
- No unresolved owner terminology choice was silently decided.
- No production runtime, SQLite database, credentials, image assets, or deployment settings were changed.
- No merge or deployment was performed.
- CI for the current PR head has not been verified; no test success is claimed.
