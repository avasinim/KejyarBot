# Course 4 — Source Audit (Preliminary)

Status: **single-source curriculum decision adopted; source inspection in progress; no lesson content approved**

This audit belongs to the isolated branch `reset/grammar-course4-content`. It does not activate Course 4, alter other courses, or deploy anything.

## Adopted source policy

The user has chosen to build Course 4 using only **ڕێزمانی ئاخافتنی کوردی** as its curriculum's primary and sole course-content book.

The separate book `ڕێزمانی ڕاناوی لكاو.pdf` is **excluded from Course 4 content development**. Do not use its lessons, classifications, examples, or theoretical framework in the course. It is recorded below only for provenance/history and is not an active course source.

Independent linguistic publications may still be consulted strictly to verify or challenge claims from the primary book. They must not silently replace its curriculum structure or be blended into lesson content as if they came from the primary book. Any disagreement must be documented, and unresolved claims must be excluded or clearly qualified.

## Active primary source and provenance

- File: `Rezmany_axawtny_kurdy.pdf`
- Source commit: `f7f5236d861aaa5f9f26e81b0d7a25ceb992914e`
- Blob: `e144eac2937c4f13a4f852fc403c17cc0fee3671`
- Visible title page (PDF p. 3): **ڕێزمانی ئاخافتنی کوردی**
- The copyright/publication page (PDF p. 4) indicates an original publication in 1990 and a second printing in 2011. The exact bibliographic role/attribution needs further careful transcription; do not infer an individual author from an editorial signature alone.
- PDF length: 400 pages.

## Excluded source — provenance only

- File: `ڕێزمانی ڕاناوی لكاو.pdf`
- Source commit: `bde4b44ddf5127e6c9762d014fd7d2cde2dc0423`
- Blob: `68da93bc3cb9e37f492b13f346a2c7961b9639dc`
- Visible title page (PDF p. 3): **ڕێزمانی ڕاناوی لکاو**
- Visible author name: **ڕیا عومەر ئەمین**.
- The title page identifies the Kurdish Department, University of Baghdad.
- PDF length: 32 pages.
- **Decision: excluded from Course 4 content.** No rules, examples, terminology, or theory from this book are to be incorporated into lessons.

## Direct visual observations from the active source

### ڕێزمانی ئاخافتنی کوردی

- PDF p. 3: title page identifies the work as **ڕێزمانی ئاخافتنی کوردی**. This is a scope warning: it must not automatically be treated as a comprehensive grammar of every Kurdish variety.
- PDF p. 4: publication information indicates an original publication in 1990 and a second printing in 2011.
- PDF pp. 5–10: these pages are introductory/foreword material, not a table of contents. They discuss the preparation and revision of the grammar and issues around Kurdish grammatical description and terminology. Page 10 ends with an editorial/committee-style signature; its precise wording and bibliographic significance have not yet been conclusively transcribed. Do not treat the foreword as a list of validated grammar rules.
- PDF p. 11: the section on **ناو** begins.
- PDF p. 12: discusses simple nouns and gives examples attributed to named writers/speakers; the page also includes a definition.
- PDF pp. 13–15: continues the distinction and discussion of simple and compound nouns, with examples and classification. These examples must be transcribed exactly before reuse.
- The introductory pages' statements about Kurdish grammar, terminology, and revision are the author's/editorial framing, not independent proof that every later rule is universally valid.
- No general rule from these pages is approved for a course lesson yet. The dialect/register scope of each example and analysis still needs confirmation.

## Inspection progress

Visually inspected directly from page images:
- PDF pp. 3–30 (title/publication pages, introduction, noun chapter, and the opening classification/personal-pronoun material).
- The noun chapter has been visually followed from its opening on p. 11 to the transition into pronouns on p. 25. The pronoun chapter has been inspected through p. 30. This remains a structural pass, not a complete rule-by-rule audit.
- Next source-review task: locate the book's actual contents/section structure after the introduction and systematically map the chapter boundaries and printed page numbers. Do not assume the book has a conventional contents page; none appeared in pp. 3–10.

### Continued visual review: PDF pp. 16–20

