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
- **PDF p. 222:** a section-opening heading is visibly printed as **چاوگ** (visual transcription; retain the source glyphs pending expert reading). The opening prose discusses this category and refers to forms including Present Case and Infinitive. The contents page (PDF p. 398) labels p. 222 as **5 — جێناو**. This is a material heading/contents discrepancy or a possible terminology/reading issue; do not silently “correct” either reading. Reinspect the original scan and verify the exact term before curriculum mapping.
- **PDF p. 223:** subsection heading appears as **جۆرەکانی چاوگ**. It classifies forms and explicitly includes the term **Consonant**. Examples include Kurdish verbal forms such as کردن، بردن، مردن، خوێندن، خواردن، ناردن، ژماردن، سووتاندن، بڕاندن، خنکاندن، لەوەڕاندن. This page appears to discuss verb-related forms rather than personal pronouns, but the heading terminology must first be resolved.
- **PDF p. 224:** continues the same classification with further forms/examples and explanatory notes.
- **PDF p. 225:** continues the classification and examples; a further subcategory is introduced.
- **PDF p. 226:** provides additional examples and explanatory discussion; the visible content continues the same grammatical category.
- **PDF p. 227:** introduces further lettered subdivisions and examples. The page continues the same topic rather than clearly beginning a personal-pronoun paradigm.

### Important audit finding
There is an unresolved inconsistency between the contents-page label **جێناو** for p. 222 and the visibly printed chapter/subsection headings **چاوگ / جۆرەکانی چاوگ** on pp. 222–223, while the examples and discussion appear verb-related. Possible explanations include an unusual source term, print/scan reading ambiguity, or an error in the contents page. No interpretation is selected yet. Do not rename the chapter, treat it as a pronoun chapter, or map its content into lessons until the original heading and intended grammatical concept are independently confirmed.

### Next review step
- Continue inspecting pp. 228–254 and compare the page headings with the contents map, especially the transition into p. 236 (listed as **ئاوەڵکار**) and p. 254 (listed as **پێوەندینیش**).
- Independently cross-check any identified category against reliable Central Kurdish/Sorani linguistic publications, but keep the agreed single-source rule: only **ڕێزمانی ئاخافتنی کوردی** supplies Course 4 lesson content.
- No lesson has been drafted, approved, or activated. Course 4 remains planned/inactive; no other course, main branch, production database, Botkeep runtime, merge, or deployment was changed.


### Boundary checks from the same artifact (additional direct inspection)
- **PDF p. 236:** the printed section heading is visibly **ئاوەڵکار**. The opening text explicitly discusses adverbs and gives examples including expressions of time and place. This agrees with the contents-page entry for p. 236.
- **PDF p. 254:** the printed section heading is visibly **پریپۆزیشن**; the page also prints the English term **A Preposition** and gives its English definition and examples (to, in, at, on, of, by, into, with, over, for, from, under, etc.). The contents page instead lists p. 254 as **پێوەندینیش**. This is a second heading/contents terminology discrepancy to resolve, not a license to rename or reinterpret the section.
- **PDF p. 255:** continues the preposition discussion with Kurdish examples and a comparison to other grammatical categories. It explicitly cautions about overlap/usage with adverb and conjunction categories; the distinctions need full contextual transcription before teaching.
- These page-boundary checks reinforce the need to preserve the book's printed terminology and record contents-page discrepancies rather than silently harmonizing them.


## Visual review checkpoint: primary book PDF pp. 349, 388, 392, 395, 398 and 400 (2026-11-05)

### Artifact and workflow
- The expanded extraction/preview workflow for commit `203bc7dee719cd8d2ef3f0aa901d67bba70ac292` completed successfully: run `41984870708`.
- Artifact `course4-source-text`, ID `13394938732`, includes the primary-book extracted text, extraction report, and individual page previews across the expanded 1–400 page range. Artifact expires 2026-11-19.
- The page images for PDF pp. 349, 388, 392, 395, 398 and 400 were visually inspected. OCR/extracted text remains a navigation aid; page-image reading governs these observations.

