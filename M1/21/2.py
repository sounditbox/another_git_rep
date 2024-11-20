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


def dfs(graph, start_node):
    visited = set()
    stack = []  # stack: .pop(), .append()

    visited.add(start_node)
    stack += graph[start_node]
    print(f'Root: {start_node}')
    while stack:
        next_node = stack.pop()
        print(next_node)
        visited.add(next_node)
        for adj_node in graph[next_node]:
            if adj_node not in visited:
                stack.append(adj_node)

    return visited


print(dfs(graph, 1))
