# Daily Conversation Course — 48-Lesson Structural Audit

Date: 2026-10-28

## Scope and safety

- Reviewed the five lesson-data files and `daily_conversation_plan.json` on branch `feature/expand-lesson-catalog-2026-10-28`.
- This is a structural/editorial triage, not approval of Kurdish language accuracy.
- All 48 lessons remain marked `draft_editorial_review`. Do not activate the course based on this audit alone.
- No lesson text was changed by this audit.

## Structural checks

- Lesson numbers cover exactly 1–48, with no missing or duplicate numbers.
- All 48 lessons have non-empty titles, objectives, dialogue, vocabulary, exercises, quiz, and role-play prompt.
- The plan's 48 working titles match the lesson-record titles.
- The lessons contain 99 quiz questions in total.
- Every quiz question has a non-empty prompt and explanation, at least three options, no normalized duplicate options within that question, and a valid integer answer index.
- No exact normalized duplicate vocabulary entries or dialogue lines were found within individual lessons.
- No structural errors were detected by these checks.

## Editorial review candidates

These are possible topic overlaps, not confirmed errors. An editor should compare the actual dialogues, vocabulary, exercises, and learning outcomes before deciding whether to merge, differentiate, or retain them as spaced practice.

| Lessons | Shared theme | Review question |
|---|---|---|
| 8, 25, 38 | Shopping / market | Do later lessons add clear progression (e.g. comparison, size, negotiation) rather than repeating the same basic transaction? |
| 10, 29, 43 | Places, directions, neighborhood | Are spatial language and navigation skills developed step by step? |
| 11, 19, 32 | Travel and transport | Are these distinct outcomes (transport vocabulary, asking directions/arrival, planning a trip)? |
| 13, 45 | Health and doctor appointments | Does lesson 45 extend the earlier health lesson into scheduling and appointment language? |
| 22, 40 | Library/reading versus books/films | Are the contexts and language functions sufficiently distinct? |
| 28, 47 | Emergency / asking for help | Is lesson 47 a deliberate practice/review lesson with a distinct scenario? |
| 6, 20, 39 | Daily routine, household tasks, preparing food | Are the dialogues and target expressions clearly differentiated? |
| 12, 18, 30, 36, 42, 48 | Review / integrated conversation | Does each review lesson have a defined cumulative target and a meaningfully different task? |

## Recommended next steps

1. Keep the course gated as `draft_for_review`.
2. Review each candidate cluster for progression and meaningful differentiation; preserve deliberate recycling where it supports learning.
3. Perform a Kurdish-language and orthography review against the project's chosen beginner-level conventions.
4. Test dialogues and quizzes with learners or a reviewer before considering activation.
5. Re-run structural tests after any editorial changes.

## Conclusion

The current data passed the listed structural checks. That does not establish linguistic correctness, pedagogical quality, or production readiness. The topic overlaps above should be reviewed by a human editor before the course is activated.


## Cross-lesson repetition scan (follow-up)

A second scan compared normalized dialogue lines, role-play prompts, quiz questions, and vocabulary terms across all 48 lessons.

- No exact duplicate role-play prompts were found across lessons.
- No exact duplicate quiz-question prompts were found across lessons.
- Two dialogue lines repeat exactly across different lessons:
  - Lessons 1 and 12: `سڵاو ئاڕگەش چۆنی`
  - Lessons 13 and 43: `زۆر سپاس بۆ ڕێنماییەکەت`
- 28 vocabulary terms appear in more than one lesson. Reuse is expected for core language, so this is not automatically a defect. Review topic overlaps to ensure that repeated terms are revisited in a useful new context.

The two repeated dialogue lines should be checked by the editor. They may be intentional reinforcement, but if not, revise one instance so the dialogue feels specific to its lesson. No lesson text was changed by this scan.


## Integration verification (2026-10-29)

