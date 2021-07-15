
from settings import SETTINGS
from core.validators import check_channel
from core.treatments import answer, search, create_sequence, read_sequence, delete_sequence, find_by_query


class VisionDialog:
    first_boot = True

    @staticmethod
    @check_channel
    def start(update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text("Je suis Vision.")

    @staticmethod
    @check_channel
    def search(update, context):
        datas_to_send = search()
        for article in datas_to_send:
            context.bot.send_message(chat_id=SETTINGS.TDV_CHAIN_ID, text=article.url)

    @staticmethod
    @check_channel
    def create_query(update, context):
        tmp_query = update.message.text.replace('/create ', '')
        create_sequence(tmp_query)
        update.message.reply_text('séquence ajoutée.')

    @staticmethod
    @check_channel
    def read_query(update, context):
        message = ''
        for i in range(len(SETTINGS.SEQUENCES)):
            message += '{0} - '.format(i) + SETTINGS.SEQUENCES[i].__str__() + '\n'
        update.message.reply_text(message)

    @staticmethod
    @check_channel
    def delete_query(update, context):
        tmp_query = update.message.text.replace('/delete ', '')
        delete_sequence(tmp_query.strip())
        update.message.reply_text('séquence supprimée.')

    @staticmethod
    @check_channel
    def find_by_query(update, context):
        tmp_query = update.message.text.replace('/find ', '')
        datas_to_send = find_by_query(tmp_query)
        for article in datas_to_send:
            context.bot.send_message(chat_id=SETTINGS.ADMIN_ID, text=article.url)

    # Conversation
    @staticmethod
    def answer(update, context):
        """Echo the user message."""
        update.message.reply_text(answer())
