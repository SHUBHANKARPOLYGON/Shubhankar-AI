# ai_tool/speech_utils.py
from gtts import gTTS

def text_to_speech(text, output_file="audio.mp3"):
    tts = gTTS(text)
    tts.save(output_file)
    return output_file
