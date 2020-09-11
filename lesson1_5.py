"""
Задание 5
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
Алгоритм:
https://app.diagrams.net/?page-id=cKQf3hZWiOmXTb9jmviH&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
"""

a = int(input("Введите позицию буквы: "))
b = chr(a + 96)
print(f"На позиции {a} буква {b}")
