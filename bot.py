from flask import Flask, request
from telegram import  Bot, ReplyKeyboardMarkup,KeyboardButton
import os
app = Flask(__name__)
url = "https://allamurod.pythonanywhere.com/"
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
@app.route('/', methods=['POST'])
def home_page():
    params  = request.args
    message = "Siz bu bot orqali pul yutib olishingiz mumkin, pul miqdorini belgilang va shoshiling. Yutuqni olish uchun biz bilan bog'laning."
    bot.delete_webhook()
    bot.set_webhook(url)
    statust = bot.get_webhook_info()
    bot.send_message(
        chat_id = "1383186462", text = params.get('text', str(statust)),
        reply_markup = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='1500 💰'),KeyboardButton(text='1000 💰')],
                [KeyboardButton(text='2500 💰'),KeyboardButton(text='3000 💰')]],resize_keyboard=True,))
    return "Hello programmer"
if __name__=="__main__":
    app.run(debug=True)   


