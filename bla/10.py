nums = [i for i in range(10)]

print(nums)
print(list(map(lambda x: x ** 2, nums)))
print(list(map(lambda x: x ** 3, nums)))
print(list(map(float, nums)))
print(list(map(str, nums)))