# KejyarBot — Append-only image asset audit

- Audit date: 2026-11-13
- Audit basis: repository branch `release/main-based-reconciled-2026-11-11`
- Audited source commit: `12d7fa1c41aa7e083ffa2072acbae2fd395fc2ee`
- Purpose: preserve the read-only findings and the user's clarified intended image policy.
- This record is additive. It does not replace lesson sources, manifests, runtime code, tests, assets, or prior audit records.

## 1. User-confirmed intended policy

The user clarified on 2026-11-13:

- Introductory Kurdish orthography Course 1, Lessons 1–7: one teaching image for each lesson.
- Lesson 5 of that course is included and has one image.
- Latin orthography Course 1, Lesson 1: one teaching image.
- Expected total: **8 images**.
- Other lessons/courses are not to receive images under this stated policy.

This is the current user intent. It supersedes older repository documentation that described Lesson 5 as intentionally text-only, but it does not itself identify or authorize activation of any particular legacy asset.

## 2. Current checked-in raster inventory

At audited commit `12d7fa1c41aa7e083ffa2072acbae2fd395fc2ee`, the repository tree contains seven raster image files:

| File | Current code mapping / verified identification |
|---|---|
| `assets/course1_infographics/lesson_01.png` | Arami introductory orthography Lesson 1 |
| `assets/course1_infographics/lesson_02.png` | Arami introductory orthography Lesson 2 |
| `assets/course1_infographics/lesson_03.png` | Arami introductory orthography Lesson 3 |
| `assets/course1_infographics/lesson_04.png` | Arami introductory orthography Lesson 4 |
| `assets/course1_infographics/lesson_06.png` | Arami introductory orthography Lesson 6 |
| `assets/course1_infographics/lesson_07.png` | Arami introductory orthography Lesson 7 |
| `photo_2026-10-27_00-13-52.jpg` | Visually inspected: Kurdish alphabet / letters-and-sounds teaching graphic labelled Lesson 1; duplicates the subject area of Arami Lesson 1, not Latin Course 1 Lesson 1 |

The JPG was fetched as base64 from the exact audited commit and visually inspected. Its heading is `پیتەکان و دەنگەکان`, and it is labelled `وانەی ١`. It is not a verified Latin-alphabet lesson image and must not be assigned to Latin Course 1 Lesson 1.

The six PNGs have the exact lesson-specific paths and are the six images mapped by the current Arami Course 1 sender. No `lesson_05.png` exists in the audited tree.

## 3. Legacy vector inventory — do not reactivate

The tree also contains ten SVGs under `assets/infographics/`:

- `lesson-01-greetings.svg`
- `lesson-02-letters-sample.svg`
- `lesson-03-daily-words.svg`
- `lesson-04-numbers.svg`
- `lesson-05-colors.svg`
- `lesson-06-home-school.svg`
- `lesson-07-family.svg`
- `lesson-08-food-drink.svg`
- `lesson-09-days-time.svg`
- `lesson-10-simple-sentences.svg`

These belong to the older 22-lesson orthography course/legacy infographic set. For example, `lesson-05-colors.svg` explicitly labels itself `وانەی ٥: ڕەنگەکان`; it is not the current Arami Course 1 Lesson 5 image. These SVGs are **not** substitutes for the two missing images and must not be reactivated, reassigned, or delivered without explicit fresh authorization and source verification.

Thus the tree has 17 files with image extensions in total (7 raster + 10 legacy SVG), but only six currently mapped Arami teaching PNGs are confirmed for the user's present eight-image policy.

## 4. Current runtime and historical policy conflict

At the audited commit, `arami_course1_telegram.py` defines:

- `COURSE1_INFOGRAPHIC_LESSONS = frozenset({1, 2, 3, 4, 6, 7})`
- `lesson_infographic_path()` returns no image for Lesson 5.
- `send_lesson_infographic()` sends the six mapped PNGs.
- The sender is called by the custom Arami Course 1 lesson flow.

The corresponding test file explicitly checks the six-image mapping and expects Lesson 5 to remain text-only. These tests describe the current checked-in behavior, not the user's latest intended policy.

Historical PR #79 / merge commit `213cf75c6c0fab4bf5c8eda8bac40a753f713ba0` explicitly restored six infographics for Lessons 1, 2, 3, 4, 6, and 7 and documented Lesson 5 as text-only. This historical policy conflicts with the user's later clarification and must not be treated as the current target requirement.

The Latin runtime module `latin_course_runtime.py` contains no image/infographic/reply-photo mapping. The Latin Course 1 source file identifies Lesson 1 as `Elfabeya Kurmancî ya Latînî`, but the checked-in source and runtime search found no image asset assignment for that lesson.

## 5. Outstanding asset identification

Two user-required images remain unverified in the current tree:

1. Arami introductory orthography Course 1, Lesson 5.
2. Latin orthography Course 1, Lesson 1.

The JPG is not a valid identified candidate for the Latin lesson; its visible content is a Kurdish-script alphabet lesson labelled Lesson 1. No other raster file in the current tree is available as a verified candidate.

No file named `lesson_05.png` exists in the audited tree, and no Latin Course 1 Lesson 1 image path is mapped in the current runtime.

## 6. Historical provenance

- JPG `photo_2026-10-27_00-13-52.jpg` was added in commit `341c6b20437a0b1cd90826fea34d114a6fbe7422` with generic message “Add files via upload”; commit metadata does not identify its lesson mapping.
- Six current Course 1 PNGs were introduced/restored in commit `213cf75c6c0fab4bf5c8eda8bac40a753f713ba0`.
- Ten legacy SVGs were introduced in commit `445d4dbe6bd9c317db54cf2d20a0d1254aab8eb6`, associated with the older 22-lesson course work.

## 7. Safety and change record

- This audit performed repository reads and image inspection only before this archival commit.
- No lesson text, manifest, image asset, runtime mapping, test, bot configuration, database, or deployment state was changed.
- No tests were run as part of this audit.
- No Botkeep action, deployment, synchronization, restart, or live Telegram test was performed.
- No legacy image or inactive feature was reactivated.
- This new Markdown file is an append-only audit record on a separate audit branch created from the exact audited source commit. The release branch and PR #152 head were not moved by this archival action.
- Next safe step: locate the original approved source files for the two missing images, verify their lesson identities, and only then consider a separately authorized implementation change. Do not manufacture mappings from filenames or reactivate legacy SVGs.
