
class Configuration:
    def __init__(self):
        self.mode = 'prod'

    # NETWORK
    DOMAINE = 'http://172.17.0.1:7111/tdv'

    # TELEGRAM
    BOT_KEY = '1432368134:AAGgRwPesrfBSPZge8hBK2RrcTHnZyuD33A'
    ADMIN_ID = 403915236
    TDV_CHAIN_ID = -1001280746539

    # MECHANICS
    SENDER_SLEEP = 5
    ENGINE_FIRST = 60
    ENGINE_INTERVAL = 3600


class ConfigurationTest:
    def __init__(self):
        self.mode = 'test'

    # NETWORK
    DOMAINE = 'http://localhost:7111/tdv'

    # TELEGRAM
    BOT_KEY = '1659088524:AAGf2bp963DKltRB2kythMJ68A1_M5bYwKI'
    ADMIN_ID = 403915236
    TDV_CHAIN_ID = -1001292509023

    # MECHANICS
    SENDER_SLEEP = 1
    ENGINE_FIRST = 10
    ENGINE_INTERVAL = 30


CONFIG = Configuration()
