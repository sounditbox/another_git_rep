# Функции высшего порядка

def logger(inner_func):
    print(f'Вызов функции {inner_func.__name__}')
    inner_func()
    print('Конец внешней функции')


def hello():
    print('Привет!')


def goodbye():
    print('Пока!')


logger(hello)
logger(goodbye)
