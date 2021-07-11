import json
import os
import random
import string
import uuid

# ДЛЯ ЭКСПЕРИМЕНТОВ!!!!
# def get_id():
#     user_id = uuid.uuid4()
#     print(user_id)


# get_id()

# https://stackoverflow.com/questions/36606930/delete-an-element-in-a-json-object
class People:
    def __init__(self, surname, name, patronymic,  phone):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def get_full_info(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname + ' ' + self.phone


class Students:
    def __init__(self, stud_list_file):

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


if __name__ == '__main__':
    db = Students('group_students.json')

#     print('''\
# Select an action:
#     1 - add student,
#     2 - selection by group number,
#     3 - selection by student status(student/headman),
#     4 - full information output
#     exit - 0

# ''')
    # while True:
    #     f = input('Your actions:  ')
    #     if f == '1':
    #         print('Enter data separated by a space(surname, name, patronymic, phone, birth_day, group_number, stud_status) :')
    #         surname, name, patronymic, phone, birth_day, group_number, stud_status, faculty = input().split()
    #         id = ''
    #         nums = ['1', '2', '3', '4', '5', '6', '7']
    #         while len(id) != 7:
    #             id += random.choice(nums)
    #         db.add_student(surname, name, patronymic, phone,
    #                        birth_day, group_number, stud_status, id, faculty)
    #     elif f == '2':
    #         num = (input('Group number->  '))
    #         items = (db.select_by_group_number(num))
    #         for i in items:
    #             print('\n----------------------------- \n')
    #             for j, k in i.items():
    #                 print(j, ': ', k)

    #     elif f == '3':
    #         items = db.select_by_stud_status(input('student/headman-> '))
    #         for i in items:
    #             print('\n----------------------------- \n')
    #             for j, k in i.items():
    #                 print(j, ': ', k)

    #     elif f == '4':
    #         with open('group_students.json', 'r') as json_file:
    #             json_dec = json.load(json_file)
    #             for i in json_dec:
    #                 print('\n----------------------------- \n')
    #                 for j, k in i.items():
    #                     print(j, ': ', k)

    #     else:

    #         break

    # db.save()


# with open('group_students.json', 'r') as json_file:
#     json_dec = json.load(json_file)
#     for i in json_dec:
#         print(i)
#         id = ''
#         nums = ['1', '2', '3', '4', '5', '6', '7']
#         while len(id) != 7:
#             id += random.choice(nums)
#         i['id'] = id
#         print(i)
# with open("group_students.json", 'w') as json_file:
#     json.dump(json_dec, json_file)

answ = input('Enter the code of the faculty : ')

with open('faculty.json') as data_file:
    data = json.load(data_file)

for element in data:
    if answ in element:
        del element[answ]

with open('faculty.json', 'w') as data_file:
    data = json.dump(data, data_file)
