from Node import Node
class AVL:
	def __init__(self):
		self.root=None

	def insert(self,key):
		self.root=self.insertRec(self.root,key)

	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def insertRec(self, root, key):
		if root is None:
			return Node(key)
		elif key <= root.data:
			self.left= self.insertRec(root.left,key)
		else:
			self.right=self.insertRec(root.right,key)

		# self-balancing
		root.height = 1 + max (self.getHeight(root.left),
							   self.getHeight(root.right))