- PDF pp. 16–17: the book continues its treatment of noun categories. The visible page structure separates several classification approaches, including distinctions presented as general/proper, and additional semantic or grammatical groupings. The lists continue across the page break.
- PDF p. 18: the text explicitly introduces English labels including **Common Noun**, **Abstract Noun**, **Concrete Noun**, **Proper Noun**, and **Collective Noun**, alongside Kurdish discussion and examples. It also refers to classifications in Persian grammatical works.
- PDF p. 19: continues the noun discussion with further groupings/examples and a comparative table. The page includes terminology and forms that need exact transcription before any instructional reuse.
- PDF p. 20: begins a discussion of material/concrete and abstract/meaning-related noun groupings, with definitions and examples. This is still part of the noun chapter, not a new chapter.
- **Important methodological caution:** pp. 16–20 visibly bring together more than one grammatical classification tradition/terminology set (including Persian and English labels). These must not be collapsed into one supposedly universal taxonomy. Each category needs its own definition, source context, scope, and independent linguistic validation. The book's presentation alone does not establish that all labels map one-to-one across Kurdish, Persian, and English grammatical traditions.
- PDF pp. 21–22: the noun discussion continues with further explanations and examples. The wording and examples require exact transcription; this review does not certify their theoretical accuracy.
- PDF pp. 23–24: the book discusses compound nouns and shows formation patterns/examples. These examples must be checked for orthographic and morphological consistency before reuse.
- PDF p. 25: a new numbered chapter begins, titled **ڕاناو - ضمیر** (pronoun). This establishes the visible transition from the noun chapter (beginning at p. 11) to the pronoun chapter at p. 25.
- PDF pp. 26–29: the pronoun chapter lays out multiple classifications and examples, and refers to more than one grammatical description tradition/source. The lists include several functional/semantic labels; they should not be assumed to form a single mutually exclusive classification system without detailed analysis.
- PDF p. 30: the text begins a distinct subsection titled **ڕاناوی کەسی (الضمیر الشخصی)** (personal pronoun), after the preceding general classification discussion. This is the first clearly visible named pronoun subtype section in the inspected pages.
- **Scope caution:** the pronoun discussion explicitly compares/mentions different descriptions and sources. We must distinguish the book's own account from cited classifications and must not merge those into one unqualified Kurdish grammar rule.
- At this stage, only the presence and broad structure of these discussions are recorded. The individual category definitions, compound-formation rules, pronoun definitions, and examples have **not** been fully transcribed or approved for lessons.

## Extraction reliability

The GitHub Actions extraction run `41982256365` completed successfully and produced visual page previews.

However:
- Source 1: 397 pages were extracted as embedded text, but the extracted text is visibly unreliable/garbled in many places; only 3 pages used OCR.
- Source 2: 31 of 32 pages used Arabic+English OCR marked **UNVERIFIED**; only one page used embedded text. Source 2 is excluded from the course regardless.
- Therefore, the extracted TXT files are navigation aids only. They are **not authoritative transcriptions** and must not be used to write rules or examples without visual checking.

## Verification rules before lesson drafting

For every proposed rule/example from the active primary source, record:
1. Exact source title and edition/publication details where available.
2. Printed page number and PDF page number (both, when different).
3. Exact transcription of the relevant Kurdish text/example.
4. Scope: Central/Sorani, another variety, spoken register, written register, or unspecified.
5. What the author actually claims, separately from our interpretation.
6. Independent corroboration from a reliable linguistic source, or an explicit note that corroboration is not yet found. Independent sources are for validation only, not a second curriculum source.
7. Decision: verified for teaching / needs clarification / conflicting evidence / exclude.

Do not silently normalize the source's orthography, dialect forms, or terminology. Preserve the original form in the evidence record and place any editorial explanation separately.

## Current decision

**No lesson text is approved.** Course 4 remains planned and inactive. The single-source decision is adopted, but the primary book still requires systematic page-by-page inspection and independent validation of claims. No other course, `main`, production database, Botkeep runtime, or deployment has been changed.

## Verified contents page and chapter map (continued visual review)

PDF p. 398 is a contents page headed **پێڕست**. Its visible chapter map is:

