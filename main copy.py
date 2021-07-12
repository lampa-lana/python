import json
import os
import random


class University:
    def __init__(self):
        self.nickname = 'Intergalactic Academy of Universal Sciences'
        self.short_nickname = 'IAUS'
        self.adress = 'Constellation Cetus, Planet Tau Whale f'
        self.hours = 'Working Hours Around the Clock'

    def get_description(self):
        print('-------------------------------------------------------------------------------------------')
        print('{} greeting you!'. format(self.nickname))
        print('-------------------------------------------------------------------------------------------')
        print('We are located at {}.'. format(self.adress))
        print('-------------------------------------------------------------------------------------------')
        return (self.hours + '\n')


class Fucalty(University):
    def __init__(self):
        super().__init__()

    def get_faculty(self):
        print('Our excellent educational institution presents the following areas of study:  \n\t')
        self.data = json.load(open('faculty.json'))
        with open('faculty.json', 'w') as fac_file:
            json.dump(self.data, fac_file, indent=2, ensure_ascii=False)
            for i in self.data:
                for j, k in i.items():
                    print(j, ': ', k, '\n')
            return ('Faculties at the {} at the moment'.format(self.short_nickname))

    def get_detailed_faculty(self):
        pass


class People:
    def __init__(self):
        self.name = 'name'
        self.surname = 'surname'
        self.patronymic = 'patronymic'
        self.phone = 'phone'

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def get_full_info(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname + ' ' + self.phone


class Students(People):
    def __init__(self, stud_list_file):
        super().__init__()

        self.stud_list_file = stud_list_file

        if os.path.exists(self.stud_list_file):
            with open(self.stud_list_file, encoding='utf-8') as f:
                self.group_students = json.load(f)

        else:
            self.group_students = []

    def save(self):
        with open(self.stud_list_file, 'w', encoding='utf-8') as f:
            # запись списка в json файл
            json.dump(self.group_students, f, ensure_ascii=False)

    def get(self, num):  # нумерация студентов
        return self.group_students[num - 1]

    def add_student(self,  surname, name, patronymic, phone, birth_day, group_number, stud_status, id, faculty, code_faculty):
        self.group_students.append({'surname': surname, 'name': name, 'patronymic': patronymic, 'phone': phone,
                                   'birth_day': birth_day, 'group_number': group_number, 'stud_status': stud_status, 'id': id, 'faculty': faculty, 'code_faculty': code_faculty})
        self.save()

    def select_by_group_number(self, group_number):
        return [x for x in self.group_students if x['group_number'] == group_number]

    def select_by_stud_status(self, stud_status):
        return [x for x in self.group_students if x['stud_status'] == stud_status]

    def select_by_stud_id(self, id):
        return [x for x in self.group_students if x['id'] == id]

    def get_studinfo_by_id(self):
        print('-------------------------------------------------------------------------------------------')
        qust = (
            input('Do you want to see information about yourself? (y/n): ').lower())
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (
                input('Do you want to see information about yourself?? (y/n): ').lower())
        if qust == 'y':
            db = Students('group_students.json')
            id = input('Enter your id, please: ')
            items = (db.select_by_stud_id(id))
            for i in items:
                print(
                    '-------------------------------------------------------------------------------------------')
                for j, k in i.items():
                    print(j, ': ', k)

        elif qust == 'n':
            print('You have exited the menu information about yourself! ')

    def get_menu_student(self):
        print('\n-------------------------------------------------------\n')
        qust = (
            input('Do you want to see your profile and get information about the Academy? (y/n): ').lower())
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (
                input('Do you want to see your profile and get information about the Academy? (y/n): ').lower())
        if qust == 'y':
            status_s = Students('group_students.json')
            print('''\
    Select an action:
            1 - Full information by id
            2 - Information about the Academy
            3 - Director Information 
            Exit - 0
    ''')

            while True:
                g = input('Your actions:  ')
                if g == '1':
                    status_s.get_studinfo_by_id()
                elif g == '2':
                    uni = Fucalty()
                    uni.get_faculty()
                elif g == '3':
                    status_d = Director()
                    print('Director Information : \n\t',
                          status_d.get_full_info())

                else:
                    print(
                        '-------------------------------------------------------------------------------------------')
                    print('You have exited the menu for creating a new specialty! ')
                    print(
                        '-------------------------------------------------------------------------------------------')
                    break
        elif qust == 'n':
            print(
                '-------------------------------------------------------------------------------------------')
            print('You have exited the information menu! ')


class Director(People):
    def __init__(self):
        super().__init__()
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.patronymic = 'Ivanovich'
        self.phone = '+10 123 124 125'

    def get_add_faculty(self):
        print('-------------------------------------------------------------------------------------------')
        qust = (input('Would you like to add a new specialty? (y/n): ').lower())
        uni = Fucalty()
        uni.get_faculty()

        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (input('Would you like to add a new specialty? (y/n): ').lower())

        if qust == 'y':
            print(
                '-------------------------------------------------------------------------------------------')
            key = input('Enter code of new faculty : ')
            value = input('Enter the name of the new faculty : ')

            def write_json(key, value):
                try:
                    data = json.load(open('faculty.json'))
                except:
                    data = [{}]
                data.append({key: value})
                with open('faculty.json', 'w') as fac_file:
                    json.dump(data, fac_file, indent=2, ensure_ascii=False)
            for i in range(1):
                write_json(key, value)
            print(
                '-------------------------------------------------------------------------------------------')
            print('You New Specialty Created! ')
            print(
                '-------------------------------------------------------------------------------------------')
        elif qust == 'n':
            print(
                '-------------------------------------------------------------------------------------------')
            print('You have exited the menu for creating a new specialty! ')

    def get_del_faculty(self):
        print('-------------------------------------------------------------------------------------------')
        qust = (input('Do you want to delete a specialty? (y/n): ').lower())
        uni = Fucalty()
        uni.get_faculty()
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (input('Want to delete a new specialty? (y/n): ').lower())
        if qust == 'y':
            print('You can choose from the list\t')
            answ = input('Enter the code of the faculty : ')
            with open('faculty.json') as data_file:
                data = json.load(data_file)

            for element in data:
                if answ in element:
                    del element[answ]

            with open('faculty.json', 'w') as data_file:
                data = json.dump(data, data_file)

            print(
                '-------------------------------------------------------------------------------------------')
            print('\n{} \nRemoved from the list of faculties !!!!'.format(answ))
            print(
                '-------------------------------------------------------------------------------------------')
            print('New Faculty List Created: ')
            uni = Fucalty()
            uni.get_faculty()

        elif qust == 'n':
            print(
                '-------------------------------------------------------------------------------------------')
            print('You have exited the specialty deletion menu !!! ')

    def get_menu_faculty(self):
        print('\n-------------------------------------------------------\n')
        qust = (
            input('Do you want to take any action on the list of faculty? (y/n): ').lower())
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (
                input('Do you want to take any action on the list of faculty? (y/n): ').lower())
        if qust == 'y':
            s = Director()
            print('''\
    Select an action:
            1 - Add faculty, 
            2 - Delete faculty,
            3 - Full information faculty  
            Exit - 0
    ''')

            while True:
                g = input('Your actions:  ')
                if g == '1':
                    s.get_add_faculty()
                elif g == '2':
                    s.get_del_faculty()
                elif g == '3':
                    uni = Fucalty()
                    uni.get_faculty()

                else:
                    print('You have exited the menu for creating a new specialty! ')
                    break
        elif qust == 'n':
            print(
                '-------------------------------------------------------------------------------------------')
            print('You have exited the specialty menu !!! ')

    def get_stud_menu(srlf):
        print('\n-------------------------------------------------------\n')
        qust = (
            input('Do you want to take any action on the list of students? (y/n): ').lower())
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (
                input('Do you want to take any action on the list of students? (y/n): ').lower())
        if qust == 'y':
            db = Students('group_students.json')
            print('''\
Select an action:
    1 - Add student,
    2 - Selection by group number,
    3 - Selection by student status(student/headman),
    4 - Full information about students
    Exit - 0

''')
            while True:
                f = input('Your actions:  ')
                if f == '1':
                    print(
                        'Enter data separated by a space(surname, name, patronymic, phone, birth_day, group_number, stud_status, faculty, code_faculty) :')
                    surname, name, patronymic, phone, birth_day, group_number, stud_status, faculty, code_faculty = input().split()
                    id = ''
                    nums = ['1', '2', '3', '4', '5', '6', '7']
                    while len(id) != 7:
                        id += random.choice(nums)
                    db.add_student(surname, name, patronymic, phone,
                                   birth_day, group_number, stud_status, id, faculty, code_faculty)
                elif f == '2':
                    num = (input('Group number->  '))
                    items = (db.select_by_group_number(num))
                    for i in items:
                        print(
                            '-------------------------------------------------------------------------------------------')
                        for j, k in i.items():
                            print(j, ': ', k)

                elif f == '3':
                    items = db.select_by_stud_status(
                        input('student/headman-> '))
                    for i in items:
                        print(
                            '-------------------------------------------------------------------------------------------')
                        for j, k in i.items():
                            print(j, ': ', k)

                elif f == '4':
                    with open('group_students.json', 'r') as json_file:
                        json_dec = json.load(json_file)
                        for i in json_dec:
                            print(
                                '-------------------------------------------------------------------------------------------')
                            for j, k in i.items():
                                print(j, ': ', k)

                else:
                    break
            db.save()
        elif qust == 'n':
            print(
                'You are exited from the action menu with the list of students !!! ')
        print('-------------------------------------------------------------------------------------------')


print(University().get_description())
print(Fucalty().get_faculty())


def get_status():
    print('------------------------------------------------------------------------------------------------\n')
    qust = input(
        'Please enter your status in the educational institution (director, student, lecturer or n(exit)) : ')
    while len(qust) == 0 or qust not in 'directorstudentlecturern':
        print('\n\n!!! The answer is not recognized!\n')
        qust = (input(
            'Please enter your status in the educational institution (director, student, lecturer) : ').lower())
    if qust == 'director':
        status_d = Director()
        print('Welcome to the Academy: \n\t', status_d.get_full_info())
        status_d.get_menu_faculty()
        status_d.get_stud_menu()
        print('Have a Nice Day')
    if qust == 'student':
        status_s = Students('group_students.json')
        status_s.get_menu_student()
        # status_s.get_studinfo_by_id()
        print('Have a Nice Day')
    elif qust == 'n':
        print('You are exited from the Academy menu! ')
        print('Have a Nice Day!!!')


get_status()
