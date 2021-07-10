import json
import os
import random


class University:
    def __init__(self):
        self.nickname = 'Intergalactic Academy of Universal Sciences'
        self.adress = 'Constellation Cetus, Planet Tau Whale f'

    def get_description(self):
        print('-------------------------------------------------------------------------------------------')
        print('{} greeting you!'. format(self.nickname))
        print('-------------------------------------------------------------------------------------------')
        print('We are located at {}.'. format(self.adress))
        print('-------------------------------------------------------------------------------------------')
        print(' Our excellent educational institution presents the following areas of study:  \t')

        data = json.load(open('faculty.json'))
        with open('faculty.json', 'w') as fac_file:
            json.dump(data, fac_file, indent=2, ensure_ascii=False)
            for i in data:
                print('\n * ', i)

    def get_univer(self):
        return self


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

    def add_student(self,  surname, name, patronymic, phone, birth_day, group_number, stud_status, id, faculty):
        self.group_students.append({'surname': surname, 'name': name, 'patronymic': patronymic, 'phone': phone,
                                   'birth_day': birth_day, 'group_number': group_number, 'stud_status': stud_status, 'id': id, 'faculty': faculty})
        self.save()

    def select_by_group_number(self, group_number):
        return [x for x in self.group_students if x['group_number'] == group_number]

    def select_by_stud_status(self, stud_status):
        return [x for x in self.group_students if x['stud_status'] == stud_status]

    def select_by_stud_id(self, id):
        return [x for x in self.group_students if x['id'] == id]

    def get_studinfo_by_id(self):
        print('\n-------------------------------------------------------\n')
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
                print('\n----------------------------- \n')
                for j, k in i.items():
                    print(j, ': ', k)
                print('\n----------------------------- \n')
        elif qust == 'n':
            print('You have exited the menu information about yourself! ')


class Lecturer(People):
    def __init__(self):
        self.name = 'name'
        self.surname = 'surname'
        self.patronymic = 'patronymic'
        self.phone = 'phone'


class Director(People):
    def __init__(self):
        super().__init__()
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.patronymic = 'Ivanovich'
        self.phone = '+10 123 124 125'

    def get_add_faculty(self):
        print('\n-------------------------------------------------------\n')
        qust = (input('Would you like to add a new specialty? (y/n): ').lower())
        data = json.load(open('faculty.json'))
        with open('faculty.json', 'w') as fac_file:
            json.dump(data, fac_file, indent=2, ensure_ascii=False)
            for i in data:
                print('\n * ', i)
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (input('Would you like to add a new specialty? (y/n): ').lower())

        if qust == 'y':
            value = input('Enter the name of the new faculty : ')

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
            print('You have exited the menu for creating a new specialty! ')

    def get_del_faculty(self):
        print('\n-------------------------------------------------------\n')
        qust = (input('Do you want to delete a specialty? (y/n): ').lower())
        while len(qust) == 0 or qust not in 'yn':
            print('\n\n!!! The answer is not recognized!\n')
            qust = (input('Want to delete a new specialty? (y/n): ').lower())
        if qust == 'y':
            data = json.load(open('faculty.json'))
            with open('faculty.json', 'w') as fac_file:
                json.dump(data, fac_file, indent=2, ensure_ascii=False)
                print('You can choose from the list\t')
                for index, value in enumerate(data):
                    print('{} {:>8}'.format(str(index+1)+'.', value))
                # print('---------------------------------------------')

            data = json.load(open('faculty.json'))
            answ = input('Enter the name of the faculty : ')
            for i in range(len(data)):
                if data[i] == answ:
                    data.pop(i)
                    break
            open("faculty.json", "w").write(json.dumps(
                data, sort_keys=True, indent=4, separators=(',', ': ')))
            print('----------------------------------------------------------')
            print('\n{} \nRemoved from the list of faculties !!!!'.format(answ))
            print('----------------------------------------------------------')
            print('New Faculty List Created: ')
            data = json.load(open('faculty.json'))
            with open('faculty.json', 'w') as fac_file:
                json.dump(data, fac_file, indent=2, ensure_ascii=False)
                for i in data:
                    print('\n * ', i)

        elif qust == 'n':
            print('You have exited the specialty deletion menu !!! ')

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
    1 - add student,
    2 - selection by group number,
    3 - selection by student status(student/headman),
    4 - full information output
    exit - 0
  
''')
            while True:
                f = input('Your actions:  ')
                if f == '1':
                    print(
                        'Enter data separated by a space(surname, name, patronymic, phone, birth_day, group_number, stud_status, faculty) :')
                    surname, name, patronymic, phone, birth_day, group_number, stud_status, faculty = input().split()
                    id = ''
                    nums = ['1', '2', '3', '4', '5', '6', '7']
                    while len(id) != 7:
                        id += random.choice(nums)
                    db.add_student(surname, name, patronymic, phone,
                                   birth_day, group_number, stud_status, id, faculty)
                elif f == '2':
                    num = (input('Group number->  '))
                    items = (db.select_by_group_number(num))
                    for i in items:
                        print('\n----------------------------- \n')
                        for j, k in i.items():
                            print(j, ': ', k)

                elif f == '3':
                    items = db.select_by_stud_status(
                        input('student/headman-> '))
                    for i in items:
                        print('\n----------------------------- \n')
                        for j, k in i.items():
                            print(j, ': ', k)

                elif f == '4':
                    with open('group_students.json', 'r') as json_file:
                        json_dec = json.load(json_file)
                        for i in json_dec:
                            print('\n----------------------------- \n')
                            for j, k in i.items():
                                print(j, ': ', k)

                else:
                    break
            db.save()
        elif qust == 'n':
            print(
                'You are exited from the action menu with the list of students !!! ')
        print('\n-------------------------------------------------------\n')


a = University()
print(a.get_description())


def get_status():
    qust = input(
        'Please enter your status in the educational institution (director, student, lecturer or n(exit)) : ')
    while len(qust) == 0 or qust not in 'directorstudentlecturern':
        print('\n\n!!! The answer is not recognized!\n')
        qust = (input(
            'Please enter your status in the educational institution (director, student, lecturer) : ').lower())
    if qust == 'director':
        status_d = Director()
        print('Welcome to the Academy: \n\t', status_d.get_full_info())
        status_d.get_add_faculty()
        status_d.get_del_faculty()
        status_d.get_stud_menu()
        print('Have a Nice Day')
    if qust == 'student':
        status_s = Students('group_students.json')
        status_s.get_studinfo_by_id()
        print('Have a Nice Day')
    if qust == 'lecturer':
        status_l = Lecturer()
        print(status_l.get_full_name())
        print('Have a Nice Day')
    elif qust == 'n':
        print('You are exited from the Academy menu! ')
        print('Have a Nice Day!!!')


get_status()
