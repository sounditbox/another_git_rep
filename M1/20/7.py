def partition(arr, low, high):
    pivot = arr[high]  # Выбираем последний элемент как опорный
    i = low - 1  # Индекс меньших элементов
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Ставим опорный элемент на правильное место
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Индекс разделения массива на две части
        pi = partition(arr, low, high)
        # Рекурсивно сортируем левую и правую части
        quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Отсортированный массив:", arr)
