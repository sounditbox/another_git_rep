class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return sum(ord(char) for char in key) % self.size

    def hash2(self, key):
        return 1 + (sum(ord(char) for char in key) % (self.size - 1))

    def insert(self, key, value):
        index = self.hash1(key)
        step = self.hash2(key)
        # Двойное хеширование для поиска свободного места
        while self.table[index] is not None:
            index = (index + step) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        start_index = index
        # Двойное хеширование для поиска элемента
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step) % self.size
            if index == start_index:
                return None  # Пройден весь массив

        return None
