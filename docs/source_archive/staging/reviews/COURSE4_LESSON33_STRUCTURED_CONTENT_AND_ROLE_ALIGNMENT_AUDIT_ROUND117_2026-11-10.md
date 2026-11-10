# کۆرسی ٤ — پشکنین و کاندیدی structured dataی وانەی ٣٣
## Round 117 — 2026-11-10

- Source: `course_data/grammar_course4_lessons.json`
- Source blob SHA: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
- Lesson: 33 — بکەر و کردار: ئەرکی ڕێزمانی و ڕۆڵی واتایی
- Candidate: `docs/source_archive/staging/candidates/COURSE4_LESSON33_STRUCTURED_CONTENT_CANDIDATE_ROUND117_2026-11-10.json`
- دۆخی candidate: `inactive_candidate_not_approved`

## ناوەڕۆکی candidate
- ٦ خاڵی سەرەکی
- ٦ نموونەی ڕێکخراو
- ٥ ڕاهێنانی سەرچاوە پارێزراو
- ١ کۆمەڵەی comprehensionی پارێزراو
- ٥ پرسیاری کویز بە ٤ هەڵبژاردە، answer indexی دروست و ڕوونکردنەوە

## پشکنینی زانستی
1. Subject لە Agent جیا کراوەتەوە: Subject ئەرکی ڕێزمانییە؛ Agent ڕۆڵێکی واتایییە.
2. لە ڕستەی نەکارا `پەنجەرەکە شکێنرا`دا پەنجەرەکە وەک بکەر هەڵسەنگێنراوە، بەڵام ئەنجامدەری کردار لە ڕستەکەدا دیاری نەکراوە.
3. لە `خانووەکە سووتا`دا نابێت ئەنجامدەری ئەنقەستی بە تەنها لەسەر بنەمای بکەر دابنرێت.
4. کردار دەتوانێت ڕووداو یان دۆخیش دەرببڕێت؛ پێویستی بە بەرکار هەمیشە نییە.
5. نموونەی `فەرزانە شووتی دەخوات` لە سەرچاوە پارێزراوە؛ وشەی `شووتی` لە candidateدا بەبێ دەستکاری هێڵراوەتەوە، بەڵام پشتڕاستکردنەوەی شێوەزاری/واتایی لە پشکنینی گشتیی زماندا پێویستە.

## پاراستن و validation
- `source_markdown` پارێزراوە.
- `source_path` پارێزراوە.
- `exercises` و `comprehension` وەک خۆیان پارێزراون.
- Quiz: ٥ دانە؛ هەر یەکە ٤ هەڵبژاردە، answer indexی valid و explanationی ناپوچەڵ.
- Candidate JSON parse و schema validation پێویستە لە دوای نووسین دووبارە بکرێتەوە.
- هیچ runtime، loader، source JSON، quiz bank، student data یان Botkeep دەستکاری نەکراوە.
- هیچ merge، deployment، sync یان restart ئەنجام نەدراوە.

## بڕیار
STRUCTURED CANDIDATE CREATED — TECHNICAL VALIDATION PENDING — NOT RUNTIME-READY.
