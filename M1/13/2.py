import pickle


class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c  # Не будем сериализовать атрибут c

    def __getstate__(self):
        return {'a': self.a, 'b': self.b}


# Создаем объект
obj = MyClass(1, 2, 3)
print(type(obj))
# Сериализуем
data = pickle.dumps(obj)
print(data)



# Десериализуем
new_obj = pickle.loads(data)
print(new_obj.a, new_obj.b)  # Вывод: 1 2
print(type(new_obj))
print(hasattr(new_obj, 'c'))  # Вывод: False
