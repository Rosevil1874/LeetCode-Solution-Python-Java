import collections
class Solution(object):
	def maxUncrossedLines(self, A, B):
		"""
		:type A: List[int]
		:type B: List[int]
		:rtype: int
		"""
		lenA, lenB = len(A), len(B)
		dp = [0]*(lenB + 1)
		for i in range(lenA):
			for j in range(lenB)[::-1]:
				if A[i] == B[j]:
					dp[j + 1] = dp[j] + 1
			for j in range(lenB):
				dp[j + 1] = max(dp[j], dp[j + 1])
		return dp[lenB]


# A = [1,4,2]
# B = [1,2,4]               

A = [2,5,1,2,5]
B = [10,5,2,1,5,2]

# A = [1,3,7,1,7,5]
# B = [1,9,2,5,1]

# A = [1,1,3,5,3,3,5,5,1,1]
# B = [2,3,2,1,3,5,3,2,2,1]

s = Solution()
r = s.maxUncrossedLines(A, B)
print(r)
