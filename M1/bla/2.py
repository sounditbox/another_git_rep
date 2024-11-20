# Функции высшего порядка

called_funcs = []


def call_recorder(func):
    def inner(*args, **kwargs):
        called_funcs.append(func.__name__)
        return func(*args, **kwargs)

    return inner


@call_recorder
def hello():
    print('Привет!')


def hello2():
    print('Привет!')


hello2 = call_recorder(hello2)

hello()
hello2()
hello()
hello2()
print(called_funcs)
