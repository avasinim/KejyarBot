# Course 4 — Source-backed release gate

## Purpose
This gate prevents unsupported grammar claims, invented examples, wrong page references, OCR mistakes, or dialect-specific rules from being published as established facts.

**Default rule: Course 4 remains blocked until every lesson is independently checked against the exact source scan.** A catalogue record, file size, OCR text, another grammar, or a general linguistics reference can help locate evidence; none alone proves what this author wrote on a particular page.

## Required workflow for every lesson

1. **Lock the source identity.** Record the exact source-part number, immutable Git commit SHA, PDF blob SHA, and the exact PDF edition/scan. Never infer a part from a filename alone.
2. **Inspect the page image.** Record both PDF page index and printed page number. OCR is a search aid only; confirm wording, diacritics, suffixes, examples and tables visually.
3. **Build a claim ledger.** Split the lesson into individual factual claims. Record each individual claim in the manifest: exact PDF page and printed page, source quotation, claim type (author/editor/external), evidence label (A/C/D), and independent approval. Do not group unrelated claims under one general citation.
4. **Preserve terminology.** Copy the author's term and spelling exactly. Any modern equivalent or clarification must be explicitly labelled as editor explanation, never attributed to the author.
5. **Audit examples.** Separate author examples from editor-created examples. Do not alter author forms to fit a preferred standard. Explain dialect/edition limits where relevant.
6. **Audit the lesson draft.** Every definition, classification, suffix, paradigm, rule and example must map to evidence. Unsupported claims are removed or visibly marked as unresolved; they are not silently completed from general knowledge.
7. **Audit the quiz separately.** Every question and answer must be answerable from the approved lesson and source evidence. No trick questions or answer keys based on unsupported generalizations.
8. **Independent review.** A second review checks source pages, claim mapping, terminology, examples and quiz answers. The reviewer and review date are recorded.
9. **Technical release checks.** Run course structure, runtime, quiz, regression and safety tests. Only then may the course-level gate be approved.

## Evidence labels
- **A — Directly verified:** visible in the exact printed source page.
- **B — OCR lead only:** found in OCR, not visually confirmed; not publishable as an author claim.
- **C — Editor explanation:** modern explanatory bridge; explicitly labelled and must not contradict the author.
- **D — External context:** supported by another source; may be used only as a separately attributed comparison.
- **U — Unverified:** unresolved; must not be presented as fact.

Only A evidence can substantiate a claim attributed to the book's author. C and D may supplement it with clear labels. B and U block publication of the affected claim.

## Release decision
The machine-readable register is `course4_release_gate.json`. Each lesson must contain a claim-by-claim evidence ledger and a separate quiz-to-evidence ledger; an empty ledger blocks release. It starts with all 30 lessons blocked. Fill the evidence fields only after checking the exact page images. The validator has two modes:

- `python tools/course4_source_audit/validate_release_gate.py` checks manifest structure and reports current blockers without pretending the course is approved.
- `python tools/course4_source_audit/validate_release_gate.py --release` fails unless all 30 lessons and all course-level checks are approved.

A successful structural check is **not** a source audit and is **not** permission to publish. This is an audit-side guard until a separately reviewed runtime integration is authorized. It does not itself change course activation, Botkeep, production data, deployment, or `main`.

## Current decision
**BLOCKED.** The source-to-file map is still provisional for repository PDFs 2, 4 and 5. The source page evidence is incomplete across the 30 lessons. Keep Course 4 inactive; do not merge or deploy based on this register alone.
