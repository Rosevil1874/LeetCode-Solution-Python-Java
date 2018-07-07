class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		if n == 0:
			return []

		res = [ [0] * n for i in range(n) ]
		num = 1
		rowBegin = colBegin = 0
		rowEnd = colEnd = n - 1
		
		while rowBegin <= rowEnd and colBegin <= colEnd:
			# 向右
			for j in range(colBegin, colEnd + 1):
				res[rowBegin][j] = num
				num += 1
			rowBegin += 1

			# 向下
			for i in range(rowBegin, rowEnd + 1):
				res[i][colEnd] = num
				num += 1
			colEnd -= 1

			# 向左
			j = colEnd
			while j >= colBegin and rowBegin <= rowEnd:
				res[rowEnd][j] = num
				num += 1
				j -= 1
			rowEnd -= 1

			# 向上
			i = rowEnd
			while i >= rowBegin and colBegin <= colEnd:
				res[i][colBegin] = num
				num += 1
				i -= 1
			colBegin += 1
			
		return res
		

n = 3
s = Solution()
r = s.generateMatrix(n)
# print(r)
