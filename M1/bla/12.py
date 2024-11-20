def digits_generator():
    i = 1
    while True:
        print(f'Сейчас напечатаем {i} и выйдем из функции')
        yield i
        i += 1
        print('Возвращаемся в функцию')


gen = digits_generator()
for i in gen:
    print(i)