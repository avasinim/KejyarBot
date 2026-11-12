# Course 4 terminology patch-provenance audit — 2026-11-12

**Disposition:** evidence-only, append-only review. No canonical terminology decision, lesson edit, quiz edit, review-status change, patch application, or deployment is authorized by this record.

## Scope and evidence boundary

Read-only inspection covered the archived Library artifacts in `/KejyarBot/Course4_Archive/`:
- `grammar_11_append_only_patch.json`
- `grammar_12_append_only_patch.json`
- `grammar_13_append_only_patch.json`
- `grammar_29_append_only_patch.json`
- `grammar_31_append_only_patch.json` and `grammar_31_append_only_patch_v2.json`
- `README_KU_PATCH_INDEX_2026-11-11.md` and `README_KU_PATCH31_VARIANTS_AND_LOADER_AUDIT_2026-11-11.md`

The current runtime comparison was read from `course_data/grammar_course4_lessons.json` at PR head `969d2c8fd80910b83a505e91fd658600bea3e06c`. This is a comparison of archived additive patch JSON and current runtime JSON, **not** a line-by-line audit against all original owner-source Markdown. The patch metadata's source paths and line references are not themselves proof that those Markdown source files were fetched.

## 1. Enclitic — `پاشبەستە` / `پاشنووس`

- Lesson 11 archived patch explicitly defines **Enclitic = پاشبەستە** and explains it as a post-host clitic. The patch distinguishes its positional description from its grammatical/semantic function.
- Current runtime Lesson 11 uses `پاشبەستە (Enclitic)` in a key point but uses `Enclitic = پاشنووس` in its appendix glossary. This is an internal runtime inconsistency.
- Lesson 12 archived patch concentrates on clitic pronouns, possession, and possible subject marking in past transitive clauses; the inspected patch does **not** establish a canonical Kurdish label for Enclitic. Current runtime Lesson 12 appendix uses `پاشنووس`.
- Lesson 13 archived patch uses `پاشبەستە` in its explanation of clitic attachment and distinguishes it from suffixes/affixes. Current runtime Lesson 13 body likewise uses `پاشبەستە`, while its appendix crosswalk uses `پاشنووس`.
- Lesson 11 patch hash recorded in the archive index: `fc5d92bd29baacf4e9f589f64ad2f78194bc88157823dc232861221665bccff0`.
- Lesson 12 patch hash recorded in the archive index: `e49c84486fa86be8d4f49f94d81b8c6d5c5f79bd531f52d67c46c396bf5264ac`.
- Lesson 13 patch hash recorded in the archive index: `2c6f24dfd2c0ff97c189c2b758bb70bfca2214811690b8ef15ecff365e9820db`.

**Provenance conclusion:** the archived Lesson 11 patch supports `پاشبەستە` as the wording chosen in that additive patch; it does not, by itself, establish a course-wide approved term. The current runtime glossary/crosswalk's `پاشنووس` conflicts with runtime body usage. Do not silently substitute either form. Keep Enclitic distinct from Clitic (`لکاو`), Clitic pronoun (`جێناوی لکاو`), Affix, and Suffix (`پاشگر`).

## 2. Inflection — `گەردان` / `لەچۆنایەتی`

- The archived Lesson 29 patch distinguishes **Derivation** from **Inflection** conceptually: derivation may create a new lexeme; inflection changes the grammatical form of the same lexeme.
- The inspected Lesson 29 patch additions use the English label `Inflection`; they do not establish either Kurdish equivalent as the patch's canonical choice.
- Current runtime Lesson 29 prose/key points/comprehension and appendix use `گەردان (Inflection)`; its structured quiz question/options retain `لەچۆنایەتی`, while the explanation uses the English label.
- The draft register records `لەچۆنایەتی` in patch/quiz history and `گەردان` in runtime Lessons 29–30. The archive evidence inspected here does not settle which Kurdish form is owner-approved.

**Provenance conclusion:** the mismatch is established in runtime and prior patch-history notes, but the inspected Lesson 29 patch itself does not prove that `لەچۆنایەتی` is the approved source term. Do not rewrite quiz strings until the original source and owner decision are verified.

## 3. Noun Phrase — `گرێی ناوی` / `گروپی ناوی`

- Both archived Lesson 31 patch variants use `گروپی ناوی` in added examples, explanations, and the terminology appendix; the appendix explicitly maps Noun Phrase to `گروپی ناوی`.
- The v2 patch supersedes v1 for review metadata only; its additions are recorded as identical. The archive README says preserve v1 historically and use v2 for review.
- v1 SHA-256: `223f58744bb09cc5fe9052865b7afdef04e38333bfd5d004a19397ec31c00d06`.
- v2 SHA-256: `2d394c7f1fac433636b6292f0e891b806cdf39d967c5fe20ef99948ad5094c69`.
- Current runtime Lesson 31 prose/key points/examples/comprehension/appendix use `گرێی ناوی`; the quiz retains `گروپی ناوی` in five occurrences.
- The v2 baseline records a discrepancy between the older Library snapshot (9 appendix items) and current main-branch JSON (10 appendix items). It explicitly says neither baseline should be silently altered.

