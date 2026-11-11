# PR #125 — file-level release classification manifest
## 2026-11-11 | Read-only diff inventory | Append-only

### Source examined
- Repository: `avasinim/KejyarBot`
- PR: #125 — `Harden academic course menus, lesson access, and pagination`
- Base: `botkeep-runtime-2026-11-09`
- Head: `botkeep-menu-clean-2026-11-09`
- Exact head SHA: `c41fc186e8e2482de336d297c3b7dd9758356e08`
- Diff inventory: 194 changed files.
- CI on exact head: three relevant workflows completed successfully. This is source-branch CI only, not a deployment or Botkeep runtime verification.

### Classification summary
| Class | Files | Release interpretation |
|---|---:|---|
| Python runtime/source | 5 | Candidate runtime code; requires full code review and tests |
| Runtime data/manifest | 4 | Mixed production and review-gated data; must preserve Beta gates |
| Tests | 13 | Validation only; not deployed as course content |
| GitHub workflows | 5 | CI configuration; not application runtime |
| Review drafts | 43 | Archive/staging only; exclude as independent runtime modules |
| Review records | 122 | Audit evidence only; exclude from learner-facing runtime |
| Other docs | 2 | Documentation only |
| **Total** | **194** | |

### Release-critical runtime source
### Python runtime/source (5)
- `arami_course1_telegram.py`
- `arami_lesson1_telegram.py`
- `arami_lesson5_telegram.py`
- `bot.py`
- `course_runtime.py`

### Release-critical data and catalogue files
### Runtime data/manifest (4)
- `course_data/grammar_course4_lessons.json`
- `course_data/grammar_course4_quiz_overrides.json`
- `courses.json`
- `curriculum/grammar_course4_plan.json`

### Test suite files
### Tests (13)
- `tests/test_academic_course_menu.py`
- `tests/test_activated_courses.py`
- `tests/test_arami_course1_telegram.py`
- `tests/test_arami_lesson1_telegram.py`
- `tests/test_arami_lesson5_telegram.py`
- `tests/test_bot_message_mode.py`
- `tests/test_bot_quiz_callbacks.py`
- `tests/test_content.py`
- `tests/test_course4_beta_review.py`
- `tests/test_course4_grammar_runtime.py`
- `tests/test_database.py`
- `tests/test_lesson_search.py`
- `tests/test_orthography_course_structure.py`

### Workflow files
### GitHub workflows (5)
- `.github/workflows/course4-50-beta-review.yml`
- `.github/workflows/course4-beta-review.yml`
- `.github/workflows/course4-quiz-overrides.yml`
- `.github/workflows/orthography-course-structure.yml`
- `.github/workflows/python-checks.yml`

