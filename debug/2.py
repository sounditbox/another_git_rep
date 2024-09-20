
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:  # Выполняется, если не было исключений
    print('Ошибок нет')
finally:
    print('Конец программы')
