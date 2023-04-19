"""
Translation module for english and french
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2023-04-18'

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def english_to_french(english_text):
    """
    function that returns the given text from english to french
    """
    if english_text is None:
        return ""
    translator_response = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translator_response["translations"][0]["translation"]

def french_to_english(french_text):
    """
    function that returns the given text from french to english
    """
    if french_text is None:
        return ""
    translator_response = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translator_response["translations"][0]["translation"]
