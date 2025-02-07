# Дан отсортированный список nums.
# Написать функцию contains(nums, value), которая возвращает True, если
# value содержится в nums и False иначе
import time

# numbers = [1, 2, 2, 3, 4, 5, 8, 44, 55, 63, 77, 256, 2456, 78479, 90679]
numbers = list(range(10 ** 8))


# Решение 0 - O(n)
def contains0(nums, value):
    return value in nums


# Решение 1 - линейный поиск - O(n) = Θ(2n + C)
def contains1(nums, value):
    for num in nums:
        if num == value:
            return True
    return False

# num = nums[0]
# num == value
# num = nums[1]
# num == value
# num = nums[2]
# num == value
# num = nums[3]
# num == value
# num = nums[4]
# num == value
# num = nums[5]
# num == value
# num = nums[6]
# num == value
# num = nums[7]
# num == value
# num = nums[8]
# num == value
#


# Решение 2 - O(log(n))
def contains2(nums, value):
    if not nums:
        return False
    mid_ind = len(nums) // 2
    mid = nums[mid_ind]

    if mid == value:
        return True
    elif value < mid:
        return contains2(nums[:mid_ind], value)
    elif mid < value:
        return contains2(nums[mid_ind + 1:], value)


# Решение 3 - O(log(n))
def contains3(nums, value):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return True
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False


start = time.time()
res = contains3(numbers, -1)
end = time.time()
print(f'N:{len(numbers)}\tTime:{end - start}\tResult:{res}')

# nums[i] - O(1)
