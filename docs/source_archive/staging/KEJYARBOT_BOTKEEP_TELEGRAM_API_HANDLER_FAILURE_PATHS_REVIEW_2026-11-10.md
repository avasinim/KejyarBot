# KejyarBot — Telegram API Failure Paths in Course Handlers Review
Date: 2026-11-10
Scope: read-only review of active Telegram course-handler modules on main. No production changes and no Botkeep operations.

## Files inspected
- `bot.py`, main entry point and handler registration, blob SHA `e825b7e277beda99e35cfa046cab349630ea2bfb`.
- `arami_course1_telegram.py`, blob SHA `53a28256b0f8da36cc7c30a9b9007facee2e30f4`.
- `arami_lesson1_telegram.py`, blob SHA `04028179c43f2b5236ff23fe6c683fcea5007797`.
- `arami_lesson5_telegram.py`, blob SHA `2e6471e8277b7ffe7ba300beed855603e6c43cdf`.
- `arami_lesson1_interaction.py`, blob SHA `1ff2f2babb49423d5ac63a4cd9676947ca4ff0a8`.

## Verified findings
1. The main `bot.py` registers callback and message handlers, then invokes `app.run_polling()`. It does not register a project-level PTB error handler. The main entry point also has no explicit wrapper around polling startup/shutdown.
2. The Arami Course 1 infographic sender, `send_lesson_infographic()`, catches broad `Exception`, writes an exception log, returns `False`, and allows the surrounding lesson flow to continue. This is a deliberate best-effort/fallback pattern: missing or undeliverable infographic should not prevent the lesson text flow from continuing.
3. In the Arami Course 1 callback handler, local source/manifest/question-bank errors are handled as `AramiCourseTelegramError` (or selected validation exceptions), with a user-facing fallback message. These catches do not generally wrap subsequent Telegram network operations such as `reply_text`, `edit_message_reply_markup`, or `edit_message_text`; Telegram API/network exceptions in those operations can propagate to PTB's application-level error path.
4. Arami Lesson 1 and Lesson 5 handlers catch expected local-file and input-validation exceptions in selected paths. Telegram send/edit calls are not consistently wrapped in a common Telegram API error policy. Therefore, handling is mixed by feature rather than centrally standardized.
5. The Arami Course 1 callback handler acknowledges most non-interaction callbacks immediately; for selection/submission it intentionally defers acknowledgement until it has validated and updated session state. No evidence from this source scan establishes a platform outage or a persistent polling failure.
6. Quiz/session state in these handlers is held in `context.user_data`; it is transient and can be lost on process restart. This is already documented in the earlier session/polling audit notes.

## Interpretation
- The infographic fallback is a positive resilience behavior.
- Other Telegram send/edit failures may bubble out of a handler. Because the application has no custom error handler, there is no bot-specific classification, alert, or tailored recovery response for those exceptions.
- This is an observability and user-experience consistency gap, not proof of the cause of the current Botkeep outage.
- A network/API exception while handling one update does not by itself establish that the polling process exits; exact behavior depends on the exception path and PTB runtime, which cannot be observed from the repository alone.

## Recommendations (not applied)
1. In a separate reviewed change later, add a central PTB error handler that logs exception class, update type, and safe non-secret context; classify network/time-out, rate-limit, conflict, and invalid-request failures.
2. Keep user-facing fallback messages limited to operations where retry/recovery is safe; do not blindly retry callback edits or duplicate reward operations.
3. Preserve the existing best-effort infographic behavior unless product requirements change.
4. Add targeted tests for failed Telegram send/edit operations and verify quiz state remains recoverable.
5. Do not restart or redeploy Botkeep while the stuck infrastructure restore remains unresolved; confirm support resolution and backup state first.

## Boundaries
- No source file was changed.
- No Botkeep server, Telegram token, process, or database was accessed or modified.
- No live Telegram API test was performed.
- This note is an append-only audit record, not a declaration of production health or outage cause.
