from flask import Flask
from telegram import Update, Bot, ReplyKeyboardMarkup,KeyboardButton
import os

app = Flask(__name__)
url = "https://allamurod.pythonanywhere.com/"
TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
@app.route('/', methods=['POST'])
def home_page():

    text = "Siz bu bot orqali pul yutib olishingiz mumkin, pul miqdorini belgilang va shoshiling. Yutuqni olish uchun biz bilan bog'laning."
    bot.send_message(
        chat_id = "1383186462", text = text,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='1500 💰'),KeyboardButton(text='1000 💰')],
                [KeyboardButton(text='2500 💰'),KeyboardButton(text='3000 💰')]
            ],
            resize_keyboard=True,
        )
    )
    return "Hello programmer"

bot.delete_webhook()
bot.set_webhook(url)
bot.get_webhook_info()

if __name__=="__main__":
    app.run(debug=True)
