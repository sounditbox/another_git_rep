import asyncio
import datetime

import grequests


async def fetch_data(url):
    print(f"Fetching data from {url}")
    start = datetime.datetime.now()
    res = grequests.get(url)
    end = datetime.datetime.now()
    return f"{url} {start}:{end}"


urls = ["https://api.github.com/users", "https://api.python.org/pypi/",
        'http://www.heroku.com',
        'http://tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://kennethreitz.com'
        ]


# DRY - Don't Repeat Yourself
async def main():
    # Создаем задачи
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    # Ждем выполнения задач и получаем результаты
    responces = []
    for task in tasks:
        response = await task
        responces.append(response)
    print(*responces, sep='\n')


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.run(main())
