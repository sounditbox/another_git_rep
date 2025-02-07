def rec_bin_search(arr, value):
    if not arr:
        return False
    mid_ind = len(arr) // 2
    mid = arr[mid_ind]
    if mid == value:
        return True
    elif mid < value:
        return rec_bin_search(arr[mid_ind + 1:], value)
    elif value < mid:
        return rec_bin_search(arr[:mid_ind], value)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 42]
print(rec_bin_search(l1, -1))
