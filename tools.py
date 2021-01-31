
from settings import CONFIG


def check_user(*args):
    if args[0].effective_chat.id == CONFIG.ADMIN_ID:
        return True
    return False


def check_command(*args):
    if '/searchweb' in args[0].effective_message.text or \
            '/searchdb' in args[0].effective_message.text or \
            '/article' in args[0].effective_message.text:
        return True
    return False


def check_channel(func):
    def wrapper(*args, **kwargs):
        if args[0].effective_chat.id == CONFIG.TDV_CHAIN_ID:
            pass
        elif args[0].effective_chat.id == CONFIG.TDV_CHAT_ID:
            pass
        else:
            if check_user(*args):
                func(*args, **kwargs)

    return wrapper
