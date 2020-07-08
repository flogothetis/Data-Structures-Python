class Node:
	def __init__(self,value=None):
		self.key= value
		self.mark=False
		self.parent= None
		self.left=self
		self.right=self
		self.child=None
		self.degree=0


