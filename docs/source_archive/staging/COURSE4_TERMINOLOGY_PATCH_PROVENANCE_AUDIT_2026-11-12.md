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


## Checkpoint ZIP inspection — Lessons 29 and 31 v2 (2026-11-12)

The Library checkpoint ZIP `Course4_AppendOnly_Checkpoint_Lessons29-38_2026-11-09.zip` was materialized and inspected, including the nested lesson packages.

### Lesson 29
- The nested package contains only `grammar_29_append_only_patch.json`; it does not contain the owner-source lesson Markdown.
- The patch title is `چاوگی سادە و داڕێژراو — بنەما و شێوازی دروستبوون`.
- It adds 6 pedagogical Sorani examples, 9 appendix entries, and 3 activities.
- It explicitly distinguishes Derivation from Inflection conceptually, but the patch itself contains no Kurdish equivalent selection for Inflection. Therefore the existing runtime discrepancy `گەردان / لەچۆنایەتی` is not resolved by this patch.
- The patch editorial note states its new examples are pedagogical Sorani and are not attributed to a specified source.

### Lesson 31 v2
- The nested package contains `grammar_31_append_only_patch_v2.json` and `README_KU.txt`; no owner-source Markdown is included.
- Its source baseline identifies `main:course_data/grammar_course4_lessons.json` and a secondary text snapshot at lines 5248–5432. It records a 9-vs-10 appendix discrepancy between that Library text snapshot and main JSON.
- The v2 patch adds 6 examples, 9 appendix entries, and 3 activities; examples are marked pedagogical.
- Appendix addition `grammar_31_app_add_09` explicitly recommends using `گروپی ناوی` for Noun Phrase in future lessons, while also saying source-specific alternative terms should be clarified in a note. This is an editorial recommendation inside an append-only patch, not evidence that the original owner lesson or an external academic authority canonically selected that form.
- The v2 README records SHA-256 `2d394c7f1fac433636b6292f0e891b806cdf39d967c5fe20ef99948ad5094c69` for the patch file. The checkpoint ZIP contains this v2 patch; it is distinct from the older v1 patch hash recorded above.

**Correction/precision:** Lesson 29's patch is about simple and derived infinitives; it does not resolve the runtime Inflection translation conflict. The conflict is visible in the lesson's runtime quiz/content, but this checkpoint package is not its source provenance.

**Current source-access result:** the nested Lesson 29 and Lesson 31 v2 packages do not include the owner-source Markdown. No owner-source lesson text was found in this inspected checkpoint. No canonical terminology decision, lesson edit, quiz edit, status change, or deployment was made.


## Runtime baseline comparison: main vs PR head (2026-11-12)

The previously timed-out source retrieval was retried successfully. The exact `course_data/grammar_course4_lessons.json` files were fetched from both `main` and the PR branch and parsed as JSON. This is a direct runtime-data comparison, not a reconstruction from patch archives.

### Lesson 29 — Inflection terminology
- `main` lesson 29 key point and appendix use `لەچۆنایەتی (Inflection)`.
- PR-head lesson 29 key point and appendix use `گەردان (Inflection)`.
- The PR-head quiz still uses `لەچۆنایەتی` in the question/options/explanation for the Derivation-vs-Inflection item. Thus the PR has not fully propagated its new prose/appendix form into the quiz; an internal terminology mismatch remains.
- The Lesson 29 research note at `docs/COURSE4_LESSON29_DERIVATION_RESEARCH.md` defines the conceptual distinction between Derivation and Inflection but does not choose a Kurdish equivalent. It therefore supports the conceptual distinction, not either Kurdish label.
- This comparison establishes what each runtime branch currently contains. It does not establish an owner-approved canonical term.

### Lesson 31 — Noun Phrase terminology
- `main` Lesson 31 key points and appendix use `گروپی ناوی (Noun Phrase)`.
- PR-head Lesson 31 key points and appendix use `گرێی ناوی (Noun Phrase)`.
- The PR-head lesson still contains occurrences of `گروپی ناوی` in prose/examples/quiz explanations, so this is not a fully normalized switch. Both forms remain in the PR-head runtime.
- The Lesson 31 research note at `docs/COURSE4_LESSON31_INFINITIVE_NOMINALIZATION_RESEARCH.md` discusses nominalized infinitives in a noun phrase but does not adjudicate between these Kurdish labels.
- The owner-source Markdown is still absent from both lesson records (`source_markdown` length 0). The comparison is limited to the structured runtime content and research notes.

