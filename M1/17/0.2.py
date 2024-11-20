import asyncio
import aiohttp
import time


async def bound_fetch(sem, session, url):
    async with sem, session.get(url) as response:
        return await response.text()


async def run_batch(batch_size, total_requests, url):
    sem = asyncio.Semaphore(batch_size)
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(total_requests):
            task = asyncio.create_task(bound_fetch(sem, session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return responses


def main():
    url = 'https://httpbin.org/get'
    total_requests = 100
    batch_size = 50

    start = time.time()
    asyncio.run(run_batch(batch_size, total_requests, url))
    print(time.time() - start)


if __name__ == '__main__':
    main()
