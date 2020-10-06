# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
#    проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
#

import sys
from random import random
from collections import Counter


print(sys.version, sys.platform)


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__}, size={sys.getsizeof(x)}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
    return sys.getsizeof(x)



# вариант 1
def alg_1(arr):
    num = arr[0]
    max_frq = 1
    n = len(arr)
    for i in range(n - 1):
        frq = 1
        for k in range(i + 1, n):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]
    print(f'Alg_1 memory usage: ')
    m = f'{show_size(num)}, {show_size(max_frq)}, {show_size(n)}, {show_size(i)}, {show_size(frq)}, {show_size(k)}'
    if max_frq > 1:
        return f'Alg_1: Число {num} встречается {max_frq} раз(а)'
    else:
        return 'Все элементы уникальны'

# Alg_1 memory usage:
#  type=<class 'int'>, size=28, object=5
#  type=<class 'int'>, size=28, object=3
#  type=<class 'int'>, size=28, object=20
#  type=<class 'int'>, size=28, object=18
#  type=<class 'int'>, size=28, object=1
#  type=<class 'int'>, size=28, object=19
#
# total = 168


# вариант 2
def alg_2(arr):
    cnt = Counter(arr)
    print(f'Alg_2 memory usage: ')
    m = f'{show_size(cnt)}'
    return f"Alg_2: Число {cnt.most_common(1)[0][0]} встречается {cnt.most_common(1)[0][1]} раз(а)"

# Alg_2 memory usage:
#  type=<class 'collections.Counter'>, size=656, object=Counter({5: 3, 4: 2, 15: 2, 7: 2, 8: 1, 2: 1, 10: 1, 0: 1, 1: 1, 14: 1, 6: 1, 13: 1, 17: 1, 9: 1, 3: 1})
# 	 type=<class 'tuple'>, size=56, object=(8, 1)
# 		 type=<class 'int'>, size=28, object=8
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(4, 2)
# 		 type=<class 'int'>, size=28, object=4
# 		 type=<class 'int'>, size=28, object=2
# 	 type=<class 'tuple'>, size=56, object=(15, 2)
# 		 type=<class 'int'>, size=28, object=15
# 		 type=<class 'int'>, size=28, object=2
# 	 type=<class 'tuple'>, size=56, object=(5, 3)
# 		 type=<class 'int'>, size=28, object=5
# 		 type=<class 'int'>, size=28, object=3
# 	 type=<class 'tuple'>, size=56, object=(2, 1)
# 		 type=<class 'int'>, size=28, object=2
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(10, 1)
# 		 type=<class 'int'>, size=28, object=10
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(0, 1)
# 		 type=<class 'int'>, size=24, object=0
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(1, 1)
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(7, 2)
# 		 type=<class 'int'>, size=28, object=7
# 		 type=<class 'int'>, size=28, object=2
# 	 type=<class 'tuple'>, size=56, object=(14, 1)
# 		 type=<class 'int'>, size=28, object=14
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(6, 1)
# 		 type=<class 'int'>, size=28, object=6
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(13, 1)
# 		 type=<class 'int'>, size=28, object=13
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(17, 1)
# 		 type=<class 'int'>, size=28, object=17
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(9, 1)
# 		 type=<class 'int'>, size=28, object=9
# 		 type=<class 'int'>, size=28, object=1
# 	 type=<class 'tuple'>, size=56, object=(3, 1)
# 		 type=<class 'int'>, size=28, object=3
# 		 type=<class 'int'>, size=28, object=1
#
# total = 2896

# вариант 3
def alg_3(arr):
    a_set = set(arr)
    most_common = None
    qty_most_common = 0
    for item in a_set:
        qty = arr.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    print(f'Alg_3 memory usage: ')
    m= f'{show_size(a_set)}, {show_size(most_common)}, {show_size(qty_most_common)}, {show_size(item)}, {show_size(qty)}'
    return f'Alg_3: Число {most_common} встречается {qty_most_common} раз(а)'


# Alg_3 memory usage:
#  type=<class 'set'>, size=728, object={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 17}
# 	 type=<class 'int'>, size=24, object=0
# 	 type=<class 'int'>, size=28, object=1
# 	 type=<class 'int'>, size=28, object=2
# 	 type=<class 'int'>, size=28, object=3
# 	 type=<class 'int'>, size=28, object=4
# 	 type=<class 'int'>, size=28, object=5
# 	 type=<class 'int'>, size=28, object=6
# 	 type=<class 'int'>, size=28, object=7
# 	 type=<class 'int'>, size=28, object=8
# 	 type=<class 'int'>, size=28, object=9
# 	 type=<class 'int'>, size=28, object=10
# 	 type=<class 'int'>, size=28, object=13
# 	 type=<class 'int'>, size=28, object=14
# 	 type=<class 'int'>, size=28, object=15
# 	 type=<class 'int'>, size=28, object=17
#  type=<class 'int'>, size=28, object=5
#  type=<class 'int'>, size=28, object=3
#  type=<class 'int'>, size=28, object=17
#  type=<class 'int'>, size=28, object=1
#
# total = 1256

def main():
    n = 20
    arr = [0] * n
    for i in range(n):
        arr[i] = int(random() * 20)
    print(arr)
    show_size(arr)
    print('*' * 50)
    print(alg_1(arr))
    print('*' * 50)
    print(alg_2(arr))
    print('*' * 50)
    print(alg_3(arr))


if __name__ == '__main__':
    main()


# 1- 168
# 2- 2896
# 3- 1256
# вывод: первый алгоритм использует меньше памяти
# (хотя второй работает почти мгновенно, так как испольуется встроенная функция)
