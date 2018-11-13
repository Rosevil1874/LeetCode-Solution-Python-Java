import collections
class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        s = set(A)
        res = 0
        for j in range(len(A)):
        	for i in range(j):
        		a, b = A[i], A[j]
        		if b - a < a and b - a in s:
        			dp[a, b] = dp.get((b - a, a), 2) + 1
        			res = max(res, dp[a, b])
        return max(dp.values() or [0])
        	
        
A = [1,2,3,4,5,6,7,8]
# A = [1,3,7,11,12,14,18]
s = Solution()
r = s.lenLongestFibSubseq(A)
print(r)
    