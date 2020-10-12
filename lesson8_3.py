"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

import random


def make_graph(x):
    graph = []
    for i in range(x):
        point = set()
        num = random.randint(1, n // 2)
        while len(point) < num:
            spam = random.randint(0, n - 1)
            if spam != i:
                point.add(spam)
        graph.append(point)
    return graph


def dfs(start, visited, prev, graph_lst):
    visited[start] = True
    for i in graph_lst[start]:
        if not visited[i]:
            prev[i] = start
            dfs(i, visited, prev, graph_lst)


n = int(input('Введите число вершин для создания графа: '))
graph = make_graph(n)
print('Сгенерированный не взвешенный ориентированный граф в виде списка смежности:')
print({i: graph[i] for i in range(n)})

start = int(input('Введите номер вершины для старта: '))

is_visited = [False] * n
prev_elem = [None] * n
dfs(start, is_visited, prev_elem, graph)

print({i: 'visited' if is_visited[i] else 'not visited' for i in range(n)})
