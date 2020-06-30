import math
import numpy as np

class SparseTable:
	def __init__(self, array):
		self.array=array
		self.cols= len(array)
		self.rows= int(math.floor(math.log(self.cols,2))+1)
		self.table= np.zeros((self.rows, self.cols), dtype='int')
		self.buildTable()

	def buildTable(self):
		self.table[0,0:self.cols]=np.asarray(self.array,dtype='int')
		i=1
		while i< self.rows:
			j = 0
			while j + (1 << (i-1))<self.cols:
				self.table[i,j]= self.function_min (self.table[i-1,j], self.table[i-1, (j + (1<<(i-1)))])
				j+=1
			i+=1
		print('Table')
		print(self.table)

	def min_range_query(self, L,R):
		if(L<=R and L>=0 and R <self.cols):
			j= int(math.log(R-L+1,2))
			return min( self.table[j,L], self.table[j,R - (1<<j)+1 ])
		else:
			return  None

	def function_min (self,a,b):
		return min(a,b)


if __name__ == '__main__':
	sparseT = SparseTable([4,2,3,7,1,5,3,3,9,6,7,-1,4] )
	print ('Query')
	print(sparseT.min_range_query(0,15))
