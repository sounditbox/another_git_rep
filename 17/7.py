import asyncio

shared_resource = 0

lock = asyncio.Lock()


async def change_shared_resource():
    global shared_resource
    async with lock:
        print(f'Resource before change: {shared_resource}')
        shared_resource += 1
        await asyncio.sleep(1)
        print(f'Resource after change: {shared_resource}')


async def main():
    await asyncio.gather(*(change_shared_resource() for _ in range(5)))


asyncio.run(main())