### PR readiness recheck
- GitHub's earlier `mergeable=false` response was transient/stale. A fresh PR metadata read now reports `mergeable=true`; PR #152 remains open and unmerged.
- The PR head at this check is `6049f5381183a27586bb1dcf8ec31d79bc942665`; base `main` is `7db20f242087e3eb9149e2e788f6c20529870f32`. The branch is 219 commits ahead and 0 behind.
- All 10 GitHub check runs attached to this exact head are completed with `success`, including Python checks, Course 4 Beta review, review-gate regression, Lesson 47–50 Beta validation, quiz override validation, orthography structure, and Kurdish months.
- CI and mergeability do not resolve the semantic/source approval gaps. PR remains unmerged; no merge, deployment, Botkeep import, restart, or database operation was performed.


## Runtime terminology comparison: Lessons 11–13 (2026-11-12)

The full structured runtime records for Lessons 11, 12, and 13 were fetched from both `main` and the PR branch and compared across key points, examples, activities, exercises, quiz, and appendix. All three records have no embedded owner-source Markdown (`source_markdown` length 0).

### Lesson 11 — Enclitic
- `main` key points define Enclitic as `پاشبەستە`; the appendix crosswalk also says `Enclitic = پاشبەستە`.
- PR head keeps `پاشبەستە` in the key-point definition, but changes the appendix crosswalk to `Enclitic = پاشنووس`.
- This creates an explicit within-lesson mismatch between the definition and glossary. The rest of the lesson's quiz remains about Clitic pronouns and does not resolve the label.
- The lesson's status is `scientific_review_complete_with_qualified_notes`; this is not an owner-approved terminology decision.

### Lesson 12 — Enclitic
- `main` appendix says `Enclitic = پاشبەستە`; PR changes it to `پاشنووس`.
- No corresponding explanatory definition or teaching content was changed to justify the new glossary form.
- The lesson's main subject distinction remains grammatical Subject = `بکەر`; its examples separately distinguish grammatical subject marking from possessive function. This does not justify translating semantic Agent or discourse Topic as the same category.

### Lesson 13 — terminology and approval boundary
- Lesson 13 remains `internal_cross_lesson_synthesis_no_external_source_mapping`, so it is not a source-verified authority for the disputed terminology.
- Its key point continues to define Enclitic as `پاشبەستە` and explicitly distinguishes it from Suffix = `پاشگر`.
- PR appendix adds a crosswalk with `Affix = گیرەک`, `Clitic = لکاو`, `Enclitic = پاشنووس`, and `Proclitic = پێشنووس`; it also records the older form `پاشبەستە` in the body/crosswalk history.
- The PR runtime still contains both `پاشبەستە` and `پاشنووس` in Lesson 13; it has not established one consistent final label.
- The PR changes `Affix` from the earlier `ئەفیکس` to `گیرەک` in the new crosswalk while retaining a note that the earlier form existed. This is a crosswalk/editorial change, not a demonstrated owner-approved canonical decision.
- Lesson 13 keeps the distinction between enclitic and suffix; do not collapse `پاشنووس/پاشبەستە` into `پاشگر`.

### Cross-lesson interpretation
- The PR changes only the glossary/crosswalk labels in Lessons 11–12, while the teaching definition in Lesson 11 and the teaching explanation in Lesson 13 retain `پاشبەستە`. This is a concrete propagation gap.
- Lesson 12 uses `بکەر` for grammatical Subject. Preserve the distinction between grammatical Subject, semantic Agent (`ئەنجامدەری کردار`), and discourse Topic; do not mechanically substitute `بابەت` or Agent for Subject.
- No term was selected or normalized during this audit. These are evidence findings only; no lesson, quiz, status, or runtime data was changed.


## Runtime parity audit: Lessons 14–20 (2026-11-12)

Fetched the complete `course_data/grammar_course4_lessons.json` from `main` and the PR branch, parsed both, and compared each entire structured lesson object (not just selected fields). Lessons 14, 15, 16, 17, 18, 19, and 20 are byte-for-byte equivalent at the parsed JSON-object serialization level: no runtime lesson-field differences were found in this range.

