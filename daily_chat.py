"""Simple, safe Kurdish daily-conversation practice for KejyarBot."""

import random
import re
import unicodedata


PROMPTS = (
    "با گفتوگۆیەکی سادە دەست پێ بکەین. ئەمڕۆ چۆنیت؟",
    "باشە، با فێری دەربڕینێکی ڕۆژانە ببین. دەتەوێت لە سڵاوکردنەوە دەست پێ بکەین یان لە بازاڕ؟",
    "من ئامادەم یارمەتیت بدەم. بە کوردی وەڵام بدەرەوە؛ ئەگەر هەڵەیەک هەبوو، بە نەرمی ڕاستت دەکەمەوە.",
)

def _clean(text: str) -> str:
    text = unicodedata.normalize("NFC", text).casefold().strip()
    text = re.sub(r"[؟?!.,،؛:…]+", " ", text)
    return " ".join(text.split())


def reply_to_daily_message(text: str, state: dict | None = None) -> str:
    """Return a short Sorani Kurdish reply based on common daily-chat intents."""
    clean = _clean(text)
    state = state if state is not None else {}

    if not clean:
        return "تکایە وشە یان ڕستەیەک بنووسە تا گفتوگۆکەمان بەردەوام بکەین."

    if any(word in clean for word in ("وەستان", "کۆتایی", "دەربچم", "منووی سەرەکی")):
        state["daily_chat_mode"] = False
        return "باشە، گفتوگۆکەمان لێرە کۆتایی پێ دێت. هەر کاتێک بتەوێت دەتوانیت دووبارە دەستی پێ بکەیت. 🌷"

    if any(word in clean for word in ("سڵاو", "بەخێربێ", "ڕۆژباش", "ئێوارەباش", "شەوباش")):
        state["daily_chat_turns"] = state.get("daily_chat_turns", 0) + 1
        return "سڵاو، بەخێربێیت! 🌷 چۆنیت ئەمڕۆ؟ دەتوانین بە کوردی گفتوگۆ بکەین."

    if any(phrase in clean for phrase in ("چۆنی", "چۆنیت", "باشی", "حاڵت چۆنە")):
        return "سوپاس، باشم و ئامادەم یارمەتیت بدەم. تۆ چۆنیت؟ ئەمڕۆ چی کردووە؟"

    if any(phrase in clean for phrase in ("ناوت چی", "کێیت", "تۆ کێی")):
        return "من کەژیارم، یاریدەدەری فێربوونی زمانی کوردی. دەتوانین وانە بخوێنینەوە و گفتوگۆی ڕۆژانە ڕاهێنان بکەین. 🌱"

    if any(word in clean for word in ("سوپاس", "دەستخۆش", "زۆر باش")):
        return "سەرچاوە، بە خۆشییەوە! 😊 ئامادەیت بە ڕستەیەکی تری ڕۆژانە ڕاهێنان بکەین؟"

    if any(word in clean for word in ("ببورە", "لێم خۆش بە")):
        return "هیچ کێشە نییە. 🌷 لە گفتوگۆدا هەڵەکردن بەشێکە لە فێربوون."

    if any(word in clean for word in ("خواحافیز", "خوات لەگەڵ", "دواتر دەبینم")):
        state["daily_chat_mode"] = False
        return "خواحافیز، بە خۆشی و تەندروستی! هەر کاتێک بتەوێت کەژیار لێرەیە. 👋"

    if any(word in clean for word in ("بازاڕ", "کڕین", "نرخ", "پارە")):
        return "لە بازاڕدا دەتوانیت بڵێیت: «تکایە، ئەمە چەندە؟» یان «من ئەمە دەمەوێت». ئێستا تۆ وەک کڕیار یەک ڕستە بنووسە."

    if any(word in clean for word in ("خواردن", "نان", "برنج", "ئاو", "چای")):
        return "با لە خواردن گفتوگۆ بکەین: «من چای دەمەوێت، تکایە». تۆ حەزت لە چییە؟"

    if any(word in clean for word in ("قوتابخانە", "مامۆستا", "وانە", "خوێندن")):
        return "باشە! دەتوانیت بڵێیت: «من لە قوتابخانە زمانی کوردی دەخوێنم». تۆ لە کام وانە زیاتر حەز دەکەیت؟"

    if any(word in clean for word in ("یارمەتی", "تێناگەم", "نەزانم", "فێر")):
        return "بە خۆشییەوە یارمەتیت دەدەم. 🌱 ڕستەکەت بەش بەش بنووسە، یان بڵێ لە کام وشەدا کێشەت هەیە."

    if any(word in clean for word in ("ڕاهێنان", "پرسیار", "تاقیکردنەوە")):
        return "زۆر باشە! ئەم ڕستەیە تەواو بکە: «سڵاو، ناوی من ____ ـە». وەڵامەکەت بنووسە تا بەردەوام بین."

    state["daily_chat_turns"] = state.get("daily_chat_turns", 0) + 1
    return random.choice((
        "تێگەیشتم. دەتوانیت کەمێک زیاتر ڕوونی بکەیتەوە؟ با بە ڕستەیەکی کورت بەردەوام بین.",
        "زۆر باشە، با گفتوگۆکەمان بەردەوام بێت. دەتوانیت ئەوە بە ڕستەیەکی سادەتر بڵێیت؟",
        "من لێرەم بۆ یارمەتیدانت. 😊 دەتەوێت ئەم وشەیە لە ڕستەیەکدا بەکاربهێنین؟",
    ))
