# کۆرسی ٤ — پشکنینی CI workflow و بەڵگەی جێبەجێبوونی regression tests

**بەروار:** 2026-11-09  
**Base SHA:** `5f0df30e6aaa6ac3f37e03dfeb84f3a43a56b5bd`  
**دۆخ:** workflow/source inspection و خوێندنەوەی Actions history؛ هیچ workflowێک trigger نەکراوە.

## ١. ئەنجامی سەرەکی

لە `.github/workflows/python-checks.yml` workflowێکی گشتی هەیە کە:
1. Python 3.12 دامەزرێنێت.
2. `requirements.txt` دامەزرێنێت.
3. `python -m compileall -q .` جێبەجێ دەکات.
4. `python -m unittest discover -s tests -v` جێبەجێ دەکات.

ئەم workflowە لە push بۆ branchەکانی `main`، `fix/**`، `feat/**`، `work/**` و pull request بۆ `main` trigger دەبێت. Permissionی تەنها `contents: read` هەیە.

لە Actions historyدا دوو workflowی سەرەکی لە base SHAی `5f0df30e...` بە سەرکەوتوویی تەواو بوون:
- Python checks: success.
- Orthography course structure tests: success.

بەڵام ئەم success ـە تەنها بەڵگەی ئەوەیە کە suiteی گشتی لەو SHAیەدا سەرکەوتوو بووە؛ بەڵگەی تاقیکردنەوەی runtimeی Telegram، DBی بەرهەمهێنان، یان review-status race نییە.

## ٢. Workflowەکان

### ٢.١ Python checks

فایل: `.github/workflows/python-checks.yml`

- Trigger: push بۆ `main`, `fix/**`, `feat/**`, `work/**`.
- Trigger: pull request بۆ `main`.
- Runner: `ubuntu-latest`.
- Python: `3.12`.
- Dependency: `requirements.txt`.
- Compile: `python -m compileall -q .`.
- Test: `python -m unittest discover -s tests -v`.
- Permission: `contents: read`.

**کەلێنی trigger:** branchەکانی `archive/**` لە push filtersدا نین. ئەمە بۆ archiveی append-only گونجاوە، بەڵام مانای ئەوەیە archive branch بە تەنها push بکرێت CIی گشتی trigger ناکات. ئەگەر پێویست بوو archiveێک CIی بگرێتەوە، PR بۆ main یان triggerی جیاواز پێویستە؛ هیچ PR یان workflowێک لەم audit ـەدا دروست/trigger نەکراوە.

### ٢.٢ Orthography course structure tests

فایل: `.github/workflows/orthography-course-structure.yml`

- Trigger: push بۆ `main` و `fix/kejyarbot-stability-2026-10-25`.
- Trigger: PR بۆ هەمان دوو branch.
- Trigger: `workflow_dispatch`.
- Python 3.12.
- تەنها `tests/test_orthography_course_structure.py` جێبەجێ دەکات.

**سنوور:** ئەمە workflowی تایبەتی Course4 نییە؛ لە ناوەڕۆکدا orthography course structure test ـە، نابێت وەک گەڕاندنەوەی regression suiteی grammar course4 حساب بکرێت.

## ٣. Actions historyی پشتڕاستکراو

لە GitHub Actions historyی کۆتا ١٠ runی خوێندراودا:
- `Python checks` — push بۆ `main`, SHA `5f0df30e6aaa6ac3f37e03dfeb84f3a43a56b5bd` — completed/success.
- `Orthography course structure tests` — push بۆ `main`, هەمان SHA — completed/success.
- هەردوو workflow لە PRی `feat/course4-clean-port-main-20261106`یشدا success بوون.

بەڵام runی Actionsی نوێتر لەو base SHAیە بۆ branchەکانی archive لە historyی خوێندراودا نەدۆزرایەوە. هیچ runێکی نوێ لەم قۆناغەدا دروست نەکرا.

## ٤. Test suite و Course4

لە treeی repositoryدا ٤١ فایل testی Python دیارە، لەوانە:
- `tests/test_course4_grammar_runtime.py`
- `tests/test_bot_quiz_callbacks.py`
- `tests/test_database.py`
- `tests/test_activated_courses.py`
- `tests/test_orthography_quiz_adapter.py`
- `tests/test_quiz_bank_quality.py`

Workflowی Python checks بە `unittest discover -s tests -v` هەموو test filesی پەیوەندیدار بە discovery دەگرێتەوە، بەڵام Actions logی کۆن تەنها دەرئەنجامی success لێرەدا بەردەستە؛ لەم audit ـەدا test name-by-name output یان test countی runی کۆن پشتڕاست نەکراوەتەوە.

## ٥. کەلێن و هەنگاوە پێشنیارکراوەکان

1. **CIی review-gate regression:** لە `test_course4_grammar_runtime.py` و `test_bot_quiz_callbacks.py` testە نوێکانی pending start، pending menu، status change mid-quiz و finalization زیاد بکرێن.
2. **Coverageی atomic policy:** ئەگەر approval لە DBدا جێگیر کرا، unit/integration testی approval revoke و reward transaction زیاد بکرێت.
3. **CI visibility:** لە داهاتوودا test count و نامی Course4 regression cases لە logدا ڕوون بکرێتەوە؛ تەنها successی suite بۆ auditی ژێرەکی بەس نییە.
4. **Archive branch:** ئەگەر مەبەست تەنها پاراستنی audit ـە، triggerنەبوونی archive branch عادییە. ئەگەر پێویستە archive branchەکانیش CIیان هەبێت، workflow filter یان PRی تایبەت بە ڕێگەپێدانی خاوەن پڕۆژە داڕێژرێت.
5. **Manual verification:** پێش هەر deployێک، CIی base و PRی گۆڕانکاری پێویستە success بن؛ ئەمە جێگرەوەی UATی Telegram/DB نییە.

## ٦. سنووری ئەم audit ـە

- Workflow YAML، test inventory و Actions history خوێندرانەوە.
- هیچ `pytest` یان `unittest` لە container/local run نەکرا.
- هیچ GitHub Actions workflow_dispatch یان PRێک trigger نەکرا.
- هیچ کۆد، workflow، test، DB، main، Telegram یان Botkeep نەگۆڕدرا.
- دەرئەنجامی successی GitHub Actions لە base SHAی دیاریکراوە؛ نابێت بە دەرئەنجامی runی نوێی ئەم audit ـە تێبگەین.
