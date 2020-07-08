import math
from FibonacciTree import FibonacciTree
class FibonacciHeap:
	def __init__(self):
		self.trees=[]
		self.least=None
		self.count=0

	def insert(self,value):
		newTree=FibonacciTree(value)
		self.trees.append(newTree)
		if(self.least is None or value < self.least.value):
			self.least=newTree
		self.count+=1

	def getMin(self):
		if(self.least is None):
			return None
		return self.least.value



	def consolidate(self):
		aux =  [None] * int(math.floor(math.log(self.count,1.618)))
		while(self.trees !=[]):
			x=self.trees[0]
			order=x.order
			self.trees.remove(x)
			while aux[order] is not None:
				y=aux[order]
				if(x.value>y.value):
					x,y=y,x
					x.add_at_end(y)
					aux[order]=None
					order+=1
			aux[order]=x
		self.least=None
		#Find new min and re-create tree
		for k in aux:
			if k is not None:
				self.trees.append(k)
				if(self.least is None or k.value<self.least.value):
					self.least=k


	def extractMin(self):
		smallest =self.least
		if(smallest is not None):
			for child in smallest.child:
				self.trees.append(child)
			#remove smallest for root list
			self.trees.remove(smallest)
			if self.trees==[]:
				self.least= None
			else:
				self.least=self.trees[0]
				self.consolidate()
			self.count-=1
		return smallest.value

fibonacci_heap = FibonacciHeap()

fibonacci_heap.insert(7)
fibonacci_heap.insert(3)
fibonacci_heap.insert(17)
fibonacci_heap.insert(24)

print('the minimum value of the fibonacci heap: {}'.format(fibonacci_heap.getMin()))

print('the minimum value removed: {}'.format(fibonacci_heap.extractMin()))