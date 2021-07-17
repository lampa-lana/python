import socket
import time
import threading
import json

# qust = {'action': 'msg_from_chat',
#         'time': time,
#         'message': message,
#         'user': {'name': name,
#                  'status': 'online'}}

# логические флаги об отключении и подключении клиента
shutdown = False
join = False


def receving(name, sock):
    while not shutdown:  # функция для приема  сообщений с сервера
        try:
            while True:
                data, addr = sock.recvfrom(1024)  # получаем сообщения
                print(data.decode('utf-8'))  # декодируем сообщения
                time.sleep(0.2)  # ждем 0.2 секунды на всякий случай
        except:
            pass


server = ('localhost', 9090)
# создаем анворгичный сокет как у сервера
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 0))  # конектимся с сервером
name = input('Name: ')

# делим потоки для получения сообщений
rT = threading.Thread(target=receving, args=('RecvThread', s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(('[' + name + '] => join chat ').encode('utf-8'),  server)
        join = True
    else:
        try:
            message = input('[You] :: ')
            if message != '':  # кодируем сообщение
                s.sendto(('[' + name + ']  ::  ' +
                         message).encode('utf-8'), server)  # указываем само сообщение и куда его отправить
            time.sleep(0.2)
        except:
            s.sendto(('[' + name + '] < = left chat ').encode('utf-8'), server)
rT.join()  # закрываем потоки
s.close()  # закрываем соединение
