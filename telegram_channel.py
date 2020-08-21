import os
import telegram

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])


def send_message_to_me(message):
    try:
        bot.send_message(chat_id='279586087', text=message)
    except Exception as e:
        print(e)
    