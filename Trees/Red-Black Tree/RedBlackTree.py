from Node import Node

class RedBlackTree:
	def __init__(self):
		self.root=None
		self.size=0

	def rightRotation(self,node):
		if(node is None):
			return
		x=node.left
		y=x.left
		if(node.parent==None):
			self.root =x
		else:
			x.parent=node.parent
			if(node.parent.isLeftChild):
				x.isLeftChild=True
				x.parent.left=x
			else:
				x.isLeftChild=False
				x.parent.right=x


		##### move node.left.right child
		if(x.right is not None):
			node.left=x.right
			node.left.isLeftChild=True
			node.left.parent=node

		x.right=node
		node.parent=x
		node.isLeftChild=True


	def leftRotation(self,node):
		temp=node.right
		node.right=temp.left
		if(node.right!=None):
			node.right.parent=node
			node.right.isLeftChild=False
		if(node.parent==None):
			self.root=temp
		else:
			temp.parent=node.parent
			if(node.isLeftChild):
				temp.isLeftChild=True
				temp.parent.left=temp
			else:
				temp.isLeftChild=False
				temp.parent.right=temp
		temp.left=node
		node.isLeftChild=True
		node.parent=temp

	def leftRightRotation(self, node):
		self.leftRotation(node.left)
		self.rightRotation(node)

	def rotateTree(self,node):
		if(node.isLeftChild):
			if(node.parent.isLeftChild):
				self.rightRotation(node.parent.parent)
				node.isBlack=False
				node.parent.isBlack=True
				node.parent.right.isBlack=False
			else:
				self.rightLeftRotation(node.parent.parent)
				node.isBlack=True
				node.right.isBlack=False
				node.left.isBlack=False
		else:
			if(node.parent.isRightChild):
				self.leftRotation(node.parent.parent)
				node.isBlack=False
				node.parent.isBlack=True
				node.parent.left.isBlack=False
			else:
				self.rightLefttRotation(node.parent.parent)
				node.isBlack = True
				node.right.isBlack=False
				node.left.isBlack=False


	def correctTree(self,node):
		if(node.isLeftChild):
			#Black Aunt
			if(node.parent.parent.right is None or node.parent.parent.right.isBlack):
				return  self.rotateTree(node)
			if(node.parent.parent.right!=None ):
				node.parent.parent.right.isBlack=True
				node.parent.isBlack=True
				node.parent.parent.isBlack=False
		else:
			if (node.parent.parent.left is None or node.parent.parent.left.isBlack):
				return self.rotateTree(node)
			if (node.parent.parent.left != None):
				node.parent.parent.left.isBlack = True
				node.parent.isBlack = True
				node.parent.parent.isBlack = False





	def checkColor(self,node):
		if(node==self.root):
			node.isBlack=True
			return
		if(not node.isBlack and not node.parent.isBlack):
			self.correctTree(node)

		self.checkColor(node.parent)



	def insert(self,key):
		#Create a new Node
		newNode= Node(key)
		if(self.root is None):
			self.root=newNode
			return
		#else invoke recursive function
		self.insertNode(self.root,newNode)
		#check violation
		self.checkColor(newNode)
		self.size+=1
		self.root.isBlack=True

	def insertNode(self,root,newNode):
		if(root is None):
			root=newNode
			return

		if(newNode.key <= root.key):
			if(root.left==None):
				root.left=newNode
				newNode.parent=root
				newNode.isLeftChild=True
				return
			self.insertNode(root.left,newNode)
		else:
			if (root.left == None):
				root.right = newNode
				newNode.parent = root
				newNode.isLeftChild = False
				return
			self.insertNode(root.right,newNode)


