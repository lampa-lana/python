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
                        self.s.sendto(self.data, client)

            except Exception as ex:
                print(ex)
                print('\n[ Server Stoppped]')
                self.quit = True
        self.s.close()  # закрываем соединение


a = Server()
a.get_server()


# https: // translate.google.com/translate?sl = en & tl = ru & u = https: // stackoverflow.com/questions/39817641/how-to-send-a-json-object-using-tcp-socket-in-python
# https://dvsemenov.ru/peredacha-fajla-cherez-soket-v-python-3/
# https://digital2.ru/zametki-python-18-setevoe-programmirovanie/
# https: // github.com/KirillVladimirov/python-messenger
# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
# https://ru.stackoverflow.com/questions/1112609/%D0%9D%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D0%BB-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82-%D0%B8-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80-%D0%BD%D0%B0-python-%D0%BD%D0%B5-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%B0%D1%85-%D0%9D%D0%B0-%D0%BE%D0%B4%D0%BD%D0%BE%D0%BC-%D0%BA
