# کۆرسی ٤ — پشکنینی dependency، deployment و پاراستنی database

**بەروار:** 2026-11-09  
**Base:** main — source snapshotی خوێندراو  
**دۆخ:** static configuration audit؛ هیچ deployment، restart یان runtime operation نەکراوە.

## ١. پوختەی دەرئەنجام

- requirements.txt تەنها python-telegram-bot>=22,<23 دەگرێتەوە؛ dependencyی سەرەکییەکە version rangeی فراوانە، lock fileی دیاریکراو نەدۆزرایەوە.
- README Python 3.10+ دەڵێت، بەڵام CI بە Python 3.12 تاقی دەکاتەوە؛ production runtime version لە deployment manifestدا دیاری نەکراوە.
- هیچ Dockerfile، Procfile، Render/Railway/Fly manifest، runtime.txt یان deployment workflow لە treeی mainدا نەدۆزرایەوە.
- بۆت بە polling کار دەکات، نە webhook.
- token لە TELEGRAM_BOT_TOKEN یان BOT_TOKEN وەردەگرێت؛ host environment بەسەر .envدا پێشینەی هەیە.
- SQLite database بە ناوی kejyar.db لە هەمان directoryی database.py دروست دەبێت؛ persistent volume لە configurationدا بەڵگەی نییە.
- .env و فایلەکانی SQLite لە .gitignoreدا ڕێگرییان لێکراوە.
- startup پێش polling runtime validation و init_db() ئەنجام دەدات.

## ٢. Dependency و Python version

requirements.txt تەنها python-telegram-bot>=22,<23 دەگرێتەوە.

README:
- Python 3.10 یان نوێتر.
- python -m pip install -r requirements.txt.
- python bot.py.

CI:
- Python 3.12.
- pip install -r requirements.txt.
- compileall و unittest discovery.

هەڵسەنگاندن:
- Rangeی PTB 22.x لە CIدا بە packageی نوێترین گونجاو لەو rangeە install دەکرێت؛ lock/reproducible dependency resolution نییە.
- هیچ constraints.txt، requirements.lock، poetry.lock یان uv.lock لە treeی دیاریکراودا نەدۆزرایەوە.
- README 3.10+ و CI 3.12 هەڵسەنگاندنی یەکسان نین؛ لە sourceدا deployment Python version پشتڕاست نەکراوەتەوە.
- پێش deploy پێویستە versionی Python و dependency resolutionی production بە شێوەی reproducible دیاری بکرێت؛ بێ بڕیاری خاوەن پڕۆژە dependency pin مەکرێت.

## ٣. Deployment و process model

- bot.py لە main()دا Application.builder().token(token).post_init(...).build() دروست دەکات.
- Handlerەکان زیاد دەکرێن و لە کۆتاییدا app.run_polling() بانگ دەکرێت.
- webhook mode، web server، health endpoint، process supervisor، container entrypoint یان deployment script لە سەرچاوەی پشکنراودا نییە.
- startup sequence: validate_activated_course_runtime() → init_db() → token validation → Telegram Application → handlers → polling.
- چونکە DB initialization پێش token validationە، tokenی نەبوون هێشتا دەتوانێت DB file دروست بکات؛ ئەمە تەنها کاری پاکی startup ـە، نە مەترسییەکی بەرز.

**کەلێنی deployment:** repo بە تەنها نیشان نادات کە host چۆن restart، single-instance، persistent storage یان graceful shutdown بەڕێوە دەبات. نابێت host یان Botkeep لە گومانەوە دیاری بکرێت.

## ٤. SQLite persistence

database.py:
- BASE_DIR = Path(__file__).resolve().parent.
- DB_NAME = str(BASE_DIR / "kejyar.db").
- SQLite لە هەمان directoryی code fileدا دەنووسێت.
- init_db() schema دروست دەکات و completed_quizzes بۆ DBی کۆن migration دەکات.
- transactionەکانی reward بە BEGIN IMMEDIATE پارێزراون.
- connectionەکان لە finallyدا داخراون.

