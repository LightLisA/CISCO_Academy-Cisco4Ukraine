import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__var_X = int(x)
        self.__var_Y = int(y)

    def getx(self):
        return self.__var_X

    def gety(self):
        return self.__var_Y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__v_A_x = Point.getx(vertice1)
        self.__v_A_y = Point.gety(vertice1)

        self.__v_B_x = Point.getx(vertice2)
        self.__v_B_y = Point.gety(vertice2)

        self.__v_C_x = Point.getx(vertice3)
        self.__v_C_y = Point.gety(vertice3)

    def perimeter(self):
        return math.sqrt((self.__v_B_x - self.__v_A_x) ** 2 + (self.__v_B_y - self.__v_A_y) ** 2) + \
               math.sqrt((self.__v_C_x - self.__v_A_x) ** 2 + (self.__v_C_y - self.__v_A_y) ** 2) + \
               math.sqrt((self.__v_B_x - self.__v_C_x) ** 2 + (self.__v_B_y - self.__v_C_y) ** 2)


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
