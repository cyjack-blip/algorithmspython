"""
Задание 6
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ
Алгоритм:
https://app.diagrams.net/?page-id=Fdn6O-2YgSkAM9akGX5q&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
"""

from random import randint

while True:
    number = randint(0, 100)
    i = 0
    while i < 10:
        guess = int(input("Угадайте число 1-100?: "))
        i += 1
        if guess == number:
            print("Вы угадали")
            break
        elif guess > number:
            print("Загаданное число меньше")
            continue
        else:
            print("Загаданное число больше")
            continue
    print(f"Было загадано {number}.")
    more_try = input("Хотите еще раз (y/n)?: ")
    if more_try != 'y':
        break
