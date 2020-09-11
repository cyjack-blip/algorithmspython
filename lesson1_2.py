"""
Задание 2
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
Алгоритм:
https://app.diagrams.net/?page-id=SrqAB-uSrEiMFuV9iCrq&hide-pages=1#G1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS
https://drive.google.com/file/d/1jy0w4PLkIXAzwbz76qYBSP8tKp96cshS/view?usp=sharing

NB! для упрощения алгоритма print приглашения ввести значения и сам ввод значения указаны на схеме одним блоком
"""

print("Координаты точки M1(x1;y1). Введите x1, x2:")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("Координаты точки M2(x2;y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print(" y = %.2f*x + %.2f" % (k, b))
