from Node import Node

class CircularList:
	def __init__(self):
		self.head=None
	def insertAtFront(self, element):
		# If list is empty, initialize head
		if self.head==None:
			self.head= Node(element)
			self.head.next=self.head
			return
		#else ...
		#Create new Node that points to the current head
		newNode= Node(element)
		newNode.next=self.head
		#Search for the last node in list
		tmp= self.head
		while(tmp.next!=self.head):
			tmp=tmp.next
		#Last node points to new node
		tmp.next=newNode
		#Change head
		self.head=newNode

	def search(self,element):
		tmp=self.head
		while True and tmp:
			if(tmp.data==element):
				return  element
			tmp=tmp.next
			if(tmp==self.head):
				break
		return None

	def delete(self,element):
		if(self.head==None):
			return
		#If deleted element is head
		if(self.head.data==element):
			# Search for the last node in list
			tmp = self.head
			while (tmp.next != self.head):
				tmp = tmp.next
			tmp.next= self.head.next
			#delete previous head
			deleteHead= self.head
			self.head= self.head.next
			del deleteHead
			return

		#Delete other nodes that are not head of the list
		prev = self.head
		next=self.head.next
		while (next != self.head):
			#If found, delete the node from the list
			if (next.data == element):
				prev.next= next.next
				deleteNode=next
				next = next.next
				del deleteNode
			#else, keep searching
			else:
				prev=next
				next=next.next

	def printList(self):
		tmp=self.head
		count=1
		while(tmp.next!=self.head):
			print("Element", count, "has value", tmp.data)
			tmp=tmp.next
			count=count+1
		print("Element", count, "has value", tmp.data)


if __name__=="__main__":
	list = CircularList()
	#Insert 124 elements
	for i in range (0 ,123):
		list.insertAtFront(i)
	#Delete the head of the list
	list.delete(122)
	#Print List
	list.printList()