from flask import Flask
import telegram
import os

TOKEN = os.getenv('TOKEN')
app = Flask(__name__)
url = "https://allamurod.pythonanywhere.com/"

bot = telegram.Bot(TOKEN)
chat_id = "1383186462"
@app.route('/', methods=['POST'])
def home_page():
    bot.send_message(chat_id = chat_id, text = "Assalomu aleykum")
    return "Hello programmer"

bot.delete_webhook()
print(bot.set_webhook(url))
print(bot.get_webhook_info())