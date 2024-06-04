import math
from hw20_1_class_Shape import Shape

class Rectangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h

    def perimeter(self):
        return (self.a + self.h) * 2

class Triangle(Shape):
    def __init__(self, base, b, c, h):
        self.base = base
        self.b = b
        self.c = c
        self.h = h

    def area(self):
        return 1/2 * self.base * self.h

    def perimeter(self):
        return self.base + self.b + self.c

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

class RegularHexagon(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.sqrt(3) / 4 * self.r ** 2 * 6    #정삼각형 넓이 * 6개

    def perimeter(self):
        return 6 * self.r

def main():
    # shapes = []
    # shapes.append(Rectangle(2, 1))
    # shapes.append(Triangle(6,5,5,4))
    # shapes.append(Circle(3))
    # shapes.append(RegularHexagon(2))

    shapes = [Rectangle(2, 1),
              Triangle(6, 5, 5, 4),
              Circle(3),
              RegularHexagon(2)]

    for shape in shapes:
        print(f"{shape.__class__.__name__} 넓이: {shape.area():.2f}, 둘레: {shape.perimeter():.2f}")

if __name__ == '__main__':
    main()