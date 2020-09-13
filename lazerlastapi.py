import requests


def prison(act, token):
    url = "http://api.lazerlast.ru/prison.php?player="+act+"&token="+token+"&format=json"
    r = requests.get(url).json()
    prison.result = 'Ник: ' + r['username'] + '\nОпыт: ' + r['exp'] + '\nБаланс: ' + r['balance'] + '\nУровень: ' + r['level'] + '\nБлоки: ' + r['blocks'] + '\nКристаллы: ' + r['crist'] + '\nКрысы: ' + r['rats']