### Staging drafts — not independently deployable lesson files
### Review drafts (43)
- `docs/source_archive/staging/drafts/COURSE4_BETA_LESSONS_032_050_STRUCTURED_QUIZ_DRAFT_V1_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_BETA_LESSONS_032_050_STRUCTURED_QUIZ_DRAFT_V2_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_BETA_LESSONS_032_050_STRUCTURED_QUIZ_DRAFT_V3_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_BETA_LESSONS_032_050_STRUCTURED_QUIZ_DRAFT_V4_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_BETA_LESSONS_032_050_STRUCTURED_QUIZ_DRAFT_V5_TERMS_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_LESSONS_QUIZ_INTEGRATED_CANDIDATE_V1_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_LESSONS_QUIZ_INTEGRATED_CANDIDATE_V2_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_LESSONS_QUIZ_INTEGRATED_CANDIDATE_V3_TERMS_2026-11-10.json`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_032_SENTENCE_FOUNDATIONS_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_033_SUBJECT_VERB_AGENT_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_034_SUBJECT_PREDICATE_COPULA_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_035_SENTENCE_FUNCTION_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_036_COMPLEMENTS_ADJUNCTS_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_037_SENTENCE_STRUCTURE_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_037_SENTENCE_STRUCTURE_DRAFT_V3_BARRISTA_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_038_CLAUSE_MAIN_SUBORDINATE_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_040_TRANSITIVITY_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_040_TRANSITIVITY_DRAFT_V3_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_040_VALENCY_CONCEPT_REFINEMENT_DRAFT_V1_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_041_COMPOUND_VERBS_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_041_COMPOUND_VERBS_DRAFT_V3_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_042_CLITIC_PRONOUNS_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_042_CLITIC_PRONOUNS_DRAFT_V3_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_043_CLITIC_OBJECT_PRONOUNS_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_043_CLITIC_OBJECT_PRONOUNS_DRAFT_V3_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_044_PASSIVE_VOICE_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_044_PASSIVE_VOICE_DRAFT_V3_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_045_OBJECT_WORD_ORDER_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_046_SENTENCE_TYPES_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_047_NOUN_PHRASE_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_047_NOUN_PHRASE_EXPANDED_DRAFT_V2_2026-11-09.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V2_2026-11-09.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V3_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V4_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V5_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V6_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V7_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V8_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_049_PERSON_CLITICS_ALIGNMENT_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_049_SORANI_PERSON_MARKING_CLITICS_ALIGNMENT_DRAFT_V2_2026-11-09.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_050_CAPSTONE_SORANI_GRAMMATICAL_DATA_ANALYSIS_APPENDIX_2026-11-09.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_050_RELATIVE_CLAUSES_DRAFT_V2_BASTEN_2026-11-10.md`
- `docs/source_archive/staging/drafts/COURSE4_LESSON_050_RELATIVE_CLAUSES_SORANI_DRAFT_V2_2026-11-09.md`

### Append-only review records — archival only
### Review records (122)
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_ACTIVATION_AND_QUIZ_GATES_ROUND36_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_BETA_ACTIVATION_CHECKPOINT_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_BETA_INTEGRATION_CHECKPOINT_ROUND28_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_BETA_POST_MERGE_CI_VERIFICATION_ROUND29_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_CONSOLIDATED_STATUS_ROUND27_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_MERGE_AND_TEST_COUNT_CORRECTION_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_STATUS_ROUND28_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_STATUS_ROUND29_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_TERMINOLOGY_INTEGRATION_ROUND39_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_LESSON_TERMINOLOGY_REGISTER_V1_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_50_QUIZ_OVERRIDE_INTEGRATION_ROUND36_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_AFFIX_PREFIX_SUFFIX_CLITIC_PREPOSITION_AUDIT_ROUND45_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_ALL_248_QUIZZES_OLD_INFLECTION_TERM_SCAN_AND_PATCH_ROUND47_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_CONSERVATIVE_PATCH_REGRESSION_ROUND60_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_CONSERVATIVE_WHOLE_PHRASE_PATCH_SHORTLIST_ROUND60_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_CONTEXT_MORPHOLOGY_SEMANTIC_REVIEW_ROUND52_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_FINAL_PATCH_REGRESSION_ROUND68_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_GLOBAL_TERM_AUDIT_ROUND64_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_LESSON48_TERM_AUDIT_ROUND74_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_MORPHOLOGY_FORMS_AUDIT_ROUND69_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_MORPHOLOGY_FORMS_AUDIT_ROUND72_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_NONQUIZ_PHRASE_CONTEXT_REVIEW_ROUND62_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_NONQUIZ_TEMP_PATCH_REGRESSION_ROUND63_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_PATCH_PROPOSAL_NOTES_ROUND67_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_PATCH_REFINEMENT_VALIDATION_ROUND73_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_QUIZ_COHERENCE_AUDIT_ROUND71_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_QUIZ_LEVEL_PATCH_REVIEW_ROUND58_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_QUIZ_SEMANTIC_AND_ANSWER_INTEGRITY_REVIEW_ROUND61_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_REVERSIBLE_PATCH_PROPOSAL_ROUND67_2026-11-10.json`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_REVERSIBLE_PATCH_PROPOSAL_ROUND73_2026-11-10.json`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_SENTENCE_LEVEL_AUDIT_ROUND70_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_SENTENCE_LEVEL_SORANI_EDITORIAL_REVIEW_ROUND59_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_SENTENCE_SEMANTIC_AUDIT_ROUND66_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_TEMP_PATCH_REGRESSION_ROUND65_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_TERM_REVERSIBLE_PATCH_PROPOSAL_ROUND57_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BASTEN_TERM_TEMP_COPY_REGRESSION_VERIFICATION_ROUND57_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BETA_QUIZ_SEMANTIC_REVIEW_ROUND98_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BETA_QUIZ_STRUCTURING_ROUND93_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BETA_QUIZ_STRUCTURING_VALIDATION_ROUND94_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_BETA_QUIZ_TERM_ALIGNMENT_ROUND97_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_CONTEXT_TERM_BASTEN_SENTENCE_LEVEL_PATCH_LEDGER_ROUND51_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_CONTEXT_TERM_FULL_CONTEXT_AND_QUIZ_ALIGNMENT_ROUND56_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_CONTEXT_TERM_OCCURRENCE_DECISIONS_ROUND55_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_CONTEXT_TERM_ROUND56_ERRATUM_COUNTS_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_CROSS_LESSON_BASTEN_TERM_CHAIN_AUDIT_ROUND54_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_END_TO_END_50_LESSON_CHAIN_AND_BASTEN_TERM_AUDIT_ROUND50_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_FINALIZATION_GATES_AND_ARCHIVE_CHECKPOINT_ROUND80_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_FINAL_50_LESSON_TERMINOLOGY_AND_COMPLETION_GATES_ROUND27_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_INFLECTION_DERIVATION_LESSONS01_31_QUIZ_AUDIT_ROUND46_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_INFLECTION_TERM_CROSSWALK_CORRECTION_ROUND32_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_KARIMI_BOOK_DIRECT_EVIDENCE_CHAPTERS_4_AND_7_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_KARIMI_GLOSSARY_AND_MORPHEME_ORDER_CROSSWALK_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON032_SOURCE_AND_SCHEMA_REVIEW_ROUND82_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON033_SOURCE_AND_AGENT_REVIEW_ROUND83_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON034_SOURCE_AND_COPULA_REVIEW_ROUND84_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON035_SOURCE_AND_PURPOSE_REVIEW_ROUND85_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON036_COMPLEMENT_ADJUNCT_REVIEW_ROUND86_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON037_SENTENCE_STRUCTURE_REVIEW_ROUND87_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON038_CLAUSE_SUBORDINATION_REVIEW_ROUND88_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON13_SCIENTIFIC_REVIEW_APPROVAL_ROUND40_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON31_QUIZ_OVERRIDES_ROUND35_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON48_CROSS_LESSON_TERMINOLOGY_AUDIT_ROUND75_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON48_V4_FULL_AUDIT_ROUND77_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON48_V4_LINE_BY_LINE_AUDIT_ROUND77_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON48_V5_V6_VALIDATION_ROUND78_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON48_V7_VALIDATION_ROUND79_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON48_VALENCY_ARGUMENT_COMPLEMENT_REFINEMENT_ROUND76_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON50_INTERNAL_CONSISTENCY_AND_STATUS_ROUND40_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS039_044_TERM_NORMALIZATION_ROUND90_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS03_11_13_16_28_29_TERM_DISCREPANCY_AUDIT_ROUND44_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS045_050_TERM_AND_DRAFT_REVIEW_ROUND91_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS41_46_CROSS_LESSON_TERMINOLOGY_AUDIT_ROUND42_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS48_49_VALENCY_AND_PERSON_MARKING_AUDIT_ROUND41_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_001_TO_015_APPEND_ONLY_SCIENTIFIC_RECONCILIATION_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_001_TO_030_QUIZ_ANSWERKEY_FIRST_PASS_AUDIT_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_001_TO_050_CONSOLIDATED_REVIEW_STATUS_ROUND26_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_016_TO_050_APPEND_ONLY_SCIENTIFIC_RECONCILIATION_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_031_TO_035_APPEND_ONLY_SCIENTIFIC_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_031_TO_035_QUIZ_AND_EXERCISE_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_032_TO_035_SCIENTIFIC_REVIEW_ROUND37_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_036_TO_040_APPEND_ONLY_SCIENTIFIC_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_036_TO_040_EXERCISE_AND_QUIZ_READINESS_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_036_TO_040_SCIENTIFIC_REVIEW_ROUND38_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_041_TO_045_APPEND_ONLY_SCIENTIFIC_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_041_TO_045_EXERCISE_AND_ANSWERKEY_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSONS_047_TO_050_FINAL_SCIENTIFIC_SCOPE_AUDIT_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON_013_SOURCE_MAP_AND_TERMINOLOGY_PATCH_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON_013_SOURCE_MAP_PATCH_STATUS_ROUND33_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON_031_QUIZ_WORD_BY_WORD_AUDIT_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON_046_APPEND_ONLY_SCIENTIFIC_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON_046_EXERCISE_ANSWERKEY_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_LESSON_050_CAPSTONE_SCIENTIFIC_ALIGNMENT_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_MORPHEME_PREFIX_PREPOSITION_CLITIC_PARTICLE_AUDIT_ROUND49_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_PR128_ROUND26_STATUS_ADDENDUM_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_PR128_STATUS_AFTER_CAPSTONE_REVIEW_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_PR128_STATUS_AFTER_LESSONS_031_TO_046_AUDIT_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_240_QUESTION_AUDIT_CONSOLIDATED_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_44_OVERRIDE_MAPPING_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_BASTEN_TERM_AND_ANSWER_INTEGRITY_AUDIT_ROUND53_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_COUNT_CLARIFICATION_ROUND30_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_INTEGRATED_CANDIDATE_DIFF_ROUND95_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_OVERRIDE_BETA_INTEGRATION_ROUND34_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_OVERRIDE_INTEGRATION_STATUS_ROUND31_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_PUNCTUATION_PRESERVATION_ROUND96_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_WORD_BY_WORD_AUDIT_LESSONS_001_TO_010_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_WORD_BY_WORD_AUDIT_LESSONS_011_TO_015_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_WORD_BY_WORD_AUDIT_LESSONS_016_TO_020_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_WORD_BY_WORD_AUDIT_LESSONS_021_TO_025_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_QUIZ_WORD_BY_WORD_AUDIT_LESSONS_026_TO_030_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_ROOT_STEM_BASE_CROSSWALK_SORANI_AUDIT_ROUND48_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_ROOT_STEM_CROSSWALK_LESSON29_ROUND42_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_ROUND26_TERMINOLOGY_CROSSWALK_CORRECTION_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_RUNTIME_46_LESSON_STRUCTURAL_AUDIT_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_RUNTIME_TERMINOLOGY_CONSISTENCY_INVENTORY_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_SOURCE_HIERARCHY_AND_DIALECT_SCOPE_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_STATUS_AFTER_PR137_TERMINOLOGY_MERGE_ROUND39_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_STRUCTURED_DATA_AND_ACTIVATION_GATES_ROUND92_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_SUBORDINATE_CLAUSE_TERM_DECISION_ROUND89_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_TERMINOLOGY_BASELINE_AND_RUNTIME_STATUS_RECONCILIATION_ROUND43_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_TERMINOLOGY_CONSISTENCY_AUDIT_ROUND81_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_TERMINOLOGY_NORMALIZATION_ROUND37_2026-11-10.md`
- `docs/source_archive/staging/reviews/COURSE4_TERMINOLOGY_NORMALIZATION_ROUND38_LESSON13_AFFIX_ADDENDUM_2026-11-10.md`