### Findings and source boundaries
- Lesson 14: no branch delta. Its appendix distinguishes noun-internal complements from the grammatical role of the whole noun phrase; no new terminology discrepancy surfaced in this comparison.
- Lessons 15–17: no branch delta. Existing distinctions remain: Tense vs Aspect; past vs non-past forms; Imperative as Mood rather than future tense; present stem vs past stem; and morpheme boundaries should not be inferred mechanically from similar endings.
- Lesson 18: no branch delta. It explicitly distinguishes Voice (active/passive) from alignment. Its appendix states no external source or page mapping was used and that a previously rejected source file must not be cited. Treat the current content as course teaching material, not source-verified external doctrine.
- Lessons 19–20: no branch delta. Their appendices state the base text was supplied by the project owner but bibliographic metadata is incomplete. Preserve the distinction between adverb as a word class and adverbial as a syntactic function; do not assume every `بە-` initial form is a prefix.
- All seven lessons have `scientific_review_complete_with_qualified_notes` status in both branches, but each structured record has no embedded owner-source Markdown (`source_markdown` length 0). Review status does not replace missing source provenance.

### Result
No patch or lesson edit is warranted from this parity check. The seven records remain unchanged; this is a verified no-delta checkpoint, not an endorsement of every underlying claim. No canonical term was changed, and no lesson, quiz, review status, or runtime data was modified.


## Runtime parity and terminology audit: Lessons 21–28 (2026-11-12)

Compared the full structured lesson objects from `main` and the PR branch for Lessons 21–28.

### Branch comparison
- Lessons 21–25 and 27–28 are identical between `main` and PR at the structured-record level.
- Lesson 26 has exactly one field-level difference: `appendix[10]` changes the description of the 2021 Ahmadi preprint from “distinguishing clitic and affix” to “distinguishing clitic and `گیرەک`.” No other Lesson 26 field or item count differs.
- All eight records have `scientific_review_complete_with_qualified_notes` in both branches; all have `source_markdown` absent (length 0). Lesson 21, 22, 23, 24, 25, 27 and 28 carry 8/8 quiz questions; Lesson 26 also has 8 quiz questions. This parity note does not independently re-validate the academic claims or quiz keys.

### Terminology and provenance observations
- Lesson 21 and 22 appendices distinguish word class / syntactic function and note owner-supplied material with incomplete bibliographic metadata (Lesson 21), while Lesson 22 identifies the directly supplied owner material and no external source mapping.
- Lessons 23–25 similarly identify owner-supplied source material; their appendices preserve distinctions among conjunction, vocative, and ezafe. Lesson 23 explicitly treats `ـیش` as a bound additive/emphatic clitic, not a free discourse particle.
- Lesson 26 cites Radnia (2022) for Sorani discourse particles and Ahmadi (2021) as a preprint. The PR's single wording change `ئەفیکس` → `گیرەک` creates a terminology-chain question against other project records that use `ئەفیکس` and/or `گیرەک`. It must not be silently normalized: “Affix” is the broader category, while Clitic is a distinct bound form; owner/academic decision is needed on the Kurdish label and on whether `گیرەک` is intended as a defined equivalent or a broader morpheme label.
- Lesson 27 keeps Interjection, Exclamation and Vocative as distinct levels/categories and explicitly points back to Lessons 24 and 26. Its long owner-supplied list of forms is not treated as a closed or universally validated inventory.
- Lesson 28 distinguishes Infinitive, Past Stem, Present Stem, Finite and Non-finite forms; it cites Kareem (2016), Haig (2018), and Ahmadi (2021), with the latter described as a preprint. It cautions that past-stem grouping is not a set of five infinitive classes and that stem formation is not a universal mechanical rule.

### Result
Only the Lesson 26 appendix wording difference was found. It is recorded as a provenance/terminology issue, not accepted as an authoritative canonical decision. No lesson content, quiz, status, or runtime data was changed in this audit. No merge or deployment action was taken.


## Runtime parity and terminology audit: Lessons 29–38 (2026-11-12)

Compared the structured records for Lessons 29–38 between `main` and the PR branch, including the key points, examples, comprehension, quizzes, appendices, review statuses, and embedded Markdown source where present.

