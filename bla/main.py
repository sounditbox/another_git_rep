def f(a, b, *c, d=1, **e):
    print(a, b, c, d, e)

    for arg in e:
        print(f'{arg}: {e[arg]}')


def f2(a, b, c, *d):
    print(a, b, c, d)


# f2(1, bla, 3)
# f2(1, bla, 4, 5)
# f2(1, bla, 4, 5, 6, 7, 8)
# #
f(1, 2)
f(1, 2, 3, 4, 5, 6)
f(1, 2, 3, d=42)
f(1, 2, 3, d=42, f=42, e=111)
