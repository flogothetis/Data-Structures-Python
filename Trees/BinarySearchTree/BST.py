from Node import Node


class BST:
	def __init__(self):
		self.root=None

	def insert(self,key):
		self.root=self.insertRec(self.root,key)

	def insertRec(self,node,key):
		#Insert at root
		if(node == None):
			node= Node(key)
			return node

		#else, create either a intermediate or leaf node
		if(key <= node.data):
			node.left = self.insertRec(node.left,key)
		else:
			node.right=self.insertRec(node.right,key)
		return  node

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


	def inOrderSuc(self,node):
		current=node
		while (current.left is not None):
			current=current.left
		return  current

	def delete(self,key ):
		self.deleteRec(self.root,key )

	def deleteRec(self,node,key):
		if(node is None):
			return node
		if key < node.data:
			node.left=self.deleteRec(node.left,key)
		elif key > node.data:
			node.right=self.deleteRec(node.right,key)
		else:
			#node data ==key
			if node.left is None:
				temp= node.right
				node=None
				return  temp
			elif node.right is None:
				temp=node.left
				node=None
				return  temp
			#locate inorder successor
			temp = self.inOrderSuc(node.right)
			node.data=temp.data
			node.right=self.deleteRec(node.right, temp.data)

		return node

	# A utility function to do inorder traversal of BST
	def inorder(self):
		self.inorderRec(self.root)
		print()

	def inorderRec(self,root):
		if root is not None:
			self.inorderRec(root.left)
			print (root.data,end=" ")
			self.inorderRec(root.right)


if __name__ == '__main__':

	bst= BST ()
	bst.insert( 50)
	bst.insert (30)
	bst.insert( 20)
	bst.insert( 40)
	bst.insert( 60)
	bst.insert( 80)
	bst.inorder()
	bst.delete(40)
	bst.inorder()














