class FibonacciTree:
	def __init__(self,value):
		self.value= value
		self.child=[]
		self.order=0
	def add_at_end(self,t):
		self.child.append(t)
		self.order+=1