### Direct observations (not yet approved teaching claims)
- **PDF p. 349:** begins section 9, printed as **ئامرازی «تعجب»**, with the English gloss **Interjection**. The prose describes an exclamatory/interjection category and gives examples. This supports the contents-page entry for p. 349 and provides a clear category boundary.
- **PDF p. 388:** heading is **وشەی سەرنجخۆ و وشەی بەستراو**. The discussion compares two broad types of words and states that the source distinguishes the following five word classes in its analysis: **ناو، ڕاناو، ئاوەڵناو، کار (چاوگ)، ئاوەڵکار**. The printed term in parentheses beside **کار** appears as **چاوگ**, consistent with the unresolved heading seen on pp. 222–227. Do not silently replace it with a modern label or assume it means pronoun.
- **PDF p. 392:** a tree diagram divides **وشە** into **سەربەخۆ** and **بەستراو**; the latter is further divided into **ئامراز، کیریۆک، نیشانە** (visual readings; exact technical spelling should be checked against surrounding pages). The page then discusses the classification and gives an explanation of **کیریۆک**. This is source-specific terminology and requires careful transcription before lesson use.
- **PDF p. 395:** continues the discussion of bound forms and describes two groups of forms/markers, including forms appearing before and after a word; the examples and terminology require full transcription and cross-checking. This is not sufficient by itself to assert a general linguistic classification.
- **PDF p. 398:** contents page reconfirms the chapter map: p. 349 **ئامرازی تعجب**; p. 388 **وشەی سەرنجخۆ و وشەی بەستراو**; p. 392 **یەکەم — کۆمەک**; p. 395 **پێشگر**. The page map is consistent with the inspected boundaries, but the p. 222 and p. 254 terminology discrepancies recorded above remain unresolved.
- **PDF p. 400:** visually appears blank apart from the printed page number; no additional chapter content is visible on this page.

### Updated structural findings and cautions
- The book's closing pages introduce a distinction between independent/free and bound words and a further internal classification of bound forms. This is a separate analytical layer from the earlier chapter list; do not flatten it into a simple list of parts of speech.
- The recurrence of **چاوگ** in the p. 388 parenthetical classification, alongside the p. 222–227 verb-related examples, strengthens the need to resolve the source's exact intended term. It does not by itself establish the correct modern linguistic equivalent.
- The p. 392 tree diagram and p. 395 discussion need line-by-line manual transcription before they can support a lesson. Preserve source spellings and terminology, and flag any claim that cannot be independently corroborated.

### Next review step
- Continue with a systematic pass over the full verb-related section and the intervening pages 301–348, then manually transcribe the p. 388–397 discussion and compare it with independent Central Kurdish linguistic research strictly for validation.
- Do not draft or activate lessons from OCR snippets or the contents page alone. Course 4 remains planned/inactive with zero lessons; no other course, main branch, production database, Botkeep runtime, merge, or deployment was changed.


## Follow-on visual sample: primary book PDF pp. 301–348 (2026-11-05)

- The expanded artifact from run `41984870708` was used to inspect page images at PDF pp. 301, 310, 320, 330, 340 and 348.
- These sampled pages visually continue the conjunction-related material following the section opening at p. 273; no new major chapter boundary is apparent in these sampled points before the interjection heading at p. 349.
- The pages contain continued explanatory prose, examples and subdivisions. This is only a spaced sample, not a complete reading or transcription of pp. 301–348; do not treat it as evidence that every subsection or claim in the range has been checked.
- Next step remains a sequential review of the intervening pages and manual transcription of source examples before any teaching content is proposed.


## Targeted close reading: conjunction section PDF pp. 309, 314, 326 and transition p. 348 (2026-11-05)

### Direct page-image observations
- **PDF p. 309:** the page opens numbered subsection **10** under the conjunction material (the printed Kurdish subtype label is not yet safely transcribed). The text explicitly discusses how the cited authors/grammars treat this conjunction form, compares their analyses, and supplies Kurdish examples. The source itself therefore reports differing descriptions; its cited authorities must not be collapsed into a single uncontested rule.
- **PDF p. 314:** begins numbered subsection **14** within the same conjunction discussion. It provides a definition/explanation and multiple numbered examples. The precise subtype label should be transcribed again from a higher-resolution crop before it is used as a lesson heading.
- **PDF p. 326:** begins numbered subsection **20**, visibly headed **ئامرازی (هەر)ی عطف** (conjunction particle/form هەر). It distinguishes uses and gives examples; among its English glosses for the discussed quantifying/related forms are **any, every, each**. These are source-specific descriptions and need contextual transcription and independent validation before teaching.
- **PDF p. 348:** the prose is a transition/introductory discussion immediately before the next section. It discusses an exclamatory category and includes the English term **Interjection**, consistent with the clear section heading on p. 349. The exact examples and definition still need manual transcription.

### Method and limitation
- These pages were inspected from the original page images, not inferred from OCR alone. The page numbers and numbered progression (10, 14, 20) show that the conjunction section contains multiple internally numbered subtypes, rather than one short undifferentiated topic.
- This is targeted close reading of four pages, not a full transcription of all pages 273–348. The OCR extract is heavily character-encoded and cannot be treated as authoritative text. Do not turn the partial observations into a complete classification or lesson sequence.
- The next safe step is to crop and transcribe the subtype headings and examples from the source images, then check each grammatical distinction against independent Sorani/Central Kurdish research. Keep the primary book as the sole lesson source; independent literature is validation only.


## Erratum — correction of the source term (2026-11-05)

