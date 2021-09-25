# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os

path_hours = os.path.join('hours_of')
path_workers = os.path.join('workers')

with open(path_hours, 'r', encoding='UTF-8') as f:
    hours = []
    for i in f.readlines():
        hours.append(i.split())

with open(path_workers, 'r', encoding='UTF-8') as f:
    workers = []
    for i in f.readlines():
        workers.append(i.split())

del hours[0]
del workers[0]

hours = sorted(hours)
workers = sorted(workers)

h_w = [int(i[-1]) for i in workers]  # список с часвами в workers
h_h = [int(j[-1]) for j in hours]  # список с часвами в hours
m_w = [int(k[2]) for k in workers]  # список с зп в workers
result_4 = [int((x * y) / z)
            for x, y, z in zip(m_w, h_h, h_w)]   # оплата недоработки
print(*result_4)

mix_name = [i for i in zip(hours, result_4,)]
print('Зарплата составила: ', *mix_name, sep='\n')

#
# result = [int(x/y) for x, y in zip(m_w, h_w)]   # стоимость часа
# print(result)
# result_2 = [int(x - y) for x, y in zip(h_w, h_h)]   # переработка
# print(result_2)
# result_3 = [int(x * y) for x, y in zip(result_2, result) if x > 0]   # оплата переработки
# print(result_3)
