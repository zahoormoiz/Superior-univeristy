import heapq

# Define directions: Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, position, g, h, parent=None):
        self.position = position  # (x, y)
        self.g = g  # Cost from start
        self.h = h  # Heuristic to goal
        self.f = g + h  # Total cost
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, Node(start, 0, heuristic(start, goal)))

    closed_set = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed_set.add(current.position)

        for dx, dy in directions:
            neighbor = (current.position[0] + dx, current.position[1] + dy)

            if (0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] == 0 and
                neighbor not in closed_set):

                g = current.g + 1
                h = heuristic(neighbor, goal)
                node = Node(neighbor, g, h, current)

                heapq.heappush(open_list, node)

    return None  # No path found
