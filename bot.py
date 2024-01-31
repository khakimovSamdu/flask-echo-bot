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
    elif data['message'].get('contact')!=None:
        bot.send_contact(user['id'], data['message']['contact']['phone_number'], data['message']['contact']['first_name'])
    elif data['message'].get('audio')!=None:
        bot.send_audio(user['id'], data['message']['audio']['file_id'], caption = "Audio file")
    elif data['message'].get('location')!=None:
        bot.send_location(chat_id = user['id'], latitude = data['message']['location']['latitude'], longitude = data['message']['location']['longitude'], heading = 2, protect_content = True)
    elif data['message'].get('document')!=None:
        bot.send_document(chat_id = user['id'], document = data['message']['document']['file_id'], caption="Documitatsiya",protect_content=True)
    elif data['message'].get('dice')!=None:
        bot.send_dice(chat_id = data['message']['dice']['emoji'], disable_notification = True)
    elif data['message'].get('animation')!=None:
        bot.send_animation(chat_id = user['id'], animation = data['message']['animation'], duration = 10)
    elif data['message'].get('poll')!=None:
        bot.send_poll(chat_id = user['id'], question = data['message']['poll']['question'], options = data['message']['poll']['options'])
    else:
        bot.send_message(chat_id = user['id'], text = "Bu so'rovga hali javob topmadik !")
    return "Hello programmer"

bot.delete_webhook()
if __name__=="__main__":
    app.run(debug=True)   
 



