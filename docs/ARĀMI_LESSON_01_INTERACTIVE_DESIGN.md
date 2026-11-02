# Arami Course 1 — Lesson 1 Interactive Design Specification

## Scope and non-negotiable boundaries

This work applies only to Lesson 1 of the Arami orthography course.

- Do not edit, paraphrase, normalize, reorder, expand, or fact-check the supplied lesson body.
- Render the existing lesson body as read-only content. Keep its headings, examples, letter forms, counts, and ordering exactly as supplied.
- Do not create new linguistic explanations or examples in the lesson body.
- Keep the Latin learning path and both Latin subcourses unchanged.
- Keep Arami Lesson 4 (grammar) postponed and unavailable until separately approved.
- Preserve the existing KejyarBot identity, character, and voice implementation. Do not add Avasin branding.
- Do not enable dynamic speech. Continue respecting `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`.

## Lesson presentation

1. Present the lesson as a dedicated course lesson screen, not as a long unstructured message.
2. Header: KejyarBot identity, course title, lesson number/title, and a compact progress indicator.
3. Split the existing body into display sections only at boundaries already present in the supplied content. Sectioning must not change the body text or order.
4. Keep the supplied alphabet chart attached to the lesson as its own media item. Do not redraw or regenerate the chart as part of this task.
5. Use readable message lengths and a visible Continue action between sections. Include Back and Resume actions.
6. **Every lesson must have its own prerecorded voice recording.** The lesson cannot be marked ready or activated if its dedicated recording is missing. Store an explicit audio asset key in that lesson's metadata, resolve it through the existing `get_voice` path, and deliver the recording with the lesson. Do not reuse an unrelated clip or synthesize replacement audio.
7. At the end, show two distinct actions: “ڕاهێنان” and “تاقیکردنەوەی کۆتایی”.

## Practice sequence

Practice is supplemental interaction; it must not be inserted into or presented as edits to the lesson body.

Recommended sequence, using only letter/sound facts and examples already present in Lesson 1:

1. **Recognize** — choose the matching letter from a small set.
2. **Classify** — sort an item into the lesson's existing consonant/vowel categories.
3. **Match** — pair a letter with its corresponding sound or lesson-provided example.
4. **Listen and choose** — play the already supplied audio and select the matching option. If no verified audio mapping exists for an item, omit this task rather than guessing.
5. **Complete** — choose the missing item in a sequence/table already shown in the lesson.
6. **Review mistakes** — retry only missed practice items, with neutral explanatory feedback that points back to the exact relevant lesson section; do not add new linguistic claims.

Practice rules:
- One question per screen; shuffle answer options, never the source content.
- Give immediate right/wrong feedback and allow retry.
- Do not reveal the correct answer until the learner submits.
- Avoid trick questions, ambiguous distractors, and options differing only by visually confusable Unicode characters unless the task explicitly tests those characters and displays them clearly.
- Support right-to-left Kurdish text and preserve exact Unicode code points.
- Practice does not count as lesson completion; it is repeatable.

## Final assessment

- Use a separate assessment session with a fixed question set drawn only from Lesson 1.
- Cover the lesson's own stated distinctions and categories; do not test knowledge not taught in this lesson.
- Mix recognition, classification, matching, and listening only where the matching audio is confirmed.
- Require explicit submission for each answer.
- Show a final score as both points and percentage, plus correct/incorrect counts.
- Show a review list of missed questions with links back to the relevant lesson section.
- Allow a full retake. Store the best score and most recent attempt separately if the existing persistence layer supports both; otherwise do not introduce a database migration for this feature.
- Do not block lesson access or progression based on a score unless the existing course policy explicitly requires it.

## Technical behavior

- Keep the lesson identifier namespaced to the Arami course; do not reuse generic `وانە_1` if that key is already used by another course.
- Resolve lesson, practice, assessment, and audio assets through explicit Arami lesson metadata rather than relying on title matching.
- Validate callback payloads, question indexes, answer indexes, and quiz state before reading or mutating state.
- Clear invalid or expired assessment state safely and return the learner to the lesson menu without crashing.
- Prevent double submission from awarding duplicate points or completion rewards.
- Keep practice state separate from final-assessment state and from Latin-course quiz state.
- Do not change shared voice settings, database schema, production credentials, deployment settings, or the Latin course manifests in this task.

