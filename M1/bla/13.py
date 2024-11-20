import datetime


def logger(file):
    def dec(func):
        def inner(*args):
            res = func(*args)
            with open(file, 'a') as f:
                f.write(f'Call {func.__name__}{args}: result: {res} at {datetime.datetime.now()}\n')
            return func(*args)

        return inner
    return dec


@logger('logs.txt')
def f(a, b):
    print(a + b)

@logger('logs2.txt')
def f2(a, b):
    print(a + b)

a = b = 42
f(1, 2)
f(1, 3)
f2(1, 3)
f2(2, 3)