import asyncio


async def get_future_result(future, value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"Set the future's result to {value}")
    await asyncio.sleep(2)


async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    await asyncio.create_task(get_future_result(future, 42))

    result = await future
    print(f"Received the future's result: {result}")


asyncio.run(main())
