a = [13, 65, 23, 75, 33, 67, 55, 899, 24, 789, 33]
a.sort(key=lambda x: sum(int(d) for d in str(x)))
print(a)