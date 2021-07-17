import json


def get_username():
    filename = 'user.json'
    try:
        with open(filename) as ft:
            user = json.load(ft)
    except FileNotFoundError:
        return None
    else:
        return user


def create_user():
    username = get_username()
    if username:
        print(' Добро пожаловать  ' + username)
    else:
        username = input(' Введите ваше имя  : ')
        filename = 'user.json'
        with open(filename,  'w', encoding='UTF-8') as f:
            json.dump(username, f, ensure_ascii=False)
            print(' Мы запомнили ваше имя как ' + username + '! ')


create_user()
