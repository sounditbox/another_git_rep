a = [1, 5, 2, 6, 9, 34, 9, 4]
# a.sort()  # Quick sort O(n * log(n))
# Bubble sort
n = len(a) - 1
for i in range(n):  # O(n**2)
    for j in range(n):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j + 1], a[j]
print(a)
