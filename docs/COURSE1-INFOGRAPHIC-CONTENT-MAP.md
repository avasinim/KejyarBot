# Course 1 — 21-lesson infographic content map

Status: production specification only; no lesson text, runtime code, database, deployment, or production assets changed.

## Locked visual identity

- Mascot: use the user's supplied Kejyar woman portrait unchanged. Do not redraw, regenerate, stylize, retouch, or substitute her.
- Brand signature: show **KejyarBot@** and the Kejyar name consistently. Keep the mascot portrait as the identity mark.
- Master reference: follow the user's supplied dashboard image for its warm cream canvas, deep forest-green structure, restrained gold accents, clear cards, balanced whitespace, and academic/educational hierarchy.
- Exclude the top course-label/header panel that says **«ڕێنووسی سەرەتایی»** in the reference. Do not reproduce it as a repeated lesson-identity banner.
- Keep a compact lesson-specific title and lesson number in the content area; do not add a second course banner.
- Kurdish text must be editable real text, not AI-rendered lettering. Use a Kurdish-capable font with correct Arabic-script shaping, RTL paragraph direction, correct punctuation placement, and careful glyph/diacritic proofing. For visually confusable Kurdish-specific glyphs, verify the actual rendered shape rather than trusting the font-family name; the letter **پ** must visibly retain its three dots below. In the approved Lesson 1 draft, use the Noto Kufi Arabic glyph fallback specifically for **پ** because the initial Noto Sans Arabic rendering did not show the expected dot structure.
- AI-generated decorative art may support a lesson, but may not supply Kurdish words, alter the mascot, or introduce unverified linguistic claims.
- Use exact lesson source wording, examples, letter inventory, and scope. Never invent examples to fill visual space. Where a source is incomplete or ambiguous, mark the visual draft for review rather than filling the gap.

## Shared layout system

1. Header strip: lesson number + exact lesson title; KejyarBot@ brand signature kept visible without the removed course banner.
2. Main teaching area: one large visual explanation, tailored to the lesson.
3. Example area: source-derived examples only, set in large Kurdish type with RTL alignment.
4. Small “یادەوەری” or “تێبینی” card only where the source itself contains a note or important qualification.
5. Footer: KejyarBot@; no unrelated course-title banner.
6. Keep contrast, spacing, line-height, and font size sufficient for mobile Telegram viewing. Avoid crowded multi-column Kurdish text.

## Lesson-by-lesson visual direction