## Acceptance tests

### Content immutability
- The exact Lesson 1 source body before and after the UI work is byte-for-byte identical.
- The chart is attached to the correct Arami Lesson 1 entry.
- No Latin lesson, quiz, audio mapping, or manifest entry changes.

### Navigation and rendering
- Learner can open Lesson 1, move forward/back between existing content sections, resume, and return to the course menu.
- Kurdish text renders RTL without clipping; letter forms and Unicode code points are preserved.
- The lesson remains readable when media or audio is unavailable; missing media must not crash the lesson.

### Practice
- Each supported practice type can be started, answered, retried, and exited.
- Feedback corresponds to the selected answer.
- Practice attempts do not mark the lesson complete and do not alter assessment scores.
- Invalid callback data is rejected safely.

### Assessment
- Assessment contains only material present in Lesson 1.
- Score, percentage, and answer review are internally consistent.
- Retake works; repeated callbacks cannot double-score.
- Empty or malformed quiz state is handled safely.
- Assessment state cannot leak into either Latin course.

### Regression and safety
- Existing Latin course IDs, lesson counts, lesson text, quiz content, and audio mappings remain unchanged.
- Existing voice selection and prerecorded voice playback continue to work.
- Arami Lesson 1 declares a dedicated audio asset; missing or unresolved recording blocks lesson readiness and is never silently skipped.
- Dynamic speech remains disabled.
- No production deployment or live database changes are part of this branch.

## Implementation order

1. Add an isolated Arami Lesson 1 runtime entry without touching the lesson body.
2. Add presentation/navigation and chart attachment.
3. Add practice flow and its isolated callbacks/state.
4. Add final assessment and scoring.
5. Add automated tests for the acceptance criteria above.
6. Run the complete test suite and report exact results before any release or deployment.


## Confirmed Lesson 1 audio asset and handoff status

The user explicitly identified commit `5642e5310cc856f7bfd8c821086a9f2febe419e6`
(title: `دەنگەکان`) as the recording for Arami Course 1, Lesson 1.
That commit adds the repository-root asset:

- `دەنگەکانی ئەلفبێ.ogg`
- Commit: https://github.com/avasinim/KejyarBot/commit/5642e5310cc856f7bfd8c821086a9f2febe419e6

This is the only audio asset currently confirmed by the user for this lesson.
Do not substitute `voices/lesson_start.mp3`, `voices/kejyar.mp3`, any other
root-level Kurdish recording, or any Latin-course recording. Do not infer that
other recordings belong to this lesson. The recording must remain attached to
this exact Arami Lesson 1 entry.


## Source reconciliation — explicit Lesson 1 clarification

The user explicitly clarified that Lesson 1 teaches **8 vowels**. This statement
is authoritative for the lesson's practice and assessment. A supplied chart
appears to show a different vowel count and a consonant count that cannot be
safely reconciled with that explanation. Therefore:

- Never quiz learners on the chart's apparent 6-vowel count.
- Do not quiz the chart's 28-consonant count or 34-letter total until the
  original lesson wording resolves the discrepancy.
- The only count item currently approved in the interaction bank is **8 vowels**.
- The chart's red vowel color key may be used as a visual recognition item,
  but only as a separate chart observation, not as a correction to the lesson.
- Do not silently change the user's lesson text or chart to make the counts fit.

The current bank intentionally contains only the supported vowel-count item
and the chart's color-key item in each mode. Listening, letter recognition,
sequence completion, and matching remain unavailable until the exact supplied
lesson/audio mapping is established.

## Work completed on the isolated feature branch

Branch: `feat/arami-lesson1-interactive-design-2026-11-01`
Base: `main` at `04a1b3e0ab9a515211ab3709513cdc1ec90d86ea`

- Added a content-agnostic practice/assessment state engine in
  `arami_lesson1_interaction.py`.
- Added automated unit tests for question-bank validation, answer selection
  and submission, scoring, retrying missed items, and audio metadata checks.
- Added `lesson_audio.py` to validate explicit lesson audio metadata and
  prevent unsafe paths or unsupported/missing files.
- Added a lesson playback hook in `bot.py` which sends a lesson-specific
  recording when its metadata is present.
- Added this design specification and its acceptance criteria.

