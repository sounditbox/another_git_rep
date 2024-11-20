def insertion_sort(arr):
    # Проходим по каждому элементу массива, начиная со второго
    for i in range(1, len(arr)):
        to_insert = arr[i]  # Элемент, который нужно вставить в отсортированную часть
        ind = i - 1
        # Сдвигаем элементы, которые больше key, вправо
        while ind >= 0 and arr[ind] > to_insert:
            arr[ind + 1] = arr[ind]
            ind -= 1
        # Вставляем key на правильное место
        arr[ind + 1] = to_insert
    return arr


# Пример использования
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Отсортированный массив:", sorted_arr)
