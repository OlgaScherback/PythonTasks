class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __add__(self, other):
        return self.square() + other.square()

    def __mul__(self, n):
        return self.square() * n


rect_1 = Rectangle(2, 2)
rect_2 = Rectangle(3, 3)
print(rect_1.square())
print(rect_2.square())
print(rect_1 == rect_2)
print(rect_1 < rect_2)
print(rect_1 + rect_2)
n = 5
print(rect_1 * n)

