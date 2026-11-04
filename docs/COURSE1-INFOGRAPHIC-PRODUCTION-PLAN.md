# Course 1 Infographic Production Plan

Status: preparation only; no learner-facing assets have been replaced and no deployment has been performed.

## Goal

Prepare a consistent, accurate set of 21 infographics for Course 1. The recurring visual identity is the woman character in the original Kejyar image: she is the Kejyar logo/mascot. Do not substitute a newly generated woman, redraw her, or alter her face, clothing, or identity. The original source image must be supplied before embedding the mascot in new artwork.

## Visual and editorial rules

- Use a warm academic palette: forest green, muted gold, and warm cream.
- Use a Kurdish-capable font and preserve Kurdish Unicode characters and right-to-left shaping.
- Add all Kurdish headings, letters, examples, and labels as real text/SVG after the background illustration is made. Never rely on image generation to spell Kurdish.
- Verify every lesson's wording against its source file; do not invent missing source material.
- Keep one shared layout system, but vary diagrams and illustrations to match each lesson's actual subject.
- In letter charts, list each grapheme once. Do not silently normalize disputed lists; reconcile them with the lesson source.
- If vowels and consonants are color-coded, use red for vowels and green for consonants, and make the legend explicit.
- Preserve the original mascot as a separate, unchanged image asset. If the original image is unavailable, leave a clearly marked mascot slot rather than substituting artwork.
- Do not overwrite the existing infographics until the replacement set is reviewed.

## Existing asset audit

The current `assets/infographics/` directory contains ten SVGs named for greetings, letters, daily words, numbers, colors, home/school, family, food/drink, days/time, and simple sentences. These names do not correspond to the current Course 1 sequence in `course_data/arami_course1_manifest.json`. Treat them as legacy/unverified assets; do not assume they are correct Course 1 illustrations.

The existing `lesson-02-letters-sample.svg` is a large SVG sample, but its header and letter-card styling should be reviewed against the current lesson source before reuse. It is not proof that the full Course 1 image set is complete.

## Course 1 asset plan

| Lesson | Manifest title | Proposed visual |
|---:|---|---|
| 1 | پیتەکان و دەنگەکان | Full alphabet overview; separate vowel/consonant groups; examples checked against source |
| 2 | بزوێنەکان | Vowel inventory and sound examples |
| 3 | یاسای بزوێنەکان | Rule map with source-backed examples |
| 4 | بزوێنەکان، نەبزوێنەکان و ئەرکی دووانەی (و) و (ی) | Comparison of vowel/consonant roles, highlighting و and ی |
| 5 | پیتەکانی زمانی کوردی بە نووسینی کوردی و لاتینی | Kurdish-to-Latin grapheme comparison |
| 6 | پیتەکان و دەنگەکان؛ جیاوازیی نێوان ژمارەی پیت و دەنگ | Grapheme-versus-sound comparison |
| 7 | یاسای نووسینی پیتە هاوشێوە دەنگەکان؛ پیتی س = S, s | س / S comparison with verified examples |
| 8 | پیتەکانی ت = T, t و ز = Z, z | ت / T and ز / Z comparison |
| 9 | ئا (الف) | Shape, position, and source-backed examples for ئا / ا |
| 10 | هەمزە (ئـ) | Hamza form and usage examples |
| 11 | پیتی بۆرە، پیتی بزوێنی سەرە و پیتی ژێرە | Three-way visual comparison, only as described by source |
| 12 | پیتی «ی» | Roles and examples of ی |
| 13 | پیتی «و» | Roles and examples of و |
| 14 | پیتی بزرۆکە و هێشوو | Source-backed explanation and word segmentation |
| 15 | پیتی «ل» و «ڵ» | Contrastive comparison of ل and ڵ |
| 16 | پیتی «ر» و «ڕ» | Contrastive comparison of ر and ڕ |
| 17 | پیتی «ڤ» | Shape, sound, and source-backed examples |
| 18 | جیاوازیی نێوان پیتی (هـ) و (ە) | Contrast of هـ and ە |
| 19 | گۆڕانی بێژەی دوو پیتی (ک، گ) لە هەندێک ناوچەی موکریاندا | Regional pronunciation map/diagram; avoid implying universal pronunciation |
| 20 | هێشوو (Cluster) | Cluster structure diagram |
| 21 | بڕگە و هێشوو (Cluster) | Syllable and cluster segmentation |

## Production checklist

For each infographic:

1. Read the exact lesson source.
2. Extract only concepts and examples actually present in that source.
3. Draft the Kurdish text separately from the illustration.
4. Check spelling, character inventory, RTL layout, and font rendering.
5. Place the unchanged original Kejyar woman image in the mascot slot once supplied.
6. Render SVG/PNG and inspect at desktop and mobile sizes.
7. Compare the infographic to the lesson source and record approval.
8. Only after approval, connect it to the bot's lesson delivery.

## Current blocker

The original Kejyar mascot image is not present in the repository's visible infographic assets or in the currently available conversation attachments. The user has clarified that the woman herself is the logo. Therefore, do not fabricate or replace her. Request the original image when the artwork stage begins.

## Safety boundary

This branch is documentation-only. Do not change `main`, production data, Botkeep files, learner progress, environment variables, tokens, or runtime behavior as part of infographic preparation.
