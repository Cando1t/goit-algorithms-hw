def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# Приклад графа у вигляді словника

graph = {
    'Singapore': {'San Francisco': 13574, 'Tokyo': 5308, 'Copenhagen': 9956},
    'San Francisco': {'Tokyo': 8269, 'Singapore': 13574},
    'Tokyo': {'Singapore': 5308, 'San Francisco': 8269},
    'Copenhagen': {'Singapore': 9956, 'Riga': 869},
    'Riga': {'Copenhagen': 869, 'San Francisco': 9016}
}

# Виклик функції для вершини A
print(dijkstra(graph, 'Tokyo'))
