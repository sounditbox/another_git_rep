# global
# nonlocal
# local

def f():
    global gl
    lol = 34
    gl += 123


gl = 42
f()
print(gl)