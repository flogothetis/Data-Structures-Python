class Graph:
    def __init__(self):
        self.graph = []
        self.parent = []
        self.dist = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printShortestPath(self, src, dist):
        if src is None or dist is None:
            return
        print (dist, end =' ')
        self.printShortestPath(src, self.parent[dist])

    def BellmanFord(self, src):
        V = len(self.graph)
        # Init distances
        self.dist = [float('inf')] * V
        # Init parents
        self.parent = [None] * V
        # Decrease dist of src vertex
        self.dist[src] = 0

        # Relax all edges V-1 times, since every path from a source to
        # ant destination has at most V-1 edges
        for _ in range(V - 1):
            for edge in self.graph:
                [u, v, w] = edge
                if self.dist[v] > self.dist[u] + w:
                    self.dist[v] = self.dist[u] + w
                    self.parent[v] = u
        # Check for negative cycles. If there is a negative cycle, then
        # we could always relax more, due to the negative edges
        for edge in self.graph:
            [u, v, w] = edge
            if self.dist[v] > self.dist[u] + w:
                print('There is a negative-cycle in graph')
                return


# driver code to test above functionality

g = Graph()
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
g.BellmanFord(0)
print("Shortest Path from vertex 4 to vertex 0 is: ")
g.printShortestPath(0,4)
