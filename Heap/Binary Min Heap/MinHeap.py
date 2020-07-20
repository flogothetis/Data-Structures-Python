class MinHeap:

	def __init__(self,maxHeapSize):
		self.heapSize=maxHeapSize
		self.size=0
		self.heap=[0]*self.heapSize

	# Function to return the position of
	# parent for the node currently
	# at pos
	def parent(self, pos):
		return pos // 2

	# Function to return the position of
	# the left child for the node currently
	# at pos
	def leftChild(self, pos):
		return 2 * pos

	# Function to return the position of
	# the right child for the node currently
	# at pos
	def rightChild(self, pos):
		return (2 * pos) + 1

	def swap(self, pos1, pos2):
		tmp=self.heap[pos1]
		self.heap[pos1]=self.heap[pos2]
		self.heap[pos2]=tmp


	def insert(self,key):
		if(self.size==self.heapSize):
			return None

		#Heapify new element
		self.heap[self.size]=key
		curr_pos= self.size
		while(self.heap[curr_pos]< self.heap[self.parent(curr_pos)]):
			self.swap(curr_pos,self.parent(curr_pos))
			curr_pos=self.parent(curr_pos)

		#Incease heap size
		self.size+=1

	def getMin(self):
		if(self.size==0):
			return None
		return self.heap[0]

	def isLeaf(self,pos):
		if(pos>= self.size//2 and pos < self.size):
			return True
		return False



	def minHeapify(self,pos):
		if(not self.isLeaf(pos)):
			if(self.heap[pos]> self.heap[self.leftChild(pos)]
			or self.heap[pos]> self.heap[self.rightChild(pos)]):

				if(self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]):
					self.swap( self.leftChild(pos), pos)
					self.minHeapify(self.leftChild(pos))
				else:
					self.swap(self.rightChild(pos), pos)
					self.minHeapify(self.rightChild(pos))

	def extractMin(self):
		if(self.size==0):
			return None
		#Store min
		min =self.getMin()
		self.heap[0]= self.heap[self.size-1]
		#Decrease size of heap
		self.size-=1
		self.minHeapify(0)
		return min


if __name__=='__main__':
	minHeap = MinHeap(15)
	minHeap.insert(5)
	minHeap.insert(3)
	minHeap.insert(17)
	minHeap.insert(10)
	minHeap.insert(84)
	minHeap.insert(19)
	minHeap.insert(6)
	minHeap.insert(22)
	minHeap.insert(9)

	print('Extract all elements....')
	while(True):
		value=minHeap.extractMin()
		if(value):
			print(value, end=' ')
		else:
			break