"""
Задание 4
Определить, какое число в массиве встречается чаще всего
"""

from random import random
from collections import Counter


n = 20
arr = [0] * n
for i in range(n):
    arr[i] = int(random() * 20)
print(arr)

# вариант 1
num = arr[0]
max_frq = 1
for i in range(n - 1):
    frq = 1
    for k in range(i + 1, n):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')


# вариант 2
cnt = Counter(arr)
print(f"Число {cnt.most_common(1)[0][0]} встречается {cnt.most_common(1)[0][1]} раз(а)")
