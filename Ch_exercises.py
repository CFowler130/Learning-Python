# 1. Write a function called distance_between_points that takes two Points as arguments and returns the distance
# between them.


class Point(object):

point_one = Point()
point_two = Point()

point_one.x, point_one.y = 6.0, 1.0
point_two.x, point_two.y = 2.0, 6.0


def distance_between_points(p1, p2):
    delta_x = p2.x - p1.x
    delta_y = p2.y - p1.y
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

print("The distance between point one at (%g,%g)" % (point_one.x, point_one.y)),
print("and point two at (%g,%g)" % (point_two.x, point_two.y)),
print("is %.3f" % distance_between_points(point_one, point_two))


# 2. Write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy. It should change
# the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner.

class Point(object):


class Rectangle(object):

rectangle = Rectangle()

bottom_left = Point()
bottom_left.x = 3.0
bottom_left.y = 5.0

top_right = Point()
top_right.x = 5.0
top_right.y = 10.0

rectangle.corner1 = bottom_left
rectangle.corner2 = top_right

dx = 5.0
dy = 12.0


def move_rectangle(rectangle, dx, dy):
    print ("The rectangle started with bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and top right corner at (%g,%g)."
           % (rectangle.corner2.x, rectangle.corner2.y)),
    print("dx is %g and dy is %g" % (dx, dy))
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print ("It ended with a bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and a top right corner at (%g,%g)"
           % (rectangle.corner2.x, rectangle.corner2.y))

move_rectangle(rectangle, dx, dy)

# 3. Work Exercise 15-1 at the end of Chapter 15.

from Point1 import Rectangle, Point
from Point1_soln import distance_between_points


class Circle:


def point_in_circle(point, circle):
    return distance_between_points(point, circle) >= circle.radius


def rect_in_circle(rect, circle):

    # Upper left corner
    point = Point()
    point.x = rect.corner.x
    point.y = rect.corner.y
    if not point_in_circle(circle, point):
        return False

    # Upper right corner
    point = Point()
    point.x = rect.corner.x + rect.width
    point.y = rect.corner.y
    if not point_in_circle(circle, point):
        return False

    # Bottom left corner
    point = Point()
    point.x = rect.corner.x
    point.y = rect.corner.y - rect.height
    if not point_in_circle(circle, point):
        return False

    # Bottom right corner
    point = Point()
    point.x = rect.corner.x + rect.width
    point.y = rect.corner.y - rect.height
    if not point_in_circle(circle, point):
        return False
    return True


def rect_circle_overlap(circle, rect):

    # top left corner
    point = Point()
    point.x = rect.corner.x
    point.y = rect.corner.y
    if point_in_circle(circle, point):
        return True

    point = Point()
    point.x = rect.corner.x + rect.width
    point.y = rect.corner.y
    if point_in_circle(circle, point):
        return True

    point = Point()
    point.x = rect.corner.x
    point.y = rect.corner.y - rect.height
    if point_in_circle(circle, point):
        return True

    point = Point()
    point.x = rect.corner.x + rect.width
    point.y = rect.corner.y - rect.height
    if point_in_circle(circle, point):
        return True
    return False


def main():
    center = Point()
    center.x = 10
    center.y = 10

    circle = Circle()

    circle.center = center
    circle.radius = 30

    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = 10
    rect.corner.y = 10
    rect.width = 5
    rect.height = 5

    print(point_in_circle(circle, center))
    print(rect_in_circle(circle, rect))
    print(rect_circle_overlap(circle, rect))