from random import randint


class Card:
    def __init__(self, name):
        bag = [i for i in range(1, 91)]
        self.lines = [self.show_lines(bag), self.show_lines(
            bag), self.show_lines(bag)]
        self.name = name
        self.count_keg = 15  # осталось бочек на карточке

    @staticmethod
    def show_lines(bag):
        string = ['' for _ in range(9)]
        for i in range(8, 3, -1):
            digit = randint(0, i)
            while string[digit] != '':
                digit += 1
            string[digit] = bag.pop(randint(0, len(bag) - 1))
        return string

    def __str__(self):
        result = '{:-^26}\n'.format(self.name)
        for i in range(3):
            result += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(
                *self.lines[i]) + '\n'
        return result + '-------------------------------------'

    def get_card(self):
        return self


player = Card(' Игрок ')
comp = Card(' Компьютер ')
bag = [i for i in range(1, 91)]
while True:
    if len(bag) < 1:
        print('Бочёнки в мешке закончились. Результат:\n'
              'у компьютера осталось {} числа/чисел,\n'
              'у игрока осталось {} числа/чисел.'
              .format(comp.count_keg, player.count_keg))
        break
    keg = bag.pop(randint(0, len(bag) - 1))
    print('\nНовый бочонок: {} (осталось {})'.format(keg, len(bag)))

    print(player)
    print(comp)
    reply = (input('Зачеркнуть цифру? (y/n/q): ')).lower()

    while len(reply) == 0 or reply not in 'ynq':
        print('\n\n!!! Ответ не распознан!\n')
        print('Новый бочонок: {} (осталось {})'.format(keg, len(bag)))

        print(player)
        print(comp)
        reply = (input('Зачеркнуть цифру? (y/n/q): ')).lower()

    if reply == 'q':
        print('Вы вышли из игры. Вы так и не выиграли.')
        break
    elif reply == 'y':
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3):
            if keg in player.lines[x]:
                test = True
                player.lines[x][player.lines[x].index(keg)] = '-'
                player.count_keg -= 1
                print('--------------------------------------------------\n')
                print('\t У Игрока вычернуто число {} '.format(keg))
                print('--------------------------------------------------\n')
            if keg in comp.lines[x]:
                comp.lines[x][comp.lines[x].index(keg)] = '-'
                comp.count_keg -= 1
                print('--------------------------------------------------\n')
                print('\t У Компьютера вычернуто число {} '.format(keg))
                print('--------------------------------------------------\n')
        if test:
            if player.count_keg < 1:
                print('Вы Выиграли!')
                break
            elif comp.count_keg < 1:
                print('Компьютер Выиграл!')
                break
        else:
            print('Вы проиграли! Такого числа нет на Вашей карточке!')
            break
    elif reply == 'n':
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3):
            if keg in player.lines[x]:
                print('Вы проиграли! Такое число есть на Вашей карточке!')
                test = True
                break
            if keg in comp.lines[x]:
                comp.lines[x][comp.lines[x].index(keg)] = '-'
                comp.count_keg -= 1
                print('--------------------------------------------------\n')
                print('\t У Компьютера вычернуто число {} '.format(keg))
                print('--------------------------------------------------\n')
        if test:
            break
        if player.count_keg < 1:
            print('Вы Выиграли!')
            break
        elif comp.count_keg < 1:
            print('Компьютер Выиграл!')
            break
