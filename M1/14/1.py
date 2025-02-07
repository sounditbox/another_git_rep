import http.client

# Создаем соединение с HTTPS-сервером
conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

# Отправляем GET-запрос
conn.request("GET", "/posts/1")

# Получаем ответ
response = conn.getresponse()
print(response.status, response.reason)

# Читаем данные ответа и декодируем их
data = response.read().decode('utf-8')
print(data)

# Закрываем соединение
conn.close()
