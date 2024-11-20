# Найти n-е число Фиббоначи
import time


# 1 решение - O(2 ** n)
def rec_fib(n):
    if n in (0, 1):
        return n
    return rec_fib(n - 1) + rec_fib(n - 2)


# 2 решение O(n)
def iter_fib(n):
    a, b = 0, 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


start = time.time()
res = iter_fib(12345)
end = time.time()
print(res, end - start)