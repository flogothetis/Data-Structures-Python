class Graph:
    def __init__(self):
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(self, parent, parent[node])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def KruskalMST(self):
        result = []
        i = 0  # used for sorted edges
        e = 0  # used for result

        # Sort edges in ascending order
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []
        V = len(self.graph)
        for node in range(V):
            parent.append(node)
            rank.append(0)

        while e < V - 1:
            # peek the smallest edge
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
