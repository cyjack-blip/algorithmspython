"""
Задание 4
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры
Алгоритм:
https://app.diagrams.net/?page-id=HTWLsSN3zPXcxTVKzDrP&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
"""

num = int(input("Введите натуральное число: "))

res = 1
sign = -1

while num > 1:
    res = res + res / 2 * sign
    sign *= -1
    num -= 1

print(res)
