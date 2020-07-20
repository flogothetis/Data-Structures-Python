from collections import defaultdict
import sys
from  MinHeap import MinHeap


class WeightedGraph:
	def __init__(self):
		self.graph=defaultdict(list)

	def addEdge(self,u,v,dist):
		self.graph[u].append([v,dist])
		self.graph[v].append([u,dist])

	def printArr(self, parent, n):
		for i in range(1, n):
			print ("% d - % d" % (parent[i], i))

	def PrimMST(self):
		#insert all vertices in min heap, with infinity key
		V=len(self.graph)
		# predecessors array
		p=[0]*V
		#keys arrays
		key=[0]*V
		#heap
		heap= MinHeap(V)

		for v in range(V):
			heap.insertWithoutHeaping(v,float('inf'))
			key[v]=float('inf')


		#Decrease key of the first vertex
		key[0]=0
		p[0]=0
		heap.decreaseKey(0,0)

		while heap.isEmpty() == False:
			minVertex= heap.extractMin()
			for v in self.graph[minVertex[0]]:
				id=v[0]
				weight=v[1]
				if(heap.isInMinHeap(id)  and key[id]> weight):
					key[id]= weight
					p[id]= minVertex[0]
					heap.decreaseKey(id,weight)
		self.printArr(p,V)


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
graph.PrimMST()



