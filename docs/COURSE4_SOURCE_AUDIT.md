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

### Additional individual-page inspection: PDF pp. 130, 140, 150, 160

- **PDF p. 130:** the page discusses verbal constructions and examples involving forms such as **توانین** (ability/can) and related forms. Treat these as possible modal/auxiliary constructions for analysis; do not assume that the book's own label maps exactly to a modern modal category.
- **PDF p. 140:** the visible discussion includes verb forms and paradigms, with a distinction between forms that appear to be inflectional patterns and the source's grouping of them. The examples need full context before any rule is transcribed.
- **PDF p. 150:** the section is explicitly concerned with negative forms/negation; examples visibly contrast forms with and without a negative marker, including **نە-**. This gives a clear candidate topic for a later lesson, but the distribution and interaction with tense/aspect still need independent validation.
- **PDF p. 160:** continues the negative-verb discussion and contrasts forms with a negative prefix and forms treated as positive. The page includes paradigmatic examples; their exact person/tense values must be checked against the preceding pages and dialect.

### Updated coverage statement
- Individual-page images now directly inspected in this review block: PDF pp. 81, 88, 93, 112, 113, 120, 130, 140, 150, and 160. These are spot checks across the 81–160 range, not exhaustive reading of all 80 pages.
- Topics now identified in the source for later detailed study: verb definitions, inflection/paradigms, infinitive and imperative forms, transitivity labels, active/passive voice, auxiliary/modal-like constructions, and negation.
- No complete lesson, final grammar rule, or teaching sequence has been written from this block. Exact source wording and examples still need systematic transcription, then independent checking.


## Visual review checkpoint: PDF pp. 81–221 (2026-11-05)

### Extraction status
- GitHub Actions run `41983766994` completed with conclusion **success** on isolated branch `reset/grammar-course4-content`, head commit `86482e43e67a6589a2f6a7261dc65e06f5e477c4`.
- Artifact `course4-source-text`, ID `13395570599`, was downloaded successfully. It contains 296 files, including individual page previews for the primary book through PDF p. 221.
- Artifact ZIP was unpacked locally and page images were inspected. The artifact itself is retained by GitHub until 2026-11-19.

### Additional direct visual inspection
The following individual page images were inspected at readable resolution in this checkpoint:
- **PDF p. 112:** section heading explicitly includes “Active and Passive” and **فعل مبنی للمعلوم و مبنی للمجهول**, with Kurdish labels **کاری کاردار و کاری کاربێژ**. A table aligns forms identified in the source as معلوم / مجهول and related forms. Record the source's labels exactly; do not equate them automatically with transitivity.
- **PDF p. 113:** continues the source's account of active/passive, with attributed reference material and examples. This confirms that the p. 112 topic is developed as a distinct discussion.
- **PDF p. 114:** continues the active/passive discussion and then begins a subsection on **زاراوەی کاردار و کاربێژ** (as visible in the page heading/text). The terminology and examples need exact transcription before teaching.
- **PDF p. 120:** continues verb constructions and examples, including forms with **دە-** and other verb material. The page also contains discussion of how forms are used; exact tense/aspect interpretation remains open.
- **PDF p. 130:** contains forms and examples involving **توانین** and related constructions. This is a candidate for studying ability/modal-like expressions, not proof that the source's category is equivalent to a modern modal auxiliary.
- **PDF p. 160:** continues discussion of negative verb forms and contrasts forms with negative marking and forms without it. The visible examples include **نە-**; its distribution must be checked across the surrounding paradigm.
- **PDF p. 180:** continues a section with imperative/command-like examples and related forms. Preserve the source's exact forms and context; do not infer a general imperative rule from this isolated page.
- **PDF p. 200:** shows further verb forms and examples, including forms discussed in relation to command/request and other verbal meanings. The precise subsection boundary and analysis require reading the intervening pages.
- **PDF p. 221:** contains a short final set of examples and appears to close the verb material immediately before the next contents-listed chapter begins at p. 222. The next chapter boundary is independently listed on the contents page (PDF p. 398) as **5 — جێناو**. Verify the opening of p. 222 directly before recording the exact transition.

### Structural and methodological observations
- The source's treatment from p. 112 onward separates active/passive terminology from other verb classifications. Keep **کاری کاردار / کاری کاربێژ**, **معلوم / مجهول**, and **فعلی متعدی** distinct unless a complete analysis of the source's definitions and examples demonstrates a justified relationship.
- The inspected pages include verb paradigms, negative forms, modal-like expressions, and imperative/command examples. These are topics for later transcription and validation, not approved teaching rules.
- A page image being inspected does not mean its full text has been transcribed. OCR remains a navigation aid only.
- No claims from pp. 81–221 have yet been marked “verified for teaching”; no lesson text has been drafted or approved from this review.

