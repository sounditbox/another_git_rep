import threading


def greet(name):
    print(f"Hello, {name}!")


# Создание таймера с аргументами
t = threading.Timer(3.0, greet, args=["Alice"])

t.start()
