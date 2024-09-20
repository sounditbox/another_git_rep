# Полиморфизм poly - много morph - форма
# арифм.сложение, конкатенация
import math

# print('ab' + 'cd')


# Оператор + - полиморфен, потому что может подстраиваться под операнды

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 4 * (self.a + self.b)


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Circle:
    def __init__(self, r):
        self.r = r

    def square(self):
        return round(self.r ** 2 * math.pi, 2)

    def perimeter(self):
        return round(self.r * 2 * math.pi, 2)


def get_shape_info(shape):
    return f'{shape.__class__.__name__}: P:{shape.perimeter()}, S:{shape.square()}'


shapes = [Circle(1), Circle(5), Rectangle(2, 5), Rectangle(10, 200), Square(5)]

for sh in shapes:
    print(get_shape_info(sh))


# DRY - Don't Rerpeat Yourself

# Натуральное число n
