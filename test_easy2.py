import math
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Side:
    def culc_side(self, A, B):  # чтобы вычислить любые параметры нужна длина стороны фигуры
        return round(math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2))


class Trapezium(Side):
    def __init__(self, A, B, C, D):  # у трапеции 4 вершины
        self._A = A
        self._B = B
        self._C = C
        self._D = D
        self.AB = 0
        self.BC = 0
        self.CD = 0
        self.DA = 0
        self.AC = 0
        self.BD = 0

    def culc_sides(self):  # метод вычисления сторон фигуры сформированного вершинами с использованием формулы родительского класса
        self.AB = self.culc_side(self._A, self._B)
        self.BC = self.culc_side(self._B, self._C)
        self.CD = self.culc_side(self._C, self._D)
        self.DA = self.culc_side(self._D, self._A)
        return (self.AB, self.BC, self.CD, self.DA)

    def culc_diag(self):  # метод вычисления диагонали
        self.AC = math.sqrt((self._C[0]-self._A[0])
                            ** 2 + (self._C[1]-self._A[1]) ** 2)
        self.BD = math.sqrt((self._D[0]-self._B[0])
                            ** 2 + (self._D[1]-self._C[1]) ** 2)
        return (self.AC, self.BD)

    def culc_base(self):  # метод вычисления большого, маленького основания
        if self.culc_sides()[1] < self.culc_sides()[3]:
            self.small_base = self.culc_sides()[1]
            self.big_base = self.culc_sides()[3]
        else:
            self.small_base = self.culc_sides()[3]
            self.big_base = self.culc_sides()[1]
        return(self.small_base,  self.big_base)

    def culc_heigh(self):
        a = self.culc_base()[0]  # пусть a - мал. основание
        b = self.culc_base()[1]  # пусть b - большое основание
        c = self.culc_sides()[0] ** 2  # пусть с - боковая сторона
        d = self.culc_sides()[2] ** 2  # пусть d - боковая сторона

        self.h = round(math.sqrt(c - 1/4 * ((c - d) / (b - a) + b - a) ** 2))
        return self.h

    def culc_perim(self):  # метод вычисления периметра (сумма всех сторон)
        self.P = self.culc_sides()[0] + self.culc_sides()[1] + \
            self.culc_sides()[2]+self.culc_sides()[3]
        return self.P

    def culc_area(self):  # метод вычисления площади
        self.S = round(
            abs((self.culc_base()[0] + self.culc_base()[1]) / 2) * self.culc_heigh())
        return self.S

    def culc_check(self):  # метод проверки равнобедренной трапеции
        if self.culc_diag()[0] == self.culc_diag()[1]:
            return "Равнобедренная трапеция"
        else:
            return "Не равнобедренная трапеция"


trap = Trapezium((1, 2), (6, 7), (8, 10), (5, 10))
print(f'Трапеция со сторонами: {trap.culc_sides()}')
print(f'Периметр трапеции: {trap.culc_perim()}')
print(f'Высота трапеции: {trap.culc_heigh()}')
print(f'Площадь трапеции: {trap.culc_area()}')
print(f'Заданные координаты это: {trap.culc_check()}')
print('-------------------------------------------------------------------------------------------')

trap2 = Trapezium((2, 7), (6, 7), (1, 10), (5, 13))
print(f'Трапеция со сторонами: {trap2.culc_sides()}')
print(f'Периметр трапеции: {trap2.culc_perim()}')
print(f'Высота трапеции: {trap2.culc_heigh()}')
print(f'Площадь трапеции: {trap2.culc_area()}')
print(f'Заданные координаты это: {trap2.culc_check()}')
