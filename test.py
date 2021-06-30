import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Side:
    def culc_side(self, A, B):
        return round(math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2))


class Triangle(Side):
    def __init__(self, A, B, C):
        self._A = A
        self._B = B
        self._C = C

    def culc_sides(self):
        self.AB = self.culc_side(self._A, self._B)
        self.BC = self.culc_side(self._B, self._C)
        self.CA = self.culc_side(self._C, self._A)
        return (self.AB, self.BC, self.CA)

    def culc_perim(self):
        self.P = self.culc_sides()[0] + \
            self.culc_sides()[1] + self.culc_sides()[2]
        return self.P

    def culc_perim_semi(self):
        self.p = self.culc_perim()/2
        return self.p

    def culc_area(self):
        self.S = round(math.sqrt(
            abs(self.culc_perim_semi()*(self.culc_perim_semi()-self.culc_sides()[0])*(self.culc_perim_semi()-self.culc_sides()[1])*(self.culc_perim_semi()-self.culc_sides()[2]))))
        return self.S


A1, A2, A3 = (2, -5), (-6, 2), (6, -2)
triangle = Triangle(A1, A2, A3)
print(f'Треугольник со сторонами: {triangle.culc_sides()}')
print(f'Периметр треугольника: {triangle.culc_perim()}')
print(f'Полупериметр треугольника: {triangle.culc_perim_semi()}')
print(f'Площадь треугольника: {triangle.culc_area()}')