| Printed page | Heading as printed / visible |
|---:|---|
| 5 | ڕوونکردنەوەیەکی پێویست |
| 11 | بەشەکانی ئاخافتن |
| 11 | 1 — ناو |
| 25 | 2 — ڕاناو (ضمیر) |
| 66 | 3 — ئاوەڵناو (الصفة) |
| 80 | 4 — کار (فعل) |
| 112 | کاری کاردار و کاری کاربێژ |
| 222 | 5 — جێناو |
| 236 | 6 — ئاوەڵکار |
| 254 | 7 — پێوەندینیش |
| 273 | 8 — هاوەڵ (عطف / Conjunction) |
| 349 | 9 — ئامرازی (تعجب) |
| 388 | وشەی سەرنجخۆ و وشەی بەستراو |
| 392 | یەکەم — کۆمەک |
| 395 | 1 — پێشگر |

The contents page shows the book's own chapter organization; it does **not** establish that the labels are theoretically equivalent to contemporary linguistic categories. In particular, the distinction between **ڕاناو** (p. 25) and **جێناو** (p. 222) must be investigated rather than silently merged or translated as one category. The two verb-related sections at pp. 80 and 112 also need separate inspection. The table above is a structural transcription from PDF p. 398, not a lesson plan or endorsement of the book's classifications.

## Independent linguistic cross-checks located (validation only)

These works are not additional curriculum books. They are independent checks to test claims from the single adopted source:

1. **W. M. Thackston, _Sorani Kurdish: A Reference Grammar with Selected Readings_.** The accessible PDF contents and text distinguish noun states, personal/possessive pronouns, verbal morphology, and other syntactic features. It treats the absolute, indefinite, and definite states of nouns separately and gives detailed sections on verb forms and transitivity/ergativity. This provides a useful independent comparison for the active book's noun, pronoun, and verb chapters. It also makes clear that the labels and chapter boundaries in one grammar should not automatically be imposed on another. Online text/PDF: https://raw.githubusercontent.com/sinaahmadi/KurdishCL/master/labs/Thackston_Sorani.pdf
2. **Hiba Gharib & Clifton Pye (2018; journal page published 2023), “The clitic status of person markers in Sorani Kurdish,” _Kansas Working Papers in Linguistics_ 39, 57–65.** The authors argue that direct and oblique person markers show a mixture of affix and clitic properties. This is a warning against teaching a simplistic one-label analysis of every attached person marker. DOI: https://doi.org/10.17161/1808.27692
3. **Sadaf Kalami (2023), “Nominal linkers in Central Kurdish (Ardalāni variety),” _Toronto Working Papers in Linguistics_ 45(1).** This study analyzes Ezafe and noun-phrase structure in the Ardalāni variety and reports phonological conditioning and a distinct definite-context pattern. It is a variety-specific check, not a universal rule for all Sorani varieties. DOI: https://doi.org/10.33137/twpl.v45i1.41691
4. **University of Arizona, Iranian Languages Catalogue — Sorani Kurdish.** Its morphosyntax overview describes noun states and split alignment, including nominative-accusative patterns in the present and ergative-absolutive patterns in the past. This is a concise reference point for checking claims about noun marking and transitive past clauses: https://iranian-languages.arizona.edu/node/2

### Initial validation implications (not final judgments)

- The book's noun classification needs to be checked against independently described noun states and nominal marking, not merely repeated as a list of semantic labels.
- Its pronoun and person-marker material requires special care: the independent clitic study shows that direct/oblique markers do not fit a simple affix-versus-clitic dichotomy.
- The contents page's two distinct headings **ڕاناو** and **جێناو** are a high-priority investigation item. Do not infer that they are synonyms or separate modern syntactic categories until the source's definitions and examples have been transcribed and compared.
- The verb section must be checked for tense/aspect, transitivity, person indexing, and split alignment, with attention to variety and register. Any mismatch with independent research must be documented.
- No claim has yet been promoted to “verified for teaching.” The references above establish a validation path, not approval of any individual rule in the primary book.

## Current visual-review checkpoint (2026-11-05)

