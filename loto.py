from random import randint
import random


class Card:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]  # Мешок с бочонками
        self.name = name
        self.card = [self.gen_str(bag), self.gen_str(
            bag), self.gen_str(bag)]
        self.count_keg = 15  # остаток незакрытых бочонков на карточке

    def __str__(self):
        result = '{:-^26}\n'.format(self.name)
        for x in range(3):
            result += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(
                *self.card[x])+'\n'
        return result + '----------------------------'

    @staticmethod
    def gen_str(bag):
        string = ['' for i in range(9)]
        for x in range(8, 3, -1):
            # возвращает случайное целочисленное значение номера строки
            digit = (random.randint(0, x))
            while string[digit] != '':  # если элемент уже не пустой
                digit += 1
            string[digit] = bag.pop(random.randint(
                0, len(bag) - 1))
        return string


player = Card('Карточка Игрока')
computer = Card('Карточка Компьтера')

bag = [x for x in range(1, 91)]
while True:
    if len(bag) < 1:  # если в мешке не осталось бочонков
        print('Бочонки закончились. Результат: \n'
              'У Компьютера осталось {} чисел, \n'
              'У Игрока осталось {} чисел'.format(computer.count_keg, player.count_keg))
        break
    keg = bag.pop(randint(0, len(bag)-1))  # получение случайного бочонка
    print('\n Новый бочонок: {} (осталось {}:)'.format(keg, len(bag)))
    print(player)
    print(computer)
    question = (input('Зачеркнуть цифру? y/n: ')).lower()

    if question == 'y':
        test = False  # Есть ли такая цифра на арточке игрока?
        for x in range(3):  # пробегает по трем рядам
            if keg in player.card[x]:
                test = True
                player.card[x][player.card[x].index(keg)] = '-'
                player.count_keg -= 1
            if keg in computer.card[x]:
                computer.card[x][computer.card[x].index(keg)] = '-'
                computer.count_keg -= 1
        if test:
            if player.count_keg < 1:
                print(' Вы выиграли!')
                break
            elif computer.count_keg < 1:
                print(' Компьютер выиграл!')
                break
        else:
            print('Вы проиграли! Такого числа нет на Вашей карточке!')
            break
    elif question == 'n':
        test = False
        for x in range(3):  # пробегает по трем рядам
            if keg in player.card[x]:
                print('Вы проиграли, такое число есть на Вашей карточке!')
                test = True
                break
            if keg in computer.card[x]:
                computer.card[x][computer.card[x].index(keg)] = '-'
                computer.count_keg -= 1
        if test:
            break
        if player.count_keg < 1:
            print('Вы выиграли!')
            break
        elif computer.count_keg < 1:
            print('Компьютер выиграл!')
            break
