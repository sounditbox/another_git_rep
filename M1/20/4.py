from functools import lru_cache


def memoize(f):
    memo = {}
    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]

    return helper


@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(42))