**Provenance conclusion:** `گروپی ناوی` is demonstrably present in both Lesson 31 archived patch variants; `گرێی ناوی` is demonstrably present in current runtime prose and elsewhere in the course. This is a patch/runtime/assessment provenance conflict, not grounds to silently replace either term. Preserve the v1/v2 history and the 9-versus-10 appendix discrepancy.

## 4. Subject — `بکەر` / `بابەت`

- Lesson 12 archived patch distinguishes the clitic form from grammatical functions and uses `بکەر` and `بەرکار` as syntactic-role labels in its examples and explanations.
- Current runtime Lesson 12 appendix maps `Subject = بکەر` and `Object = بەرکار`.
- Current runtime Lesson 31 uses `بابەت (Subject)` for a nominalized constituent in subject position and uses `بابەتی ڕستە` in its quiz. Lesson 31 patch additions also use `بابەت` in the analysis of a constituent occupying the sentence-subject position.
- These artifacts do not demonstrate that `بابەت` and `بکەر` are interchangeable across frameworks or contexts.

**Provenance conclusion:** maintain separate contextual records for grammatical Subject, Agent (`ئەنجامدەری کردار`), Theme/Patient, and discourse Topic. A source/framework decision is needed before mapping `بابەت` to `بکەر`.

## Required next evidence

1. Retrieve and verify the original owner-source Markdown and the expanded drafts for Lessons 11, 12, 13, 29, and 31, including exact commit/version provenance; do not treat patch metadata paths as fetched source.
2. Inspect the cited grammatical sources and the course owner's established terminology policy before selecting any canonical form.
3. Record each term's first **defined** occurrence separately from incidental mentions.
4. After an explicit decision, create a dated append-only decision record and narrowly scoped lesson/quiz changes with regression tests. Keep the original patch files and all historical variants intact.
5. Keep Lesson 13's status `internal_cross_lesson_synthesis_no_external_source_mapping` unchanged; it is not an academic authority for resolving terminology.

## Preservation and operational boundary

This audit changes no lesson JSON, patch, quiz, academic status, database, Botkeep environment, or Telegram state. It does not apply any archived patch. No merge, import, restore, restart, sync, or deployment is performed or authorized by this record.


## Exact archived-patch byte verification — 2026-11-12 (append-only)

The five Library JSON files were materialized as raw bytes and parsed independently. SHA-256 was recomputed from those exact bytes and compared with the archive README where an index entry exists:

| Patch | Bytes | Recomputed SHA-256 | Result |
|---|---:|---|---|
| `grammar_11_append_only_patch.json` | 7,415 | `fc5d92bd29baacf4e9f589f64ad2f78194bc88157823dc232861221665bccff0` | matches README |
| `grammar_12_append_only_patch.json` | 5,412 | `e49c84486fa86be8d4f49f94d81b8c6d5c5f79bd531f52d67c46c396bf5264ac` | matches README |
| `grammar_13_append_only_patch.json` | 5,858 | `2c6f24dfd2c0ff97c189c2b758bb70bfca2214811690b8ef15ecff365e9820db` | matches README |
| `grammar_29_append_only_patch.json` | 6,276 | `896bba6987b49f26fb43015dc068d5d2936e781eee88584840c53e091e2dcbae` | exact bytes verified; no matching hash line was surfaced in the inspected README excerpt |
| `grammar_31_append_only_patch.json` (v1) | 11,804 | `223f58744bb09cc5fe9052865b7afdef04e38333bfd5d004a19397ec31c00d06` | matches v1 archive record |

Additional source-level observations from the parsed patch JSON:

- Lesson 11 patch explicitly describes Enclitic as a post-host clitic and labels it `پاشبەستە`; it says that this positional label alone does not determine grammatical/semantic function.
- Lesson 12 patch explicitly warns that Clitic pronoun is a form/category while Subject, Object and Possession are functions/relations. Its examples distinguish possessive `ـیان` from possible subject marking in a past transitive construction. It does not establish an Enclitic translation.
- Lesson 13 patch states that Enclitic and Suffix are not interchangeable and gives `پاشبەستە`; its examples are explicitly pedagogical Sorani examples, not quotations or rules attributed to Saeed Karimi.
- Lesson 29 patch itself gives the Derivation/Inflection conceptual contrast but does not choose either Kurdish equivalent for Inflection. Its added examples are identified as pedagogical Sorani.
- Lesson 31 v1 patch baseline records 14 key points, 8 examples, 3 activities, 5 exercises, 8 quiz items and 9 appendix items. Its added appendix explicitly uses `گروپی ناوی` for Noun Phrase. The v2 package/metadata remains a separate historical variant; do not overwrite v1 or erase the runtime 9-versus-10 appendix discrepancy.

**Integrity limit:** byte/hash verification proves the identity of the archived patch files inspected; it does not prove that the owner-source Markdown referenced in patch metadata was retrieved, nor that the patches are applied to the current runtime. No patch was applied and no lesson/quiz/status was changed.
