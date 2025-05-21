#task1
def dfs_stack(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add neighbors in reverse order for correct DFS
            stack.extend(reversed(graph.get(node, [])))

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS using stack:")
dfs_stack(graph, 'A')



#task 2

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')

# Creating a binary tree:
#         A
#       /   \
#      B     C
#     / \   /
#    D   E F

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')

print("\nInorder Traversal:")
inorder(root)     # D B E A F C

print("\nPreorder Traversal:")
preorder(root)    # A B D E C F

print("\nPostorder Traversal:")
postorder(root)   # D E B F C A


