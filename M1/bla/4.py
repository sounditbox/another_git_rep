from datetime import datetime

cached = {}  # key-params, value-rusult


# 1 1 bla 3 5 8 13 21 ...

def cache_dec(func):
    def inner(*args):
        if args in cached:
            return cached[args]
        result = func(*args)
        cached[args] = result
        return result

    return inner


def timed(func):
    def inner(*args):
        start = datetime.now()
        res = func(*args)
        end = datetime.now()
        print(f'Функция {func.__name__} с аргументами {args} выполнялась {end - start}')
        return res

    return inner


# @cache_dec
@timed
def fib(n):  # Найти n-е число Фибоначчи
    if n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(30))
