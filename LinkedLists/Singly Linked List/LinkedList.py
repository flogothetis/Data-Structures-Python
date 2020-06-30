from Node import Node

class LinkedList:
	def __init__(self):
		self.head=None
	def insert(self, element):
		# If list is empty, initialize head
		if self.head==None:
			self.head= Node(element)
			return
		#else ...
		tmp= self.head
		while(tmp.next!=None):
			tmp=tmp.next
		tmp.next=Node(element)

	def search(self,element):
		tmp=self.head
		while(tmp!=None):
			if(tmp.data==element):
				return  element
			tmp=tmp.next
		return None

	def delete(self,element):
		#If deleted element is head
		if(self.head.data==element):
			self.head=self.head.next
		#Delete other nodes that are not head of the list
		prev = self.head
		next=self.head
		while (next != None):
			if (next.data == element):
				prev.next= next.next
				next = next.next

			else:
				prev=next
				next=next.next

	def printList(self):
		tmp=self.head
		count=1
		while(tmp!=None):
			print("Element", count, "has value", tmp.data)
			tmp=tmp.next
			count=count+1


if __name__=="__main__":
	list = LinkedList()
	for i in range (0 ,123):
		list.insert(i)
	list.delete(122)
	list.printList()