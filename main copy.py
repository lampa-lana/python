import json


class University:
    def __init__(self):
        self.nickname = 'Межгалактическая Академия Вселенских Наук'
        self.adress = 'Созвездие Кита, Планета Тау Кита f'

    def get_description(self):
        print('-------------------------------------------------------------------------------------------')
        print('{} приветствует Вас!'. format(self.nickname))
        print('-------------------------------------------------------------------------------------------')
        print('Мы находимся по адресу {}.'. format(self.adress))
        print('-------------------------------------------------------------------------------------------')
        print(' В нашем великолепнои учебном заведении представлены следующие направления обучения:  \t')
        data = json.load(open('faculty.json'))
        for i in data:
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

    def get_add_faculity(self):
        qust = (input('Желаете добавить новую специальность? (y/n): ').lower())
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! Ответ не распознан!\n')
            qust = (input('Желаете добавить новую специальность? (y/n): ').lower())
        if qust == 'y':
            value = input('Введите название нового факультета : ')

            def write_json(faculty_dict):
                try:
                    data = json.load(open('faculty.json'))
                except:
                    data = []
                data.append(faculty_dict)
                with open('faculty.json', 'w') as fac_file:
                    json.dump(data, fac_file, indent=2, ensure_ascii=False)
            for i in range(1):
                write_json(value)
        elif qust == 'n':
            print('Вы вышли из меню создания новой специальноcти! ')


a = Director('Иванов', ' Иван', 'Иванович', '15.01.1979', '+7 926 564 97 85')
print(a.get_add_faculity())

# a = University()
# print(a.get_description())
