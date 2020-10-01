# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
#

from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество компани: '))):
    arg = input('Введите в одну строку через пробел название компании и поквартальную прибыль: ').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(float, arg[1:]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print(f'Средняя прибыль всех компаний: {avg}')

if len(lst) == 1:
    for i in lst:
        print(f'Вы ввели всего одну компанию "{i.name}", ее средняя прибыль: {i.avg}')
else:
    print('Компании с прибылью меньше средней:')
    for i in lst:
        if i.avg < avg:
            print(i.name)
    print('Компании с прибылью больше средней:')
    for i in lst:
        if i.avg > avg:
            print(i.name)
