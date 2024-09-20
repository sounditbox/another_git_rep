import requests
from requests.auth import HTTPBasicAuth

with requests.Session() as session:
    # Аутентификация
    response = session.post('https://httpbin.org/post',
                            auth=HTTPBasicAuth('user', 'pass'))
    # Последующие запросы с использованием сессии
    response = session.get('https://httpbin.org/get')
    print(response.text)
