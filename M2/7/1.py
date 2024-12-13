# global
# nonlocal
# local

gl = 42


def f():
    def g():
        lol = 45

        print(gl, nonl, lol)

    nonl = 34
    g()

f()