- The integration branch retains the Course 1 source lesson file from the four-course safety base; the separate PR #5 edit to that original source was not copied, so this integration does not silently rewrite user-provided lesson text.
- The adapter regression test now loads all five conversation data files and verifies namespaced keys for lessons 1–48. Existing malformed-question, blank-option, duplicate-option, duplicate-number, and non-contiguous-number checks are preserved.
- Runtime integrity tests verify all 82 manifest lessons load without ID collisions, all 48 conversation lessons remain locked even when fake completion rows exist, and progress/quiz listings stay scoped to active courses.
- GitHub Actions run #40827126187 passed on commit `0d2c8ec9302dc1a89ef06d4254dd2f46768eb6f3`: compile check and 236 Python tests passed.
- This is integration evidence only. The PR remains Draft; no merge, deployment, bot activation, production data change, or dynamic-speech enablement occurred.

### Follow-up regression coverage (2026-10-29)

- Added two database regression tests that were present on the separate course-expansion branch but missing from the integration branch:
  - `test_namespaced_course_rewards_do_not_collide_with_legacy_course_one`
  - `test_namespaced_quiz_rewards_do_not_collide_with_legacy_course_one`
- These tests verify that a legacy Course 1 lesson key (`وانە_1`) and a namespaced conversation key (`daily_conversation_01`) retain separate completion/reward records, and that repeating the legacy key does not award twice.
- GitHub Actions run #40827536324 passed on commit `63063b7aa488403e26e59cd6f13acfffe0e702eb`: `compileall` and all 238 Python tests passed.
- The test suite logs one expected error-level message from the test that deliberately simulates failed voice delivery and checks quota refund behavior; the workflow and test suite still completed successfully.
- Current PR #6 remains open and Draft, with no merge or deployment. All 48 conversation lessons remain review-gated; dynamic speech remains disabled.

### Follow-up packaging and plan consistency check (2026-10-29)

- Updated the Botkeep packager's required-file list and its regression test to require all five current conversation lesson data files (lessons 1–48) plus `daily_conversation_plan.json`; the obsolete `daily_conversation_lessons_07_12.json` is no longer treated as the required runtime source.
- Corrected stale plan notes that still described the course as having only 30 lessons and incorrectly said the release status should remain `planned`. The plan now accurately records 48 proposed lesson entries and states that the course remains `draft_for_review` until editorial review and explicit activation approval.
- Updated `course_runtime.py` documentation examples to match the actual namespaced lesson keys.
- GitHub Actions run #40828234599 passed on commit `9f0de71653586c9fc6a7fef1063f3bc30705c634`: compile check and all 238 Python tests passed.
- The PR remains open and Draft; no merge, deployment, production bot/data changes, or dynamic-speech enablement occurred.


### Follow-up content overlap and menu clarity review (2026-10-29)

- Re-read the titles, objectives, dialogue lines, role-play prompts, quiz prompts, and vocabulary across all five current data files (48 lessons). This was a cross-lesson repetition and progression scan, not a Kurdish-language correctness review.
- Confirmed two exact repeated dialogue lines after whitespace/punctuation normalization:
  - Lessons 1 and 12: “سڵاو ئاڕگەش! چۆنی؟” / “سڵاو ئاڕگەش، چۆنی؟”
  - Lessons 13 and 43: “زۆر سپاس بۆ ڕێنماییەکەت.”
- No exact repeated role-play prompts or quiz prompts were found across lessons. Vocabulary recycling occurs, including terms reused in the same broad topic; that is not inherently a defect.
- The title/objective scan adds these editorial review candidates to the previously identified clusters:
  - Lessons 7, 26, 37, 39: food/drink, restaurant requests, meat-free requests, and preparing food. Verify that each lesson teaches a distinct communicative outcome.
  - Lessons 33 and 46: parks/nature and environmental protection. Confirm lesson 46 extends rather than duplicates the environmental language in lesson 33.
  - Lessons 34 and 40: art/exhibitions and books/films both practice opinions; distinguish the target expressions and context.
  - Lessons 35 and 41: future goals and weekly planning; verify that long-term goals and near-term scheduling are clearly differentiated.
