from flask import Flask, request
from telegram import  Bot
import os
app = Flask(__name__)
url = "https://allamurod.pythonanywhere.com/"
TOKEN = "6717011499:AAFA-BIJ_s7nkr9BFGE78UHYdOcQDGSWJEo"
bot = Bot(TOKEN)

@app.route('/', methods=['POST'])
def home_page():
    data = request.get_json()
    if data['message'].get('text')!=None:
        bot.send_message(chat_id = data['message']['chat']['id'], text = data['message']['text'])
    elif data['message']['photo']['file_id']:
        bot.send_message(chat_id = data['message']['form']['id'], photo = data['message']['photo']['file_id'])
        

    return "Hello programmer"

if __name__=="__main__":
    app.run(debug=True)   
 



