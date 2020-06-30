from Node import Node
class DoublyLinkedList:
	def __init__(self):
		self.head=None

	def insertAtFront(self,data):
		newNode= Node(data)
		newNode.next=self.head
		if(self.head):
			self.head.prev=newNode
		self.head=newNode


	def deleteNode(self, node):
		if(node==None):
			return
		#If node is head
		if node ==self.head:
			tmp_head = self.head
			self.head =self.head.next
			#delete Node
			tmp_head.next=None
			del tmp_head
			return
		#If node is somewhere in the list
		prevNode= node.prev
		nextNode=node.next
		prevNode.next=nextNode
		#delete node
		node.prev=None
		node.next=None
		del node

	def searchNodeWithValue(self,value):
		tmp=self.head
		count=0
		while(tmp):
			if(tmp.data == value):
				return tmp
			tmp=tmp.next
		return None

	def printForward(self):
		tmp=self.head
		count=0
		while(tmp):
			print('Value of node', count, 'is', tmp.data)
			tmp=tmp.next


if __name__ == '__main__':
	doublyList= DoublyLinkedList()
	for i in range (0,100):
		doublyList.insertAtFront(i);

	doublyList.printForward()
	node=doublyList.searchNodeWithValue(50)
	print('Delete 50 ')
	doublyList.deleteNode(node)
	doublyList.printForward()
