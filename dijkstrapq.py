from collections import defaultdict
from heapq import *

def dijkstra(edges, start, goal):

    g = defaultdict(list)

    for u, v, d in edges:
        g[u].append((d, v))

    queue = [(0, start, ())]
    visited = set()
    distances = {start: 0}

    while queue:
        
        (cost, min, path) = heappop(queue)

        if min not in visited:
            
            visited.add(min)
            
            path = (min, path)
            
            if min == goal: 
                return (cost, path)

            for d, node in g.get(min, ()):
                if node in visited: 
                    continue

                prev = distances.get(node, None)
                next = cost + d

                if prev is None or next < prev:
                    distances[node] = next
                    heappush(queue, (next, node, path))

    return float("inf")

if __name__ == "__main__":

    edges = [
        ("A", "B", 4),
        ("A", "C", 3),
        ("A", "E", 7),
        ("B", "A", 4),
        ("B", "C", 6),
        ("B", "D", 5),
        ("C", "A", 3),
        ("C", "B", 6),
        ("C", "D", 11),
        ("C", "E", 8),
        ("D", "B", 5),
        ("D", "C", 11),
        ("D", "E", 2),
        ("D", "F", 2),
        ("D", "G", 10),
        ("E", "C", 8),
        ("E", "D", 2),
        ("E", "G", 5),
        ("F", "D", 2),
        ("F", "G", 3),
        ("G", "D", 10),
        ("G", "E", 5),
        ("G", "F", 3)
    ]

    # edges = [
    #     ("A", "B", 4),
    #     ("A", "C", 3),
    #     ("A", "E", 7),
    #     ("B", "C", 6),
    #     ("B", "D", 5),
    #     ("C", "D", 11),
    #     ("C", "E", 8),
    #     ("D", "E", 2),
    #     ("D", "F", 2),
    #     ("D", "G", 10),
    #     ("E", "G", 5),
    #     ("F", "G", 3),
    #     ("G", "F", 3)
    # ]

    # edges = [
    #     ("A", "B", 7),
    #     ("A", "D", 5),
    #     ("B", "C", 8),
    #     ("B", "D", 9),
    #     ("B", "E", 7),
    #     ("C", "E", 5),
    #     ("D", "E", 15),
    #     ("D", "F", 6),
    #     ("E", "F", 8),
    #     ("E", "G", 9),
    #     ("F", "G", 11)
    # ]

    print("=== Dijkstra ===")
    # print(edges)
    # print("A -> E:")
    # print(dijkstra(edges, "A", "F"))
    # print("F -> G:")
    print(dijkstra(edges, "F", "G"))