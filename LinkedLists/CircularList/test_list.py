import  unittest

from CircularList import CircularList


class Testing(unittest.TestCase):


	def insert_elements(self):
		self.list = CircularList()
		for i in range(0, 1234):
			self.list.insertAtFront(i)

	def test_search(self):
		self.insert_elements()
		self.assertEqual(self.list.search(0),0)
		self.assertEqual(self.list.search(50),50)
		self.assertIsNone(self.list.search(1234))

		


if __name__ == '__main__':
	unittest.main()