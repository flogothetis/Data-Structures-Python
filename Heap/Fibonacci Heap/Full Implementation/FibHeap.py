import math
from FibonacciTree import Node

class FibHeap:
	def __init__(self):
		self.min=None
		self.n=0
		self.trace=False
		self.found=None

	def insertNode(self, x):
		if(self.min is None):
			self.min=x
			x.left=self.min
			x.right=self.min
		else:
			x.right=self.min
			x.left=self.min.left
			self.min.left.right=x
			self.min.left=x
			if(x.key < self.min.key):
				self.min=x
		self.n+=1

	def getMin(self):
		if(self.min is not None):
			return self.min.key
		return None

	def extractMin(self):
		z=self.min
		#Traverse or list of children
		# and insert them into list of trees
		if z is not None:
			c=z.child
			k=c
			if( c is not None):
				while True:
					p=c.right
					self.insertNode(c)
					c.parent=None
					c=p
					if(c is None or c==k):
						break
			#Remove min from tree list
			z.left.right=z.right
			z.right.left=z.left
			z.child=None
			if(z==z.right):
				self.min=None
			else:
				self.min=z.right
				self.consolidate()

			self.n-=1
			return z.key
		else:
			return None

	def getDegree(self):
		f=(1+math.sqrt(5))/2
		return int(math.floor(math.log(self.n,f)))+1

	def fib_heap_link(self, y,x):
		y.left.right= y.right
		y.right.left=y.left

		p=x.child
		if p is None:
			y.right=y
			y.left=y
		else:
			y.right=p
			y.left=p.left
			p.left.right=y
			p.left=y
		y.parent=x
		x.child=y

		x.degree=x.degree+1
		x.mark=False

	def displayNode(self,c):
		print('(',end=' ')
		if (c is None):
			print(')',end=' ')
			return
		else:
			tmp = c
			while True:
				print(tmp.key,end=' ')
				k=tmp.child
				self.displayNode(k)
				print('->',end=' ')
				tmp=tmp.right
				if(tmp==c):
					break
			print(')',end=' ')



	def display(self):
		self.displayNode(self.min)
		print()


	def consolidate(self):
		Degree=self.getDegree()
		A=[None]*Degree
		w=self.min
		if w is not None:
			check = self.min
			while True:
				x=w
				d=x.degree
				while A[d] is not None:
					y=A[d]
					if (x.key > y.key):
						temp=x
						x=y
						y=temp
						w=x
					self.fib_heap_link(y,x)
					check=x
					A[d]=None
					d+=1
				A[d]=x
				w=w.right
				if(w is None or w==check):
					break

			self.min=None
			for i in range(0,Degree):
				if(A[i] is not None):
					self.insertNode(A[i])


	def insert(self,key):
		self.insertNode(Node(key))


	def find(self, c, key ):
		if (c is None):
			return None
		else:
			tmp = c
			while True:
				if(tmp.key==key):
					return tmp
				k = tmp.child
				answer = self.find(k,key)
				if(answer is not None):
					return answer
				tmp = tmp.right
				if (tmp == c):
					break
	def  decreaseKey(self,  key,  val):
		if((self.min is not None)):
			x =self.find(self.min, key)
			if(x is not None):
				if(x.key< val):
					return
				#Change value
				x.key=val
				y=x.parent
				if(y!=None and x.key <y.key):
					self.cut(x,y)
					self.cascading_cut(y)
				if(x.key<self.min.key):
					self.min=x
	def cut (self,x,y):
		x.right.left=x.left
		x.left.right=x.right
		y.degree-=1
		x.right=None
		x.left=None
		self.insertNode(x)
		x.parent=None
		x.mark=False

	def cascading_cut(self,y):
		z=y.parent
		if(z is not None):
			if(y.mark==False):
				y.mark= True
			else:
				self.cut(y,z)
				self.cascading_cut(z)













obj = FibHeap()
obj.insert(7)
obj.insert(26)
obj.insert(30)
obj.insert(39)
obj.insert(10)
obj.display()

obj.extractMin()
obj.display()

#System.out.println(obj.extract_min());
#obj.display();
#System.out.println(obj.extract_min());
#obj.display();
#System.out.println(obj.extract_min());
#obj.display();
#System.out.println(obj.extract_min());
#obj.display();