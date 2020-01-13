from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, u, v, d):
        self.edges[u].append(v)
        self.edges[v].append(u)
        self.distances[(u, v)] = d
    
def min_distance(nodes, visited):
    min = None
    for node in nodes:
        if node in visited:
            if min is None:
                min = node
            elif visited[node] < visited[min]:
                min = node
    return min

def dijsktra(graph, source):
    
    visited = {source: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:

        min = min_distance(nodes, visited)

        if min is None:
            break

        nodes.remove(min)
        
        w = visited[min]

        for edge in graph.edges[min]:
            weight = w + graph.distance[(min, edge)]

            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min

    return visited, path