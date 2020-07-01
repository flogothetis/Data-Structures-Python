from Node import Node


class BST:
	def __init__(self):
		self.root=None

	def insert(self,key):
		self.insertRec(self.root,key)

	def insertRec(self,node,key):
		#Insert at root
		if(node == None):
			node= Node(key)
			return

		#else, create either a intermediate or leaf node
		if( key <= node.data):
			self.insertRec(node.left,key)
		else:
			self.insertRec(node.right,key)

	#Search on a binary tree for a key
	def search(self,key):
		self.searchRec(self.root,key)

	def searchRec(self,node,key):
		#Insert at root
		if(node == None or node ==key):
			return node
		elif( key < node.data):
			self.searchRec(node.left,key)
		else:
			self.searchRec(node.right,key)

	def delete(self,key):
		node=self.search(self.root,key)
		if(node!=None):
			# Node with only one child or no child
			if(node.left is None and node.right is None):
				node=None
			elif ( node.left is None or node.right is None):
				if( node.left is None):
					node.right = node.right.