## Remaining integration work — do not treat as release-ready

- The confirmed audio filename has not yet been added to an Arami Lesson 1
  runtime metadata record. The playback hook therefore does not yet prove that
  this recording is played for the correct lesson.
- The bot's existing generic lesson registry still uses shared lesson keys;
  the Arami lesson needs a dedicated namespaced runtime key before wiring the
  audio or quiz into the live navigation.
- The dedicated Arami Lesson 1 content, its supplied chart, and the actual
  practice/assessment question bank have not been integrated. Do not reconstruct
  or edit the user's lesson text.
- The complete repository test suite has not yet been run for this branch.
- No pull request, merge, deployment, production database change, or Botkeep
  live update has been performed.

## Restart checklist

1. Resume from this feature branch, not `main`.
2. Keep the Arami and Latin course registries, quiz state, lesson IDs, and audio
   mappings isolated.
3. Bind only `دەنگەکانی ئەلفبێ.ogg` to Arami Course 1 Lesson 1 after confirming
   the namespaced lesson metadata and existing voice-resolver compatibility.
4. Preserve the supplied Lesson 1 body byte-for-byte.
5. Complete integration and run focused plus full tests; report actual results.
6. Stop before merge, deployment, production DB changes, or Botkeep live changes
   unless the user explicitly authorizes them.


## Runtime adapter added (isolated; not wired into bot navigation)

Added `arami_course1_runtime.py` and
`tests/test_arami_course1_runtime.py`.

The adapter:
- Loads only `course_data/arami_course1_manifest.json`.
- Enforces exactly four unique, namespaced Arami lesson IDs.
- Requires the user-supplied Lesson 1 content to remain marked immutable.
- Verifies the exact user-confirmed recording `دەنگەکانی ئەلفبێ.ogg`.
- Resolves the recording from the repository root and rejects missing or unsafe paths.
- Does not import or modify the Latin course loaders, `LESSON_DATA`, or shared quiz IDs.

The adapter is intentionally not imported into `bot.py` yet. The main bot's current
course navigation and shared lesson registry do not yet implement the user's
two-top-level-course Arami structure. Wiring this prematurely could expose old
Course 1 lesson data or collide with Latin lesson state. The adapter and tests
are isolated preparatory work; they do not make the lesson active in Telegram.

Focused tests were authored but have not been executed in this environment.
No PR, merge, deployment, production DB change, or Botkeep update was performed.

## Round 1 — complete 20-lesson catalogue and interaction rollout

The feature branch now exposes the complete **20-lesson Arami Course 1 / Round 1**
catalogue from the bot's «📕 ڕێنووسی ئارامی» menu. This is separate from the
legacy orthography course and from both Kurmanji Latin courses.

- The catalogue has exactly 20 numbered lesson entries, each with its own
  manifest-bound source file and source reader.
- Lesson 1 and Lesson 5 retain their dedicated interaction flows.
- Lessons 2–4 and 6–20 use their own lesson-scoped practice and assessment
  banks. Question IDs and source evidence remain tied to their lesson.
- The source reader sends the selected lesson text in bounded Telegram message
  chunks; it does not merge lesson sources or alter the stored source files.
- Verified lesson recordings are delivered only after the corresponding
  lesson text. Audio is never borrowed from another lesson or synthesized.
- The «ل / ڵ» additions in Lesson 15 are represented in both practice and
  assessment banks, including the source contrasts چڵ/چل, پەڵە/پەلە and
  گوڵ/گول.

### Audio readiness is intentionally separate from reader/quiz activation

All 20 lessons are reachable for reading and their approved practice and
assessment paths are exposed. Ten lessons still lack an explicitly confirmed
dedicated recording mapping: **3–8, 10, 17–19**. The catalogue marks those
recordings as pending; it does not claim those lessons are audio-complete.
The two unassigned recordings «دەنگی ر.ogg» and «دەنگی ڕ.ogg» remain unassigned
until the owner confirms their lesson mapping. No guesswork or audio reuse.

### Release boundary

The catalogue and interactions are enabled on this feature branch and PR #49.
This does not mean the live Telegram deployment has changed. Merge to main,
Botkeep synchronization, production credentials, live Telegram testing, and
deployment remain outside this change until explicitly authorized. Dynamic
speech remains disabled.