- These are review flags, not confirmed defects. No lesson text or vocabulary was changed.
- Found a learner-facing clarity gap in the course catalog: the explanatory text described course status, but the four selection buttons themselves did not show it. Updated the buttons to label active, review-gated, draft, and planned courses while preserving the existing callback IDs. Added a regression test asserting the four statuses and unchanged callback IDs.
- The new regression test has been committed, but its GitHub Actions result must be checked before considering this change verified. The 238-test result above predates this menu change.
- All 48 conversation lessons remain `draft_for_review`; no course was activated, and no merge, deployment, production bot/data change, or dynamic-speech enablement occurred.


### Follow-up targeted progression review and latest CI verification (2026-10-29)

- Inspected the actual dialogue, objectives, exercises, role-play prompts, and quiz prompts for the repeated-topic clusters, rather than relying on titles alone.
- Shopping progression is visible but needs editorial confirmation: lesson 8 practices a multi-item produce purchase and total cost; lesson 25 compares prices and sizes; lesson 38 asks about clothing size and trying an item before deciding. The currency changes from toman in lesson 8 to dinar in lesson 38 without an explanation of the setting. Flag this for consistency/context review; do not silently rewrite it in this technical audit.
- Directions progress from multi-step directions and spatial relations in lesson 10, to finding a park and estimating walking time in lesson 29, to locating a neighborhood bakery in lesson 43. The latter is simpler than lesson 10, so lesson 43 should be confirmed as deliberate review/consolidation rather than assumed progression.
- Food lessons have distinguishable stated targets: lesson 7 preferences and drinks, lesson 26 requesting a meat-free meal, lesson 37 ordering from a menu, and lesson 39 sequencing meal preparation. Lesson 37 and lesson 26 overlap on restaurant requests; lesson 37 should ideally add a clearly different function such as clarifying ingredients, confirming the order, or asking for the bill.
- Environmental lessons differ in emphasis: lesson 33 is park etiquette/protecting plants and avoiding litter; lesson 46 adds separating plastic for reuse and group action. This appears to be a plausible progression, subject to language review.
- Long-term learning goals in lesson 35 differ from scheduling weekly activities in lesson 41; the exercise prompts reinforce that distinction.
- No lesson prose was changed in this pass. These are content-editorial flags, not claims of grammatical correctness.
- Verified the latest PR head `ebf71bd702b0a36368261498939d47916be57934`: GitHub Actions run #40830749666 (“Python checks”, run 1727) completed successfully, including `compileall` and the full unittest step. This is the first verified CI result after the course-status menu regression test was added.
- PR #6 remains open and Draft. All 48 conversation lessons remain review-gated; no merge, deployment, production bot/data change, course activation, or dynamic-speech enablement occurred.


### Student progress isolation and callback-gate verification (2026-10-29)

- Re-inspected runtime gates for opening lessons, finishing lessons, starting quizzes, answering quizzes, and awarding badges. Course-level status is rechecked on lesson and quiz callbacks; quiz-answer callbacks also revalidate active course status and lesson completion. Forged callbacks for the 48 draft conversation lessons are covered by callback-level regression tests.
- Added a database regression test confirming that the same namespaced lesson key is stored independently for two student IDs, each student receives their own first-completion reward, and a repeated completion by one student does not alter the other student's progress or XP.
- GitHub Actions run #40834804899 passed on commit `2bc232f0338fcea2e4cedb8bb2a1820f6987107c`. Dependency installation, `compileall`, the complete unittest step, and job cleanup all completed successfully.
- The test was first appended below the module's `unittest.main()` guard; this placement was caught during review and corrected so the test remains a method of the database test class and is discoverable by unittest. CI passed after that correction.
- Current PR #6 head is `2bc232f0338fcea2e4cedb8bb2a1820f6987107c`; it remains open and Draft against `fix/four-course-structure-2026-10-27`. No merge, deployment, production bot/data change, course activation, or dynamic-speech enablement occurred.
- Remaining limitation: GitHub Actions validates automated behavior, not Kurdish language naturalness or pedagogical quality. The editorial review flags above remain unresolved until a human language review is completed.

