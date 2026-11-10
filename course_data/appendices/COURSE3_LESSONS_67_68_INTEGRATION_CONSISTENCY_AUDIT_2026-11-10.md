# COURSE 3 — LESSONS 67–68 INTEGRATION CONSISTENCY AUDIT
Date: 2026-11-10
Branch: work/course3-lessons67-68-practice-archive-2026-11-10
Audited head: 586b32e92a6e9dd0c933111f184cd5823c9c6dd5
Status: read-only audit; no lesson, practice item, quiz, answer key, loader, runtime or production configuration changed.

## 1. Structural verification

The candidate dataset parses as JSON and contains 68 lesson objects. Lessons 67 and 68 have the expected IDs:
- unified_orthography_67
- unified_orthography_68

Counts in the candidate:
| Lesson | Activities | Exercises | Comprehension | MCQ |
|---|---:|---:|---:|---:|
| 67 | 8 | 10 | 12 | 12 |
| 68 | 10 | 10 | 12 | 12 |
| Total | 18 | 20 | 24 | 24 |

The append-only practice patch contains the same counts. A structural object comparison of each patch lesson against its matching candidate lesson returned exact equality for both lessons. Thus the candidate currently incorporates the original practice patch exactly; it does not yet incorporate the separate proposed-remediation appendix.

The candidate root status is candidate_not_runtime_active. Both lesson objects still carry review_status=draft_editorial_review. The manifest is explicitly candidate_only and says it is not a replacement for courses.json.

## 2. Important separation of states

The working-branch courses.json entry lists all 68 IDs and labels Course 3 status active. This is a branch-local candidate/runtime registration change, not proof that the live production branch or Botkeep host has activated the 68-lesson candidate. The candidate JSON itself remains marked candidate_not_runtime_active, and the manifest carries a host-safety gate. Do not describe this as production activation.

PR #140 remains open, Draft, unmerged. At the audited head it contains 24 changed files. No production action was taken during this audit.

## 3. Content-level issues carried forward in candidate

The exact candidate/patch match means the following known risks are still present in candidate content pending a deliberate reviewed revision:

### Lesson 67
- The candidate still labels «ڕەشەبا» as a compound in its example note. Lexical existence and meaning are attested; internal segmentation/productive morphology is not established by that evidence.
- The example «ئەو ڕۆیشتووە» is still glossed as present perfect, but the full Sorani parsing of participle and copular clitic requires a dialect-specific analysis.
- «کچە جوانەکە» and «ئەو کچە جوانەیە» still invite a single Ezafe/adjective/copula parse despite unresolved phrase boundaries and dialect details.
- The exercise with fragments «ئەو پیاو... زیرەک...» and «ئەو کتێبەی خوێندوو...» still has multiple possible completions.
- «دەچێتە بازاڕ» and «بچنە دەرەوە» need whole-construction treatment; do not teach the written final «ە» as an independently established universal directional suffix.
- «کوڕەکە» must be taught through the complete definite suffix -ەکە/-eke, not isolated «ە».

### Lesson 68
- The key point describing «نا» in “present and future” risks implying a dedicated future negative marker. Sorani future interpretation is contextual; do not present a separate future morphology without evidence.
- «نەدەنووسی» and the past-continuous negative paradigm remain held pending direct Sorani source evidence.
- «بەدشکڵ» is a partial lexical attestation only; it does not establish productive بەد- derivation.
- «بەدخواز» and «چاونەشۆر» remain unverified in the cited search; they should not be scored as canonical examples.
- The full person paradigm requested for «ناخوێنم» needs a sourced table; do not infer all six forms from one example.
- «نییە» must remain distinct as a negative copular/non-verbal predicate, not a verbal prefix.
- «تێرنەخۆر» has lexical attestation and a segmented lexical analysis; teach it as a lexicalized word/compound, not as a free clause-negation pattern.

## 4. Assessment cross-check

The 24 MCQ items and their answer keys remain unchanged in the candidate. The separate quiz audit classifies:
- KEEP: 11
- REVISE: 3
- HOLD: 4
- REPLACE/DE-DUPLICATE: 6

The separate proposed-remediation appendix provides replacement wording for activities, exercises and comprehension, but it is a proposal only. It has not been applied to the candidate data and does not yet contain a finalized 24-item replacement MCQ bank with a reviewed answer key. Therefore the current 24 MCQs should not be described as fully remediated.

## 5. Required next work — in safe order

1. Obtain specialist Sorani review of Lesson 67 distinctions: copula =e, directional clitic =(y)e, definite suffix -eke, vocative, Ezafe/linker and the verbal construction in «ڕۆیشتووە».
2. Obtain a dialect-labelled Sorani paradigm/source for Lesson 68: negative indicative nā-, negative subjunctive/past ne-, negative imperative me-, negative copula «نییە», and any past-continuous or perfect forms proposed for teaching.
3. Prepare a separately versioned replacement MCQ proposal: replace duplicates; revise ambiguous stems; hold unsupported items; add accepted answer variants and explanations. Do not overwrite the original 24 items.
4. Map every proposed activity/exercise/comprehension item to its original audit ID and decision, so no original item is silently lost.
5. Apply approved revisions as a new append-only patch version, then update the candidate dataset and manifest together.
6. Validate JSON schema, lesson counts, IDs, quiz answer indices, adapter rendering, page/pagination boundaries and the complete unit-test suite on the exact new commit.
7. Keep PR #140 Draft until the linguistic review and host-safety confirmation are recorded. Do not merge, deploy, sync, restart, or alter production while Botkeep's infrastructure status is unresolved.

## 6. Preservation and conclusion

No source lesson 1–66 was changed by this audit. No current practice patch, quiz item, answer key, candidate lesson, loader, database, token or production setting was changed. This report records that the candidate and practice patch are structurally aligned, while the proposed remediation is not yet integrated. The correct state is: structurally consistent candidate; pedagogically and linguistically still under review; not approved for production activation.
