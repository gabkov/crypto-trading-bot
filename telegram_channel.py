import os
import telegram

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])


def send_message_to_me(message):
    bot.send_message(chat_id='279586087', text=message)