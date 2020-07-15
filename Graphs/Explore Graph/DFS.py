from Graph import Graph

#Time Complexity: O(V+E)
class DFS(Graph):
	def DFSUtil(self,u,visited):
		visited[u]=True
		print(u, end=' ')

		for v in self.graph[u]:
			if visited==False:
				self.DFSUtil(v,visited)

	def DFS(self):
		#Mark all nodes as not visited
		visited=[False]*len(self.graph)

		for u in range (len(self.graph)):
			if visited[u]==False:
				self.DFSUtil(u,visited)



# Driver code

# Create a graph given in
# the above diagram
g = DFS()
g.insert(0, 1)
g.insert(0, 2)
g.insert(1, 2)
g.insert(2, 0)
g.insert(2, 3)
g.insert(3, 3)

print("Following is Breadth First Traversal"
	  " (starting from vertex 2)")
g.DFS()