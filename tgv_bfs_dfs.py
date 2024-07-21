from collections import deque
from tgv_graph import get_tgv_graph_data

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)



def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

graph = get_tgv_graph_data()
print(f'DFS algorithm path of TGV rail roads, starting from Marseille city:')
print()
dfs_recursive(graph, 'Marseille')
print()
print()
print('BFS algorithm path of TGV rail roads, starting from Marseille city:')
print()
bfs_recursive(graph, deque(['Marseille']))