#task1
def bfs_basic(graph, start):
    visited = set()
    frontier = [start]  # Simulates a queue

    while frontier:
        current = frontier[0]
        frontier = frontier[1:]

        if current not in visited:
            print(current, end=' ')
            visited.add(current)
            frontier.extend(graph.get(current, []))

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS without Queue and Node class:")
bfs_basic(graph, 'A')

#Task2
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_with_queue(root):
    visited = set()
    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current.value not in visited:
            print(current.value, end=' ')
            visited.add(current.value)
            queue.extend(current.children)

# Build a tree/graph
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')

nodeA.children = [nodeB, nodeC]
nodeB.children = [nodeD, nodeE]
nodeC.children = [nodeF]

print("\nBFS with Queue and Node class:")
bfs_with_queue(nodeA)
