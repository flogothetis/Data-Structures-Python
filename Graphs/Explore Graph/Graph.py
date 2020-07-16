from  collections import defaultdict


class Graph:
	def __init__(self):
		self.graph=defaultdict(list)

	def insert(self,u,v):
		self.graph[u].append(v)