### Concurrency reward regression coverage (2026-10-29)

- Added `test_concurrent_duplicate_lesson_and_quiz_callbacks_award_once` in `tests/test_database.py`.
- The test fires 16 concurrent duplicate lesson-completion calls and 16 concurrent duplicate quiz-completion calls for the same user and lesson key. It verifies each operation grants rewards exactly once and that XP, score, coins, chests, and test totals match the expected single-award totals.
- GitHub Actions run #40835142571 passed on commit `48e7569e84ee018d530fddd339c0369f7794495f`: Python compilation and the full unittest suite passed.
- PR #6 remains open, Draft, and unmerged. No production bot/token/data changes, deployment, course activation, or dynamic-speech enablement occurred.

### Focused progression review (2026-10-29)

A focused reread compared the actual dialogue, vocabulary, exercises, and quiz prompts in the main overlap clusters. This is an editorial triage only; no lesson text was changed.

- **Shopping (8, 25, 38):** the dialogue scenarios are meaningfully different: lesson 8 buys fruit and calculates a total; lesson 25 compares bag prices and size; lesson 38 asks about shirt size and trying it on. The principal consistency decision is currency localization: lesson 8 uses toman while lesson 38 uses dinar. Choose an intentional learner-region policy (or explicitly teach the distinction) before approval; do not silently change prices.
- **Directions (10, 29, 43):** these also have distinct contexts: finding a library with relative positions; following left/right turns and estimating walking time; locating a bakery in a neighborhood. Reuse of location words appears purposeful rather than an exact lesson duplicate.
- **Health (13, 45):** lesson 13 practices describing symptoms and finding a clinic; lesson 45 practices booking/rescheduling an appointment. These are complementary functions, though a language reviewer should check the naturalness of the appointment exchange.
- **Environment (33, 46):** lesson 33 focuses on keeping a park clean and protecting plants; lesson 46 adds separating plastic bottles for reuse. The learning outcomes are distinct enough to retain pending language review.
- **Help (28, 47):** lesson 28 concerns an urgent incident involving a person who has fallen; lesson 47 concerns a lost item and asking staff for help. These are distinct scenarios, but lesson 28's emergency wording and advice should receive careful human review for clarity and appropriateness.
- **Review lessons (12, 18, 30, 36, 42, 48):** these intentionally recycle everyday functions. Their dialogues increasingly combine multiple settings and planning tasks, but the repeated “review + plan + library/food/shopping” pattern remains a possible monotony risk. A reviewer should verify that each review lesson explicitly assesses a different cumulative skill, rather than removing useful spaced practice automatically.
- Repeated dialogue lines remain limited to the previously recorded pairs in lessons 1/12 and 13/43. This scan found no exact duplicate quiz prompts or role-play prompts and no malformed quiz answer indices or fewer-than-three-option quiz questions.

**Disposition:** retain the 48 lessons as drafts. Resolve currency/localization policy and complete Kurdish naturalness/teaching review before considering activation.

### Follow-up cumulative-skill and sensitive-dialogue review (2026-10-29)

This pass reread the actual review-lesson dialogue and exercises for lessons 12, 18, 30, 36, 42, and 48, plus the emergency and appointment scenarios. No lesson text was edited; the findings below are review guidance, not final Kurdish-language judgments.

