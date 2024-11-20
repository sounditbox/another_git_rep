import asyncio


async def main():
    print('Start of coroutine')
    await asyncio.sleep(1)
    print('End of coroutine')


asyncio.run(main())