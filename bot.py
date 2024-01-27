from flask import Flask
import telegram
import os
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
)
from handlers import flask_echo

app = Flask(__name__)
url = "https://allamurod.pythonanywhere.com/"
TOKEN = os.getenv('TOKEN')


bot = telegram.Bot(TOKEN)
@app.route('/', methods=['POST'])
def home_page():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text, callback=flask_echo))
    return "Hello programmer"

print(bot.delete_webhook())
print(bot.set_webhook(url))
print(bot.get_webhook_info())
