import asyncio


async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} starting to fetch data...')
    await asyncio.sleep(sleep_time)
    return {'data': f'Some data from coroutine {id}', 'id': id}


async def main():
    tasks = asyncio.gather(fetch_data(1, 2),
                           fetch_data(2, 1),
                           fetch_data(3, 3))

    results = await tasks
    for res in results:
        print(f'Received result: {res}')


asyncio.run(main())