.gitignore:
- .env
- kejyar.db
- *.sqlite، *.sqlite3، WAL/SHM sidecars
- .venv/، venv/، cache و pyc

### مەترسیی persistence
ئەگەر host filesystemی ephemeral بێت یان app لە containerی نوێدا بکرێتەوە، DBی local دەتوانێت لەدەست بچێت یان لە instanceەکاندا هاوبەش نەبێت. لە repositoryدا persistent volume mount/path یان backup schedule دیاری نەکراوە. ئەمە بەڵگەی ئەوە نییە کە production DB لەدەستچووە؛ تەنها مانای ئەوەیە configی host لە repoدا بەردەست نییە.

### پێش deploy پێویستە
1. host و storage model پشتڕاست بکرێتەوە.
2. pathی kejyar.db لە persistent writable volumeدا بێت.
3. backup و restore testی DB هەبێت.
4. ئەگەر multiple instances پێویستە، SQLite local-file architecture دووبارە هەڵبسەنگێنرێت؛ local DB بە خۆی shared database نییە.
5. پێش migration یان moveکردنی DB، backupی verified و rollback plan هەبێت.

## ٥. Secrets و environment

- bot.py .env بە خوێندنەوەی سادە parse دەکات؛ packageی python-dotenv پێویست نییە.
- os.environ.setdefault واتە host env لە .env پێشینەی هەیە.
- token: TELEGRAM_BOT_TOKEN یان legacy BOT_TOKEN.
- README ئاگاداری دەدات token لە GitHub نەخرێت.
- .env لە .gitignoreدا هەیە.

**پێشنیار:** production token تەنها لە secret manager/environmentی host دابنرێت؛ هیچ tokenێک لە archive، test output یان logدا دانەنرێت. هیچ secret scan یان rotate operation لەم audit ـەدا نەکرا.

## ٦. Risk register

| بابەت | دۆخی بەڵگە | گرنگی |
|---|---|---|
| Dependency lock | lock file نەدۆزرایەوە | مامناوەند |
| Python production version | deployment manifest نییە | مامناوەند |
| Persistent SQLite volume | لە repoدا دیار نییە | بەرز پێش deploy |
| Multi-instance safety | shared DB architecture نییە | بەرز ئەگەر multi-instance |
| Polling process supervision | host config نەدۆزرایەوە | مامناوەند |
| Token secret handling | env/.env pattern هەیە؛ .env gitignored | باش، بەڵام host نامەزانراوە |
| Backup/restore | schedule و test نەدۆزرایەوە | بەرز بۆ data durability |

## ٧. هەنگاوە پێشنیارکراوەکان

1. خاوەن پڕۆژە hostی ڕاستەقینە و شێوازی deploy پشتڕاست بکاتەوە؛ repo بە تەنها ناوی host نادات.
2. persistent volume و pathی DB پشتڕاست بکرێتەوە؛ پێش deploy backup/restore test بکرێت.
3. Python versionی production لەگەڵ CI یەکسان بکرێت.
4. dependency lock/constraints بە بڕیاری خاوەن پڕۆژە زیاد بکرێت و CI لەسەر هەمان dependency set بڕوات.
5. single-instance policy بۆ polling bot ڕوون بکرێتەوە؛ دوو pollerی هەمان token لە دوو instanceدا نابێت بە بێ دیزاینی ڕوون هەڵبکرێن.
6. runtime smoke test بە test bot/tokenی جیاواز و DBی staging، لە ژینگەیەکی جیاواز لە production، دیزاین بکرێت.

## ٨. سنووری کار

- main source، README، workflow، requirements، .gitignore و database configuration خوێندرایەوە.
- هیچ dependency install نەکرا.
- هیچ test یان runtime process نەکرا.
- هیچ database، secret، host، Botkeep، Telegram، server یان deployment دەستکاری نەکرا.
- هیچ گۆڕانکارییەک بۆ main نەکرا.
