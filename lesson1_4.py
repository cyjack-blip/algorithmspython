"""
Задание 4
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
Алгоритм:
https://app.diagrams.net/?page-id=hgxazAHc-ibabDy5Ekb4&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
https://drive.google.com/file/d/1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS/view?usp=sharing
"""

a1 = input("Введите первую букву: ")
a2 = input("Введите вторую букву: ")

p1 = ord(a1) - 96
p2 = ord(a2) - 96

gap = p2 - p1 - 1

print(f"\nБуква {a1} на {p1} позиции\nБуква {a2} на {p2} позиции\nМежду ними {gap} букв")
