from sys import getsizeof

with open('Война и мир.txt') as file:
    content = file.readlines()

print(getsizeof(content))

# 3055908
# 136632

