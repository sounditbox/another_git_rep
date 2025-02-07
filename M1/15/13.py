import asyncio
import time


async def say(what, delay):
    await asyncio.sleep(delay)
    return what


async def main():
    task1 = asyncio.create_task(say('hello', 1))
    task2 = asyncio.create_task(say('world', 1.49999999999999999))
    done, pending = await asyncio.wait([task1, task2], timeout=1.5)
    for task in done:
        print(task.result())
    print(pending)
    time.sleep(0.5)

    
asyncio.run(main())
