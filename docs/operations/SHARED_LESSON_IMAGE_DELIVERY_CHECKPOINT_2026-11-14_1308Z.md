# Shared lesson image delivery checkpoint — 2026-11-14 13:08Z

## Scope
One approved image is shared by exactly two lesson routes:
- Arami orthography foundations: `arami_course1_lesson_05`
- Kurmanji Latin orthography: `kurmanji_latin_orthography_01`

Image path: `assets/lessons/kejyar_lesson5_kurdish_letters_v2.png`

## Findings and changes
- Confirmed the generic lesson callbacks `open_selected_lesson` and `open_next_lesson` call `send_shared_lesson_image` after lesson text.
- Confirmed Latin Course 1 Lesson 1 is listed under course ID `kurmanji_latin_orthography`; its course menu emits `open_lesson_<lesson_id>`, routed to `open_selected_lesson`. The exact pair matches the shared-image allowlist.
- Found the dedicated Arami Lesson 5 callback `arami5:lesson` bypassed the generic reader and did not send the shared image.
- Corrected only `arami_lesson5_telegram.py` to call the exact allowlisted route after lesson text, and updated `tests/test_arami_lesson5_telegram.py` to assert exactly one call with the expected course ID, lesson ID, and base directory.
- No lesson content, image asset, database, environment secret, unrelated course, server, or deployment configuration was changed.

## Verification
- New Release head: `918096cd7372496a1cef654444f3c1ff556a1b3a`.
- GitHub Actions: all 10 workflow runs observed for this head completed with `success`.
- Python checks log: `Ran 589 tests`; `OK (skipped=11)`.
- The log explicitly includes the updated dedicated Lesson 5 callback test as `ok` and the Latin course selection route test as `ok`.
- Shared helper tests verify the exact two-pair allowlist, missing-file fail-closed behavior, one photo send, and nonfatal Telegram photo errors.
- This is automated CI evidence only. No live Telegram end-to-end send was performed or claimed.

## Safety and next boundary
- No deploy, Start, Restart, restore, sync, or server-side operation was performed.
- Next safe work: continue read-only audit of the image asset/package constraints and record findings. Any server or deployment action remains out of scope without separate explicit approval.
