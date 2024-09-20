from math import sqrt


class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        """Определяет поведение оператора <"""
        if isinstance(other, Vector2d):
            return sqrt(self.x ** 2 + self.y ** 2) < sqrt(
                other.x ** 2 + other.y ** 2)
        return NotImplemented

    def __le__(self, other):
        """Определяет поведение оператора <="""
        if isinstance(other, Vector2d):
            return sqrt(self.x ** 2 + self.y ** 2) <= sqrt(
                other.x ** 2 + other.y ** 2)
        return NotImplemented

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __truediv__(self, other): # /
        pass

    def __divmod__(self, other): # //
        pass

    def __mul__(self, other):  # *
        pass

    def __pow__(self, power, modulo=None):  # **
        pass

    def __mod__(self, other):  # %
        pass


    def __repr__(self):
        """Определяет кодовое представление объекта"""
        return f"Vector2d({self.x}, {self.y})"


v1 = Vector2d(5, 5)
v2 = Vector2d(-2, 8)
v3 = v1 - v2
print(v3)
# print(v1 < v2)
# print(v1 == v2)
# print(v1 <= v2)
# print(v1 != v2)
# print(v1 >= v2)
# print(v1 > v2)
# print(v1)