# Наследование - subclass(наследник) использует атрибуты и методы superclass'а(родителя)
import math


class Shape: # CamelCase
    def square(self):
        pass

    def perimeter(self):
        pass

    def print_info(self):  # snake_case
        print(f'{self.__class__.__name__}: P:{self.perimeter()}, S:{self.square()}')


class RegularPolygon(Shape):
    def __init__(self, n, l):
        self.n = n
        self.l = l

    def perimeter(self):
        return self.n * self.l

    def square(self):
        return 42


class Rectangle(Shape):
    # magic methods
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(RegularPolygon, Rectangle):
    def __init__(self, a):
        # Rectangle(self, a, a)
        RegularPolygon.__init__(self, 4, a)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def square(self):
        return round(self.r ** 2 * math.pi, 2)

    def perimeter(self):
        return round(self.r * 2 * math.pi, 2)


shapes = [Rectangle(2, 5), Rectangle(10, 200), Square(5), Circle(5)]
for sh in shapes:
    sh.print_info()

