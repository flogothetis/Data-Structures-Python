from BTreeNode import BTreeNode

class BTree:
	def __init__(self,minDegree):
		self.root=None
		self.t=minDegree



	def insert(self,  k ):
		#If tree is empty
		if(self.root is None):
			self.root=BTreeNode(self.t,True)
			self.root.keys[0]= k
			self.root.n+=1
		else:
			#If root is ful, then tree grows in height
			if(self.root.isNodeFull()):
				print("Spit")
				#Allocate memory or new node
				s=BTreeNode(self.t,False)
				#Make old root as child of new root
				s.C[0]=self.root
				#split the old root
				s.splitChild(0,self.root)
				#Now we have two children
				#Decide the position of the new key
				i=0
				if(s.keys[0]<k):
					i+=1
				s.C[i].insertNonFull(k)
				#Change root
				self.root=s
			else:
				self.root.insertNonFull(k)

	def  traverse(self):
		if(self.root is not None):
			self.root.traverse()


	def search(self,key):
		if (self.root is not None):
			return (self.root.search(key)==None)? None : key



if __name__=='__main__':
	t= BTree(3)
	for i in range (0,1234):
		t.insert(i)

	t.traverse()

	key=1000
	print()
	print('Search key: ', key)
	print(t.search(key))