### Lessons 29–31: targeted terminology deltas
- **Lesson 29:** three structured-field differences. The PR changes `لەچۆنایەتی (Inflection)` to `گەردان (Inflection)` in a key point, comprehension summary, and glossary. It also adds a Sorani/Kurmanji terminology crosswalk distinguishing Root, Bound Root and Stem, while explicitly saying the Sorani paradigm of Lessons 16 and 28 is primary. The quiz still contains `لەچۆنایەتی`; therefore the term replacement is not fully propagated. Both terms are present in the PR glossary/crosswalk context. No canonical equivalent is established by this mechanical branch comparison.
- **Lesson 30:** one appendix wording delta changes the phrase describing verbal particles from “not part of `لەچۆنایەتی` of the verb” to “not part of `گەردان` of the verb.” This follows the Lesson 29 label change but does not itself resolve the wider terminology decision.
- **Lesson 31:** the PR changes the Noun Phrase label from `گروپی ناوی` to `گرێی ناوی` in most teaching prose and in the glossary. Five residual occurrences of `گروپی ناوی` remain in the PR record, so propagation is incomplete. This includes the earlier identified quiz-related residue. The owner-source Markdown is absent from the structured record; both branches retain the same review status.

### Lessons 32–38: draft terminology and editorial deltas
- Lessons 32–34 and 36–38 differ between branches; Lesson 35 is identical. These are all `owner_review_pending_expanded_draft`, not academically approved runtime lessons. Their embedded source Markdown is present and must remain preserved.
- Lessons 32–34 contain changes to the use/count of `بکەر` and/or Noun Phrase terminology (`گروپی ناوی` / `گرێی ناوی`). The changes are in pending draft material, not evidence of an owner-approved terminology decision. In Lesson 34 the count of `بکەر` rises sharply in the PR record; this requires careful line-by-line editorial review rather than accepting a global replacement as a semantic correction.
- Lesson 36 has a small change in the number of `بکەر` occurrences; Lesson 37 has a small source-Markdown length change but no change in its structured lesson status or content counts. These small deltas are recorded for provenance and are not independently judged correct.
- **Lesson 38:** the PR changes the term `بەرڕستە` to `ژێرەڕستە` in the title, objective, explanatory text, exercises, and comprehension/source Markdown. This is a systematic terminology substitution, but the owner-source segment is separately preserved and the lesson remains pending owner review. Do not treat the substitution as an approved canonical choice until owner review confirms it.

### Shared source and safety observations
- Lessons 29–31 are marked `scientific_review_complete_with_qualified_notes`; this status does not erase the recorded terminology inconsistencies or the absence of embedded owner-source Markdown.
- Lessons 32–38 remain pending owner review. Their Markdown drafts are present (roughly 5.0–7.5 KB each) and must not be overwritten or silently promoted to runtime.
- The branch comparison found no reason to apply any further content edits as part of this audit. The existing lesson/quiz/status data was not changed; only this append-only evidence document was extended.
- The terminology decisions still requiring explicit owner/academic adjudication include: `گەردان` vs `لەچۆنایەتی` for Inflection; `گرێی ناوی` vs `گروپی ناوی` for Noun Phrase; and `ژێرەڕستە` vs `بەرڕستە` for Subordinate Clause. Keep Subject (`بکەری ڕێزمانی`), Agent (`ئەنجامدەری کردار`), Theme/Patient, and discourse Topic conceptually distinct.

### Result
This is a source/runtime comparison record, not approval of any changed term. No canonical term was selected, no owner-pending lesson was promoted, no lesson or quiz was edited, and no runtime data or production service was touched.


## Runtime parity and terminology audit: Lessons 39–46 (2026-11-12)

Compared the complete structured records for Lessons 39–46 between `main` and the PR branch, including objectives, key points, examples, activities, exercises, comprehension, quizzes, appendices, status and embedded source Markdown.

### Lessons 39–45
- Lessons 39, 40, 41, 42, 43, 44 and 45 are identical between `main` and the PR branch at the parsed structured-record level.
- All seven remain `owner_review_pending_expanded_draft`. Their preserved source Markdown is present (approximately 7.2–8.4 KB each).
- Their unchanged terminology includes the distinct concepts of Object, transitivity, intransitivity, light/compound verb constructions, clitic pronouns, grammatical Subject and semantic Agent. The unchanged status means these drafts are not approved runtime teaching material.

### Lesson 46
- Lesson 46 differs in 11 structured fields. The PR systematically substitutes `ژێرەڕستە` for `بەرڕستە` in the title, objective, explanatory material, exercises, comprehension and embedded source Markdown.
- The PR source also changes one phrase from `بکەر/نیهاد` to `بکەر/بکەر`; this appears to remove a synonym rather than introduce a new grammatical distinction, but requires editorial/source review.
- The draft itself explicitly states that the Compound/Complex distinction is a proposal and not a final course-owner decision.
- Lesson 46 remains `owner_review_pending_expanded_draft`; its preserved source Markdown is present (9,958 characters). The systematic terminology substitution is not evidence of approval.

