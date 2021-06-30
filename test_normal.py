import math
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классеПе
# ----------------------------------------------------------------------------------------------


class Class_Rooms:
    def __init__(self, class_room):
        self.class_room = {'class_num': int(class_room.split()[0]),
                           'class_char': class_room.split()[1]}

    def get_name_class(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_char']


class People:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic


class Student(People):
    def __init__(self, name, surname, patronymic, class_room, human_status):
        People.__init__(name, surname, patronymic)
        # self.class_room = {'class_num': int(class_room.split()[0]),
        #                    'class_char': class_room.split()[1]}
        self._class_room = class_room
        self._human_status = human_status

    def get_name_parents(self):
        if self._human_status == 'Ученик':
            self.parents_mam = input(' Как зовут вашу маму?:\n(ФИО) ')
            self.parents_dad = input(' Как зовут вашего папу?:\n(ФИО) ')

        return (' Родителями ученика: ', self.get_full_name(), ' являются: ', self.parents_mam, self.parents_dad)

    def get_class_room(self):
        return self._class_room


class Teacher(People):
    def __init__(self, name, surname, patronymic, courses, classes):
        People.__init__(name, surname, patronymic)
        self._courses = courses
        self._classes = classes

    def get_courses(self):
        return self._courses

    def get_classes(self):
        return self._classes


class_rooms = ['5 А', '7 Б', '10 Г']
students = [Student('Иван', 'Петрович', 'Кузнецов', class_rooms[0], 'ученик'),
            Student('Петр', 'Иванович', 'Соколов', class_rooms[0], 'ученик'),
            Student('Мария', 'Федоровна', 'Петрова', class_rooms[1], 'ученик'),
            Student('Наталия', 'Сергеевна', 'Алексеева', class_rooms[2], 'ученик')]
