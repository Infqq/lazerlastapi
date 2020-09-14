from lazerlastapi import LOBBY

check = LOBBY(token='test')
result = check.get('_GameDoctor_')
print(result)
