"""
Задание 7
Определить, является ли год, который ввел пользователь, високосным или не високосным.
Алгоритм:
https://app.diagrams.net/?page-id=F0HdssvT1WAU-l7wSX0H&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
https://drive.google.com/file/d/1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS/view?usp=sharing
"""

a = int(input("Введите год: "))
if a % 4:
    print(f"Год {a} - не високосный")
else:
    print(f"Год {a} - високосный")
