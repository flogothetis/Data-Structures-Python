class BTreeNode:
	def __init__(self,t=2,isLeaf=False):
		self.t=t
		self.isLeaf=isLeaf
		#array of keys for each node
		self.keys=[None]* (2*self.t-1)
		#array of child pointer
		self.C=[None]*(2*t)
		#alrady inserted number of keys
		self.n=0

	def isNodeFull(self):
		if self.n == 2*self.t -1:
			return True
		return False

	def splitChild(self, i , y ):
		#Create a new node, which is going
		#to store (t-1) keys of y
		z=BTreeNode(y.t,y.isLeaf)
		z.n=self.t-1

		#Copy the last (t-1) keys of y to z
		for j in range (0,self.t-1):
			z.keys[j]=y.keys[j+self.t]

		#Copy the last t children of y to z
		if(y.isLeaf==False):
			for j in range(0, self.t):
				z.C[j] = y.C[j + self.t]
		y.n=self.t-1

		#Since self node is going to have a new
		#child, create space
		for j in range (self.n,i,-1):
			self.C[j+1]=self.C[j]
		self.C[i+1]=z
		#Move one position ahead all children
		for j in range(self.n-1,i-1,-1):
			self.keys[j+1]=self.keys[j]
		self.keys[i]=y.keys[self.t-1]
		self.n+=1

	def search(self,key):
		i=0

		while(i < self.n and key > self.keys[i]):
			i+=1

		if(self.keys[i]==key):
			return self
		if(self.isLeaf==True):
			return None
		return self.C[i].search(key)

	def insertNonFull(self, k):
		i=self.n-1
		if(self.isLeaf==True):
			#Move all greater keys one place ahead
			while(i>=0 and self.keys[i]>k):
				self.keys[i+1]=self.keys[i]
				i-=1
			#Insert key
			self.keys[i+1]= k
			self.n+=1
		else:
			while (i >= 0 and self.keys[i] > k):
				i -= 1
			if self.C[i+1].isNodeFull():
				self.splitChild(i+1, self.C[i+1])
				if(self.keys[i+1]<k):
					i+=1
			self.C[i+1].insertNonFull(k)


	def traverse (self):
		for i in range(0,self.n):
			if( self.isLeaf==False):
				self.C[i].traverse()
			print(self.keys[i], end=' ')

		if(self.isLeaf==False):
			self.C[self.n].traverse()






