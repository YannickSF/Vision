
import time
import requests
from requests import HTTPError
from settings import CONFIG
from tools import check_channel
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


@check_channel
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Je suis Vision, pour vous servir.")


def schedule_vision(context):
    try:
        r = requests.get(CONFIG.DOMAINE + '/vision')
        data = r.json()
        if data['waiting'] > 10:
            if 'datas' in data.keys():
                for i in range(len(data['datas'])):
                    context.bot.send_message(chat_id=CONFIG.TDV_CHAIN_ID, text=data['datas'][i]['url'])
                    if i % 5 == 0:
                        time.sleep(5)

    except HTTPError as h:
        context.bot.send_message(chat_id=CONFIG.ADMIN_ID,
                                 text="" + h.response)


def callback_hour_vision(context: CallbackContext):
    schedule_vision(context)


def schedule_engine(context):
    try:
        r = requests.get(CONFIG.DOMAINE + '/engine')
        data = r.json()
        if 'validates' in data.keys():
            context.bot.send_message(chat_id=CONFIG.ADMIN_ID,
                                     text="engine effectué.")

    except HTTPError as h:
        context.bot.send_message(chat_id=CONFIG.ADMIN_ID,
                                 text="" + h.response)


def callback_hour_engine(context: CallbackContext):
    schedule_engine(context)


# Conversation
# @check_channel
def answer(update, context):
    """Echo the user message."""
    r = requests.get('https://baconipsum.com/api/?type=all-meat&sentences=1').json()
    update.message.reply_text(r[0])


def main():
    """Start the bot."""
    updater = Updater(CONFIG.BOT_KEY, use_context=True)
    # Get JobQueue to schedule watch()
    jb = updater.job_queue
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, answer))

    job_hour = jb.run_repeating(callback_hour_engine, interval=60, first=20)
    job_hour = jb.run_repeating(callback_hour_vision, interval=30, first=10)

    # log all errors
    # dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