### Cross-lesson terminology implications
- The PR's use of `ژێرەڕستە` in Lessons 37, 38 and 46 is consistent as an editorial direction, but Lesson 37–38 and Lesson 46 remain owner-review drafts. It must not be silently treated as the final course-wide canonical term.
- The established distinctions remain important: `بکەری ڕێزمانی` (grammatical Subject) is not interchangeable with `ئەنجامدەری کردار` (Agent); Object is a separate grammatical relation; Theme/Patient and discourse Topic are semantic/discourse notions and must not be collapsed into Subject or Agent.
- Lessons 39–45 contain no branch delta, so no new PR-only terminology change was found there. Their equality with `main` does not certify the academic correctness of their content.

### Result
Lessons 39–45 are parity-identical; Lesson 46 has 11 recorded field differences, primarily a systematic replacement of `بەرڕستە` with `ژێرەڕستە`. No term was canonized, no owner-review lesson was promoted, and no lesson/quiz/runtime or production data was modified. This section is an evidence-only append to the provenance audit.


## Cross-course terminology-chain scan: Lessons 1–46 (2026-11-12)

A lexical co-occurrence scan was run over the PR branch's structured Course 4 lesson records (all 46 lessons). This scan is a triage index only: co-occurrence of two forms does not prove synonymy or inconsistency, because a lesson may explicitly contrast grammatical functions, semantic roles, or competing terminology.

### Confirmed propagation candidates requiring manual semantic review
- **Enclitic — Lessons 11 and 13:** Lesson 11 contains both `پاشبەستە` and `پاشنووس`; Lesson 13 contains both (13 and 1 lexical occurrences respectively) and remains `internal_cross_lesson_synthesis_no_external_source_mapping`. These are high-priority propagation conflicts already documented above. Do not use Lesson 13 as a canonical authority.
- **Inflection — Lesson 29:** both `گەردان` and `لەچۆنایەتی` occur (3 each in the serialized lesson record), consistent with the incomplete propagation between explanatory text and quiz/glossary material already recorded.
- **Noun Phrase — Lesson 31:** both `گرێی ناوی` (15) and `گروپی ناوی` (5) remain in the same record. Review the five residual instances in context; do not mechanically replace every occurrence without checking quotations, historical notes, and quiz text.
- **Root/Stem crosswalk — Lessons 13, 15–17, 29:** both `ڕەگ` and `بنج` occur in lessons that discuss Root and Stem distinctions. Their co-occurrence is expected in contrastive explanations and is not itself a conflict. Lesson 13 also includes crosswalk forms `ڕیشە` and `بنکە`; the audit must preserve the explicit distinction between the course's Sorani terms and Kareem's Central Kurdish glossary terms.
- **Subject/Agent/Topic — Lessons 1, 3, 6, 8–10, 13, 18, 22–24, 27–29, 31–34, 39, 42–45:** several lessons contain two or more of `بکەر`, `ئەنجامدەری کردار`, and `بابەت`. This is a review flag, not an instruction to unify them. In particular, grammatical Subject, semantic Agent, and discourse Topic must remain distinct; Lesson 31's use of `بابەت (Subject)` requires context-level review.
- **Derivation — Lessons 3, 5 and 29:** both `داڕێژە` and `داڕشتن` occur. The forms may appear in different morphological contexts (derivational morpheme/process); inspect the definition and grammatical category before deciding whether a wording inconsistency exists.

### Lesson-state coverage
- The branch contains 46 Course 4 lessons: 30 `scientific_review_complete_with_qualified_notes`, 1 `internal_cross_lesson_synthesis_no_external_source_mapping`, and 15 `owner_review_pending_expanded_draft`.
- Lessons 32–46 are pending owner review; lexical findings within them must not be promoted to official terminology decisions.
- The scan does not replace source-level review or the full reading of examples, quiz options, explanations and appendices. It is a discovery aid to guide targeted inspection.

### Result
No automated terminology replacement was performed. No canonical forms were selected. No lesson, quiz, status, source record, or runtime content was changed by this scan; only this append-only audit was extended.
