
from settings import SETTINGS
from core.database import DATABASE
from core.objects import Article
from sources.newsorg import Newsorg

import requests

newsorg_service = Newsorg(SETTINGS)


def search():

    def newsorg(args):
        # News Org API Search
        for sequence in SETTINGS.SEQUENCES:
            query_args = newsorg_service.create_args(sequence)
            args += newsorg_service.query(SETTINGS.TOP_HEADLINE, query_args).articles

    results = []
    newsorg(results)
    # todo : analyses
    for elem in results:
        DATABASE.insert(Article(None, elem.title, elem.description, elem.url, None).__repr__())

    return results


def create_sequence(args):
    sequence = {}
    for el in args.split(','):
        members = el.split('=')
        if len(members) == 2:
            sequence[members[0]] = members[1]

    SETTINGS.SEQUENCES.append(sequence)


def read_sequence():
    return SETTINGS.SEQUENCES


def delete_sequence(args):
    del SETTINGS.SEQUENCES[int(args)]


def find_by_query(args):
    sequence = {}
    for el in args.split(','):
        members = el.split('=')
        if len(members) == 2:
            sequence[members[0]] = members[1]

    query_args = newsorg_service.create_args(sequence)
    return newsorg_service.query(SETTINGS.TOP_HEADLINE, query_args).articles


def answer():
    r = requests.get('https://baconipsum.com/api/?type=all-meat&sentences=1').json()
    return r[0]
