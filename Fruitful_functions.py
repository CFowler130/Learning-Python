#  Fruitful Functions

import math


# Return Values
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


# Incremental Development
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is ', dx)
    print('dy is ', dy)
    return 0.0


print(distance(1, 2, 4, 6))


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result


print(distance(1, 2, 4, 6))


# Function Composition
def area(radius):
    return math.pi * radius ** 2


def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


# composed
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


# Boolean Functions
# example 1
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


is_even(24)
is_even(103)


# example 2
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


print(is_divisible(24, 2))
print(is_divisible(113, 2))
