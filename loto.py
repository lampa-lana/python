from random import randint


class Player:
    def __init__(self, name, player_type='computer'):
        self.name = name
        self.type = player_type
        self.card = Card()
        self.numbers_left = 15

    def check_barrel(self, barrel):
        barrel_in_cart = False
        barrel_line = None
        barrel_column = None
        if self.type == 'human':
            answer = input("Is Barrel in your card?")
        else:
            for line_num, line in enumerate(self.card.lines):
                if barrel in line:
                    barrel_in_cart = True
                    barrel_line = line_num
                    barrel_column = line.index(barrel)
                    break

        if barrel_in_cart:
            self.cross_barrel(barrel_line, barrel_column)

    def cross_barrel(self, line, column):
        self.card.lines[line][column] = '-X'
        self.numbers_left -= 1


class Bag:
    def __init__(self):
        self.bag = list(range(1, 91))

    def _calculate_random_position(self):
        return randint(0, len(self.bag)-1)

    def get_barrel(self):
        rand_pos = self._calculate_random_position()
        return str(self.bag.pop(rand_pos))


class Card:
    def __init__(self):
        self.lines = [
            list('__' for j in range(0, 9)) for i in range(3)
        ]
        self._put_numbers()

    def show_lines(self):
        print('- '*9, 'Cart', '- '*9)
        for i in self.lines:
            print(i)
        print('- ' * 9, '++++', '- ' * 9)

    def _gen_numbers(self, number_to_search=15, start=1, end=90):
        continue_search = number_to_search
        my_numbers = []

        while continue_search:
            number = randint(start, end)
            if number not in my_numbers:
                my_numbers.append(number)
                continue_search -= 1

        return my_numbers

    def _put_numbers(self):
        numbers = self._gen_numbers()
        otr1 = numbers[:5]
        otr2 = numbers[5:10]
        otr3 = numbers[10:]
        otrs = [otr1, otr2, otr3]

        for stroka, otr in zip(self.lines, otrs):
            sorted_otr = sorted(otr)

            rand_positions = self._gen_numbers(5, 0, 8)
            rand_positions = sorted(rand_positions)
            for num, pos in zip(sorted_otr, rand_positions):
                stroka[pos] = str(num)


def game():
    player = Player('Bob', 'computer')
    player.card.show_lines()
    player2 = Player('Mike', 'computer')
    player2.card.show_lines()

    bag = Bag()
    while len(bag.bag) > 0:
        print(len(bag.bag))
        barrel = bag.get_barrel()
        player.check_barrel(barrel)
        player2.check_barrel(barrel)
        player.card.show_lines()
        player2.card.show_lines()


# my_card = Card()
# my_card.show_lines()

bag = Bag()
print("Barrel is", bag.get_barrel())

game()
