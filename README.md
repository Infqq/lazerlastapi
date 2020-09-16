<h1 align="center">LazerLastApi - удобная библиотека для LLAPI</h1>
    <blockquote>Это библиотека, упрощающая работу с LazerLastApi, находится в постояннной разроботке</blockquote>
</p>
<hr>

## Установка
1) С помощью установщика pip из GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/lazerlastapi/archive/master.zip --upgrade
   ```

### Check Online

Библиотека отправляет запрос в АПИ, после проверяет статус.

```python
from lazerlastapi import *

check = PLAYER(token='test')
result = check.get('_GameDoctor_')
print(result)
```

### Check Prison

Больше режимов можно узнать в Examples

```python
from lazerlastapi import *

check = PLAYER(token='test')
result = check.get('_GameDoctor_')
print(result)
```
