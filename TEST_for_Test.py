import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__var_X = int(x)
        self.__var_Y = int(y)

    def getx(self):
        return self.__var_X

    def gety(self):
        return self.__var_Y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__var_X - x), abs(self.__var_Y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
