text = ''
from text_to_speech import tts
from translate import translate
import speech_recognition as sr


global_source_language = 'ja'
global_target_language = 'en'
name = 'Utrans'

# when the name hey utrans is called, it stops translating and instead follows a number of commands
    #change_tlang [completed] (target language) **can use string to find specific word so it triggers without specific command
    #change_mylang [] (my language)**same thing as target language**
        # see the language options
    #state all the commands(help)
    #turn off
#translate command


def intro():
    tts('Hi, I am'+name+'.I can solve the problems of the world', 'en')
    tts('People can talk in any language they want. I can universally translate in real-time.','en')
    tts('Hahaha','en')
    tts('My commands are: 1 set language to target language. 2 set target language to new language.','en')
    tts('3 set mode to real-time, slow, or chat mode','en')
    tts('choose your destiny...','en')



#
##
# 0. "Hi, I am <insert name here>. I can solve the problems of the world.
# People can talk in any language they want. I can universally translate in real-time.
# Hahhaha :)
# Your commands are:
# 1. Set language to <language> ->
# 2. Set target language to <new language>
# 3. Set mode to be real-time or SLOW or CHAT mode
# Choose your destiny...

# 1. get_audio is an always on microphone
# 2. Listen for special commands
#   2.1.

language_mapping = {'Spanish': 'es', 'Russian':	'ru','Portuguese': 'pt','English': 'en','Japanese': 'ja', 'Chinese': 'zh'}


def call_t(said):
#changes target language by calling name
    if said and "target language" in said.lower():
        words = said.split(" ")
        target_language = words[-1]
        print("target_language: {}".format(language_mapping[target_language]))
        global_target_language = language_mapping[target_language]


    if said and "my language" in said.lower():
        words = said.split(" ")
        my_language = words[-1]
        print("source_language: {}".format(language_mapping[my_language]))
        global_source_language = language_mapping[my_language]


def audio_processor():
    r = sr.Recognizer()
    # tts("Hello donkeys", "es")
    print("Recording.. ")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = ""
        try:
            said = r.recognize_google(audio, language=global_source_language)
        except:
            said = None

        if said and "bob" in said.lower():
            # Process commands:
            #
            # 1. Set language to <language> ->
            # 2. Set target language to <new language>
            # tts("Oh, you called me?", "en")
            call_t(said)

        # except:
        #     pass
        print("Said: {}".format(said))
        try:
            text = translate(said, global_target_language, src=global_source_language)
            tts(text, global_target_language)
        except:
            pass

if __name__ == "__main__":
    # intro()
    while True:
        audio_processor()
        # print(text)
