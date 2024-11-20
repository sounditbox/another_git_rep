import requests

import requests

# Данные для отправки
data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com'
}
# Отправка POST-запроса
response = requests.post('https://httpbin.org/post', data=data)
# Вывод ответа сервера
print(response.text)
