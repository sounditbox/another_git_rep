from pprint import pprint

import requests

# Замените 'YOUR_API_KEY' на ваш реальный API ключ
api_key = '67ad722f344bbab57f17ee1dbe5101c9'
city = 'Tbilisi'

# Формируем URL запроса
url = f'http://api.openweathermap.org/data/2.5/weather'
params = {
    'appid': api_key,
    'units': 'metric',
    'lat': 50.6941,
    'lon': 50.8337}
# Отправляем запрос и получаем ответ
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"В городе {city} сейчас: {weather}, температура:{temperature}°C")
    print()
    pprint(data)
else:
    print("Ошибка при получении данных о погоде.")
