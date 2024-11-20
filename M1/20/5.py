def select_sort(a):
    for i in range(len(a) - 1):
        min_index = i
        for k in range(i + 1, len(a)):
            if a[k] < a[min_index]:
                min_index = k
        a[i], a[min_index] = a[min_index], a[i]
    return a


arr = [5, 2, 4, 6, 1, 3]
print(select_sort(arr))
