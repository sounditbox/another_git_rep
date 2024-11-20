import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    async with asyncio.TaskGroup() as tg:
        print(f"started at {time.strftime('%X')}")
        tg.create_task(say_after(1, 'hello'))
        tg.create_task(say_after(2, 'world'))
        print(f"finished at {time.strftime('%X')}")
    print("Both tasks have completed now.")
asyncio.run(main())