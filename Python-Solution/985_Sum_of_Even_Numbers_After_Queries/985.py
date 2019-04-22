class Solution(object):
	def sumEvenAfterQueries(self, A, queries):
		"""
		:type A: List[int]
		:type queries: List[List[int]]
		:rtype: List[int]
		"""
		res = []
		origin_sum = sum([i for i in A if i%2 == 0 ])
		print(origin_sum)
		for item in queries:
			val, index = item[0], item[1]
			if A[index]%2 == 0: origin_sum -= A[index]		# 这个数是偶数，已经加进origin_sum中了，先将其减掉
			A[index] += val									# 加上val
			if A[index]%2 == 0: origin_sum += A[index]		# 若加上val后是偶数，就将其加进origin_sum

			res.append(origin_sum )
		return res

	   
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
s = Solution()
r = s.sumEvenAfterQueries(A, queries)
print(r)
