import asyncio

# Получение текущего цикла событий
loop = asyncio.get_event_loop()
print("Current event loop:", loop)
# Создание нового цикла событий
new_loop = asyncio.new_event_loop()
print("New event loop:", new_loop)
# Установка нового цикла событий как текущего
asyncio.set_event_loop(new_loop)
print("Current event loop after setting:", asyncio.get_event_loop())


# Определение асинхронной функции
async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

print(greet())

new_loop.call_soon()
# Запуск цикла событий до завершения конкретной задачи
new_loop.run_until_complete(greet())
# Проверка, запущен ли цикл событий
print("Is the loop running?", new_loop.is_running())
# Остановка цикла событий
new_loop.stop()
# Закрытие цикла событий
new_loop.close()