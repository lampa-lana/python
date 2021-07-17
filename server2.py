import socket
import time
import json

# answer = {'response': code,
#           'time': time,
#           'user': {'name': name,
#                    'status': 'online'},
#           'message': message}

# настройки хоста и порта
host = 'localhost'
port = 9090
clients = []  # список подключаемых клиентов


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создаем сокет
s.bind((host, port))  # присвоение хоста и порта
s.listen(10)  # максимальное количество одновременных звпросов
quit = False
print('[Server Srartet]')

while not quit:  # пока есть запросы на подключение от клиента
    try:
        # получаем данные клиентов данные, адрес и их максимальное количество которое можно принять от клиента
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        itsatime = time.strftime(
            '%Y-%m-%d-%H.%M.%S', time.localtime())  # текущее время
        print('[' + addr[0] + '] = [' + str(addr[1]) +
              '] = [' + itsatime + '] /', end='')
        print(data.decode('utf-8'))
        for client in clients:
            if addr != client:
                s.sendto(data, client)  # передаем данные
    except Exception as ex:
        print(ex)
        print('\n[ Server Stoppped]')
        quit = True
s.close()  # закрываем соединение
# https: // translate.google.com/translate?sl = en & tl = ru & u = https: // stackoverflow.com/questions/39817641/how-to-send-a-json-object-using-tcp-socket-in-python
# https://dvsemenov.ru/peredacha-fajla-cherez-soket-v-python-3/
# https://digital2.ru/zametki-python-18-setevoe-programmirovanie/
# https: // github.com/KirillVladimirov/python-messenger
# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
# https://ru.stackoverflow.com/questions/1112609/%D0%9D%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D0%BB-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82-%D0%B8-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80-%D0%BD%D0%B0-python-%D0%BD%D0%B5-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%B0%D1%85-%D0%9D%D0%B0-%D0%BE%D0%B4%D0%BD%D0%BE%D0%BC-%D0%BA
