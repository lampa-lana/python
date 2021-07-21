# from functools import wraps
import sys
import logging
import log_config


# def bread(func):
#     """ это функция lдля хлеба"""
#     @wraps(func)
#     def wrapper(*args):
#         print(' булка ')
#         func(*args)
#     wrapper.__doc__ = 'это функция для хлеба с мяслм'
#     return wrapper


# def ing(func):
#     @wraps(func)
#     def wrapper(*args):
#         print(' сыр ')
#         func(*args)
#         print(' зелень ')
#     return wrapper


# @bread
# @ing
# def sand(meat='мясо'):
#     """ это функция для мяса
#     """
#     print(meat)


# # my_sand = ing(sand)
# # bread(my_sand)
# # sand('курица')
# # print(sand.__doc__)
# # print(sand.__name__)


# def repeat(n):
#     n = int(input(' Введите число: '))

#     def _repeat(f):
#         @wraps(f)
#         def inner(*args, **kwargs):
#             for _ in range(n):
#                 f(*args, **kwargs)
#         return inner
#         # не забываем ее вернуть!

#     return _repeat


# def repeat1(f):
#     def inner(*args, **kwargs):
#         for i in range(10):
#             f(*args, **kwargs)
#     return inner


# @repeat(1)
# def foo():
#     print('hello')


# foo()
# print('---------------------------------------------------------')


# @repeat1
# def foo():
#     print('hello')

# foo()
# -------------------------------------------------------------------------------------------
# logging.basicConfig(filename='sample.log',
#                     level=logging.DEBUG,
#                     format="%(levelname)-10s %(name)-5s %(asctime)s %(message)s",
#                     )

# log = logging.getLogger("app")
# # Записать сообщение, используя позиционные аргументы форматирования
# host = 'localhost'
# port = 7777
# log.critical("Can't connect to %s at port %d", host, port)
# # Записать сообщение, используя словарь значений
# parms = {'host': 'www.python.org',
#          'port': 80
#          }
# log.critical("Can't connect to %(host)s at port %(port)d", parms)


# logging.debug(' This is DEBUG msg ')
# logging.info(' This is INFO msg ')
# logging.warning(' This is WARNING msg ')
# logging.error(' This is ERROR msg ')
# logging.critical(' This is CRITICAL msg ')

# Определить формат сообщений
# format = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

# # Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
# crit_hand = logging.StreamHandler(sys.stderr)
# crit_hand.setLevel(logging.CRITICAL)
# crit_hand.setFormatter(format)

# # Создать обработчик, который выводит сообщения в файл
# applog_hand = logging.FileHandler('app.log')
# applog_hand.setFormatter(format)

# # Создать регистратор верхнего уровня с именем 'app'
# app_log = logging.getLogger('app')
# app_log.setLevel(logging.INFO)
# app_log.addHandler(applog_hand)
# app_log.addHandler(crit_hand)


# app_log.debug(' This is DEBUG msg ')
# app_log.info(' This is INFO msg ')
# app_log.warning(' This is WARNING msg ')
# app_log.error(' This is ERROR msg ')
# app_log.critical(' This is CRITICAL msg ')
# ----------------------------------------------------------------


def trace2(func):
    def callf(*args, **kwargs):
        global app_log
        log_config.app_log.info("Function %s%s call from %s \n" %
                                (func.__name__, args, 'trace2'))
        func(*args, **kwargs)
    return callf


@trace2
def ggg():
    print('Hello')


ggg()
