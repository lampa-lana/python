class University:
    def __init__(self):
        self.nickname = 'Межгалактическая Академия Вселенских Наук'
        self.adress = 'Созвездие Кита, Планета Тау Кита f'
        self.faculty = {'1F': 'Факультет изучения форм жизни галактик.',
                        '2F': 'Факультет межгалактических военных летчиков.',
                        '3F': 'Факультет межгалактических финансовых расчетов. ',
                        '4F': 'Факультет изучения межгалактических языков.',
                        '5F': 'Факультет межгалактических технических достижений.',
                        }
        self.only_faculty = self.faculty.values()

    def get_description(self):
        print('-------------------------------------------------------------------------------------------')
        print('{} приветствует Вас!'. format(self.nickname))
        print('-------------------------------------------------------------------------------------------')
        print('Мы находимся по адресу {}.'. format(self.adress))
        print('-------------------------------------------------------------------------------------------')
        print(' В нашем великолепнои учебном заведении представлены следующие направления обучения:  \t')
        for i in self.only_faculty:
            print('\n * ', i)

    def get_univer(self):
        return self


class People:
    def __init__(self, surname,  name, patronomyc, birth_day, phone):
        self.name = name
        self.surname = surname
        self.patronomyc = patronomyc
        self.birth_day = birth_day
        self.phone = phone


class Students(People):
    def __init__(self, surname, name, patronomyc, birth_day, phone):
        super().__init__(surname, name, patronomyc, birth_day, phone)


class Lecturer(People):
    def __init__(self, surname, name, patronomyc, birth_day, phone):
        super().__init__(surname, name, patronomyc, birth_day, phone)


class Parents(People):
    def __init__(self, surname, name, patronomyc, birth_day, phone):
        super().__init__(surname, name, patronomyc, birth_day, phone)


class Director(People):
    def __init__(self, surname, name, patronomyc, birth_day, phone):
        super().__init__(surname, name, patronomyc, birth_day, phone)


a = University()
print(a.get_description())
