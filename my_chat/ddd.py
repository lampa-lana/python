import socket


# def get_port():
#     port = int(input('Please enter the port number: '))
#     return port


ip = socket.gethostbyname('localhost')


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if s.connect_ex((ip, port)):
        pass
    else:
        print(f' Порт {port} открыт')


def search_port():
    for i in range(int(input('Finding a free port from: ')), int(input('Search for a free port before: '))+1):
        scan_port(i)


# search_port()


def get_p():
    search_port()
    port = int(input('Enter the selected port:'))
    print('Your free port: {}'. format(port))


# get_p()


def search_port2():
    for port in range(int(input('Finding a free port from: ')), int(input('Search for a free port before: '))+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if s.connect_ex((ip, port)):
            pass
        else:
            print(f' Порт {port} открыт')
    port = int(input('Enter the selected port:'))
    print('Your free port: {}'. format(port))


search_port2()
