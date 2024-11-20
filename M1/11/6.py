class CustomList:
    def __init__(self, *elements):
        self.data = list(elements)

    def __getitem__(self, index):
        """Возвращает элемент по индексу."""
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __setitem__(self, index, value):
        """Присваивает значение элементу по индексу."""
        self.data[index] = value

    def __delitem__(self, index):
        return
        """Удаляет элемент по индексу."""
        # del self.data[index]

    def __repr__(self):
        """Возвращает строковое представление списка."""
        return repr(self.data)


object
# Использование
c_list = CustomList(1, 2, 3, 4, 5)
print(c_list[1])  # Выведет: 2
c_list[1] = 42
print(c_list)  # Выведет: [1, 42, 3, 4, 5]
del c_list[1]
print(c_list)  # Выведет: [1, 3, 4, 5]
