
from settings import CONFIG
from sources.newsorg import Newsorg

import requests

newsorg_service = Newsorg(CONFIG)


def search():
    newsorg_results = []
    # News Org API Search
    for word in CONFIG.WORDS:
        query_args = newsorg_service.create_args({'q': word})
        newsorg_results += newsorg_service.query(CONFIG.TOP_HEADLINE, query_args).articles

    return newsorg_results


def answer():
    r = requests.get('https://baconipsum.com/api/?type=all-meat&sentences=1').json()
    return r[0]
