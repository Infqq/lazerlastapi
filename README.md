<h1 align="center">LazerLastApi - удобная библиотека для LLAPI</h1>
    <blockquote>Это библиотека, упрощающая работу с LazerLastApi, находится в постояннной разработке</blockquote>
</p>
<hr>

## Установка
1) С помощью установщика pip из GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/lazerlastapi/archive/master.zip --upgrade
   ```

### Пример использования библиотеки

```python
from lazerlastapi import lazerlastapi

api = lazerlastapi(token='test')
result = api.player('_GameDoctor_')
print(result)
```

### Доступные методы
- player
