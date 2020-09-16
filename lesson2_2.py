"""
Задание 2
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
Алгоритм:
https://app.diagrams.net/?page-id=vrhaKvpOc3HoDHh4iCSP&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
"""

num = int(input("Введите натуральное число: "))
even = 0
odd = 0

while num > 0:
    if (num % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10

print(f"четные: {even}, нечетные: {odd}")
