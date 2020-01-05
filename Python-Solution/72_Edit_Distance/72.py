class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
        	return None

        m = len(matrix)
        n = len(matrix[0])
        row0 = col0 = 1			# 第一列的状态
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			if i == 0:
        				row0 = 0
        			if j == 0:
        				col0 = 0
        			matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
        	for j in range(1, n):
        		if matrix[i][0] == 0 or matrix[0][j] == 0:
        			matrix[i][j] = 0

        if not row0:
        	matrix[0] = [0] * n

        if not col0:
        	for i in range(m):
        		matrix[i][0] = 0
        
       
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

s = Solution()
s.setZeroes(matrix)
print(matrix)