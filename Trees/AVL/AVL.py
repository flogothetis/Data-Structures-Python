from Node import Node
class AVL:
	def __init__(self):
		self.root=None

	def insert(self,key):
		self.root=self.insertRec(self.root,key)

	#Get the height of a node
	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	#Get the difference of height between
	#left and right subtree
	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)


	def leftRotate(self,z):
		y=z.right
		T2=y.left

		y.left=z
		z.right=T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
					   self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
					   self.getHeight(y.right))

	# Return the new root
		return y

	def rightRotate(self,z):
		y=z.left
		T2=y.right

		y.right=z
		z.left=T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
					   self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
					   self.getHeight(y.right))
	# Return the new root
		return y

	#make rotation, if it is needed
	def makeRotations(self, root):
		if root is None:
			return root

		balance=self.getBalance(root)

		# left-right rotate
		if (balance > 1 and self.getBalance(root.left) < 0):
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)
		# right-left rotate
		elif (balance < -1 and self.getBalance(root.right) > 0):
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)
		# left-left
		elif (balance > 1 and self.getBalance(root.left) >= 0):
			return self.rightRotate(root)
		# right-right
		elif (balance < -1 and self.getBalance(root.right) <= 0):
			return self.leftRotate(root)
		else:
			return root

	def insertRec(self, root, key):
		if root is None:
			return Node(key)
		elif key <= root.data:
			root.left= self.insertRec(root.left,key)
		else:
			root.right=self.insertRec(root.right,key)

		# self-balancing
		root.height = 1 + max (self.getHeight(root.left),
							   self.getHeight(root.right))
		#balance tree
		return self.makeRotations(root)

	#Search for inorder successor if it is
	#needed
	def inOrderSuccessor(self,node):
		current = node
		while (current.left is not None):
			current = current.left
		return current

	def delete(self,key):
		self.root=self.deleteRec(self.root,key)


	def deleteRec(self,root,key):
		if root is None:
			return root
		elif key < root.data:
			root.left= self.deleteRec(root.left,key)
		elif key > root.data:
			root.right=self.deleteRec(root.right,key)
		else:
			#Delete node that is either leaf or intermediate node
			if (root.left is None):
				tmp=root.right
				root=None
				return tmp
			elif (root.right is None):
				tmp=root.left
				root=None
				return tmp
			else:
				#Node has two childen
				minNode=self.inOrderSuccessor(root.right)
				root.data=minNode.data
				root.right=self.deleteRec(root.right,minNode.data)
			# Step 2 - Update the height of the
			# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
								  self.getHeight(root.right))
		return self.makeRotations(root)



	def preOrder(self):
		self.preOrderRec(self.root)

	def preOrderRec(self, root):

		if root is None:
			return
		print(root.data, end=" ")
		self.preOrderRec(root.left)
		self.preOrderRec(root.right)


if __name__ == '__main__':
	tree=AVL()
	tree.insert( 10)
	tree.insert( 20)
	tree.insert( 30)
	tree.insert( 40)
	tree.insert( 50)
	tree.insert( 25)

	#delete node from AVL
	tree.delete(30)
	"""The constructed AVL Tree would be 
	            30 
	           /  \ 
	         20   40 
	        /  \     \ 
	       10  25    50"""

	# Preorder Traversal
	print("Preorder traversal of the",
		  "constructed AVL tree is")
	tree.preOrder()
	print()






