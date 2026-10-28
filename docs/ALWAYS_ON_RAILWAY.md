# بەردەوام چالاککردنی ڕۆبۆتی کەژیار لە Railway

ئەم ڕێکخستنە بۆ worker ـێکی بەردەوامە، نەک web service. بۆت بە Telegram long polling کار دەکات؛ نابێت دوو replica بە هەمان تۆکن polling بکەن.

## پێش مەبەست

- ئەم ڕێنماییە تەنها بۆ برانچی تاقیکردنەوە/ئامادەکاریی دیپلۆیە. `main`، PR #4، بۆتی بەرهەمهێنان یان هیچ خزمەتگوزارییەکی بەرهەمهێنان بەبێ ڕەزامەندیی ڕوونی خاوەن پڕۆژە مەگۆڕە.
- هەژماری Railwayی پێشووی بەکارهێنەر Trial ـەکەی کۆتایی هاتووە؛ پێش چالاککردنی worker پێویستە پلانی چالاک و بەرامبەر/بودجەی پەسەندکراو هەبێت.
- تۆکنی بۆتی تاقیکردنەوە بەکاربهێنە بۆ smoke test؛ تۆکنی بەرهەمهێنان مەخە ناو Git یان log.
- `KEJYAR_ENABLE_DYNAMIC_SPEECH=false` بهێڵەوە.

## ڕێکخستنی Railway

1. لە Railway service ـێکی Python worker لە repository ـەکە دروست بکە، بەڵام تا پشکنین و پەسەندکردنی deployment، auto-deploy لە `main` چالاک مەکە.
2. فایلەی `railway.toml` فرمانی دەستپێکردن، restart policyی `ALWAYS` و یەک replica دیاری دەکات؛ Railway هەوڵ دەدات worker دووبارە هەڵبکاتەوە ئەگەر بوەستێت.
3. لە Settings ـی service ـەکە، Volume ـێک زیاد بکە و Mount Path ـەکە بکە بە `/data`. بێ volume، داتابەیسی SQLite لە نێوان redeploy/restart ـەکاندا دەتوانێت لەدەست بچێت.
4. لە Variables ـی service ـەکە دابنێ:
   - `TELEGRAM_BOT_TOKEN` = تۆکنی بۆتی تاقیکردنەوە (لە deploymentی بەرهەمهێناندا تەنها دوای ڕەزامەندی، تۆکنی بەرهەمهێنان).
   - `KEJYAR_DB_PATH=/data/kejyar.db`
   - `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`
5. بۆتەکە بە تۆکنی تاقیکردنەوە لە ژینگەی جیاوازدا deploy بکە و لە logs پشتڕاستی بکەوە کە Telegram authentication سەرکەوتووە و polling دەستی پێکردووە.
6. لە Telegram، `/start`، کردنەوەی کۆرسی چالاک، تەواوکردنی وانە، کویز و پاراستنی XP/progress تاقی بکەرەوە. دوای restart/redeploy دڵنیابە پێشکەوتنی خوێندکار هەر ماوەتەوە.
7. دڵنیابە تەنها یەک worker بۆ ئەو تۆکنە چالاکە. ئەگەر دوو worker هەمان تۆکن بەکاربهێنن، polling دەتوانێت conflict دروست بکات.

## دۆخی ئێستا

- ئەم فایلی config و پشتگیریی DB path تەنها ئامادەکارییە؛ خۆی سرویس دروست ناکات و بۆت deploy ناکات.
- Railway service/volume/variables لە dashboard پێویستیان بە دانان هەیە؛ ئەمانە لە repository ـەوە ناتوانرێن پشتڕاست بکرێنەوە.
- چالاکبوونی هەمیشەیی تەنها دوای deployی سەرکەوتوو، log ـی دەستپێکردن و smoke testی Telegram پشتڕاست دەکرێتەوە.
