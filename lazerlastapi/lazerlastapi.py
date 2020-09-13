import requests

print('LLAPI was started')
print()

class API:
	def __init__(self, token: str, nick: str):
		self._token = token
		self.nick = nick
		url = "http://api.lazerlast.ru/prison.php?player="+self.nick+"&token="+self._token+"&format=json"
		r = requests.get(url).json()
		result = 'Ник: ' + r['username'] + '\nОпыт: ' + r['exp'] + '\nБаланс: ' + r['balance'] + '\nУровень: ' + r['level'] + '\nБлоки: ' + r['blocks'] + '\nКристаллы: ' + r['crist'] + '\nКрысы: ' + r['rats']

class Prison1():
    def prison(act, token):
        url = "http://api.lazerlast.ru/prison.php?player="+act+"&token="+token+"&format=json"
        r = requests.get(url).json()
        prison.result = 'Ник: ' + r['username'] + '\nОпыт: ' + r['exp'] + '\nБаланс: ' + r['balance'] + '\nУровень: ' + r['level'] + '\nБлоки: ' + r['blocks'] + '\nКристаллы: ' + r['crist'] + '\nКрысы: ' + r['rats']
