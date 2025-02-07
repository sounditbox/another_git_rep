class Function:
    def __call__(self, *args, **kwargs):
        return 42


def f():
    return 42

f2 = Function()


def print_obj(obj):
    print(obj.__class__.__name__, dir(obj))


#print_obj(f)
func = f

print(func())
#print_obj(f2)
