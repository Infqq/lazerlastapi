import requests


class lazerlastapi:
    def __init__(self, token: str):
        self._token = token

    def player(self, nickname: str):
        r = requests.get(f"http://api.lazerlast.ru/player.php?token={self._token}&player={nickname}").json()
        return r
    
    def token(self):
        r = requests.get(f"http://api.lazerlast.ru/token.php?token={self._token}").json()
        return r
