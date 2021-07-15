
class Configuration:
    # TELEGRAM
    BOT_KEY = '1794267120:AAGZ4OWaUTl5BtLCZl9Lqy7EjnCofirbaQ8'
    ADMIN_ID = 403915236
    TDV_CHAIN_ID = -1001280746539

    # MECHANICS
    SENDER_SLEEP = 5
    ENGINE_FIRST = 60
    ENGINE_INTERVAL = 10800

    # NewsOrgs :
    NEWS_API_KEY = '8f8d40fbcc36400b832e29f1e3ac67b0'
    NEWS_ORG = 'https://newsapi.org/v2/'
    EVERYTHING = 'everything'
    HEADLINE = 'headline'
    TOP_HEADLINE = 'top-headlines'
    WORDS = []


class ConfigurationTest:
    # TELEGRAM
    BOT_KEY = '1794267120:AAGZ4OWaUTl5BtLCZl9Lqy7EjnCofirbaQ8'
    ADMIN_ID = 403915236
    TDV_CHAIN_ID = 403915236

    # MECHANICS
    SENDER_SLEEP = 1
    ENGINE_FIRST = 5
    ENGINE_INTERVAL = 600

    # NewsOrgs :
    NEWS_API_KEY = '8f8d40fbcc36400b832e29f1e3ac67b0'
    NEWS_ORG = 'https://newsapi.org/v2/'
    EVERYTHING = 'everything'
    HEADLINE = 'headline'
    TOP_HEADLINE = 'top-headlines'
    WORDS = ['bitcoin', 'covid']


CONFIG = ConfigurationTest()
