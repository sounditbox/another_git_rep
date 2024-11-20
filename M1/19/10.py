class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def simple_hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.simple_hash(key)
        # Линейное пробирование: ищем следующий свободный слот
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self.simple_hash(key)
        start_index = index  # Чтобы избежать бесконечного цикла
        # Линейное пробирование для поиска элемента
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                return None  # Пройден весь массив
        return None