- GitHub Actions run 41983195239 completed successfully on isolated branch reset/grammar-course4-content, commit 83b11fc1aa4d7ed73ab1f16eb8ece7f63a2de0ef.
- Steps for extraction, rendering, and artifact upload all completed successfully.
- Artifact course4-source-text, ID 13395325514, contains 146 files, including individual page previews for PDF pp. 1–80 and 380–400, contact sheets, extraction report, and diagnostics. It is retained until 2026-11-19.
- The preview artifact was downloaded and its page images inspected locally. Directly inspected in this continuation: PDF pp. 11–13, 25, 40, 50, 60, 70, 80, and 398. Earlier review notes above record prior inspection of pp. 3–30.
- PDF p. 398 has now established the full high-level chapter map. The next task is to render and inspect the primary book's intervening pages systematically, beginning with pp. 66–160, and manually transcribe candidate rules/examples before validation.
- OCR remains unverified and is not used as an authoritative source.

## Visual review block: PDF pp. 81–160 (2026-11-05)

### Extraction and rendering status
- GitHub Actions run `41983515805` completed successfully; all seven substantive workflow steps succeeded.
- Artifact `course4-source-text`, ID `13395126038`, was downloaded and unpacked locally. It contains 231 files, including individual page images and contact sheets for the primary book.
- The following primary-book pages were directly inspected at readable individual-page resolution in this block: PDF pp. 81, 88, 93, 112, 113, and 120. Contact sheet `main_grammar_06.jpg` also gives an overview of pp. 81–96. This is a selective visual review, not yet a line-by-line transcription of every page 81–160.

### Directly observed content
- **PDF p. 81** is within the verb chapter. It quotes an English definition from Evan Penglis, _An English Grammar Book_: “A verb is that part of speech which asserts or predicates something.” The Kurdish text then presents another definition attributed to an Arabic grammar reference and discusses action/state and related examples. These are source-attributed definitions, not yet accepted as an adequate modern linguistic definition.
- **PDF p. 88** continues the verb discussion with inflected examples and a distinction in the examples between forms treated as ordinary/non-compound and forms discussed as compound or auxiliary constructions. The exact paradigms need transcription from the surrounding pages before teaching.
- **PDF p. 93** contains tables contrasting infinitive/base forms, imperative forms, and forms identified in the book as **فعلی متعدی** (transitive verb). This classification and the examples require checking against argument structure and dialect before use.
- **PDF p. 112** begins a section headed in English “Active and Passive” and in Kurdish **فعل مبنی للمعلوم و مبنی للمجهول**, followed by discussion of **کاری کاردار** and **کاری کاربێژ**. The table aligns forms labelled معلوم / مجهول and رەک (as visible in the source).
- **PDF p. 113** continues the active/passive discussion, refers to an earlier grammar reference, and describes how active/passive is determined in the source's framework. This is a separate topic from merely classifying verbs as transitive/intransitive; the contents-page label at p. 112 should not be simplified into that distinction.
- **PDF p. 120** continues with verb forms and examples, including a discussion of forms with **دە-** and **نە-** in the source's analysis. The exact scope and function of these prefixes need comparison with modern descriptions of Sorani tense/aspect and negation.

### Cautions raised by this block
- The primary book relies in places on definitions attributed to older English/Arabic grammar references. A borrowed definition should not be treated as a sufficient contemporary linguistic analysis without checking how it fits Kurdish morphology and syntax.
- The book's terms **کاری کاردار / کاری کاربێژ**, **معلوم / مجهول**, and **فعلی متعدی** occur in related but non-identical discussions. Keep these distinctions separate pending a careful transcription and syntactic analysis.
- The book's classification and paradigms may reflect a specific variety/register of spoken Kurdish. Every candidate rule must be checked for dialect, tense/aspect, person marking, and argument structure.
- No verb rule from pp. 81–160 has yet been approved as verified teaching content. This review records what the source visibly contains, not an endorsement of its accuracy.

### Next review target
- Continue individual-page inspection through PDF pp. 121–160, with priority to headings, paradigm tables, and examples; then review pp. 161–221 before reaching the next chapter boundary at p. 222.
