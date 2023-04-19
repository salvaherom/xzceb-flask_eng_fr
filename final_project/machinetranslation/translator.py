import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2023-04-18'

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def englishToFrench(englishText):
    translator_response = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    return translator_response["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    translator_response = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    return translator_response["translations"][0]["translation"]
  
print(englishToFrench('Hello, how are you today?'))
print(frenchToEnglish("Bonjour, comment vous êtes aujourd'hui?"))
