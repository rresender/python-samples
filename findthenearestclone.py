from collections import defaultdict

class Graph:

    colors = []

    def __init__(self, colors):
        self.colors = colors 

    graph = defaultdict(list)
    color_node = defaultdict(list)

    def addEdge(self, u, v): 
        self.graph[u].append(v)
        self.graph[v].append(u)
        if u not in self.color_node[self.colors[u-1]]:
            self.color_node[self.colors[u-1]].append(u)
        if v not in self.color_node[self.colors[v-1]]:
            self.color_node[self.colors[v-1]].append(v)

    def bfs_shortest_path(self, start, goal):
        explored = []
        queue = [[start]]
        if start == goal:
            return -1
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return len(new_path) - 1
                explored.append(node)

        return -1

def findShortest(graph_nodes, graph_from, graph_to, ids, val):

    g = Graph(ids)

    for i in range(len(graph_from)):
        g.addEdge(min(graph_from[i], graph_to[i]), max(graph_from[i], graph_to[i]))

    cn = g.color_node[val]
    if len(cn) < 2:
        return -1

    return g.bfs_shortest_path(cn[0], cn[1])

if __name__ == '__main__':
    print(findShortest(4, [1, 1, 4], [2, 3, 2], [1, 2, 3, 4], 2))
    print(findShortest(4, [1, 1, 4], [2, 3, 2], [1, 2, 1, 1], 1))
    print(findShortest(6, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2))
    print(findShortest(7, [1, 1, 1, 5, 2, 3], [6, 5, 2, 7, 3, 4], [1, 2, 3, 1, 2, 3, 1], 1))
    print(findShortest(7, [1, 1, 1, 5, 2, 3, 1], [6, 5, 2, 7, 3, 4, 8], [1, 2, 3, 1, 2, 3, 1, 1], 1))
    
