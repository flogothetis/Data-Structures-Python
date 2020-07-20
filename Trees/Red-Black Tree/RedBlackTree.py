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
		x.parent = node.parent

		if(node.parent==None):
			self.root =x

		else:
			if(node.isLeftChild):
				x.isLeftChild=True
				x.parent.left=x
			else:
				x.isLeftChild=False
				x.parent.right=x

		if(x.right is not None):
			node.left=x.right
			node.left.isLeftChild=True
			node.left.parent=node
		else:
			node.left=None

		x.right=node
		node.parent=x
		node.isLeftChild=False


	def leftRotation(self,node):
		if(node is None):
			return
		x=node.right
		y=x.right
		x.parent = node.parent

		if(node.parent==None):
			self.root =x

		else:
			if(node.isLeftChild):
				x.isLeftChild=True
				x.parent.left=x
			else:
				x.isLeftChild=False
				x.parent.right=x


		if(x.left is not None):
			node.right=x.left
			node.right.isLeftChild=False
			node.right.parent=node
		else:
			node.right=None

		x.left=node
		node.parent=x
		node.isLeftChild=True

	def leftRightRotation(self, node):
		self.leftRotation(node.left)
		self.rightRotation(node)

	def rightLeftRotation(self, node):
		self.rightRotation(node.right)
		self.leftRotation(node)


	def inOrder(self):
		self.inOrderRec(self.root)


	def inOrderRec(self,root):
		if(root is None):
			return
		self.inOrderRec(root.left)
		print ( root.key, end =' ')
		self.inOrderRec(root.right)

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
				self.leftRightRotation(node.parent.parent)
				node.isBlack = True
				node.right.isBlack=False
				node.left.isBlack=False


	def correctTree(self,node):
		if(node.isLeftChild):
			#Black Aunt
			if(node.parent.parent.right is None or node.parent.parent.right.isBlack):
				return  self.rotateTree(node)
			#Color Flip
			if(node.parent.parent.right!=None ):
				node.parent.parent.right.isBlack=True
			node.parent.isBlack=True
			node.parent.parent.isBlack=False
		else:
			if (node.parent.parent.left is None or node.parent.parent.left.isBlack):
				return self.rotateTree(node)
			#Color Flip
			if (node.parent.parent.left != None):
				node.parent.parent.left.isBlack = True
			node.parent.isBlack = True
			node.parent.parent.isBlack = False





	def checkColor(self,node):
		if(node==self.root):
			node.isBlack=True
			return

		if(node.isBlack==False and node.parent.isBlack==False):
			self.correctTree(node)

		self.checkColor(node.parent)



	def insert(self,key):
		#Create a new Node
		newNode= Node(key)
		if(self.root is None):
			self.root=newNode
		else:
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
			if (root.right == None):
				root.right = newNode
				newNode.parent = root
				newNode.isLeftChild = False
				return
			self.insertNode(root.right,newNode)
	def preOrder(self):
		self.preOrderRec(self.root)

	def preOrderRec(self, root):

		if root is None:
			return
		print(root.key, end=" ")
		self.preOrderRec(root.left)
		self.preOrderRec(root.right)


tree=RedBlackTree()

tree.insert(7)
tree.insert(6)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(1)

print("Inoder Traversal of Created Tree")
tree.inOrder()
print()
print("PostOrder Traversal of Created Tree")
tree.preOrder()