- **Lesson 12** is an early integrated task: greeting, meeting time/place, shopping, walking directions, food, and studying. Its exercises separately prompt asking prices and directions. The dialogue includes the phrase “کۆببینەوە”; confirm the intended spelling/inflection with the project's Kurdish-language reviewer rather than silently normalizing it.
- **Lesson 18** has a narrower, identifiable target: negotiate a meeting time and place, account for rain, and communicate a plan change. Its exercise to use expressions from lessons 1–17 is useful cumulative practice.
- **Lesson 30** combines shopping, food, and directions, much like lesson 12. To keep it from feeling like a repeat, the editor should ensure the learner is assessed on combining functions independently—not only recalling a similar itinerary.
- **Lesson 36** has a distinct conditional-planning target: decide what to do if the weather changes and communicate a changed meeting plan. Keep that as its assessment focus.
- **Lesson 42** combines transport, returning a library book, choosing a restaurant, and an optional park visit. Its stated “opinion” target is not clearly demonstrated in the dialogue; either add a clear opinion function during language editing or narrow the objective.
- **Lesson 48** is a final multi-stop integrated conversation (library, market, park, lunch) and uses material from lessons 43–47 in the exercise. Its distinction from lesson 42 should be explicit in the assessment: a complete independent plan across multiple places, with a contingency if a problem occurs.
- **Curriculum recommendation:** retain spaced review, but label each review lesson with a short cumulative skill checklist (e.g. meeting negotiation; conditional plan change; multi-function itinerary; independent multi-stop plan). Make quiz and role-play assess that skill, not just topic recall. This is a differentiation recommendation, not a reason to remove lessons.
- **Lesson 28 (emergency):** the current scenario asks learners to call for help, give the location, stay calm, and avoid blocking traffic. Because this is an emergency-themed learning dialogue, have a qualified reviewer check the safety wording. Keep any advice minimal and broadly safe, and emphasize contacting local emergency services and following their instructions; avoid presenting the language exercise as comprehensive first-aid guidance.
- **Lesson 45 (medical appointment):** the dialogue teaches requesting and changing a booking, but the time exchange “پێنجشەممە کاتژمێر دە” does not specify morning/evening and “کاتژمێر دوای نیوەڕۆ هەیە؟” should be checked for naturalness and clarity. Make the appointment time unambiguous during human language review.
- These are editorial flags only. No source lesson data, active course status, runtime behavior, production bot, or dynamic-speech setting was changed.

### Follow-up shopping lesson objective-to-exercise alignment (2026-10-29)

A reread of the course plan and shopping lessons 8, 25, and 38 confirms that the plan does not define a learner-region or currency-localization policy.

- **Lesson 8:** the dialogue gives a consistent total: two kilograms of apples at 3,000 toman per kilogram plus one kilogram of oranges at 3,000 toman totals 9,000 toman. The arithmetic is correct as written.
- **Lesson 25:** the dialogue models asking for a cheaper bag and comparing price/size. The task matches its stated comparison focus.
- **Lesson 38:** the dialogue models asking about a shirt's price and size and trying it on; its final exercise asks the learner to request a discount, but the dialogue does not model a discount request. This is an objective-to-practice alignment gap. During language editing, either add a natural example of asking for a discount or change the exercise to practise the expressions actually taught.
- **Currency policy:** lesson 8 uses toman while lesson 38 uses dinar. The course plan contains no rule explaining the intended region or why both currencies are introduced. Before approval, choose a consistent setting or explicitly teach the currency distinction; do not silently alter prices or currencies during a technical audit.
- No lesson source text was changed in this pass. These are review flags for the language/content editor, not an approval to revise the authored dialogue.

### Follow-up appointment-time and cumulative-assessment consistency check (2026-10-29)

