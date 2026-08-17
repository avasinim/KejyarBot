import json

with open('dictionary.json', 'r', encoding='utf-8') as f:
    DICTIONARY = json.load(f)


def find_word(word):
    return DICTIONARY.get(word)


def answer_word(word):
    data = find_word(word)

    if not data:
        return '❌ ئەم وشەیە لە فەرهەنگی کەژیاردا نییە.'

    return f"""📚 {word}

واتا:
{data['meaning']}

🎓 ئاست:
{data['level']}

📝 نموونە:
{data['example']}

🔥 +2 XP"""
