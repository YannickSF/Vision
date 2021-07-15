
from settings import CONFIG
from core.validators import check_user, check_channel
from core.treatments import answer, search


class VisionDialog:
    first_boot = True

    @staticmethod
    @check_channel
    def start(update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text("Je suis Vision, pour vous servir.")

    @staticmethod
    @check_channel
    def search(update, context):
        datas_to_send = search()
        for article in datas_to_send:
            context.bot.send_message(chat_id=CONFIG.TDV_CHAIN_ID, text=article.url)

    # Conversation
    @staticmethod
    def answer(update, context):
        """Echo the user message."""
        update.message.reply_text(answer())
