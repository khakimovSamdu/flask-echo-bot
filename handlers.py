from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


def flask_echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_message(
        chat_id = user.id, text = message.text,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='1500 💰'),KeyboardButton(text='1000 💰')],
                [KeyboardButton(text='2500 💰'),KeyboardButton(text='3000 💰')]
            ],
            resize_keyboard=True,
        )
    )