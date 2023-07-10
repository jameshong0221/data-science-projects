import requests
from googletrans import Translator
import openai

# Configure the Telegram API parameters
TELEGRAM_API_BASE_URL = 'https://api.telegram.org/bot'
TELEGRAM_API_TOKEN = 'YOUR_TELEGRAM_API_TOKEN'
TELEGRAM_CHAT_ID = '-1709130877'

# Configure the language for translation
TRANSLATE_TO_LANG = 'en'  # Translate to English

# Configure the OpenAI model
OPENAI_API_TOKEN = 'YOUR_OPENAI_API_TOKEN'
OPENAI_MODEL = 'gpt-3.5-turbo'

def send_telegram_message(text):
    """Send a message to the Telegram chat"""
    url = f'{TELEGRAM_API_BASE_URL}{TELEGRAM_API_TOKEN}/sendMessage'
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print('Failed to send message to Telegram')
        print(response.text)

def translate_and_paraphrase(message):
    """Translate and paraphrase the message"""
    # Translate the message to English
    translator = Translator()
    translation = translator.translate(message, dest=TRANSLATE_TO_LANG)
    translated_text = translation.text

    # Paraphrase the translated text using OpenAI
    openai.api_key = OPENAI_API_TOKEN
    response = openai.Completion.create(
        engine=OPENAI_MODEL,
        prompt=translated_text,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7,
        n=1
    )
    paraphrased_text = response.choices[0].text.strip()

    # Send the paraphrased text back to the Telegram chat
    send_telegram_message(paraphrased_text)

def process_telegram_update(update):
    """Process the incoming Telegram update"""
    message = update['message']['text']
    translate_and_paraphrase(message)

def get_updates():
    """Get updates from the Telegram API"""
    url = f'{TELEGRAM_API_BASE_URL}{TELEGRAM_API_TOKEN}/getUpdates'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['ok']:
            return data['result']
        else:
            print('Failed to get updates from Telegram')
    else:
        print('Failed to get updates from Telegram')
    return []

def start_telegram_bot():
    """Start the Telegram bot"""
    updates = get_updates()
    if updates:
        latest_update_id = updates[-1]['update_id']
        offset = latest_update_id + 1
    else:
        offset = None

    while True:
        url = f'{TELEGRAM_API_BASE_URL}{TELEGRAM_API_TOKEN}/getUpdates'
        params = {'offset': offset}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['ok']:
                results = data['result']
                if results:
                    for result in results:
                        process_telegram_update(result)
                        offset = result['update_id'] + 1
                else:
                    continue
            else:
                print('Failed to get updates from Telegram')
        else:
            print('Failed to get updates from Telegram')

# Start the Telegram bot
start_telegram_bot()
