import asyncio
import random


async def coro(t):
    await asyncio.sleep(t)
    return 42


async def main():
    fut = await coro(1)

    print(fut)

if __name__ == '__main__':
    asyncio.run(main())