### Other documentation
### Other docs (2)
- `docs/COURSE4_GRAMMAR_APPENDIX.md`
- `docs/archives/2026-11-09-END-OF-DAY-PRESERVATION.md`

### Required release gates
1. Review the five Python files as a coherent runtime change, including course routing, callbacks, progress and reward eligibility.
2. Review the four data/catalogue files as a coordinated set. The Course 4 JSON contains 50 lesson records, but lessons 32–50 are review-gated beta drafts; do not expose them as approved course material or unlock official quiz/reward paths.
3. Preserve original 248 quiz items and their snapshots/answer keys. Apply only reviewed overrides whose exact original snapshots match the canonical source.
4. Treat the 43 draft files and 122 review records as provenance/audit material, not as approved lesson replacements. In particular, the 142-field reversible terminology patch and Lesson 48 V3 remain unapplied drafts unless separately approved and verified.
5. Run full tests against this exact release candidate after any inclusion/exclusion changes; a previous successful CI run does not validate a later modified candidate.
6. Validate the existing Botkeep test database schema and backup restore in an isolated copy before changing any live data.
7. Do not import, restore, restart, redeploy, or sync on Botkeep until Botkeep support confirms Node17 staging recovery. Do not merge or deploy PR #125 by implication.
8. Rotate the exposed Telegram bot token before further user-facing testing; never put token values in Git or logs.

### Explicit non-actions
This inventory is based on PR #125's Git diff and read-only metadata. No files in Botkeep were changed; no GitHub PR was merged; no production or test deployment was performed; no database write or migration was performed.

This manifest is an append-only classification record, not an approval to release every changed file.
