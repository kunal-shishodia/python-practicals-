import math

class Point2D:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def distance_to(self, other_point):

        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point2D(input(),input())
point2 = Point2D(input(),input())

distance = point1.distance_to(point2)
print(f"The distance between the points is: {distance:.2f}")
