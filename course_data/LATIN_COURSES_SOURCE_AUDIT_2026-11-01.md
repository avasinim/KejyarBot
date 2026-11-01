# Latin Courses — Source and Quiz Audit
**Audit date:** 2026-11-01  
**Branch:** `audit/latin-courses-source-review-2026-11-01`

## Scope and safety
- This audit is limited to the two Latin Kurdish courses in the KejyarBot repository.
- Course 1 remains grounded in its own *Rê zimanê Kurmancî* source.
- Course 2 remains grounded only in Part II, *Bingehên gramera kurdmancî*, by Celadet Alî Bedir-Xan.
- The two source books, lesson examples, language scope, and orthographic conventions must not be mixed.
- No changes were made to `main`, production credentials, the live bot, Botkeep, production databases, or deployment configuration.

## Course 2 source review
### Lesson 6 — Bireserê Navdêrê
- Rechecked against Celadet's sections 59–60.
- The source defines a `bireser` as a word accompanying a noun and modifying/restricting its meaning.
- It explicitly gives pre-noun examples including `ev keçik`, `kîjan mirov`, `çar xanî`, `hin çiya`, `çend kitêb`, `deh bizin`, and `van zarokan`.
- It also gives post-noun examples including `hespê beza`, `mehîna spehî`, and `xencera min`.
- The five-question quiz and master answer key now test this lesson rather than demonstrative pronouns.

### Lesson 11 — Pronavên Îşarkî, Girêkî û Pirsiyarkî
- Rechecked against Celadet's sections 97–103.
- The source identifies `yê / ya / yên` as demonstrative pronouns that take the relative pronoun `ko`.
- Section 99 defines `ko` as the relative pronoun and provides examples such as `Mirove ko te dît biraye min e`.
- Section 100 explicitly distinguishes a second `ko), the conjunction, which joins clauses and follows a verb; it gives `Min got ko ez nayem`.
- The lesson quiz now tests the distinction directly: question 3 checks `ko` as the relative pronoun; question 4 checks `ko` as the conjunction.

## Quiz and answer-key integrity
- Course 2 has 12 lessons and five multiple-choice questions per lesson.
- The master answer key contains 60 rows.
- All 60 answer-key rows were rebuilt from the actual embedded quiz options.
- A consistency pass confirms: 60 questions parsed, 60 key rows, zero answer-text/option mismatches.
- Added `tests/test_latin_course_2_quiz_keys.py` to enforce exact option-text matching and the Lesson 11 `ko` distinction.

## Verification status
- The source/quiz consistency check was performed against the branch files after the edits.
- The new Python unit test has been added but has **not** been executed in a local test environment.
- GitHub Actions are configured for pushes to `main` and `fix/**`, and pull requests targeting `main`; this audit branch is not included in the push trigger. No CI success is claimed for this branch.
- Runtime integration, live-bot behavior, and deployment were not changed or verified.

## Remaining work
1. Continue source-level review of Course 2 lessons 1–5 and 8–10, checking every example and terminology choice against Celadet's text.
2. Review Course 1's remaining lessons and all its quiz keys against its separate source.
3. Run the full test suite in the project environment before proposing any activation or release step.
