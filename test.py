import math
import random
# EASY
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for index, value in enumerate(fruits, 1):
    print('{} {:>8}'.format(str(index)+'.', value))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 10]

set_a = set(a)  # преобразование в set
set_b = set(b)  # преобразование в set

new_a = set_a - set_b  # вычитание и нахождение разницы м/у set
print(list(new_a))

set_b = set(b)
for i in a.copy():
    if i in set_b:
        a.remove(i)
print(a)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_a = []  # новый список для заполнения
for i in a:
    if i % 2 == 0:  # если число кратно 2, то
        new_a.append(i / 4)  # добавляем в new_a число/4
    else:
        # во всех других случаях добвляем элемент *2 в new_a
        new_a.append(i * 2)
print(new_a)

# NORMAL
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

my_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []  # создаем новый список в который будем добавлять элем с квадратными корнями
for k in my_list:
    if k > 0:  # если элемюбольше нуля, то
        # создаем новую переменную, которая равна квадр корням исход элем
        y = math.sqrt(k)
        if y % int(y) == 0:  # задаем условия , какие из у помещать в новый список, те что делятся без остатка
            # создаем новый список методом append и округдляем элем у
            new_list.append(round(y))
print(new_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

days = {'01': 'первое', '02': 'второе',
        '03': 'третье', '04': 'четертое', '05': 'пятое',  '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одинадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',  '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое',  '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',  '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
months = {'01': 'января', '02': 'февраля',
          '03': 'марта', '04': 'апреля', '05': 'мая',  '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
date = input('Введите дату : ').split('.')

print(days[date[0]] + ' ' + months[date[1]] + ' ' + date[2] + ' ' + ' года')


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

r_list = []  # создаем пустой список
# получаем от пользователя количестиво
count = int(input(" Введите количество производных элементов: "))
# создаем переменню, кот рамдомно выбирает число в дипазоне
# number = random.randint(-100, 100)

for el in range(0, count):
    # создаем цикл , кот. перебирает числа, количеством заданное пользователем
    number = random.randint(-100, 100)
    r_list.append(number)  # добавляем в список числа
print(r_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
lst = [1, 2, 4, 5, 6, 2, 5, 2]
# получаем новый список, созданный с помощью множества set, которое откидывает повторы элементов
lst_set = list(set(lst))
print(lst_set)

lst1 = lst.copy()  # создаем копию первого списка
lst2 = []  # создаем пустой список в который будем доваблять необходимые значения

for item in lst1:  # перебираем lst1
    # если в lst1 методом count, кот. возвращает целое число(int) равное количеству вхождений искомого значение в список, у нашем случае количество == 1
    if lst1.count(item) == 1:
        lst2.append(item)  # добавляем новые элементы в новый список
print(lst2)
