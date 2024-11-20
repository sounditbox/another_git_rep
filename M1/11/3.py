# iterable
a = 'aethaet'

try:
    iterator = iter(a)
    while True:
        i = next(iterator)
        print(i)
except StopIteration:
    pass
