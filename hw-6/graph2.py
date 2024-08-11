import networkx as nx

#---directed graph---
G = nx.DiGraph(directed=True)

# add nodes
G.add_node('Singapore')
G.add_node('San Francisco')
G.add_node('Tokyo')
G.add_nodes_from(['Riga', 'Copenhagen'])

# add edges
G.add_edge('Singapore','San Francisco', weight=13574)
G.add_edge('San Francisco','Tokyo', weight=8269)
G.add_edge('Riga','Copenhagen', weight=868)
G.add_edge('Copenhagen','Singapore', weight = 9956)
G.add_edge('Singapore','Tokyo', weight = 5308)
G.add_edge('Riga','San Francisco', weight=9016)
G.add_edge('San Francisco','Singapore', weight=13574)
G.add_edge('Copenhagen','Riga', weight = 868)
G.add_edge('Singapore', 'Copenhagen', weight = 9956)
G.add_edge('Tokyo', 'Singapore', weight = 5308)
G.add_edge('Tokyo', 'San Francisco', weight=8269)

# set layout
pos = nx.circular_layout(G)

# draw graph
nx.draw(G, pos, with_labels = True)

# draw edge labels
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
        ("Singapore","Tokyo"): '2 flights daily', 
        ("San Francisco","Singapore"): '5 flights daily',
    },
    font_color='red'
)


num_nodes = G.number_of_nodes() 
num_edges = G.number_of_edges() 
#is_connected = nx.is_connected(G)  
print('кількість вузлів:', num_nodes, ', кількість ребер:', num_edges)
print(G.degree)


# алгоритм DFS
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

dfs_recursive(G, 'Tokyo')

# BFS алгоритм
from collections import deque

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  


# Запуск алгоритму BFS
bfs_iterative(G, 'Tokyo')