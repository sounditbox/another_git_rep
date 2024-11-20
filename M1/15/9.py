# Пример: Простая корутина
import asyncio


async def greet():
    print('Hello')
    # Симулируем асинхронную операцию
    await asyncio.sleep(1)
    print('world!')


asyncio.run(greet())
