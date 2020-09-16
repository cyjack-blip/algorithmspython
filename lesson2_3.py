"""
Задание 3
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843
Алгоритм:
https://app.diagrams.net/?page-id=Rz8vnFs6Qg1t9Pijctwk&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
"""

num = int(input("Введите натуральное число: "))
s = ''

while num > 0:
    s = f"{s}{num % 10}"
    num //= 10

print(f"{s}")
