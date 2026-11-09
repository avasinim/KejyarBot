# Course 4 — Lessons 10–13
## Append-only clarification patch: independent pronouns, clitics, alignment, and verb morphology
### Round 19 — 2026-11-09

**Status:** archival clarification / proposed editorial guidance. Not an approved replacement lesson, not a source JSON edit, and not deployment authorization.

**Preservation rule:** retain every original lesson, example, exercise, and quiz item. This patch adds analysis notes only. It does not migrate or rewrite quizzes.

**Source integrity:** reviewed against `course_data/grammar_course4_lessons.json` on `main`; source blob SHA at review: `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`. No source file was modified.

---

## Shared analysis protocol for Lessons 10–13

Keep these levels distinct:

1. **Form / morphology:** the phonological and morphological shape of a pronoun, clitic, affix, or verbal ending.
2. **Syntactic function:** Subject, Object, possessor inside an NP, complement of a preposition, etc.
3. **Semantic role:** Agent, Patient, Recipient, and other participant roles.
4. **Alignment / agreement:** how grammatical relations are indexed or expressed across tense/aspect and transitivity patterns.

Never infer a clitic's function from its written shape alone. A form such as `ـم`, `ـی`, or `ـیان` must be analysed in its complete host construction, clause type, tense/aspect, transitivity, and discourse context.

The terms **independent pronoun**, **clitic**, **enclitic**, **affix**, **suffix**, and **person marker** are not interchangeable.

## Lesson 10 — Independent personal pronouns

- Retain the six pedagogical person/number forms: `من، تۆ، ئەو، ئێمە، ئێوە، ئەوان`.
- Distinguish grammatical number from pragmatic honorific use: `ئێوە` is morphologically second-person plural, but may address one person politely. Do not describe the polite use as a new singular paradigm.
- Distinguish an overt independent pronoun from person/number marking on the verb. In `ئێمە دەچین`, `ئێمە` is an independent pronoun and `ـین` is part of the verbal form; they are not one morpheme or one word.
- Do not teach that every independent pronoun is obligatorily a subject. It may be omitted, contrastive, emphatic, or used in another syntactic position depending on construction.
- The lesson's examples are suitable as introductory illustrations, but any claim about the full person-agreement paradigm must be checked across present and past transitive/intransitive patterns, not inferred from present-tense examples alone.

## Lesson 11 — Personal clitics: form and use

- Keep the core distinction between an independent form such as `من` and a bound form such as `ـم`.
- The listed forms `ـم، ـت، ـی، ـمان، ـتان، ـیان` are a useful introductory inventory, not a guarantee that every occurrence has the same syntactic function or that every dialect has identical phonological distribution.
- In an NP such as `کتێبەکەم`, the clitic is possessive in the construction illustrated. Do not generalize that interpretation to every occurrence of the same shape.
- In past transitive Sorani constructions, person markers may index the agent/subject under an ergative alignment pattern. That is distinct from nominal possession. Analyse the whole clause rather than assigning a possessive reading automatically.
- For prepositional hosts, inspect each preposition and construction independently. Do not create a universal rule from one cliticized example.
- Preserve the distinction between a clitic (a syntactically dependent element) and an affix (a bound morphological element); their diagnostics can overlap, so avoid presenting one orthographic test as decisive.
- The Persian comparison may remain as a pedagogical analogy only. It must not be used as evidence that Persian and Sorani clitic systems are identical.

## Lesson 12 — Grammatical functions of clitics

- Preserve the lesson's central contrast between a possessive reading and an agent/person-marking reading.
- The pair involving `ـیان` must remain explicitly context-sensitive:
  - In an NP such as `کتێبەکەیان`, it can mark third-person plural possession.
  - In a past transitive clause such as `ئەوان کتێبەکەیان خوێند`, the intended reading may involve an agent/person marker associated with the past transitive alignment; a possessive reading is also possible in an appropriate context.
- Do not present the sentence above as unambiguous without supplying the intended meaning and discourse context. The quiz explanation must preserve this qualification.
- Separate grammatical Subject from semantic Agent. In an ergative alignment construction, the participant interpreted as Agent need not be expressed with the same coding pattern as the Subject of an intransitive clause.
- Separate the Object NP from any clitic hosted on or associated with it. The presence of a clitic does not make the noun phrase itself a clitic, nor does it automatically make the clitic an Object.
- Avoid defining Object only as “the thing affected by the action” as a universal test. Semantic role and syntactic function are related but not identical.
- The current quiz item on `ـیان` is acceptable only if its explanation keeps the stated intended reading and acknowledges the alternative reading in context.

## Lesson 13 — Verb, stem, tense, and morphological structure

- Preserve the three-way distinction:
  - **Infinitive / چاوگ:** citation form of the verb.
  - **Root / ڕەگ:** lexical base, where the analysis supports identifying one.
  - **Stem / بنج:** morphological base used to form inflected forms.
- Keep present stem and past stem distinct. Do not mechanically derive one from the other or claim that all verbs follow a single predictable rule without a paradigm.
- In `دەخۆم`, the lesson's segmentation `دەـ + خۆ + ـم` is an introductory analysis for that example. Do not generalize it to all verbs without checking their paradigms and morphophonological alternations.
- `دەـ` must not be equated with a single tense meaning. Its interpretation depends on construction and context, including present, habitual, or future-oriented uses.
- Distinguish tense from aspect. The contrast among `خوێند`, `دەخوێند`, `خوێندووە`, and `خوێندبوو` should be explained through the intended temporal/aspectual context, not by labels alone.
- Keep negative markers and imperative marking tied to the constructions actually illustrated. Do not present `نەـ`, `ناـ`, `مەـ`, and `بـ` as interchangeable or as exceptionless across all verb classes.
- Distinguish person/number endings on the verb from independent pronouns and from enclitic person markers. Similar person values do not make these forms morphologically identical.
- Distinguish active/passive voice from transitivity. An intransitive verb is not automatically passive, and a passive construction is not defined simply by absence of an overt Agent.
- The examples `مامۆستا وانەکەی نووسی` and `وانەکە نووسرا` should not be used to teach a universal one-to-one conversion rule. The first clause's `ـی` requires contextual morphological analysis; the second clause's voice classification should be grounded in the target Sorani variety and the adopted grammatical framework.

## Cross-lesson consistency checks

- Lesson 10: independent pronoun versus verbal person marking.
- Lesson 11: clitic form versus syntactic function; possession versus agent/person marking.
- Lesson 12: Subject versus Agent; Object NP versus clitic; past transitive alignment.
- Lesson 13: infinitive/root/stem; present/past stems; tense/aspect; affix/clitic; transitivity/voice.
- Reuse the same terminology and analysis protocol in Lessons 14–18 and 39–43. Do not let the same written clitic receive a fixed function merely because it has the same spelling.

## Quiz and assessment handling

- Existing quiz items remain untouched in the source JSON.
- Items that ask for the function of `ـیان` in `ئەوان کتێبەکەیان خوێند` must state the intended reading and retain the alternative-reading caveat.
- Items that identify `ـم`, `ـی`, or `ـیان` by form alone should be revised only in a later, separately archived patch after their full host construction and intended meaning are specified.
- No quiz item is considered fully validated solely because its answer key is structurally valid.

## Validation and release status

- This patch is an internal editorial synthesis from the current course source, not a fresh external-source verification.
- No page-level source mapping is claimed here.
- Target-dialect speaker validation remains desirable for disputed examples and readings.
- No lesson is newly marked approved by this patch.
- No structured quiz migration, source JSON update, runtime change, database change, `main` modification, Botkeep action, or Telegram deployment was performed or authorized.