- **Lesson 45 appointment-time consistency:** the dialogue first offers “پێنجشەممە کاتژمێر دە” without clarifying morning/evening, then asks whether there is a time in the afternoon and confirms 3 PM. The quiz treats 3 PM as the accepted appointment. The learner can infer the final time, but the first offer is needlessly ambiguous and does not explicitly teach the morning/afternoon contrast. During language review, specify a clear time period for the first offer and make the change/selection exchange explicit. Do not change the actual appointment data silently.
- **Lesson 18 vs. lesson 36:** both practise arranging a meeting and changing the plan if it rains, and both quiz the learner on the time/place or rainy-weather alternative. Lesson 36 does add a library-book pickup and a longer cumulative prompt, but the skill distinction could be stronger. Recommendation: lesson 18 should assess negotiating a time/place and confirming the plan; lesson 36 should assess handling a contingency and independently adapting the plan using several earlier functions.
- **Lesson 48 final assessment:** its dialogue contains a multi-stop plan, but the two quiz items only check the first destination and a generic response to a problem. The role-play and longer writing exercise are better aligned with the stated integrated-conversation objective. To verify mastery, consider adding one assessment item that requires ordering or justifying the stops, or responding to a concrete disruption, rather than relying on simple recall alone.
- **Lesson 13 health wording:** the dialogue is a basic everyday-language scenario, not a medical lesson. Keep advice minimal and avoid implying that a single symptom determines a diagnosis; language review should ensure the phrase about yellow/pale appearance is natural and not used as a diagnosis.
- This pass only records editorial observations. No lesson JSON, course status, bot runtime, production data, or speech configuration was modified.

### Food-and-restaurant cluster: objective distinction and dietary clarity (2026-10-29)

- **Lessons 26 and 37 overlap materially:** both objectives cover ordering food and explaining requirements; both dialogues ask for a menu, request food without meat, and practise a polite order. Lesson 26 adds a general request to omit an ingredient, but this distinction is mostly in the exercise rather than the dialogue. During instructional editing, make lesson 26 explicitly practise communicating a dietary restriction and confirming what “without meat” includes; keep lesson 37 focused on reading the menu, selecting a dish, and completing a restaurant order. This is a teaching-design flag, not a claim that the existing Kurdish wording is definitively wrong.
- **Lesson 26 dietary clarity:** the dialogue orders soup and bread, then adds “without meat.” A learner may not know whether the request applies to the soup, the whole meal, or ingredients such as broth. Add a natural clarification/confirmation exchange during reviewed editing. Do not silently label the meal vegetarian or vegan, or assume every soup is meat-free.
- **Lesson 7 versus lesson 37:** lesson 7 already introduces favourite foods/drinks and includes a restaurant role-play; lesson 37 repeats the restaurant ordering function. This can be reasonable spiral practice, but the lesson 37 exercise should demand a more specific new skill (e.g. selecting from menu options and confirming the order) instead of a generic restaurant dialogue.
- **Lesson 39 cooking sequence:** the dialogue and exercises align around ingredients, task-sharing, and cooking steps. The line about keeping the heat from being “too high” is intentionally general; if this remains a beginner language course, avoid presenting it as complete cooking-safety guidance. No need to expand into technical safety material here.
- **Lesson 40 quiz alignment:** the quiz checks the film topic and the meaning of “سەرنجڕاکێش,” consistent with the objective of expressing opinions about books and films. No objective/quiz mismatch found in this limited check.
- No lesson source text or quiz was edited in this pass. Findings are review flags only; all draft/release guardrails remain unchanged.

### Mechanical integrity sweep: all 48 draft lessons and quiz answer indexes (2026-10-29)

- Re-read the six lesson JSON files on the integration branch and confirmed the combined lesson set contains exactly lessons 1–48, with no missing lesson numbers.
- Confirmed each of the 48 records has an objective, at least one exercise, and a role-play activity.
- Checked every quiz item across the 48 lessons: all answer indexes point to an existing option, and no quiz item has duplicate option strings. No structural quiz-option/index defects were found in this pass.
- This is a structural check only; it does **not** certify that every marked answer is pedagogically ideal, that every distractor is fair, or that the Kurdish wording is fully natural. Those require lesson-by-lesson semantic and language review.
- No lesson content, activation status, runtime logic, production data, or speech settings were changed.

