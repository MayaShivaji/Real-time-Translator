# A Python program to convert text to speech


# Packages to install:
#               pip install gtts
#               pip install pydub
#               pip install ffmpeg-python

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
import time


def tts(text, lang):
    #   gTTS object that will create the audio file of the given text
    TextAudio = gTTS(text=text, lang=lang)

    #   filepath to save the audio file in the desired directory
    filePath = './audio.mp3'
    TextAudio.save(filePath)

    #   playback of the audio and removal on exit
    audio = AudioSegment.from_mp3(filePath)
    print('Playing...')
    play(audio)
    os.remove(filePath)


if __name__ == "__main__":
    tts('India is a beautiful country', 'en')
    tts('India ek sundar desh hai', 'hi')