"""
Задание 3
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Алгоритм:
https://app.diagrams.net/?page-id=a755YjVcnFh0HYkA5hIH&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
https://drive.google.com/file/d/1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS/view?usp=sharing
"""

import numpy as np

print("Случайное целое число")
a1 = int(input("Введите нижнюю границу: "))
b1 = int(input("Введите верхнюю границу: "))

int_random = np.random.randint(a1, b1+1)
print(f"Случайное целое число в диапазоне [{a1}, {b1}]: {int_random}")

print("\nСлучайное вещественное число")
a2 = float(input("Введите нижнюю границу: "))
b2 = float(input("Введите верхнюю границу: "))

float_random = round(np.random.uniform(a2, b2), 10)
print(f"Случайное вещественное число в диапазоне [{a2}, {b2}]: {float_random}")

print("\nСлучайная буква")
a3 = input("Введите нижнюю границу: ")
b3 = input("Введите нижнюю границу: ")

char_random = chr(np.random.randint(ord(a3), ord(b3)+1))
print(f"Случайная буква в диапазоне [{a3}, {b3}]: {char_random}")
