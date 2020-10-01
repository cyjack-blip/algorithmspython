"""
Задание 4 из 2-го урока
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
"""
import functools
import sys
import cProfile

sys.setrecursionlimit(10000)


def test_fun(func):
    lst = [0, 1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625, 0.66796875, 0.666015625]
    for i, item in enumerate(lst):
        assert item == func(i)
        print("Pass", i)


def fun_1(n):
    """ алгоритм: суммирование в цикле """
    item = 1
    summa = 0
    for i in range(n):
        summa += item
        item /= -2
    return summa

# "lesson4_1.fun_1(10)": 990 nsec per loop
# "lesson4_1.fun_1(100)": 5.28 usec per loop
# "lesson4_1.fun_1(500)": 27.5 usec per loop
# "lesson4_1.fun_1(5000)": 303 usec per loop


def fun_2(n):
    """ рекурсивный алгоритм """
    if n < 2:
        return n
    sign = 1
    if n % 2 == 0:
        sign = -1
    return sign * (1 / (2 ** (n - 1))) + fun_2(n - 1)

# "lesson4_1.fun_2(10)": 5.09 usec per loop
# "lesson4_1.fun_2(100)": 70.4 usec per loop
# "lesson4_1.fun_2(500)": 509 usec per loop
# "lesson4_1.fun_2(5000)": 18.8 msec per loop


@functools.lru_cache(maxsize=1024)
def fun_3(n):
    """ рекурсивный алгоритм с мемоизаций """
    if n < 2:
        return n
    sign = 1
    if n % 2 == 0:
        sign = -1
    return sign * (1 / (2 ** (n - 1))) + fun_2(n - 1)

# "lesson4_1.fun_3(10)": 281 nsec per loop
# "lesson4_1.fun_3(100)": 1.34 usec per loop
# "lesson4_1.fun_3(500)": 1.96 usec per loop
# "lesson4_1.fun_3(5000)": 22.6 usec per loop


#  test_fun(fun_1)
#  print(fun_1(100))

#  test_fun(fun_2)
#  print(fun_2(100))

#  test_fun(fun_3)
#  print(fun_3(100))


# cProfile.run('fun_3(5000)')
