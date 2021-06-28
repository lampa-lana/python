import os
import argparse
from test import create_folders, remove_folders, list_dir_func


print('Наберите в консоле python test_hard.py -h  с новой строки для входа в меню программы')
parser = argparse.ArgumentParser()


parser.add_argument(
    '--action', default='help', choices=['touch', 'rm', 'rmd', 'ls', 'mkdir', 'change'],
    help='\t Какой пункт меню вы выбирате?: \n '
    '\n  --action change - сменить папку; \n '
    '\n --action rmd - удалить папку; \n '
    '\n --action rm - удалить файл; \n '
    ' \n --action ls - посмотреть путь папок; \n '
    '\n --action mkdir - создать папку; \n '
    '\n --action touch - создать файл; \n ')

args = parser.parse_args()

# print(args)


def change_dir():
    try:
        path = input('Введите имя папки для перехода: ')
        os.chdir(path)
        print('Успешно перешли в папку: {}'.format(path))
        print(os.getcwd())
    except FileNotFoundError:
        print(' {} - папки не существует'.format(path))


def create_file():
    file_path = input('Имя файла: ')
    try:
        fp = open(file_path, 'r')
        print('Такой файл уже существует!')
    except IOError:
        fp = open(file_path, 'w+')
        print(' Ваш файл создан!')


def remove_file():
    file_path = input('Имя файла: ')
    if os.path.isfile(file_path):
        os.remove(file_path)
        print('Ваш файл удален!')
    else:
        print(' Файла не существует!!! ')


if args.action == 'change':
    change_dir()
elif args.action == 'rmd':
    remove_folders()
    print(os.getcwd())
elif args.action == 'ls':
    list_dir_func()
elif args.action == 'mkdir':
    create_folders()
    print(os.getcwd())
elif args.action == 'touch':
    create_file()
    print(os.getcwd())
elif args.action == 'rm':
    remove_file()
    print(os.getcwd())
