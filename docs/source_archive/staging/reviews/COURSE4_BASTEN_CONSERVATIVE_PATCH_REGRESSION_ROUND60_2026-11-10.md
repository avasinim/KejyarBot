# Course 4 — Round 60 Temporary-Copy Regression Results
Date: 2026-11-10
Source SHA: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
Proposal: `COURSE4_BASTEN_CONSERVATIVE_WHOLE_PHRASE_PATCH_SHORTLIST_ROUND60_2026-11-10.md`

## Verified results
The Round60 whole-phrase rules were applied to an in-memory copy only.

- Lessons: **50**, unchanged.
- Changed JSON string paths: **35**.
- Whole-phrase replacement occurrences: **35**.
- Changed quiz string paths: **9**.
- JSON structural shape and object/array keys: unchanged.
- Quiz counts per lesson: unchanged.
- Answer values and answer indices: unchanged.
- Residual occurrences of the exact source phrases covered by the rules in scanned fields: **0**.
- Source blob SHA remains `fd8dfbde7e6937841214cacac653ef10d0c6097d`; repository source was not written.

## Limitations
This validates the exact-match mechanical application and structural invariants only. It does not replace a final native Sorani proofreading of all 35 full sentences, particularly where the source has a following ezafe or postposition. Round59's hold categories remain excluded.

## Decision
The conservative shortlist passes the temporary-copy structural and quiz-answer integrity checks. It is a stronger candidate than the Round57 substring map, but remains **unapplied and unapproved** pending final phrase-level proofreading and explicit source-edit authorization.

## Change control
No raw source, quiz object, answer key, runtime, database, Botkeep, Telegram, deployment or merge change.
