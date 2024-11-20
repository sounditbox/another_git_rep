import asyncio
import time


async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} starting to fetch data...')
    await asyncio.sleep(sleep_time)
    return {'data': f'Some data from coroutine {id}', 'id': id}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]
    for res in results:
        print(f'Received result: {res}')


start = time.time()
asyncio.run(main())
end = time.time()
print(end - start)
