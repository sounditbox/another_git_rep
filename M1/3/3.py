class A:
    def __init__(self, number=17):
        self.number = number

a = A(42)
a2 = A()
print(a.number)
print(a2.number)