### Coverage update and next step
- Individual-page visual inspections now recorded across the verb chapter include pp. 81, 88, 93, 112–114, 120, 130, 140, 150, 160, 180, 200, and 221. This remains selective sampling, not exhaustive line-by-line inspection of every page from 81 to 221.
- The next step is to inspect the verb chapter's intervening paradigms and examples where a specific claim needs to be evaluated, then inspect PDF p. 222 and the **جێناو** chapter independently. Do not draft a curriculum or lessons until the source's structure, exact examples, and independent validation have been reconciled.
- Course 4 remains planned and inactive. No other course, `main`, production database, Botkeep runtime, merge, or deployment has been changed.


## Visual review checkpoint: primary book PDF pp. 222–227 (2026-11-05)

### Artifact and coverage
- The preview workflow triggered by commit `ab5cc7412cd1a0723232aa00eaa0b0cc08cf4d10` completed successfully: run `41984446777`.
- Artifact `course4-source-text`, ID `13395033327`, was downloaded and unpacked. It contains individual page images through PDF p. 300; artifact expires 2026-11-19.
- Individual images for PDF pp. 222–227 were inspected at readable resolution.

### Direct observations (not yet approved teaching claims)
- **PDF p. 222:** a section-opening heading is visibly printed as **جاوک** (visual transcription; retain the source glyphs pending expert reading). The opening prose discusses this category and refers to forms including Present Case and Infinitive. The contents page (PDF p. 398) labels p. 222 as **5 — جێناو**. This is a material heading/contents discrepancy or a possible terminology/reading issue; do not silently “correct” either reading. Reinspect the original scan and verify the exact term before curriculum mapping.
- **PDF p. 223:** subsection heading appears as **جۆرەکانی جاوک**. It classifies forms and explicitly includes the term **Consonant**. Examples include Kurdish verbal forms such as کردن، بردن، مردن، خوێندن، خواردن، ناردن، ژماردن، سووتاندن، بڕاندن، خنکاندن، لەوەڕاندن. This page appears to discuss verb-related forms rather than personal pronouns, but the heading terminology must first be resolved.
- **PDF p. 224:** continues the same classification with further forms/examples and explanatory notes.
- **PDF p. 225:** continues the classification and examples; a further subcategory is introduced.
- **PDF p. 226:** provides additional examples and explanatory discussion; the visible content continues the same grammatical category.
- **PDF p. 227:** introduces further lettered subdivisions and examples. The page continues the same topic rather than clearly beginning a personal-pronoun paradigm.

### Important audit finding
There is an unresolved inconsistency between the contents-page label **جێناو** for p. 222 and the visibly printed chapter/subsection headings **جاوک / جۆرەکانی جاوک** on pp. 222–223, while the examples and discussion appear verb-related. Possible explanations include an unusual source term, print/scan reading ambiguity, or an error in the contents page. No interpretation is selected yet. Do not rename the chapter, treat it as a pronoun chapter, or map its content into lessons until the original heading and intended grammatical concept are independently confirmed.

### Next review step
- Continue inspecting pp. 228–254 and compare the page headings with the contents map, especially the transition into p. 236 (listed as **ئاوەڵکار**) and p. 254 (listed as **پێوەندینیش**).
- Independently cross-check any identified category against reliable Central Kurdish/Sorani linguistic publications, but keep the agreed single-source rule: only **ڕێزمانی ئاخافتنی کوردی** supplies Course 4 lesson content.
- No lesson has been drafted, approved, or activated. Course 4 remains planned/inactive; no other course, main branch, production database, Botkeep runtime, merge, or deployment was changed.


### Boundary checks from the same artifact (additional direct inspection)
- **PDF p. 236:** the printed section heading is visibly **ئاوەڵکار**. The opening text explicitly discusses adverbs and gives examples including expressions of time and place. This agrees with the contents-page entry for p. 236.
- **PDF p. 254:** the printed section heading is visibly **پریپۆزیشن**; the page also prints the English term **A Preposition** and gives its English definition and examples (to, in, at, on, of, by, into, with, over, for, from, under, etc.). The contents page instead lists p. 254 as **پێوەندینیش**. This is a second heading/contents terminology discrepancy to resolve, not a license to rename or reinterpret the section.
- **PDF p. 255:** continues the preposition discussion with Kurdish examples and a comparison to other grammatical categories. It explicitly cautions about overlap/usage with adverb and conjunction categories; the distinctions need full contextual transcription before teaching.
- These page-boundary checks reinforce the need to preserve the book's printed terminology and record contents-page discrepancies rather than silently harmonizing them.
