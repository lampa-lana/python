import os
import sys
import shutil
# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

# -----------------------задача 1-------------------------------------'


def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.
    Параметры:
        - a, b (int или float).
    Результат:
        - float.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError(
            " Невозможно определить среднее геометрическое, введеных Вами чисел ")


# a = float(input("a = "))
# b = float(input("b = "))
if __name__ == '__main__':
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = avg(a, b)
        print("Среднее геометрическое = {:.2f}".format(c))
    except ValueError as err:
        print("Ошибка! Вы ввели значения несовместимых типов: " + str(err))
    except Exception as ve:
        print("Ошибка: " + str(ve))
    finally:
        print('thanks for your cooperation')

if __name__ == '__main__':
    avg(a, b)
# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# -----------------------задача 2-------------------------------------'
# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_folders():
    real_dir = os.getcwd()  # определяем тек директорию
    print("Текущая деректория:", real_dir)
    name = input(' Введите имя для создания ')
    try:
        os.makedirs(name)
        # пробуем создатьб если она не существует
        print('Успешно создана папка: ', name)
    except FileExistsError:
        print('{} - уже существует, невозможно создать'.format(name))


def create_folders_for_easy(name):
    real_dir = os.getcwd()  # определяем тек директорию
    print("Текущая деректория:", real_dir)
    try:
        os.makedirs(name)
        # пробуем создатьб если она не существует
        print('Успешно создана папка: ', name)
    except FileExistsError:
        print('{} - уже существует, невозможно создать'.format(name))


def remove_folders():
    real_dir = os.getcwd()  # определяем тек директорию
    print("Текущая деректория:", real_dir)
    name = input(' Введите имя для удаления ')
    try:
        os.rmdir(name)
        # пробуем удалить директорию если она существует
        print('Успешно удалена папка: ', name)
    except FileNotFoundError:
        print('{} - файла не существует'.format(name))


def remove_folders_for_easy(name):
    real_dir = os.getcwd()  # определяем тек директорию
    print("Текущая деректория:", real_dir)
    try:
        os.rmdir(name)
        # пробуем удалить директорию если она существует
        print('Успешно удалена папка: ', name)
    except FileNotFoundError:
        print('{} - файла не существует'.format(name))


def work_dir():
    answer = input(  # справшиваем у пользователя, что он хочет сделать
        '1. создать папки dir_1 - dir_9 \n'
        '2. удалить папки dir_1 - dir_9 \n'
        '3. Выход  \n'
        'Введите пункт меню для работы с папками: ')
    #num_dirs = range(1,10)
    for i in answer:  # если создать папки б то...
        if i == '1':
            # после ввода единицы запускает перебор от 1 до 9 вклб чтобы добавить к имени директории
            for j in range(1, 10):
                create_folders_for_easy('dir_' + str(j))  # создаем папки
        elif i == '2':  # если удалить папки б то...
            # после ввода двойки запускает перебор от 1 до 9 вклб чтобы удалить все папки с именами перебора
            for k in range(1, 10):
                remove_folders_for_easy('dir_' + str(k))  # удаляем папкм
        elif i == '3':  # если тройка-выход тз цикла
            break


if __name__ == '__main__':
    work_dir()

# -----------------------задача 3-------------------------------------
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
print("Текущая деректория:", os.getcwd())


def list_dir_func():
    """ вывод  списка всех папок и файлов в текущей директории """
    os_list_dir = os.listdir()
    print(os_list_dir)
    for index, value in enumerate(os_list_dir, 1):
        print('{} {}'.format(str(index) + '.', value))


if __name__ == '__main__':
    list_dir_func()

path = os.getcwd()


def list_dir_func2():
    """ вывод  папки текущей директории"""
    for dirs, folders, files in os.walk(path):
        print('Полный путь к текущей директории', dirs)
        print('Папки текущей директории', folders)
        break


if __name__ == '__main__':
    list_dir_func2()

# -----------------------задача 4-------------------------------------

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def clone_func():
    """ Создание копии текущего файла"""
    path2 = os.path.realpath(
        __file__)  # возвращает канонический путь текущего файла, убирая все символические ссылки (если они поддерживаются).
    print(path2)
    path3 = path2 + '_clone.py'  # создаем имя для клона файла
    # если файлб путь которого мы описали выше path3 не существует
    if os.path.isfile(path3) != True:
        # копируем текущий файл и бросаем его в эту же папку
        shutil.copy2(path2, path2 + '_clone.py')
        print(' Файл-копия создан! ')
    else:
        print('Файл уже создан!!!')  # g проверка на уже существующий файл


if __name__ == '__main__':
    clone_func()
