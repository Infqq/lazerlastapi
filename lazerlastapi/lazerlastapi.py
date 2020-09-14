import requests

print('LLAPI was started')
print()

class PRISON:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/prison.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                result = 'Ник: ' + r['username'] + '\nОпыт: ' + r['exp'] + '\nБаланс: ' + r['balance'] + '\nУровень: ' + r['level'] + '\nБлоки: ' + r['blocks'] + '\nКристаллы: ' + r['crist'] + '\nКрысы: ' + r['rats']
                return result
