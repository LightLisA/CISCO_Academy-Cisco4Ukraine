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
        self.var1 = vertice1
        self.var2 = vertice2
        self.var3 = vertice3

    def perimeter(self):
        var_1_2 = math.sqrt(math.pow(Point.getx(self.var2) - Point.getx(self.var1), 2) \
                                 + math.pow(Point.gety(self.var2) - Point.gety(self.var1), 2))
        var_1_3 = math.sqrt(math.pow(Point.getx(self.var3) - Point.getx(self.var1), 2) \
                                 + math.pow(Point.gety(self.var3) - Point.gety(self.var1), 2))
        var_2_3 = math.sqrt(math.pow(Point.getx(self.var3) - Point.getx(self.var2), 2) \
                                 + math.pow(Point.gety(self.var3) - Point.gety(self.var2), 2))

        Perimeter = var_1_2 + var_1_3 + var_2_3
        return Perimeter


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
