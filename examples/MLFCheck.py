from lazerlastapi import MLF

check = MLF(token='test')
result = check.get('_GameDoctor_')
print(result)
