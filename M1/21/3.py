from collections import deque

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def bfs(graph, start):
    visited = set()  # Множество для посещённых вершин
    queue = deque(graph[start])  # Очередь для вершин на текущем уровне
    visited.add(start)  # Добавляем стартовую вершину
    print(f'Root: {start}')

    while queue:
        node = queue.popleft()  # Берём вершину из начала очереди
        print(f"Посещаем вершину: {node}")
        visited.add(node)
        # Добавляем все смежные вершины в очередь
        for adj_node in graph[node]:
            if adj_node not in visited:
                visited.add(adj_node)
                queue.append(adj_node)


bfs(graph, 1)
