# filter(func, iter) - возвращает те элементы x из iter,
#                      для которых func(x) == True
# map(func, iter)    - возвращает  элементы y из iter,
#                     полученные с помощью y = func(x), где x - элемент iter

# def last_digit_is_five(elem):
#     return elem % 10 == 5  # True / False
# def digits_sum_greater_than_10(elem):
#     return sum(int(d) for d in str(elem)) > 10


a = [13, 65, 23, 75, 33, 67, 55, 899, 24, 789, 33]
filtered = list(filter(lambda x: x % 10 == 5, a))
filtered2 = list(filter(lambda x: sum(int(d) for d in str(x)) > 10, a))
print(filtered)
print(filtered2)