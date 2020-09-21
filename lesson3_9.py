"""
Задание 9
Найти максимальный элемент среди минимальных элементов столбцов матрицы
"""

from random import random

m = 5  # количество столбцов
n = 5  # количество строк
r = 200  # диапазон случайных чисел
a = []

# заолнение исходной матрицы
for i in range(n):
    b = []
    for j in range(m):
        k = int(random() * r)
        b.append(k)
        print('%4d' % k, end='')
    a.append(b)
    print()

# нахождение мамксимамльного среди минимамльных
mx = -1
for j in range(m):
    mn = r
    for i in range(n):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn

print("Максимальный среди минимальных: ", mx)
