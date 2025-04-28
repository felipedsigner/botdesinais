from telegram import Bot
from settings import TOKEN, CHAT_ID

def send_signal(signal):
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=signal)
