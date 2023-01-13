text = ''

import speech_recognition as sr
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = ""
        try:
            said = r.recognize_google(audio)
        except:
            pass
    return text.lower()

while True:
    text += get_audio()
    print(text)
