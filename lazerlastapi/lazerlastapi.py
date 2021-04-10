import requests


class lazerlastapi:
        def __init__(self, token: str):
                self._token = token

        def player(self, nickname: str):
                r = requests.get(f"http://api.lazerlast.ru/player.php?player={nickname}&token={self._token}&format=json").json()
                return r.text
