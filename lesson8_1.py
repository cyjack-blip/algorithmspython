"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


def handshake(friends):
    graph = []

    for i in range(friends):
        for j in range(friends):
            if i != j:
                graph.append((i, j))

    return len(graph) // 2


friends = int(input('Введите количество встретившихся друзей: '))
print(f'Количество рукопожатий :', handshake(friends))
