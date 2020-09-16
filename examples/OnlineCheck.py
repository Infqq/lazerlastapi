from lazerlastapi import *

check = PLAYER(token='test')
result = check.get('_GameDoctor_')
print(result)
