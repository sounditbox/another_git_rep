def logger(func):
    def inner(n):
        res = func(n)
        print(f'{func.__name__}({n}) = {res}')
        return res

    return inner


def square(n):
    return n ** 2

square = logger(square)

print(square(42))
print(square(123))
print(square(45))