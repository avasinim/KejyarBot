import os

VOICE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "voices",
    "kejyar.mp3"
)

def get_voice_file():
    if os.path.exists(VOICE_FILE):
        return VOICE_FILE
    return None