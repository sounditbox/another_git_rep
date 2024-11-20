import asyncio
import time


async def fetch_data(delay, id):
    print(f'Fetching data... id: {id}')
    await asyncio.sleep(delay)
    print(f'Data fetched, id: {id}')
    return {'data': 'Some data', 'id': id}


async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    result2 = await task2

    print(f'Received result: {result1}')
    print(f'Received result: {result2}')

start = time.time()
asyncio.run(main())
end = time.time()
print(end - start)

