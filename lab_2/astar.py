from heapq import heappush, heappop

start = (
    (5, 8, 2),
    (1, 0, 3),
    (4, 7, 6)
)

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)


# h1: Number of Misplaced Tiles
def h1(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count = count + 1
    return count

# h2: Manhattan Distance
def h2(state):
    sum = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                index = [(r,c) for r, row in enumerate(goal) for c, col in enumerate(row) if col == state[i][j]]
                sum = sum + abs(i-index[0][0])+ abs(j-index[0][1])
    return sum

# Combined: h1 + h2
def combined(state):
    return max(h1(state), h2(state))

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j
            
def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    neighbors = []
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            board = [list(row) for row in state]
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            neighbors.append(tuple(map(tuple, board)))
            
    return neighbors

def display(state):
    for row in state:
        print(row)
    print()

def aStar(start, heuristic):
    pq = []
    heappush(pq, (heuristic(start), 0, start))
    parent = {start: None}
    g_cost = {start: 0}
    expanded = 0
    while pq:
        f, g, current = heappop(pq)
        
        if g < g_cost.get(current, float('inf')):
            continue
        
        expanded = expanded + 1
        if current == goal:
            return True, parent, expanded
        for neighbor in get_neighbors(current):
            naya_g = g + 1
            if neighbor not in g_cost or naya_g < g_cost[neighbor]:
                g_cost[neighbor] = naya_g
                f_cost = naya_g + heuristic(neighbor)
                heappush(
                    pq,
                    (f_cost, naya_g, neighbor)
                )
                parent[neighbor] = current
    return False, parent, expanded

def reconstruct(parent, current):
    path = []
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]

goalFound, parent, expanded = aStar(start, h1)
if goalFound:
    print(f"GOAL STATE FOUND AFTER EXPANDING {expanded} states using h1: Misplaced Tiles only")
    for state in reconstruct(parent, goal):
        display(state)
else:
    print(f"GOAL STATE NOT FOUND AFTER EXPANDING {expanded} states")
    
goalFound, parent, expanded = aStar(start, h2)
if goalFound:
    print(f"GOAL STATE FOUND AFTER EXPANDING {expanded} states using h2: Manhattan Distance only")
    for state in reconstruct(parent, goal):
        display(state)
else:
    print(f"GOAL STATE NOT FOUND AFTER EXPANDING {expanded} states")
    
goalFound, parent, expanded = aStar(start, combined)
if goalFound:
    print(f"GOAL STATE FOUND AFTER EXPANDING {expanded} states using h1+h2: Combined Heuristic")
    for state in reconstruct(parent, goal):
        display(state)
else:
    print(f"GOAL STATE NOT FOUND AFTER EXPANDING {expanded} states")