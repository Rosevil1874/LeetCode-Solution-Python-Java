class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		res = []
		n = len(matrix)
		if n == 0:
			return []
		
		rowBegin = 0
		rowEnd = n - 1
		colBegin = 0
		colEnd = len(matrix[1]) - 1

		while rowBegin <= rowEnd and colBegin <= colEnd:
			# 向右
			for j in range(colBegin, colEnd + 1):
				res.append(matrix[rowBegin][j])
			rowBegin += 1

			# 向下
			for i in range(rowBegin, rowEnd + 1):
				res.append(matrix[i][colEnd])
			colEnd -= 1

			# 向左
			j = colEnd
			while j >= colBegin and rowBegin <= rowEnd:
				res.append(matrix[rowEnd][j])
				j -= 1
			rowEnd -= 1

			# 向上
			i = rowEnd
			while i >= rowBegin and colBegin <= colEnd:
				res.append(matrix[i][colBegin])
				i -= 1
			colBegin += 1
			
		return res


matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
s = Solution()
r = s.spiralOrder(matrix)
print(r)
