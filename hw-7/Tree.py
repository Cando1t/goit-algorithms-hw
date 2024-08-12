import math
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

#модернізація обходу дерева, для запису значень в масив
s = []
def preorder_traversal(root):
    global s
    if root:
        #print(root.val)
        s.append(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)
    return s
# шукає мінімальне значення
def min_value(root):
    return min(preorder_traversal(root))

# шукає максимальне значення
def max_value(root):
    return max(preorder_traversal(root))

# шукає суму всих елементів
def sum_value(root):
    return sum(preorder_traversal(root))





 

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)




print('Мінімальне значення:', min_value(root))
print('Максимальне значення:', max_value(root))
print('Сума значень:', sum_value(root))
