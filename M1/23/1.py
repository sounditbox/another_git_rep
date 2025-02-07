# Константная сложность О(1) - от n время работы алгоритма не зависит
# in (set)
# a[i]
# =
# +
# .method()
# Линейная сложность О(n) - от n время работы алгоритма растёт линейно
# В строке через пробел записаны n чисел. Вывести сумму этих чисел
# nums = list(map(int, input().split()))  # O(n)
# s = 0
# for num in nums:  # O(2n)
#     s += num
# print(s)
# O(n) + O(1) + O(2n) + O(1) = O(n + 1 + 2n + 1) = O(3n) = O(n)

# Квадратичная сложность O(n^2)
nums = [5, 2, 8, 3, 6, 2, 1, 1, 4, 5]

n = len(nums)
for i in range(n - 1):  # O(n^2)
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)