### Follow-up bank-and-money lesson objective coverage (2026-10-29)

- Lesson 31, **«لە بانک و پارە»**, states an objective covering asking about money, making payments, and protecting money. The dialogue demonstrates locating a bank, asking about withdrawing money, needing a bank card, and protecting cash; it does not actually model a payment or compare payment methods.
- The exercises ask learners to write two payment methods, so this part of the objective/exercise is not scaffolded by the dialogue. During editorial revision, either add a short, everyday payment exchange (for example, asking which payment methods are accepted) or narrow the stated objective/exercise to the functions the dialogue teaches. Do not invent bank policies or change the lesson JSON without the user's approval.
- This is a teaching-alignment flag, not a code/runtime defect. No lesson content or activation status was changed.

### Final review lesson: stated opinion skill is not assessed (2026-10-29)

- Lesson 48 objective explicitly includes **«بۆچوون»** (expressing an opinion), but its dialogue is primarily a sequence of errands and conditional plans (library return, shopping, park, lunch, and notifying each other if a problem occurs). Neither quiz item asks the learner to express, understand, or justify an opinion.
- This creates a specific objective-to-dialogue-and-assessment gap in the final integrated review. During editorial revision, either add a natural exchange in which the speakers state a preference and briefly give a reason, with a quiz item checking that function, or remove «بۆچوون» from the objective. Do not silently change the draft lesson.
- This finding complements the earlier flag for lesson 42, whose objective also includes expressing an opinion without a clear opinion exchange in its dialogue. When revising, distinguish lesson 42's everyday planning/opinion practice from lesson 48's independent multi-stop plan and contingency handling.
- No lesson JSON, runtime logic, or activation state was changed.

### Gallery lesson: permission-seeking exchange is left unresolved (2026-10-29)

- Lesson 34, **«لە پێشانگا و هونەر»**, includes the question **«ئایا دەتوانین وێنەکە بگرینەوە؟»** (can we take a photo of the artwork?), but the reply only says to read the gallery rules first. The dialogue never models how to check the rule, ask staff, or respond to a yes/no permission answer.
- The exercises include preparing questions for gallery staff, but the quiz does not assess this practical permission-seeking function. This leaves a useful real-world interaction introduced but not completed or assessed.
- During editorial revision, add a brief exchange in which they check the posted rule or ask staff and receive an explicit answer, without assuming all galleries allow photography. Add a quiz item only if the lesson's objective is intended to assess this function.
- This is a pedagogical completeness flag only. No lesson JSON, policy assumption, runtime behavior, or activation state was changed.

### Lesson 14 objective alignment (2026-10-29)

- Lesson 14 lists asking about class start time as an objective, but the dialogue only covers unfinished assignments, a difficult language lesson, and arranging to meet at the library after noon. It never asks when a class starts.
- The exercises focus on favourite subjects, unfinished assignments, and planning study time; neither quiz item assesses the stated start-time skill.
- During editorial revision, either add a brief question-and-answer about class start time and assess it, or narrow the objective to match the content. No lesson data was changed; this remains a review flag.

### Lesson 38: discount-request exercise lacks a dialogue model (2026-10-29)

- Lesson 38, **«لە کڕین و بازاڕ»**, has a clear dialogue about shirt price, larger size, and trying the shirt on before deciding. Its third exercise, however, asks the learner to write a sentence requesting a discount; no speaker models or responds to a discount request in the dialogue.
- The quiz assesses price and trying on the shirt, so it aligns with the dialogue but leaves the discount function in the exercise unsupported.
- During editorial revision, either add a short, natural discount-request exchange with a clear seller response, or replace the exercise with one practising a function already modelled. Do not assume every seller offers a discount, and do not silently alter the draft.
- Review flag only; no lesson JSON was changed.

