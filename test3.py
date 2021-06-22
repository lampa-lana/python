from itertools import groupby
import random
import os


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

MAX_NUMBER = 2500

a = [random.randint(0, 9) for _ in range(MAX_NUMBER)]
print(a)
b = (max(reversed([list(g) for _, g in groupby(a)]), key=len))
print(b)

outputefile = 'bignum.txt'
myfile = open(outputefile, 'a+', encoding="UTF-8")

if b:
    myfile.write(" Самая большая последовательность " + str(b) + '\n')
