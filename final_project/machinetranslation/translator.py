'Module creating functions to translate from french to english and vice versa using IBM Watson'

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('fVCAHh1TYHQJwba1U4Tk8kg2wC8_c3XqGRVXGvSGG72U')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/7c78f173-d836-4682-a8f6-a6c92716407f')

def english_to_french(englishtext):

    'english to french translation'

    translation = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()

    frenchtext_json = (json.dumps(translation, indent=2, ensure_ascii=False))
    frenchtext_dict = json.loads(frenchtext_json)
    frenchtext = frenchtext_dict['translations'][0]['translation']

    return frenchtext

def french_to_english(frenchtext):

    'french to english translation'

    translation = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()

    englishtext_json = (json.dumps(translation, indent=2, ensure_ascii=False))
    englishtext_dict = json.loads(englishtext_json)
    englishtext = englishtext_dict['translations'][0]['translation']

    return englishtext
