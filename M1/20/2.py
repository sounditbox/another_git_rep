def rec_fact(n: int):
    if n in (0, 1):
        return 1
    return rec_fact(n - 1) * n


def iter_fact(n):
    res = 0
    for i in range(1, n + 1):
        res *= i
    return res


print(rec_fact(5))
