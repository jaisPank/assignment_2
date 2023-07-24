import math


class Shape:
    def get_area(self):
        raise NotImplementedError("Function Not Implemented")


class Rectangle(Shape):
    def __init__(self, length, width):
        if length > 0 and width > 0:
            self.length = length
            self.width = width
        else:
            raise ValueError("Dimensions Error")

    def get_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("Radius Error")

    def get_area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, base, height):
        if base > 0 and height > 0:
            self.base = base
            self.height = height
        else:
            raise ValueError("Dimensions Error")

    def get_area(self):
        return 0.5 * self.base * self.height


rectangle = Rectangle(5, 5)
print("Rectangle Area:", rectangle.get_area())

circle = Circle(5)
print("Circle Area:", circle.get_area())

triangle = Triangle(5, 5)
print("Triangle Area:", triangle.get_area())


