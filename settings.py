
class Configuration:
    # TELEGRAM
    BOT_KEY = ''
    ADMIN_ID = 0
    TDV_CHAIN_ID = -1

    # MECHANICS
    SENDER_SLEEP = 5
    ENGINE_FIRST = 60
    ENGINE_INTERVAL = 10800

    # NewsOrgs :
    NEWS_API_KEY = ''
    NEWS_ORG = 'https://newsapi.org/v2/'
    EVERYTHING = 'everything'
    HEADLINE = 'headline'
    TOP_HEADLINE = 'top-headlines'
    SEQUENCES = [
        {'q': 'space'},
        {'country': 'fr', 'category': 'technology'},
        {'country': 'fr', 'category': 'business'},
        {'domains': 'techcrunch.com'}
    ]


class ConfigurationTest:
    # TELEGRAM
    BOT_KEY = ''
    ADMIN_ID = 0  # your admin id from telegram
    TDV_CHAIN_ID = 0  # chain id from telegram

    # MECHANICS
    SENDER_SLEEP = 1
    ENGINE_FIRST = 5
    ENGINE_INTERVAL = 600

    # NewsOrgs :
    NEWS_API_KEY = ''
    NEWS_ORG = 'https://newsapi.org/v2/'
    EVERYTHING = 'everything'
    HEADLINE = 'headline'
    TOP_HEADLINE = 'top-headlines'
    SEQUENCES = [
        {'q': 'bitcoin'},
        {'country': 'fr', 'category': 'technology'},
        {'country': 'fr', 'category': 'business'},
        {'domains': 'techcrunch.com'}
    ]


SETTINGS = ConfigurationTest()
