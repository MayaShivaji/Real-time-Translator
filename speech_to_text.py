#   # A Python program to convert speech to text


# Pakages to install:
#           pip install SpeechRecognition
#           pip install pipwin
#           pipwin install pyaudio


import speech_recognition as sr

#   initialize a recognizer object
#   this object will record the audio and recognize the language of the audio, i.e, english, russian, chinese, etc.
r = sr.Recognizer()

#   initialize the Microphone object as the source of audio file
with sr.Microphone() as source:
    print("Please speak anything :")
    #   calling the recognizer object to listen the audio from the source
    #   you can also pass your google cloud speech API key through the key parameter(key="YOUR_GOOGLE_CLOUD_SPPECH_API_KEY")
    audio = r.listen(source)
    try:
        #   now the audio will be recognized by google cloud speech API and converted to text
        text = r.recognize_google(audio)
        print(text)
    except :
        print("Sorry ! Speech Recognition failed !")