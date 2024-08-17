import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"  # Початковий колір - чорний
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_colors(n):
    # Створює градієнт кольорів від темного до світлого
    colors = list(mcolors.TABLEAU_COLORS.values())
    return colors[:n]


def bfs(root):
    queue = [root]
    visited_order = []
    colors = generate_colors(len(queue))

    i = 0
    while queue:
        node = queue.pop(0)
        visited_order.append(node)

        # Призначаємо вузлу колір
        node.color = colors[i % len(colors)]
        i += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_order


def dfs(root):
    stack = [root]
    visited_order = []
    colors = generate_colors(len(stack))

    i = 0
    while stack:
        node = stack.pop()
        visited_order.append(node)

        # Призначаємо вузлу колір
        node.color = colors[i % len(colors)]
        i += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_order


# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Обхід у ширину (BFS)
print("BFS Traversal:")
bfs(root)
draw_tree(root)

# Повертаємо кольори вузлів до початкових для наступного обходу
for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]:
    node.color = "#000000"

# Обхід у глибину (DFS)
print("DFS Traversal:")
dfs(root)
draw_tree(root)
