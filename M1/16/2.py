import asyncio


def my_callback():
    print("Эта функция будет выполнена как можно скорее!")


loop = asyncio.get_event_loop()
loop.call_soon(my_callback)
loop.run_forever()
