"""
Конфигурационный файл для защиты ключей.
"""

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN is None:
  exit('BOT_TOKEN отсутствует в переменных окружения')

API_KEY_RAPID = os.getenv('API_KEY_RAPID')
if API_KEY_RAPID is None:
  exit('API_KEY_RAPID отсутствует в переменных окружения')

API_KEY_GPT35 = os.getenv('API_KEY_GPT35')
if API_KEY_GPT35 is None:
  exit('API_KEY_GPT35 отсутствует в переменных окружения')

API_KEY_HUGCHAT_READ = os.getenv('API_KEY_HUGCHAT_READ')
if API_KEY_HUGCHAT_READ is None:
  exit('API_KEY_HUGCHAT_READ отсутствует в переменных окружения')

API_KEY_HUGCHAT_WRITE = os.getenv('API_KEY_HUGCHAT_WRITE')
if API_KEY_HUGCHAT_WRITE is None:
  exit('API_KEY_HUGCHAT_WRITE отсутствует в переменных окружения')

EMAIL_HUGCHAT = os.getenv('EMAIL_HUGCHAT')
if EMAIL_HUGCHAT is None:
  exit('EMAIL_HUGCHAT отсутствует в переменных окружения')

PASSWORD_HUGCHAT = os.getenv('PASSWORD_HUGCHAT')
if PASSWORD_HUGCHAT is None:
  exit('PASSWORD_HUGCHAT отсутствует в переменных окружения')

API_KEY_SPEECH_TO_TEXT = os.getenv('API_KEY_SPEECH_TO_TEXT')
if API_KEY_SPEECH_TO_TEXT is None:
  exit('API_KEY_SPEECH_TO_TEXT отсутствует в переменных окружения')


API_KEY_TEXT_TO_SPEECH = os.getenv('API_KEY_TEXT_TO_SPEECH')
if API_KEY_TEXT_TO_SPEECH is None:
  exit('API_KEY_TEXT_TO_SPEECH отсутствует в переменных окружения')

API_KEY_YANDEX = os.getenv('API_KEY_YANDEX')
if API_KEY_TEXT_TO_SPEECH is None:
  exit('API_KEY_YANDEX отсутствует в переменных окружения')

ADMIN_LIST = os.getenv('ADMIN_LIST')
if ADMIN_LIST is None:
  exit('ADMIN_LIST отсутствует в переменных окружения')

SIS_ADMIN_LIST = os.getenv('SIS_ADMIN_LIST')
if SIS_ADMIN_LIST is None:
  exit('SIS_ADMIN_LIST отсутствует в переменных окружения')

PROXY_SETTING = os.getenv('PROXY_SETTING')
if PROXY_SETTING is None:
  exit('PROXY_SETTING отсутствует в переменных окружения')

PROXY_IP = os.getenv('PROXY_IP')
if PROXY_IP is None:
  exit('PROXY_IP отсутствует в переменных окружения')

PROXY_USERNAME = os.getenv('PROXY_USERNAME')
if PROXY_USERNAME is None:
  exit('PROXY_USERNAME отсутствует в переменных окружения')

PROXY_PASS = os.getenv('PROXY_PASS')
if PROXY_PASS is None:
  exit('PROXY_PASS отсутствует в переменных окружения')

API_HOST_RAPID_ALIEXPRESS = 'aliexpress-datahub.p.rapidapi.com'
API_HOST_RAPID_MICROSOFT_AZURE = "microsoft-translator-text.p.rapidapi.com"
API_URL_GPT35 = ''
API_URL_SPEECH_TO_TEXT = ''
API_URL_TEXT_TO_SPEECH = ''
API_URL_GIPHY = ''
API_URL_HUGCHAT = 'https://api-inference.huggingface.co/'
API_URL_YANDEX_TRANSLATION = ''
