from flask import Flask, request
from telegram import  Bot
import os
app = Flask(__name__)
url = "https://allamurod.pythonanywhere.com/"
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)


@app.route('/', methods=['POST'])
def home_page():
    data = request.get_json()
    print(data)
    bot.send_message(
        chat_id = "1383186462", text = "message")

    return "Hello programmer"
if __name__=="__main__":
    app.run(debug=True)   
 


