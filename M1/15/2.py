import threading


def worker(num, text):
    print(f"Worker {num}: {text}")


# Создаем поток с аргументами
t = threading.Thread(target=worker, args=(1, "Hello"))
t2 = threading.Thread(target=worker, args=(2, "Hello"))


t.start()  # Запустили поток
t2.start()
t.join()  # Ожидаем завершения потока
t2.join()
