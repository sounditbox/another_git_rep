import datetime


def timed(func):
    def inner(*args):
        start = datetime.datetime.now()
        res = func(*args)
        end = datetime.datetime.now()
        print(f'Функция {func.__name__} с аргументами {args} выполнялась {end - start}')
        return res

    return inner



