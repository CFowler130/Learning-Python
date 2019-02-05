import math


# define getters and setters
# shape needs color and filled
class Shape:
    def __init__(self, color="black", filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled


# rectangle inherits shape, adds length and breadth
class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length + self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


class Square(Shape):

    def __init__(self, length):
        super().__init__()
        self.__length = length

    def area(self):
        return self.__length ** 2


class Triangle(Shape):

    def __init__(self, base=0, height=0):
        super().__init__()
        self.base = base
        self.height = height

    def set_base(self, base):
        self.base = base

    def get_base(self):
        return self.base

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def get_area(self):
        area = self.base * self.height / 2
        return area


r1 = Rectangle(10.5, 2.5)
print("Area of rectangle r1: ", r1.get_area())
print("Perimeter of rectangle r1: ", r1.get_perimeter())
print("Color of rectangle r1: ", r1.get_color())
print("Is rectangle r1 filled? ", r1.get_filled())
r1.set_filled(True)
print("Is rectangle r1 filled? ", r1.get_filled())
r1.set_color("orange")
print("Color of rectangle r1: ", r1.get_color())

c1 = Circle(12)

print("\nArea of circle c1: ", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1: ", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1: ", c1.get_color())
print("Is circle c1 filled? ", c1.get_filled())
c1.set_filled(True)
print("Is circle c1 filled? ", c1.get_filled())
c1.set_color('blue')
print("Color of circle c1: ", c1.get_color())

s1 = Square(5)
print("\nArea of square s1: ", s1.area())
print("Color of square s1: ", s1.get_color())
print("Is square s1 filled? ", s1.get_filled())
s1.set_filled(True)
print("Is square s1 filled? ", s1.get_filled())
s1.set_color("red")
print("Color of square s1: ", s1.get_color())

t1 = Triangle(6, 6)
print("\nArea of triangle t1: ", t1.get_area())
print("Color of triangle t1: ", t1.get_color())
print("Is triangle t1 filled? ", t1.get_filled())
t1.set_filled(True)
print("Is triangle t1 filled? ", t1.get_filled())
t1.set_color("yellow")
print("Color of triangle t1: ", t1.get_color())

# Read Chapters on Tuples and Files
# Create a point class

import math


def testPoint(y=0):
    p1 = Point(3, 4)
    print(p1)
    p2 = Point(3, 0)
    print(p2)
    return math.hypot(dx, dy)


class Point(object):
    COUNT = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def move(self, dx, dy):
        self.X = self.X + dx
        self.Y = self.Y + dy

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx ** 2 + dy ** 2)

    print("distance = %s" % (testPoint()))
