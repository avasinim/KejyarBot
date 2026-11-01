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
