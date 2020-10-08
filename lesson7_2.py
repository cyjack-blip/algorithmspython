# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
#

from random import random
import operator


N = 20
a = []
b = []
for i in range(N):
    tm = int(random() * 5000) / 100
    a.append(tm)
    b.append(tm)
print(f'исходный вещесвенный список:\n{a}')
print('*' * 80)


def merge_sort(L, compare=operator.lt):

    def merge(left, right, compare):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        print(left, right)  # вывод промежуточных шагов
        return merge(left, right, compare)


print('демонстрация сортировки слиянием (merge)')
res = merge_sort(b)
print('*' * 80)
print(f'отсортированный вещественный список:\n{res}')
