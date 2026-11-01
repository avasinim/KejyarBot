# KejyarBot — Latin Courses: Editorial Index

**Status:** This file is an index only. It is not a runtime source and does not contain a combined lesson master. The runtime loader reads each course's dedicated lesson document and answer key separately. Do not restore or use the older combined draft because its Course 1 source attribution was incorrect and its lesson copies are outdated.

## Course 1 — Bingehên Rastnivîsîna Kurdî ya Latînî

- **Distinct source:** Dr. Efrasîyab Şikofteh, *Rê zimanê Kurmancî* (Havîn 2010).
- **Scope:** North Khorasan Kurmanji Latin orthography, alphabet, vowel/consonant distinctions, spelling rules and syllables.
- **Canonical lessons:** `course_data/latin_course_1_source_aligned_lessons_01_12.md`
- **Canonical quiz key:** `course_data/latin_course_1_quiz_answer_key_draft.md`
- **Source review:** The source identity is corrected and initial page mapping is recorded, but final scientific approval remains pending.

## Course 2 — Bingehên Gramera Kurmancî

- **Distinct source:** Celadet Alî Bedir-Xan, *Elfabêya Kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002; Part II, “Bingehên gramera kurdmancî”.
- **Scope:** Kurmanji grammar. Keep its grammar terminology, forms, examples and dialect scope separate from Course 1.
- **Canonical lessons:** `course_data/latin_course_2_source_aligned_lessons_01_12.md`
- **Canonical quiz key:** `course_data/latin_course_2_quiz_answer_key_draft.md`
- **Source review:** Dedicated source and content audit remain separate from Course 1.

## Runtime and release boundary

- Runtime loader: `latin_course_runtime.py`
- Course 1 and Course 2 each have their own lesson file and 60-row answer key.
- The loader validates lesson sequence, quiz structure and answer-key consistency; it does not certify scientific source alignment.
- Lessons carry the consistent signature **🤖 کەژیار — KejyarBot@**. Editorial provenance is excluded from learner-facing runtime lesson text.
- Both course documents remain editorial review drafts until the remaining scientific review and actual test suite are completed.
- No production deployment, Botkeep update, main-branch change or merge is authorized by this index.
