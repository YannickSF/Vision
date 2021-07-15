
from core.dialogs import VisionDialog, CONFIG
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


vision_corpus = VisionDialog()


def callback_hour_vision(context: CallbackContext):
    vision_corpus.search(context)


def main():
    """Start the bot."""
    updater = Updater(CONFIG.BOT_KEY, use_context=True)
    # Get JobQueue to schedule watch()
    jb = updater.job_queue
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", vision_corpus.start))
    dp.add_handler(CommandHandler("search", vision_corpus.search))
    dp.add_handler(MessageHandler(Filters.text, vision_corpus.answer))

    # job_hour = jb.run_repeating(callback_hour_vision, interval=CONFIG.ENGINE_INTERVAL, first=CONFIG.ENGINE_FIRST)

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