| # | Exact lesson title | Main visual treatment | Source/content guardrail |
|---:|---|---|---|
| 1 | پیتەکان و دەنگەکان | Two-part alphabet board: consonants in green, vowels in red; separate callouts for written letter vs heard sound; small dual-role cards for و and ی; a distinct short /i/ note. | Use only `arami_course1_lesson_01_content.json`. It states 34 letters and 8 vowels in this lesson's classification. Preserve its exact letter inventory and eight-vowel explanation; do not substitute another alphabet table. |
| 2 | بزوێنەکان | Airflow/vocal-tract concept illustration paired with a vowel-in-word listening sequence; examples displayed as separate source word cards. | Use only the lesson 2 source. Its examples are سەر، گەرما، هێمن، خۆر، کورد، گیان. Distinguish written sign from vowel sound. |
| 3 | یاسای بزوێنەکان | A five-step analysis pathway: read → list written letters → pronounce → identify vowel sounds → compare spelling and sound; example cards for کورد، خۆر، هێمن، گیان. | Preserve the source's caution: orthographic rules and phonological behavior are related but not identical; do not generalize from one example. |
| 4 | بزوێنەکان، نەبزوێنەکان و ئەرکی دووانەی (و) و (ی) | Split comparison board: vowel vs consonant roles, with separate paired role panels for و and ی. | Source is `arami_course1_lesson_04_source.md`. The source has known missing opening sections 1–2 in the audit history; do not reconstruct missing material. |
| 5 | پیتەکانی زمانی کوردی بە نووسینی کوردی و لاتینی | Aligned Kurdish/Latin comparison table with clear one-to-one or many-to-one visual links only where the source explicitly provides them. | Use lesson 5 source and its exact mapping; never infer Latin equivalents. |
| 6 | پیتەکان و دەنگەکان؛ جیاوازیی نێوان ژمارەی پیت و دەنگ | Side-by-side “what is written / what is heard” diagram, plus a source-backed counting example. | Use received lesson 6 source. Keep grapheme/letter and sound counts distinct; do not add a count rule not in the source. |
| 7 | یاسای نووسینی پیتە هاوشێوە دەنگەکان؛ پیتی س = S, s | Large س ↔ S/s correspondence card and source examples; show the writing relationship as a mapping, not a claim that all sounds/letters are universally identical. | Exact mappings and examples must come from lesson 7 source. |
| 8 | پیتەکانی ت = T, t و ز = Z, z | Two parallel letter panels: ت ↔ T/t and ز ↔ Z/z, each with its own verified examples. | Use combined lesson 8 source only. Keep both mappings visually separate and faithful to source. |
| 9 | ئا (الف) | Large ا / ئا form study, positional/word examples arranged as source provides; clear writing-form focus. | Use lesson 9 source; do not invent positional variants or example words. |
| 10 | هەمزە (ئـ) | Shape-and-placement study of ئـ with source-backed word examples and a small form comparison if present in source. | Use lesson 10 source; preserve exact terminology and forms. |
| 11 | پیتی بۆرە، پیتی بزوێنی سەرە و پیتی ژێرە | Three-column contrast board with large letter/sign forms and source examples; clear labels and no decorative reinterpretation. | Use lesson 11 source exactly. Do not confuse the three named categories or add alternate definitions. |
| 12 | پیتی «ی» | Central ی glyph with clearly separated source-verified roles/examples; role branches only where the source states them. | Use lesson 12 source; do not import examples or rules from another dialect/source. |
| 13 | پیتی «و» | Central و glyph with source-verified roles/examples; distinguish the written character from its different sound values only as described by source. | Use lesson 13 source; no extra generalizations. |
| 14 | پیتی بزرۆکە و هێشوو | Sound/letter distinction plus a segmented cluster diagram using the exact source examples; keep /i/ notation typographically distinct. | Use lesson 14 source; do not imply that the short vowel has a dedicated Kurdish alphabet letter unless the source says so. |
| 15 | پیتی «ل» و «ڵ» | Large paired contrast cards ل / ڵ with source words aligned for direct comparison. | Use lesson 15 source; preserve all distinctions and source spelling. |
| 16 | پیتی «ر» و «ڕ» | Paired ر / ڕ comparison with source words; use spacing and labels to prevent glyph confusion. | Use lesson 16 source; never conflate the two letters or reassign recordings. |
| 17 | پیتی «ڤ» | Large ڤ letter study with pronunciation/word examples and a small contextual note if the source includes one. | Use `arami_course1_lesson_16_v_source.md`; source examples only. |
| 18 | جیاوازیی نێوان پیتی (هـ) و (ە) | Clear two-glyph comparison, with separate sound/position/example rows as supported by source. | Use lesson 17 source; do not visually imply هـ and ە are interchangeable. |
| 19 | گۆڕانی بێژەی دوو پیتی (ک، گ) لە هەندێک ناوچەی موکریاندا | Carefully bounded regional pronunciation map/diagram: mark the Mukriani scope explicitly and show the source's contrast without presenting it as universal Kurdish pronunciation. | Use lesson 18 source; retain the qualification “لە هەندێک ناوچەی موکریاندا”. |
| 20 | هێشوو (Cluster) | Cluster structure diagram with letter sequence segmentation and exact source examples; distinguish a cluster from a syllable if source does. | Use lesson 19 source; do not invent phonotactic rules. |
| 21 | بڕگە و هێشوو (Cluster) | Combined syllable/cluster segmentation: layered blocks showing boundaries and the exact source examples. | Use lesson 20 source; preserve the source's own segmentation and definitions. |

## Draft production status

- Lesson 1: first visual draft prepared locally; user identified a Kurdish glyph rendering issue for **پ**. The rendering QA rule now requires visual confirmation that its three dots are below the letter.
- Lesson 2: first visual draft prepared from `course_data/arami_course1_lesson_02_vowels_source.md`. It uses the exact six source examples: سەر، گەرما، هێمن، خۆر، کورد، گیان. The diagram illustrates the source definition of vowel airflow and distinguishes written letter from heard vowel sound. This is a review draft, not a final approved asset.
- Lesson 3: first visual draft prepared from `course_data/arami_course1_lesson_03_vowel_rules_source.md`. It distinguishes orthographic rules from phonological behavior, visualizes the five source-prescribed analysis steps, includes the source caution against equating letter counts with sound/vowel counts, and uses the four source examples: کورد، خۆر، هێمن، گیان. This is a review draft, not a final approved asset.
- No image has been added to the live runtime or deployed. Review and approval are required before wiring assets into Telegram delivery.

## Production QA gate for every infographic

- [ ] Original Kejyar mascot portrait is used unchanged wherever the mascot appears.
- [ ] KejyarBot@ and Kejyar name are present; no unrelated brand.
- [ ] The removed «ڕێنووسی سەرەتایی» course-banner panel is absent.
- [ ] Every Kurdish string is editable text, RTL-shaped, and proofread against the source.
- [ ] Kurdish-specific glyphs are visually checked after rendering; **پ** has three dots below, and no font fallback changes a letter's identity.
- [ ] All lesson examples and letter forms match the exact lesson source.
- [ ] No AI-generated Kurdish text or unverified linguistic claims.
- [ ] Lesson-specific visual treatment is clear at mobile size.
- [ ] No clipping, collisions, malformed ligatures, reversed punctuation, or mixed RTL/LTR ordering.
- [ ] User review completed before final release.

## Current implementation boundary

This file is a content/design map only. The user's two image references are supplied in the conversation; this commit does not embed or modify those image files. No runtime wiring, Telegram send behavior, database, learner progress, Botkeep configuration, production token, or deployment is changed.
