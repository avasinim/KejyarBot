# Course 2 Lesson 12 — learning-objective and assessment alignment audit

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** audit-only; no lesson, exercise, quiz, key, or runtime changes applied.

## Evidence inspected

- Source-aligned Course 2 lesson file, blob SHA `19090077a11dc9d7211987e958e560b328fcd3d6`.
- Reviewed Lesson 12 draft, blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Reviewed answer key, blob SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.
- Existing key-alignment audit, blob SHA `464b2c284dbff250f979aa03a091d10eaf49350d`.
- Existing adjective-class/function review, blob SHA `d76164ef5c2bbad97d63c4b10058cad6a415e931`.

The reviewed lesson's current objectives are: (1) distinguish adjectives from nouns and numerals; (2) recognize six adjective classes in the adopted framework; (3) recognize degrees of descriptive adjectives; and (4) understand `jmarnav` as a separate class and recognize basic examples.

## 1. Objective-to-learning-activity map

| Objective / content | Lesson teaching and practice | Quiz evidence | Alignment |
|---|---|---|---|
| Basic adjective function | §1 definition; descriptive examples in §2 | Q1 tests the basic definition | Direct but introductory only |
| Six adjective classes | §§2–7; Xebata 1 asks learners to classify examples; Xebata 2 asks for one new example per class | No quiz item directly asks learners to identify all six classes; Q2 samples only the descriptive class | Taught and practiced, weakly sampled in quiz |
| Degrees of descriptive adjectives | §2 teaches base `mezin` and comparative `mezintir`; source/review history also records a superlative form in earlier source-aligned version | No quiz question assesses degree formation or interpretation | Taught, not assessed |
| Demonstrative adjectives and adjective/pronoun distinction | §3; examples include `ev mirov`, `ew mirov`, oblique/gender-number forms; distinction from independent demonstrative pronoun | No quiz question tests this distinction | Taught, practiced indirectly in Xebata 1 |
| Numeral adjectives | §4; examples `sê mal`, `çar xanî`, ordinal examples; Xebata 1 includes `sê mal` | Q3 directly tests `sê` in `sê mal` | Direct |
| Interrogative adjectives | §5; `kîjan mirov`, `çend kitêb` | No direct quiz item | Taught, practiced indirectly |
| Indefinite adjectives | §6; examples include `tu mirov`, `gelek fêkî`, `hemî mirov`, `çend çiya` | No direct quiz item | Taught, practiced indirectly |
| Possessive adjectives | §7; examples with expressed nouns | No direct quiz item | Taught, practiced indirectly |
| `jmarnav` as a separate class | §8; defined and contrasted with numeral adjective; examples and special forms | Q4 tests the course's classification; Q5 asks about `nîv` | Direct, but shallow |
| Distinguish numeral adjective from `jmarnav` | §8; contrast and Xebata 3 explicitly asks for distinction in one sentence | Quiz splits the concepts across Q3/Q4, but does not ask the learner to compare them in a single context | Partial |

## 2. Main finding: the quiz is not a complete sample of the lesson objectives

The five-item quiz is conceptually aligned with its own lesson content and answer key, but it samples only a narrow portion of the lesson:
- Q1: basic adjective function.
- Q2: descriptive adjective subclass.
- Q3: numeral adjective modifying an expressed noun.
- Q4: `jmarnav` as a separate class in the adopted framework.
- Q5: `nîv` as a numeral example.

It does **not** directly assess the six-class taxonomy as a whole, adjective degrees, adjective/pronoun boundary, interrogative, indefinite, or possessive adjective recognition. Those are present in the teaching material and some are sampled by practice activities, but not by the five quiz questions.

This is a coverage limitation, not a finding that the five keyed answers are wrong. A five-question quiz cannot thoroughly assess every subtopic; whether broader sampling is required is a course-design decision.

## 3. Exercise-level ambiguity and instructional risk

1. **Xebata 1** contains a useful spread of examples, including `ev keçik`, `kîjan mirov`, `tu mirov`, `gelek fêkî`, `hespê min`, `kurên van`, and `nîv roj`. However, the instruction “cureya rengdêr an jmarnav” should be interpreted with the lesson's word-class/function distinction in mind. Some forms need the learner to identify whether a noun is expressed and whether the numeral modifies it or is treated as an independent numeral.
2. **`nîv roj`** is a potentially useful boundary example, but its expected label should be stated in the teacher key with a short reason: is the exercise asking for the numeral form's lexical class, its role in the noun phrase, or the course's adjective-vs-`jmarnav` distinction? Without that rubric, different analytical levels may be conflated.
3. **Xebata 3** is the strongest direct activity for the objective of distinguishing numeral adjective from `jmarnav`, but it requests only one sentence. A model answer should compare a numeral modifying an expressed noun (e.g. `sê mal`) with an independent/substantive numeral use, making the criterion explicit. This is a proposal, not a prepared answer inserted into the lesson.

## 4. Recommendations (approval required)

- Keep the current five quiz questions and key unchanged unless the course owner chooses to expand assessment coverage.
- If the quiz must remain five items, decide explicitly whether it is intended as a short end-of-lesson checkpoint or a representative test of all objectives. It currently functions as the former.
- If representative coverage is required, consider replacing or expanding one item to assess adjective/pronoun or degree recognition, and use a balanced sampling plan across the six adjective classes. Do not alter the quiz without approval.
- Add teacher-facing criteria/model answers for Xebata 1 and Xebata 3, especially for `nîv roj` and the numeral adjective/`jmarnav` boundary.
- Preserve the source/course taxonomy distinction and the qualifier “Li gorî vê rêbazê” for the adopted numeral classification.

## 5. Disposition and preservation

- No contradiction was found between the five current keyed answers and the lesson's directly taught concepts.
- The primary issue is **assessment coverage**, not key correctness.
- No lesson, exercise, quiz, answer key, source-aligned file, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was modified.
- No tests/CI or live runtime checks were performed. `main` remains read-only.
- All audit work remains on `archive/preservation-audit-2026-11-10`. GitHub archive history is not a separate ZIP/off-site backup.
