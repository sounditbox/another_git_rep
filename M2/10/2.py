class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_method(self) -> None:
        print(self.a, self.b)

    @staticmethod
    def my_static_method():
        print(42)


mc = MyClass(1, 2)
mc.my_method()
mc2 = MyClass(3, 4)
MyClass.my_method(mc2)

MyClass.my_static_method()
mc.my_static_method()
mc2.my_static_method()
