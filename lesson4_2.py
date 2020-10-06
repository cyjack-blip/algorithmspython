# Задание 2
#
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
#
# Внимание! В программе первое простое число считается = 2
#
#  для того чтобы получить n-ое число, надо определить какого размера массив чисел просеивать через решето
#  нужное нам n-ое простое число будет оценочно не больше max
# max = int(n * (math.log(n) + math.log(math.log(n)) - 0.5))

import functools
import math
import cProfile


def sieve(n):
    """решето эратосфена просеивает n элементов"""
    def _max_range(n):
        return int(n * (math.log(n) + math.log(math.log(n)) - 0.5)) if n > 20 else 80

    max = _max_range(n)
    m = (max - 1) // 2
    b = [True]*m
    i, p, ps = 0, 3, [2]
    while p*p < max:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i += 1
        p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1
        p += 2
    return ps[n-1]

# "lesson4_2.sieve(10)" 1000 loops, best of 5: 6.86 usec per loop
# "lesson4_2.sieve(100)" 1000 loops, best of 5: 51.8 usec per loop
# "lesson4_2.sieve(1000)" 1000 loops, best of 5: 972 usec per loop
# "lesson4_2.sieve(5000)" 1000 loops, best of 5: 6.35 msec per loop

# cProfile.run('sieve(10)'), 26 function calls in 0.000 seconds
# cProfile.run('sieve(100)'), 110 function calls in 0.000 seconds
# cProfile.run('sieve(1000)'), 1052 function calls in 0.001 seconds
# cProfile.run('sieve(5000)'), 5211 function calls in 0.010 seconds

# сложность алгоритма линейная O(n)

def get_n_prime(a):
    """получает простое число перебором"""
    @functools.lru_cache()
    def _check_prime(n):
        if n < 1:
            return False
        for i in range(2, n, 2):
            if n % i == 0:
                return False
        return True

    i = 1
    while a > 0:
        i += 1
        if _check_prime(i):
            a -= 1
    return i

# "lesson4_2.get_n_prime(10)" 1000 loops, best of 5: 21.1 usec per loop
# "lesson4_2.get_n_prime(100)" 1000 loops, best of 5: 1.2 msec per loop
# "lesson4_2.get_n_prime(1000)" 1000 loops, best of 5: 186 msec per loop
# "lesson4_2.get_n_prime(5000)" 100 loops, best of 5: 6.01 sec per loop

# cProfile.run('get_n_prime(10)') 49 function calls in 0.000 seconds
# cProfile.run('get_n_prime(100)') 561 function calls in 0.001 seconds
# cProfile.run('get_n_prime(1000)') 7939 function calls in 0.201 seconds
# cProfile.run('get_n_prime(5000)') 48631 function calls in 6.255 seconds

# сложность алгоритма логарифмическая O(log n)

def prime_7(n):
    """ вариант решета """
    def _max_range(n):
        return int(n * (math.log(n) + math.log(math.log(n)) - 0.5)) if n > 20 else 80
    max = _max_range(n)
    lst = [2]
    for i in range(3, max + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[n-1]

# "lesson4_2.prime_7(10)" 1000 loops, best of 5: 13.4 usec per loop
# "lesson4_2.prime_7(100)" 1000 loops, best of 5: 128 usec per loop
# "lesson4_2.prime_7(1000)" 1000 loops, best of 5: 3.3 msec per loop
# "lesson4_2.prime_7(5000)" 1000 loops, best of 5: 30.7 msec per loop

# cProfile.run('prime_7(10)'), 26 function calls in 0.000 seconds
# cProfile.run('prime_7(100)'), 110 function calls in 0.000 seconds
# cProfile.run('prime_7(1000)'), 1052 function calls in 0.004 seconds
# cProfile.run('prime_7(5000)'), 5211 function calls in 0.037 seconds

# сложность алгоритма линейная O(n)


n = 100

# print(f'Result by sieve {sieve(n)}')
# print(f'Result by ya_prime {prime_7(n)}')
# print(f'Result by bruteforce {get_n_prime(n)}')

# cProfile.run('prime_7(5000)')

