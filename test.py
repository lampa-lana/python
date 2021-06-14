import math
import random
# EASY
# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили


def convert(km):
    if km > 0:
        miles = km * 1.609
        print(miles)
    else:
        print(" Задайте положительное число!")


convert(int(input(' Введите количество км для перевода в мили: ')))

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    # Чтобы сохранить определенное количество разрядов после запятой число следует сначала сдвинуть влево на соответствующее число разрядов,
    number = number*(10**ndigits)+0.41
    number = number//1  # Дробная часть числа равна остатку от его деления на единицу
    # взять  целую часть числа и сдвинуть обратно в право на столько же разрядов
    return number/(10**ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        # перевод переменной в строку, чтобы сделать срезы строки и отдельно посчитать их
        num = str(ticket_number)
        lst1 = int(num[:1]) + int(num[1:2]) + \
            int(num[2:3])  # складываем первые три знака
        lst2 = int(num[-1]) + int(num[-2]) + \
            int(num[-3])  # складываем последние три знака
        if lst1 == lst2:  # если сумма справа и слева номера билета равны - возвращаем true
            return True
    else:
        return False  # в противном случае - возвращаем false


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


# Normal
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a, b = 1, 1  # первые элементв ряда
    lst = [1, ]  # создание списка для заполнения ряда
    for i in range(m):  # перебор циклом ряда до значения m
        a, b = b, a + b  # порядок формирования элем в ряду значение "a" становится 'b', a'b' -считается как сумма пред элементов
        lst.append(a)  # добавляем элементы в список
    return lst[n - 1: m]  # возвращаем список в срезе заданных элементов


print('fibonacci(1, 6): ', fibonacci(
    int(input(' Введите число n: ')), int(input(' Введите число m: '))))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                # Меняем элементы
                origin_list[i], origin_list[i +
                                            1] = origin_list[i + 1], origin_list[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return origin_list


z = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(z)
print(z)
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

numbers = [10, 4, 2, -1, 6]
print(list(filter(lambda x: x < 5, numbers)))


def filt(num):
    new_l = []
    for i in num:
        if i < 5:
            new_l.append(i)
    return new_l


print(filt([10, 4, 2, -1, 6]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False


print(is_parallelogram((-3, 11), (12, -4), (1, -7), (-14, 8)))
print(is_parallelogram((3, 11), (12, -4), (1, -7), (-14, 8)))
