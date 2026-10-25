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
        state.pop("daily_chat_scenario", None)
        state.pop("daily_chat_stage", None)
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
        state.pop("daily_chat_scenario", None)
        state.pop("daily_chat_stage", None)
        return "خواحافیز، بە خۆشی و تەندروستی! هەر کاتێک بتەوێت کەژیار لێرەیە. 👋"

    # Continue a small role-play instead of treating each turn as an unrelated keyword.
    scenario = state.get("daily_chat_scenario")
    if scenario == "market" and state.get("daily_chat_stage") == 1:
        if any(word in clean for word in ("چەندە", "دەمەوێت", "تکایە", "نرخ")):
            state["daily_chat_stage"] = 2
            return "زۆر باشە! 🛍 فرۆشیار دەڵێت: «٣٠ هەزار دینارە». تۆ چۆن داوای داشکاندن دەکەیت؟"
        return "با یەک ڕستەی سادە تاقی بکەینەوە: «تکایە، ئەمە چەندە؟» بە وشەی خۆت بنووسە."

    if scenario == "market" and state.get("daily_chat_stage") == 2:
        state["daily_chat_stage"] = 3
        return "باشە، دەتوانیت بڵێیت: «تکایە، کەمێک داشکاندنم بۆ بکە». گفتوگۆکەمان باش بوو! دەتەوێت بابەتێکی تر هەڵبژێریت؟"

    if scenario == "food" and state.get("daily_chat_stage") == 1:
        state["daily_chat_stage"] = 2
        return "باشە! فرۆشیار دەڵێت: «چی دەتەوێت بخۆیتەوە؟» تۆ داواکارییەک بە کوردی بنووسە."

    if scenario == "food" and state.get("daily_chat_stage") == 2:
        state["daily_chat_stage"] = 3
        return "زۆر باشە! دەتوانیت زیاد بکەیت: «تکایە، سوپاس». گفتوگۆکەمان تەواو بوو؛ بابەتێکی تر هەڵبژێرە."

    if scenario == "school" and state.get("daily_chat_stage") == 1:
        state["daily_chat_stage"] = 2
        return "مامۆستا دەپرسێت: «کام وانە بە دڵتە؟» بە ڕستەیەک وەڵام بدەرەوە."

    if scenario == "school" and state.get("daily_chat_stage") == 2:
        state["daily_chat_stage"] = 3
        return "وەڵامێکی باشە! دەتوانیت هۆکارەکەشی زیاد بکەیت: «چونکە ...». گفتوگۆکەمان بەردەوام بکەین؟"

    if any(word in clean for word in ("بازاڕ", "کڕین", "نرخ", "پارە")):
        state["daily_chat_scenario"] = "market"
        state["daily_chat_stage"] = 1
        return "با ڕۆڵگێڕی بازاڕ بکەین. 🛍 من فرۆشیارم و تۆ کڕیاریت. پرسیار بکە: «تکایە، ئەمە چەندە؟»"

    if any(word in clean for word in ("خواردن", "نان", "برنج", "ئاو", "چای")):
        state["daily_chat_scenario"] = "food"
        state["daily_chat_stage"] = 1
        return "با لە چێشتخانە ڕۆڵگێڕی بکەین. 🍵 من کارمەندی چێشتخانەم؛ تۆ چی داوا دەکەیت؟"

    if any(word in clean for word in ("قوتابخانە", "مامۆستا", "وانە", "خوێندن")):
        state["daily_chat_scenario"] = "school"
        state["daily_chat_stage"] = 1
        return "با گفتوگۆی قوتابخانە ڕاهێنان بکەین. 🎒 من هاوپۆلت دەبم: «سڵاو، کام وانە دەخوێنین؟»"

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
