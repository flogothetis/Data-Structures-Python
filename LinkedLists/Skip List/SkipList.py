import math
import random

class Node:
	def __init__(self, element,right,down):
		self.value= element
		self.right = right
		self.down= down


class SkipList:
	def __init__(self):
		#head of the highest list
		self.head = Node (-math.inf,None,None)
		self.tail= Node(math.inf,None,None)
		self.head.right=self.tail


	def coinFlip(self):
		return  random.randint(0,1)



	def printAllLevels(self):
		tmp_head=self.head
		tmp_head_down=self.head.down
		while tmp_head:
			print(tmp_head.value, end=" ")
			tmp_head=tmp_head.right
			if(tmp_head==None):
				tmp_head=tmp_head_down
				if(tmp_head_down):
					tmp_head_down=tmp_head_down.down
				print(" ")



	def createNewLevel(self):
		#Create a new level
		# -inf  ------------> +inf
		#-inf  is the new head of the skip list
		head_tmp = Node (-math.inf,None,self.head)
		#inf is the new tail of the skip list
		tail_tmp= Node(math.inf,None,self.tail)
		head_tmp.right=self.tail
		self.head=head_tmp
		self.tail=tail_tmp

	def insert(self,key):

		#Search Path until level 0
		tmp = self.head
		path = []
		while(tmp):
			#move right
			if (tmp.right.value <=key):
				tmp = tmp.right
			else:
				#Store the nodes that yields the algorithm to
				#move one level down
				if(tmp.down!=None):
					path.append(tmp)
				# When it reaches the level  0 --> stop
				if(tmp.down==None):
					break
				else:
					#move down
					tmp=tmp.down
		#if key already exists
		if(tmp.value==key):
			print('Key ', key, 'already exists')
			return

		#Add new node at level 0 and flip a coin. If coin gives '1'
		#then promote the node at level i+1, where i is the current level.
		#If the promoting exceeds the current max height create a new level
		#and add the new node.
		prevNode=None
		pointer= len(path)-1
		while True:
			newNode=Node(key, tmp.right,prevNode)
			tmp.right=newNode
			prevNode=newNode
			if(self.coinFlip()==1):
				if(pointer<0):
					self.createNewLevel()
					tmp=self.head
				else:
					tmp=path[pointer]
					pointer=pointer-1

			else:
				break




if __name__ == '__main__':
	list = SkipList()
	#Insert all elements
	for i in range (0,1024):
		list.insert(i)
	#Print all levels top-down
	list.printAllLevels()