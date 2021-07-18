import socket
import time
import json
import re

# answer = {'response': code,
#           'time': time,
#           'user': {'name': name,
#                    'status': 'online'},
#           'message': message}

# настройки хоста и порта


class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self. file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 9090
        self.clients = []  # список подключаемых клиентов

    def get_server(self):
        self.s = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)  # создаем сокет
        self.s.bind((self.host, self.port))  # присвоение хоста и порта
        self.quit = False
        print('[Server Srartet]')

        while not self.quit:  # пока есть запросы на подключение от клиента
            try:
                # получаем данные клиентов данные, адрес и их максимальное количество которое можно принять от клиента
                self.data, self.addr = self.s.recvfrom(1024)

                if self.addr not in self.clients:
                    self.clients.append(self.addr)
                itsatime = time.strftime(
                    '%Y-%m-%d-%H.%M.%S', time.localtime())  # текущее время
                print('[' + self.addr[0] + '] = [' + str(self.addr[1]) +
                      '] = [' + itsatime + '] /', end='')
                print(self.data.decode('utf-8'))
                for client in self.clients:
                    if self.addr != client:
                        self.s.sendto(self.data, client)
                for client in self.clients:
                    if self.addr == client:
                        r = self.data.decode('utf-8')
                        l = r.find(':')
                        name = r[:l]
                        t = self.data.decode('utf-8')
                        m = t.find(' - ')
                        n = t.find('**')
                        message = t[m:n]
                        self.answ = {'response': '202',
                                     'time': time.strftime(
                                         '%Y-%m-%d-%H.%M.%S', time.localtime()),
                                     'user': {'name': name,
                                              'status': 'online'},
                                     'message': message}
                        with open('cl_json.json', 'a+', encoding='UTF-8') as f:
                            json.dump(self.answ, f, sort_keys=True,
                                      indent=2,  ensure_ascii=False)
                        self.s.sendto(
                            bytes('Message sent!!!', 'UTF-8'), client)

            except Exception as ex:
                print(ex)
                print('\n[ Server Stoppped]')
                self.quit = True
        self.s.close()  # закрываем соединение


a = Server()
a.get_server()
