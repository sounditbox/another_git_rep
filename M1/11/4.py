# Duck Typing

class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ReverseIterator(self.data)


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item


class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.prev = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.prev, self.index = self.index, self.index - 1
        return item


# Использование
my_iterable = MyIterable([1, 2, 3, 4])
for item in my_iterable:
    print(item)
