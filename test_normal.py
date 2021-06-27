import os
import sys
import shutil
from test import create_folders, remove_folders, list_dir_func


# def avg(a, b):
#     """Вернуть среднее геометрическое чисел 'a' и 'b'.
#     Параметры:
#         - a, b (int или float).
#     Результат:
#         - float.
#     """
#     if a * b >= 0:
#         return (a * b) ** 0.5
#     else:
#         raise ValueError(
#             " Невозможно определить среднее геометрическое, введеных Вами чисел ")


# # a = float(input("a = "))
# # b = float(input("b = "))
# if __name__ == '__main__':
#     try:
#         a = float(input("a = "))
#         b = float(input("b = "))
#         c = avg(a, b)
#         print("Среднее геометрическое = {:.2f}".format(c))
#     except ValueError as err:
#         print("Ошибка! Вы ввели значения несовместимых типов: " + str(err))
#     except Exception as ve:
#         print("Ошибка: " + str(ve))
#     finally:
#         print('thanks for your cooperation')

# if __name__ == '__main__':
#     avg(a, b)

# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

print('sys.argv = ',
      sys.argv[:], '\nНаберите в консоле python test_normal.py help с новой строки для входа в меню программы')


def choice_help():
    print('help')  # выбор пункта
    print('change_dir')  # сменить папку
    print('look_dir')  # Посмотреть текущую папку
    print('remove_dir')  # Удалить папку <dirname>
    print('create_dir')  # Создать папку <dirname>


def change_dir():
    try:
        path = input('Введите имя папки для перехода: ')
        os.chdir(path)
        print('Успешно перешли в папку: {}'.format(path))
    except FileNotFoundError:
        print(' {} - папки не существует'.format(path))


# словарь действий т функций для них
do = {
    'help': choice_help,
    'change_dir': change_dir,
    'look_dir': list_dir_func,
    'remove_dir': remove_folders,
    'create_dir': create_folders,
}

# связываем действие do (вкл функции) с aргументами sys
try:
    change_dir = sys.argv[2]  # print('change_dir') # сменить папку
except:
    change_dir = None

try:
    ist_dir_func = sys.argv[3]  # print('look_dir') #Посмотреть текущую папку
except:
    ist_dir_func = None

try:
    remove_folders = sys.argv[4]  # print('remove_dir') #Удалить папку
except:
    remove_folders = None

try:
    create_folders = sys.argv[5]  # print('create_dir')# Создать папку
except:
    create_folders = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Не корректный выбор')
        print('Напишите выбор пункта для выбора пункта')
