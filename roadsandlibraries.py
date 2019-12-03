from collections import defaultdict

class Graph: 
  
    def __init__(self, size): 
        # self.graph = defaultdict(list) 
        self.graph = {x: list() for x in range(1, size + 1)}
  
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
        self.graph[v].append(u)
  
    def dfs_util(self, v, visited, adjacents=None):
        if adjacents == None:
            adjacents = list() 
    
        visited[v] = True
        adjacents.append(v)
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.dfs_util(i, visited, adjacents)

        return adjacents
  
    def dfs(self):

        length = len(self.graph) + 1
  
        visited =[False] * (length)
        clusters = list()

        for i in range(1, length):
            if visited[i] == False: 
                clusters.append(self.dfs_util(i, visited))

        return clusters

def roadsAndLibraries(n, c_lib, c_road, cities):
    g = Graph(n)

    for u,v in cities:
        g.addEdge(min(u, v), max(u, v))
    
    if c_lib < c_road:
        return c_lib * n
    
    clusters = g.dfs()
    print(clusters)
    total = 0
    for c in clusters:
        total += len(c) - 1

    return (len(clusters) * c_lib) + (total * c_road)

if __name__ == '__main__':

# 2
# 3 3 2 1
# 1 2
# 3 1
# 2 3
# 6 6 2 5
# 1 3
# 3 4
# 2 4
# 1 2
# 2 3
# 5 6

    # q = 1

    # for q_itr in range(q):

    #     nmC_libC_road = "6 6 2 5".split()

    #     n = int(nmC_libC_road[0])

    #     m = int(nmC_libC_road[1])

    #     c_lib = int(nmC_libC_road[2])

    #     c_road = int(nmC_libC_road[3])

    #     cities = [(1, 3), (3, 4), (2, 4), (1, 2), (2, 3), (5, 6)]
      
    #     result = roadsAndLibraries(n, c_lib, c_road, cities)

    #     print(str(result) + '\n')
    
    # q = 1

    # for q_itr in range(q):
    #     nmC_libC_road = "3 3 2 1".split()

    #     n = int(nmC_libC_road[0])

    #     m = int(nmC_libC_road[1])

    #     c_lib = int(nmC_libC_road[2])

    #     c_road = int(nmC_libC_road[3])

    #     cities = [(1,2), (3,1), (2, 3)]
       
    #     result = roadsAndLibraries(n, c_lib, c_road, cities)

    #     print(str(result) + '\n')

# 1
# 5 3 6 1
# 1 2
# 1 3
# 1 4

    q = 1

    for q_itr in range(q):
        nmC_libC_road = "5 3 6 1".split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = [(1,2), (1,3), (1, 4)]
       
        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result) + '\n')


