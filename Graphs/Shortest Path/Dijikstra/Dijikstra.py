from collections import defaultdict
import sys
from MinHeap import MinHeap


class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        # predecessors array
        p = []
        # distance from parent array
        dist = []

    def addEdge(self, u, v, dist):
        self.graph[u].append([v, dist])
        self.graph[v].append([u, dist])

    def printShortestPath(self, start, end):
        print(end, end=' ')
        if end == start or self.dist[end] == 0:
            return
        self.printShortestPath(start, self.p[end])

    def DijikstraMST(self):
        # insert all vertices in min heap, with infinity key
        V = len(self.graph)
        # predecessors array
        self.p = [0] * V
        # keys arrays
        self.dist = [0] * V
        # heap
        heap = MinHeap(V)

        for v in range(V):
            heap.insertWithoutHeaping(v, float('inf'))
            self.dist[v] = float('inf')

        # Decrease key of the first vertex
        self.dist[0] = 0
        self.p[0] = 0
        heap.decreaseKey(0, 0)

        while not heap.isEmpty():
            minVertex = heap.extractMin()
            for v in self.graph[minVertex[0]]:
                id = v[0]
                weight = v[1]
                if heap.isInMinHeap(id) and self.dist[id] > self.dist[minVertex[0]] + weight:
                    self.dist[id] = self.dist[minVertex[0]] + weight
                    self.p[id] = minVertex[0]
                    heap.decreaseKey(id, self.dist[id])


# Driver program to test the above functions
graph = WeightedGraph()
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.DijikstraMST()
graph.printShortestPath(1, 5)
