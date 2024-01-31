from flask import Flask, request
from telegram import  Bot

app = Flask(__name__)
url = "https://allamurod.pythonanywhere.com/"
TOKEN = "6717011499:AAFA-BIJ_s7nkr9BFGE78UHYdOcQDGSWJEo"
bot = Bot(TOKEN)

@app.route('/', methods=['POST'])
def home_page():
    data = request.get_json()
    print(data)
    user = data['message']['chat']
    if data['message'].get('text')!=None:
        bot.send_message(chat_id = user['id'], text = data['message']['text'])
    elif data['message'].get('photo')!=None:
        bot.send_photo(chat_id = user['id'], photo = data['message']['photo'][0]['file_id'])
        
    return "Hello programmer"
bot.delete_webhook()
if __name__=="__main__":
    app.run(debug=True)   
 



