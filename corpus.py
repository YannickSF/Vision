
import time
from requests import HTTPError
from tools import check_channel
from core import *


class VisionDialog:
    first_boot = True

    @staticmethod
    @check_channel
    def start(update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text("Je suis Vision, pour vous servir.")

    @staticmethod
    @check_channel
    def get_engine(update, context):
        response = 'Engine liste : ' + ', '.join(core_get_engine(update))
        update.message.reply_text(response)

    @staticmethod
    @check_channel
    def post_engine(update, context):
        words = update.message.text.split('/add_words')
        update.message.reply_text(core_post_engine(update, words=words[1]))

    @staticmethod
    @check_channel
    def get_articles(update, context):
        data = core_get_articles(update)
        for i in range(len(data)):
            update.message.reply_text(text=data[i]['url'])
            if i % 5 == 0:
                time.sleep(CONFIG.SENDER_SLEEP)

    @staticmethod
    @check_channel
    def search(update, context):
        pass

    def schedule_vision(self, context):
        try:
            r = requests.get(CONFIG.DOMAINE + '/vision')
            data = r.json()
            if data['validates'] > 0:
                for i in range(len(data['articles'])):
                    context.bot.send_message(chat_id=CONFIG.TDV_CHAIN_ID, text=data['articles'][i]['url'])
                    if i % 5 == 0:
                        time.sleep(CONFIG.SENDER_SLEEP)

            if self.first_boot:
                context.bot.send_message(chat_id=CONFIG.ADMIN_ID, text='Validate Schedule from First Boot !')
                self.first_boot = False
            else:
                if CONFIG.mode == 'test':
                    context.bot.send_message(chat_id=CONFIG.ADMIN_ID, text='First_Boot > False value.')

        except HTTPError as h:
            context.bot.send_message(chat_id=CONFIG.ADMIN_ID,
                                     text="" + h.response)

    # Conversation
    # @check_channel
    @staticmethod
    def answer(update, context):
        """Echo the user message."""
        r = requests.get('https://baconipsum.com/api/?type=all-meat&sentences=1').json()
        update.message.reply_text(r[0])
