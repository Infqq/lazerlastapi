import requests

class PLAYER:
        def __init__(self, token: str):
                self._token = token

        def get(self, name: str):
                url = "http://api.lazerlast.ru/player.php?player="+name+"&token="+self._token+"&format=json"
                r = requests.get(url).json()
                return r
