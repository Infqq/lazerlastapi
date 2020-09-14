from lazerlastapi import LW

check = LW(token='test')
result = check.get('_GameDoctor_')
print(result)
