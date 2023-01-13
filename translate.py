#   A Python program to translate text in different languages


#  Packages to install:
#               pip install googletrans

from googletrans import Translator


def translate(text, lang):
    #   an instance of Translator object
    translator = Translator(service_urls=['translate.google.com', 'translate.google.co.in'])
    #   Translate text from source language to destination language
    trans = translator.translate(text=text, dest=lang)
    #   to check if the user is passing a list of strings
    if isinstance(trans, list):
        for translations in trans:
            if translations.pronunciation == None:
                print(translations.text, '\n')
            else:
                print(translations.text, '->', translations.pronunciation, '\n')
    else:
        if trans.pronunciation == None:
            print(trans.text, '\n')
        else:
            print(trans.text, '->', trans.pronunciation, '\n')

if __name__ == "__main__":
    #   My favourite quote by El profesor from Money Heist
    # translate( 'When someone is in love, they look through rose-tinted glasses. Everything is wonderful. They transform into a soft teddy bear that is smiling all the time.', 'es')
    #   Breaking down that quote into list
    # translate(['When someone is in love', 'they look through rose-tinted glasses', 'Everything is wonderful.', 'They transform into a soft teddy bear that is smiling all the time.'], 'es')

    #   some other translation examples
    translate('I am a young man', 'es')
    # translate('この文章は日本語で書かれました。', 'en')
    # translate('안녕하세요.', 'ja')