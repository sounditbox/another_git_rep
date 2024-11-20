class StaticArray:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size  # Создаём массив с фиксированным количеством элементов

    def __getitem__(self, index):
        """Получение элемента по индексу."""
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Индекс вне диапазона")

    def __setitem__(self, index, value):
        """Изменение элемента по индексу."""
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Индекс вне диапазона")


arr = StaticArray(5)  # Создаем статический массив размером
# 5
arr[0] = 10
print(arr[0])  # Выведет: 10
