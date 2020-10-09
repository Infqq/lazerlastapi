import requests

class PRISON:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/prison.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                try:
                        result = 'Ник: ' + r['username'] + '\nОпыт: ' + r['exp'] + '\nБаланс: ' + r['balance'] + '\nУровень: ' + r['level'] + '\nБлоки: ' + r['blocks'] + '\nКристаллы: ' + r['crist'] + '\nКрысы: ' + r['rats']
                except:
                        result = r['error']
                return result

class MLF:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/mlf.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                try:
                        result = 'Ник: ' + r['username'] + '\n$/сек: ' + r['production'] + '\nБаланс: ' + r['balance']
                except:
                        result = r['error']
                return result

class LW:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/luckywars.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                try:
                        result = 'Ник: ' + r['username'] + '\nБаланс: ' + r['money'] + '\nУбийств: ' + r['kills'] + '\nСмертей: ' + r['deaths'] + '\nПобеды: ' + r['wins']
                except:
                        result = r['error']
                return result
        
class LOBBY:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/lobby.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                try:        
                        result = 'Ник: ' + r['username'] + '\nОпыт: ' + r['exp'] + '\nКоины: ' + r['coin'] + '\nУровень: ' + r['level']
                except:
                        result = r['error']
                return result

class PLAYER:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/online.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                try:        
                        result = 'Ник: ' + name + '\nСтатус: ' + r['status']
                except:
                        result = r['error']
                return result

class TEST:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/prison.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                try:
                        result = 'Ник: ' + r['username'] + '\nОпыт: ' + r['exp'] + '\nБаланс: ' + r['balance'] + '\nУровень: ' + r['level'] + '\nБлоки: ' + r['blocks'] + '\nКристаллы: ' + r['crist'] + '\nКрысы: ' + r['rats']
                        username = 'Ник: ' + r['username']
                        exp = '\nОпыт: ' + r['exp']
                        balance = '\nБаланс: ' + r['balance']
                        level = '\nУровень: ' + r['level']
                        blocks = '\nБлоки: ' + r['blocks']
                        crist = '\nКристаллы: ' + r['crist']
                        rats = '\nКрысы: ' + r['rats']
                except:
                        result = r['error']
                return result
