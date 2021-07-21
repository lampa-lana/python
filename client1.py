import socket
import time
import threading
import json
import sys
import logging
from log_config import app_log


def trace(func):
    def callf(*args, **kwargs):
        app_log.critical("CRITICAL!!! Function %s %s %s call from %s \n" %
                         (func.__name__, args, kwargs, 'trace'))
        func(*args, **kwargs)
    return callf


def trace2(func):
    def callf(*args, **kwargs):
        app_log.info("Function %s  %s  %s call from %s \n" %
                     (func.__name__, args, kwargs, 'trace2'))
        func(*args, **kwargs)

    return callf


class Client:
    def __init__(self):
        # логические флаги об отключении и подключении клиента
        self.shutdown = False
        self.join = False

    @trace
    def receving(self, name, sock):
        self.name = name
        self.sock = sock
        while not self.shutdown:  # функция для приема  сообщений с сервера
            try:
                while True:
                    data, addr = self.sock.recvfrom(1024)  # получаем сообщения
                    print(data.decode('utf-8'))  # декодируем сообщения
                    time.sleep(0.2)  # ждем 0.2 секунды на всякий случай
            except:
                pass

    @trace2
    def get_client(self):
        self.server = ('localhost', 9090)
        # создаем анворгичный сокет как у сервера
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.connect(('localhost', 0))  # конектимся с сервером
        self.name = input('Name: ')

        # делим потоки для получения сообщений
        rT = threading.Thread(target=self.receving,
                              args=(self.name, self.s))
        rT.start()

        while not self.shutdown:
            if not self.join:
                self.s.sendto(
                    ('[' + self.name + '] => join chat ').encode('utf-8'),  self.server)
                self.join = True
            else:
                try:
                    message = input('[You] :: ')
                    if message != '':  # кодируем сообщение
                        self.qust = {'action': 'msg_from_chat',
                                     'time': time.strftime(
                                         '%Y-%m-%d-%H.%M.%S', time.localtime()),
                                     'message': message,
                                     'user': {'name': self.name,
                                              'status': 'online'}}

                        with open('cl_json.json', 'a+', encoding='UTF-8') as f:
                            json.dump(self.qust, f, sort_keys=True,
                                      indent=2,  ensure_ascii=False)
                        self.s.sendto(('[' + self.name + ']  ::  ' + ' - ' + message + '-'
                                       ).encode('utf-8'), self.server)  # указываем само сообщение и куда его отправить

                    time.sleep(0.2)

                except:
                    self.s.sendto(
                        ('[' + self.name + '] < = left chat ').encode('utf-8'), self.server)
        rT.join()  # закрываем потоки
        self.s.close()  # закрываем соединение


d = Client()
d.get_client()
