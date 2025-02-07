class MyClass:
    def method(self, arg1, arg2):
        print(self.__class__.__name__, arg1, arg2)


class AnotherClass:
    pass

a = AnotherClass()
MyClass.method(a, 1, 2)