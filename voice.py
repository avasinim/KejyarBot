import os


VOICE_DIR = os.path.join(
    os.path.dirname(__file__),
    "voices"
)


def get_voice(filename):
    path = os.path.join(
        VOICE_DIR,
        filename
    )

    if os.path.exists(path):
        return path

    return None


# سازگاری با نسخه قبلی bot.py
def get_voice_file():
    return get_voice("kejyar.mp3")