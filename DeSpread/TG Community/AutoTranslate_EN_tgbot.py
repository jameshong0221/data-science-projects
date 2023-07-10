import logging
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from googletrans import Translator
import openai

# Configure the Telegram bot token and OpenAI API token
TELEGRAM_TOKEN = '6336119344:AAEizmEg2VplsJkz4kvj8c5Vn459jCcZSvA'
OPENAI_API_TOKEN = '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'

# Configure the language for translation
TRANSLATE_TO_LANG = 'en'  # Translate to English

# Configure the OpenAI model
OPENAI_MODEL = 'gpt-3.5-turbo'

# Set up the Telegram bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    """Handler for the /start command"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Hello! I am ready to translate and paraphrase your messages.')


def translate_and_paraphrase(update, context):
    """Handler for processing incoming messages"""
    message = update.message.text

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
    context.bot.send_message(chat_id=update.effective_chat.id, text=paraphrased_text)


# Register handlers
start_handler = telegram.ext.CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, translate_and_paraphrase)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()



# ChatGPT Integration
# 1. Input text from Telegram
# 2. Translate
# 3. Paraphrase
# 4. Output to Telegram Channel