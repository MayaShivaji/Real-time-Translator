#   A Python program to translate text in different languages


#  Packages to install:
#               pip install googletrans

from googletrans import Translator



def translate(text, lang, src=None):
    #   an instance of Translator object
    # translator = Translator(service_urls=['translate.google.com', 'translate.google.co.in'])
    translator = Translator()
    #   Translate text from source language to destination language
    if src:
        trans = translator.translate(text=text, dest=lang, src=src)
    else:
        trans = translator.translate(text=text, dest=lang)
    #   to check if the user is passing a list of strings
    if isinstance(trans, list):
        for translations in trans:
            # if translations.pronunciation == None:
            #     return translations.text
            # else:
            #     return (translations.text, '->', translations.pronunciation, '\n')
            return translations.text
    else:
        # if trans.pronunciation == None:
        #     return (trans.text, '\n')
        # else:
        #     return (trans.text, '->', trans.pronunciation, '\n')
        return trans.text

if __name__ == "__main__":
    #   My favourite quote by El profesor from Money Heist
    translate( 'When someone is in love, they look through rose-tinted glasses. Everything is wonderful. They transform into a soft teddy bear that is smiling all the time.', 'es')
    #   Breaking down that quote into list
    # translate(['When someone is in love', 'they look through rose-tinted glasses', 'Everything is wonderful.', 'They transform into a soft teddy bear that is smiling all the time.'], 'es')

    #   some other translation examples
    translate('I am a young man', 'es')
    translate('この文章は日本語で書かれました。', 'en')
    translate('안녕하세요.', 'ja')