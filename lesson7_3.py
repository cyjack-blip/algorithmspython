# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).
#

from random import randint
from statistics import median

N = 51
a = []
b = []
c = []
for i in range(N):
    tm = randint(1, 100)
    a.append(tm)
    b.append(tm)
    c.append(tm)
print(f'исходный список:\n{a}')
print('*' * 50)

print(f'значение для проверки statistics.median(): {median(a)}')


def get_median(numeric_values):
    """используем предварительную сортировку встроенной функцией sorted()"""
    the_values = sorted(numeric_values)
    if len(the_values) % 2 == 1:
        return the_values[int((len(the_values)+1)/2) - 1]
    else:
        lower = the_values[len(the_values)/2 - 1]
        upper = the_values[len(the_values)/2]
        return (float(lower + upper))/2


def median2(b):
    """не используем сортировку.
    последовательно убираем парами максимальный и минимальный элементы:
    отъедаем сосиску с двух сторон, встретимся на середине"""
    bb = b
    while len(bb) > 1:
        min = bb[0]
        max = bb[0]
        for i in range(len(bb)):
            if bb[i] > max:
                max = bb[i]
            if bb[i] < min:
                min = bb[i]
        bb.remove(min)
        bb.remove(max)
    return bb.pop()


def median3(c):
    """используем сортировку кучей, такого варианта еще не было"""
    def heap_sort(nums):
        def heapify(nums, heap_size, root_index):
            largest = root_index
            left_child = (2 * root_index) + 1
            right_child = (2 * root_index) + 2
            if left_child < heap_size and nums[left_child] > nums[largest]:
                largest = left_child
            if right_child < heap_size and nums[right_child] > nums[largest]:
                largest = right_child
            if largest != root_index:
                nums[root_index], nums[largest] = nums[largest], nums[root_index]
                heapify(nums, heap_size, largest)

        n = len(nums)
        for i in range(n, -1, -1):
            heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)

    heap_sort(c)
    return c[len(c)//2]


print('медиана с встроенной сортировкой: ', get_median(a))
print('медиана с сортировкой кучей: ', median3(c))
print('медиана без сортировки: ', median2(b))
