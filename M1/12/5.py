from sys import getsizeof

print(getsizeof([]))
print(getsizeof(['1', '2', '3', '4']))
print(getsizeof([['1', '2', '3'], ['4', '5', '6']]))
print(getsizeof(''))
print(getsizeof('1234'))
print(getsizeof('123456'))
