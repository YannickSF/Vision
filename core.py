
from settings import CONFIG
import requests


def core_get_engine(*args):
    r = requests.get(CONFIG.DOMAINE + '/engine')
    data = r.json()
    return data['words']


def core_post_engine(*args, words):
    payload = {'word_list': [i.strip() for i in words.split(',')]}
    r = requests.post(CONFIG.DOMAINE + '/engine', json=payload)
    return "Code[" + str(r.status_code) + "]| Nouvelles données enregistré dans l'engine : " \
           + ' | '.join(payload['word_list'])


def core_delete_engine(*args, word):
    r = requests.delete(CONFIG.DOMAINE + '/engine/' + word)
    retour = r.json()
    return "Nouvelle liste : " + ' | '.join(retour['list'])


def core_get_articles(*args):
    r = requests.get(CONFIG.DOMAINE + '/article')
    data = r.json()
    return data['articles']


def core_search(*args, sch_type, keyword):
    payload = {'type': sch_type, 'keyword': keyword}
    r = requests.post(CONFIG.DOMAINE + '/search', json=payload)
    return r.json()