- **Correction:** the earlier visual transcriptions in this audit that read **جاوک** were incorrect. The correct printed/grammatical term is **چاوگ**. All seven occurrences in the previous audit text have been corrected to **چاوگ**.
- This is a substantive terminology correction, not a stylistic normalization. Future references to the category and its subdivisions must use **چاوگ**, while preserving any other exact source forms as printed.
- The earlier uncertainty caused by the mistaken reading **جاوک** is withdrawn. The remaining task is to verify the precise definitions, subdivisions, and examples of **چاوگ** directly against the relevant page images and independent linguistic research; do not infer a full grammatical analysis from the corrected label alone.
- The source's contents-page entry **جێناو** for p. 222 still needs to be reconciled with the actual section heading **چاوگ** and the chapter's content. Do not equate **چاوگ** with **جێناو** or silently change either term.
- Going forward, every technical term must be checked character by character against a readable source-page image and cross-checked before it is used in course material. No OCR-only transcription is acceptable for lesson headings or core terminology.


## High-resolution terminology verification: چاوگ (2026-11-05)

- Re-opened the original page images at readable resolution and enlarged the heading on PDF p. 222. The heading is **چاوگ**; the initial consonant is **چ** (three dots), not **ج**. The earlier reading **جاوک** was a visual transcription error.
- PDF p. 223 independently confirms the subsection heading **جۆرەکانی چاوگ** and uses **چاوگ** repeatedly in the body text. Its examples and explanation are directly associated with this term.
- PDF p. 388 independently prints the parenthetical term **(چاوگ)** in its list: **کار (چاوگ)**. This confirms the same corrected spelling in a separate part of the book.
- Accordingly, **چاوگ** is now the verified source spelling on pp. 222, 223 and 388. The previous erratum's correction is confirmed against multiple original page images, not merely accepted from a user correction or OCR.
- The contents page p. 398 still appears to list **جێناو** at p. 222. This is now a distinct source-internal discrepancy: the actual chapter heading and internal cross-reference say **چاوگ**, while the contents list says **جێناو**. Do not silently rewrite the contents entry, and do not treat **چاوگ** as a synonym for **جێناو**. Record the contents discrepancy until the original print edition or an authoritative erratum resolves it.
- Quality-control rule reinforced: every course-critical Kurdish term must be visually verified on at least two relevant source-page images when available, including a high-resolution crop of the first occurrence; OCR is never sufficient for spelling decisions.


## Sequential visual review: primary book PDF pp. 228–235 (2026-11-05)

### Page-by-page observations
- **PDF p. 228:** continues the **چاوگ** chapter with numbered divisions and paired examples. The page visibly includes a heading that appears to read **وەربین**; exact reading and its technical status require a closer crop before treating it as a formal subtype label. The body repeatedly uses **چاوگ**.
- **PDF p. 229:** continues numbered divisions and examples; the page includes a bracketed explanatory note and a further numbered group. Do not extract individual forms without checking their full context and spelling.
- **PDF p. 230:** explicitly introduces a **تێبینی** (note) and discusses how a form behaves in relation to its complement/argument; it then lists further examples and introduces a distinction between **چاوگی سادە** and **چاوگی ناسادە**. These are the source's own terms; their exact definitions and boundaries need transcription before they are taught.
- **PDF p. 231:** continues the simple/complex distinction and introduces numbered subtypes within the latter discussion. The visible prose and examples are not enough to equate these labels with modern transitivity, valency, or another standard category without a full analysis.
- **PDF p. 232:** presents a further three-part classification, with visible headings **چاوگی دایزراو (درۆست کراو)**, **چاوگی لێکدراو**, and **چاوگی ناوەتە** (last reading requires confirmation from a close crop). The page gives long paradigmatic/example lists and explanatory notes. Do not modernize these labels or infer equivalence from their apparent form.
- **PDF p. 233:** continues the same section with more examples and prose discussing forms and usage. The page's examples are context-dependent and need exact transcription.
- **PDF p. 234:** continues a discussion of the same category and provides comparative/paired forms. The prose refers to grammatical/structural properties; no independent conclusion is drawn here.
- **PDF p. 235:** continues the explanation and examples, including forms with negative morphology. It appears to close the **چاوگ** section immediately before the next section opening at p. 236 (**ئاوەڵکار**).

### Findings and limits
- This sequential pass confirms that pp. 228–235 are not a personal-pronoun paradigm: they continue a detailed, internally subdivided **چاوگ** discussion, with examples and source-specific subtype terminology.
- The source uses labels such as **چاوگی سادە / چاوگی ناسادە** and further subtypes. These labels must be preserved verbatim in source notes until their definitions are manually transcribed and independently validated. Do not substitute labels such as transitive/intransitive, simple/compound verb, or infinitive without evidence.
- The contents-page entry **جێناو** for p. 222 remains inconsistent with the actual chapter heading **چاوگ** and the continuation through p. 235. The discrepancy remains open; this review does not resolve the table-of-contents error.
- This is a visual sequential review of pp. 228–235, not a complete transcription. Before drafting any lesson, transcribe the definitions, each subtype heading, and representative examples from high-resolution crops, then validate the analysis against independent Sorani/Central Kurdish linguistic research. The primary book remains the sole lesson source.
