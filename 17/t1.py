# Задача 1: Асинхронные HTTP-запросы
# С помощью библиотеки aiohttp напишите асинхронную функцию,
# которая получает данные из списка URL-адресов одновременно и
# выводит длину содержимого, полученного с каждого URL.

import asyncio
import time

import aiohttp
import requests

urls = ['https://github.com', 'https://youtube.com', 'https://ya.ru',
        'https://chatgpt.com', 'https://pumble.com', 'https://telegram.org']


# def main():
#     for url in urls:
#         response = requests.get(url)
#         print(len(response.content))


async def get_data_length(session, url):
    response = await session.get(url)
    return len(await response.text())


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.create_task(get_data_length(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        print(*results, sep='\n')


start = time.time()
asyncio.run(main())
end = time.time()
print(f'Time spent: {end - start}')
