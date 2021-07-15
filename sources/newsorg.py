
import requests
from requests import RequestException
from sources.objects import Result


class Newsorg:
    def __init__(self, config):
        self._config = config

    @staticmethod
    def create_args(query):
        more = False
        args = '?'
        for key in query.keys():
            if key == 'q':
                if more:
                    args += '&'
                args += 'q={0}'.format(query['q'])
                more = True

            if key == 'from':
                if more:
                    args += '&'
                args += 'from={0}'.format(query['from'])
                more = True

            if key == 'to':
                if more:
                    args += '&'
                args += 'to={0}'.format(query['to'])
                more = True

            if key == 'sortBy':
                if more:
                    args += '&'
                args += 'sortBy={0}'.format(query['sortBy'])
                more = True

            if key == 'sources':
                if more:
                    args += '&'
                args += 'sources={0}'.format(query['sources'])
                more = True

            if key == 'country':
                if more:
                    args += '&'
                args += 'country={0}'.format(query['country'])
                more = True

            if key == 'domains':
                if more:
                    args += '&'
                args += 'domains={0}'.format(query['domains'])
                more = True

            if key == 'category':
                if more:
                    args += '&'
                args += 'category={0}'.format(query['category'])
                more = True

        return args

    def query(self, qtype, args):

        if qtype == self._config.EVERYTHING:
            try:
                url = self._config.NEWS_ORG + self._config.EVERYTHING + args + '&apiKey=' + self._config.NEWS_API_KEY
                requete = requests.get(url)
                page = requete.json()
                return Result(page)
            except RequestException:
                return {}

        if qtype == self._config.TOP_HEADLINE:
            try:
                url = self._config.NEWS_ORG + self._config.TOP_HEADLINE + args + '&apiKey=' + self._config.NEWS_API_KEY
                requete = requests.get(url)
                page = requete.json()
                return Result(page)
            except RequestException:
                return {}
        return None
