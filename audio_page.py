import streamlit as st
import time
# text to speech
from gtts import gTTS

# playing speech
from playsound import playsound

def _process_chunk(chunk):
    return []

def text_to_speech(message: str, language = "en"):

    # text to speech
    speech = gTTS(text=message, lang=language)
    speech.save('output.mp3')
    playsound('output.mp3')


if __name__=="__main__":
    # parse personal.txt
    # list of strings split based on \n\n\n
    with open("personal.txt", "r") as f:
        personal = f.read().split("\n\n\n")

        trimmed_file = [chunk for chunk in personal if len(chunk) > 5]

        for idx, chunk in enumerate(trimmed_file):
            iterated_list = _process_chunk(chunk)
            text_to_speech(chunk)
            time.sleep(5)

    

