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


class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname


class Student(People):
    def __init__(self, name, patronymic, surname, student_class, father, mother):
        People.__init__(self, name, patronymic, surname)

        self.student_class = student_class
        self.father = father
        self.mother = mother

    def get_student_class(self):
        return self.student_class

    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())

    def name_parent(self):
        return self.father.get_full_name(), self.mother.get_full_name()


class Teacher(People):
    def __init__(self, name, patronymic, surname, classes, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
        self.classes = classes

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes


class ClassRooms:
    def __init__(self, class_room):
        self.class_room = {'class_num': int(class_room.split()[0]),
                           'class_letter': class_room.split()[0]}

    def get_class_room(self):
        return self.class_room

    def get_name(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_letter']


class_rooms = ['5 А', '7 Б', '10 В']

teachers = [Teacher('Тамара', 'Ивановна', 'Часова', [class_rooms[0], class_rooms[1], class_rooms[2]], 'Математика'),
            Teacher('Иван', 'Петрович', 'Медведев', [
                    class_rooms[1], class_rooms[2]], 'Химия'),
            Teacher("Лариса", "Сергеевна", "Блинова", [class_rooms[0], class_rooms[1]], 'Английский')]
parents = [People('Петр', 'Иванович', 'Кузнецов'),
           People('Мария', 'Ивановна', 'Кузнецова'),
           People('Иван', 'Сидорович', 'Соколов'),
           People('Марта', 'Петровна', 'Соколова'),
           People('Федор', 'Сергеевич', 'Петров'),
           People('Татьяна', 'Олеговна', 'Петрова'),
           People('Сергей', 'Семенович', 'Алексеев'),
           People('Дарья', 'Игоревна', 'Алексеева'), ]

students = [Student('Иван', 'Петрович', 'Кузнецов', class_rooms[0], parents[0], parents[1]),
            Student('Петр', 'Иванович', 'Соколов',
                    class_rooms[0], parents[2], parents[3]),
            Student('Мария', 'Федоровна', 'Петрова',
                    class_rooms[1], parents[4], parents[5]),
            Student('Наталия', 'Сергеевна', 'Алексеева',  class_rooms[2], parents[6], parents[7])]

print('------------------------------------------------------------------------------------------\n')
# получить все классы в школе


def get_school_class():
    quest = input('Вывести список классов в школе (да/нет)?: ')
    if quest == 'да'.lower():
        print(' Список классов в школе: ')
        for i in class_rooms:
            print(i)
    else:
        print(' Хорошего дня! ')


get_school_class()

print('------------------------------------------------------------------------------------------\n')
# Получить список всех учеников в указанном классе
# (каждый ученик отображается в формате "Фамилия И.О.")


def get_list_stud():
    quest1 = input('Хотите увидеть список учащихся в классе (да/нет)?: ')
    if quest1 == 'да'.lower():
        quest = input('Укажите класс для вывода списка учащихся: ')
        print(' В {} классе учатся : '.format(quest))
        for i in class_rooms:
            for j in students:
                if i in quest and j.get_student_class() in quest:
                    print('\t', j.get_short_name())

    else:
        print(' Хорошего дня! ')


get_list_stud()

print('------------------------------------------------------------------------------------------\n')
#  Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)


def choice_stud():
    quest1 = input('Хотите увидеть список предметов ученика (да/нет)?: ')
    if quest1 == 'да'.lower():
        st = input('Введите имя студента (формат Фамилия И.О.): ')
        st1 = ''
        for i in students:
            i.get_short_name()
            i.get_student_class()
            if i.get_short_name() == st:
                st1 = i.get_student_class()
                print('\t Ученик : ', i.get_short_name(), 'Класс : ', st1)
                for j in teachers:
                    j.get_full_name()
                    j.get_subject()
                    j.get_classes()
                    if st1 in j.get_classes():
                        print('Учитель:', j.get_full_name(),
                              '--- ', 'Предмет: ', j.get_subject())
    else:
        print(' Хорошего дня! ')


choice_stud()


print('------------------------------------------------------------------------------------------\n')
#  Узнать ФИО родителей указанного ученика


def parents_stud():
    quest1 = input(
        'Хотите увидеть ФИО родителей указанного ученика (да/нет)?: ')
    if quest1 == 'да'.lower():
        st = input('Введите имя студента (формат Фамилия И.О.): ')
        for i in students:
            i.get_short_name()
            i.name_parent()
            if st == i.get_short_name():
                print('Родителями ученика: ', i.get_short_name(),
                      '\n', '\t являются: ',  i.name_parent())
    else:
        print(' Хорошего дня! ')


parents_stud()
print('------------------------------------------------------------------------------------------\n')
# Получить список всех Учителей, преподающих в указанном классе


def choice_teacher():
    quest1 = input(
        'Хотите увидеть список всех Учителей, преподающих в указанном классе (да/нет)?: ')
    if quest1 == 'да'.lower():
        tch = input(
            ' Введите класс, для вывода списка учителей (формат ввода например 1 Г): ')
        for i in teachers:
            tch2 = i.get_classes()
            i.get_full_name()
            if tch in tch2:
                print(i.get_full_name())
    else:
        print(' Хорошего дня! ')


choice_teacher()
print('----------------------------------------------END------------------------------------------\n')
