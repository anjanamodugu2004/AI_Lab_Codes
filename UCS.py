import heapq

graph = {
    'A': [('B', 10), ('C', 15)],
    'B': [('D', 12), ('F', 15)],
    'C': [('E', 10)],
    'D': [('E', 2), ('F', 1)],
    'F': [('E', 5)],
    'E': []
}

def uniform_cost_search(start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current == goal:
            return path, cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float('inf')

path, total_cost = uniform_cost_search('A', 'E')
print(f"Optimal Path: {' -> '.join(path)}")
print(f"Total Cost: {total_cost}")
