class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def simple_hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.simple_hash(key)
        bucket = self.table[index]
        # Проверяем, есть ли ключ уже в списке
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                bucket[i] = (key, value)  # Обновляем значение
                return
            # Если ключа нет, добавляем его
            bucket.append((key, value))

    def get(self, key):
        index = self.simple_hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

ht = HashTable(5)
ht.insert("apple", 50)
ht.insert("banana", 30) # Коллизия разрешена методом цепочек
print(ht.table)
print(ht.get("banana")) # Поиск работает корректно