### Lesson 41: changing a plan is assigned but not modelled or assessed (2026-10-29)

- Lesson 41, **«پلان بۆ هەفتە»**, models listing activities by weekday and negotiating an exercise time (“after noon is better”). Its third exercise asks the learner to change a plan and explain why, but the dialogue contains no actual cancellation, rescheduling, or reason for a change; neither quiz item checks this function.
- During editorial revision, either add a short exchange that changes one scheduled activity and gives a reason, then assess that function, or narrow the exercise to the scheduling language demonstrated. Keep the exercise accessible to learners at this level and do not change the draft lesson silently.
- Review flag only; no lesson JSON was changed.

### Lesson 30: cumulative review does not assess all stated functions (2026-10-29)

- Lesson 30, **«پێداچوونەوەی گشتی و گفتوگۆی درێژ»**, states that learners will combine questions, requests, directions, planning, and everyday responses. The dialogue does include shopping, food, directions, and a contingency message, and the exercises ask for a longer integrated dialogue.
- Both quiz items focus on the first destination and interpreting location/direction language. Neither checks the planning/contingency function or whether the learner can combine multiple turns independently. This is a cumulative-assessment coverage gap rather than a dialogue contradiction.
- During editorial revision, consider replacing or supplementing one quiz item with a short integrated decision or plan-change question grounded in the dialogue. Keep the quiz at the course's beginner level and do not change the draft silently.
- Review flag only; no lesson JSON was changed.

### Lesson 24: troubleshooting exercise is only lightly scaffolded (2026-10-29)

- Lesson 24, **«داواکردن و چارەسەرکردنی کێشە»**, introduces an internet connection problem. The dialogue asks whether the modem was checked and suggests restarting it, so it models one initial check and one simple response.
- Exercise 2 asks learners to write two questions to identify the cause of a problem, but the dialogue does not provide a second diagnostic question or a clear sequence of checks. This makes the requested exercise more demanding than the dialogue's model and leaves the troubleshooting objective only partly scaffolded.
- During editorial revision, add one or two simple, non-technical diagnostic questions (for example, whether other devices can connect) or narrow the exercise to the troubleshooting language already modelled. Keep it beginner-friendly and avoid presenting a single fix as guaranteed. Do not change the draft silently.
- Review flag only; no lesson JSON was changed.

### Lesson 11: return-time planning is raised but not completed (2026-10-29)

- Lesson 11, **«گواستنەوە و گەشت»**, includes planning a trip by bus, a meeting point/time, estimated journey duration, and preparation. Near the end, Kêjyar says they should also decide when to return, but the dialogue ends without either speaker proposing or confirming a return time.
- The exercise asks learners to plan a fictional trip, so it could naturally practise this missing step; the current quiz only assesses the meeting point and checking trip information. This leaves a practical planning turn unresolved rather than modelling a complete itinerary.
- During editorial revision, either complete the return-time exchange with a clearly tentative example and confirmation, or remove the unfinished prompt. Do not invent a real timetable or imply that the example is an actual transport schedule. Do not change the draft silently.
- Review flag only; no lesson JSON was changed.


### Owner-directed activation update (2026-10-29)

- Following the owner's explicit instruction, Courses 2 (48 daily-conversation lessons) and 3 (12 unified-orthography lessons) are now marked `active` in `courses.json` on the working branch.
- Runtime access follows each course's own lesson order: the first lesson opens, and later lessons remain locked until the immediate predecessor is completed. Progress remains isolated by course-specific lesson IDs.
- Existing lesson-level `draft_editorial_review` metadata and the plan's provisional notes are retained as editorial provenance; they are not runtime course-activation gates.
- This is a branch-level code change only. PR #6 remains open and Draft; no merge or deployment has been performed. Dynamic speech remains disabled.
