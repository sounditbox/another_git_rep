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


def dfs(graph, cur_node, visited=None):
    if visited is None:
        visited = set()  # Множество для хранения посещённых вершин
    visited.add(cur_node)  # Добавляем начальную вершину в посещённые
    print(cur_node)  # Выводим посещённую вершину
    # Рекурсивно проходим по всем смежным вершинам
    for next_node in graph[cur_node]:
        if next_node not in visited:
            # Рекурсивно вызываем DFS для каждой смежной вершины
            dfs(graph, next_node, visited)
    return visited  # Возвращаем множество посещённых вершин


print(dfs(graph, 1))
