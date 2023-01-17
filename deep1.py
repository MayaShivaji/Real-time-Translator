import requests, sys, json, os
import pprint
from os.path import dirname, abspath

# get parent directory of this script
parent_dir = dirname(abspath(__file__))

# get api key
api_key_file = os.path.join(parent_dir, 'api_key.txt')
with open(api_key_file) as f:
    api_key = f.read()

url = "https://api.deepl.com"
auth_key = {
    'host': "https://api.deepl.com/v2/translate?",
    'auth_key': f"auth_key={api_key}"
}

# define parameters
list = ['Quem caralho manda aqui?', 'Estou farto de vós!']
source_lang = 'pt'
target_lang = 'en'

# get the translations
try:
    response = requests.post(url='https://api.deepl.com/v2/translate',
                             data={
                                 'source_lang': source_lang,
                                 'target_lang': target_lang,
                                 'auth_key': api_key,
                                 'text': list
                             })

    if response.status_code == 200:
        json = json.loads(response.text)
        translations = json['translations']
        for xlat in translations:  # type list
            print(xlat['text'])

    else:
        print("The connection didn't resolve successfully.")
except:
    print("There was a problem to fetch the translation.")