# Course 2 (Daily Conversation) — Visual Asset Audit
Date: 2026-11-16
Branch: fix/course1-menu-label-2026-11-16

## Confirmed delivery status
The project owner confirmed on 2026-11-16 that the lesson images they tested display and deliver correctly. Treat image transport/rendering as verified by the owner; do not request another delivery test unless a new change affects it.

## Scope inspected
- Active course: `daily_conversation`, 42 lessons.
- Existing visual assets inspected: `assets/infographics/lesson-01-greetings.svg` through `lesson-10-simple-sentences.svg`.
- Runtime function `send_lesson_infographic` in `bot.py` is intentionally a compatibility no-op. This audit does not enable it or alter runtime delivery.

## Asset-to-lesson content comparison

| Asset | Visible subject | Closest current lesson | Assessment |
|---|---|---|---|
| lesson-01-greetings.svg | Greetings and self-introduction | 1 — کات باش و ماڵاوایی; 2 — ناسین و ناساندنی خۆ | Partial overlap across two lessons; not an exact one-lesson match. |
| lesson-02-letters-sample.svg | Kurdish alphabet and 34 signs | None in Daily Conversation | Belongs to an alphabet/orthography learning context, not this conversation course. |
| lesson-03-daily-words.svg | Everyday expressions, requests and thanks | 3 — پرسیارکردن و وەڵامدانەوە (partial) | Broad vocabulary support; not a precise match to the lesson's question/answer focus. |
| lesson-04-numbers.svg | Numbers | No exact match established from current lesson titles | Do not assign based on title alone. |
| lesson-05-colors.svg | Colors and descriptive sentences | No exact match established | Do not assign based on title alone. |
| lesson-06-home-school.svg | Home, school objects and spatial relations | 5 — ماڵ و شوێنی نیشتەجێبوون (partial) | Home overlap; school and spatial vocabulary broaden beyond the lesson title. |
| lesson-07-family.svg | Family and close people | 4 — خێزان و هاوڕێکان | Strong topical match; verify all labels/examples against lesson 4 before routing. |
| lesson-08-food-drink.svg | Food and drinks | 7 — خواردن و خواردنەوە | Strong topical match; verify all labels/examples against lesson 7 before routing. |
| lesson-09-days-time.svg | Weekdays and time | 9 — کات و ڕێکەوت | Strong topical match; verify date/calendar coverage before routing. |
| lesson-10-simple-sentences.svg | Simple sentences and questions | 3 — پرسیارکردن و وەڵامدانەوە | Partial topical match; not yet an exact match. |

## Design decisions
1. Do not delete, overwrite, rename, or regenerate any of the ten existing SVG assets.
2. Do not enable the no-op infographic sender or add routes based only on filename/title similarity.
3. Treat assets 7, 8, and 9 as strong candidates for lessons 4, 7, and 9 respectively, subject to line-by-line comparison with the complete lesson content.
4. Assets 1 and 3 may be reusable only after deciding whether their content is split across lessons or intentionally supplementary.
5. Asset 2 is not appropriate for the Daily Conversation course based on its visible alphabet content.
6. Assets 4 and 5 have no exact target established in the inspected lesson titles; leave them unassigned.
7. No new image is currently justified. The next design work is content alignment and, only if needed, a targeted correction to a specific asset—not producing images merely to increase the image count.

## Safety and release boundary
This is a documentation-only audit. It changes no lesson text, lesson order, course activation, bot runtime, image routing, database, token, or deployment configuration. No scientific approval is implied by this visual audit.
