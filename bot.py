from flask import Flask
import telegram
import os

bot = os.getenv('TOKEN')
app = Flask(__name__)

user = telegram.Bot(bot)
chat_id = "1383186462"
@app.route('/')
def home_page():
    user.send_message(chat_id = chat_id, text = "Assalomu aleykum")
    return "Hello programmer"
