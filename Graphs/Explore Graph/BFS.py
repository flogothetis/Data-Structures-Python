from Graph import Graph

class BFS(Graph):

	def BFS(self,s):
		#Mark all nodes as not visited
		visited=[False]*len(self.graph)
		#Create a FIFO queue
		queue=[]
		#append node -s- in queue
		queue.append(s)

		while queue:
			node=queue.pop(0)
			print(node, end=' ')

			for u in self.graph[node]:
				if( visited[u]==False):
					visited[u]=True
					queue.append(u)


# Driver code

# Create a graph given in
# the above diagram
g = BFS()
g.insert(0, 1)
g.insert(0, 2)
g.insert(1, 2)
g.insert(2, 0)
g.insert(2, 3)
g.insert(3, 3)

print("Following is Breadth First Traversal"
	  " (starting from vertex 2)")
g.BFS(2)