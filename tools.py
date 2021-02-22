
from settings import CONFIG


def check_user(*args):
    if args[0].effective_chat.id == CONFIG.ADMIN_ID:
        return True
    return False


def check_command(*args):
    if '/start' in args[0].effective_message.text or \
            '/engine_words' in args[0].effective_message.text or \
            '/add_words' in args[0].effective_message.text or \
            '/articles' in args[0].effective_message.text or \
            '/search' in args[0].effective_message.text:
        return True
    return False


def check_channel(func):
    def wrapper(*args, **kwargs):
        if args[0].effective_chat.id == CONFIG.TDV_CHAIN_ID:
            pass
        else:
            if check_user(*args):
                func(*args, **kwargs)

    return wrapper
