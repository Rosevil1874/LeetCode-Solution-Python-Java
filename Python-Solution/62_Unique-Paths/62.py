class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        curr = [1] * m
        for i in range(1, n):
        	for j in range(1, m):
        		curr[j] += curr[j - 1]
        return curr[m - 1]
        

s = Solution()
r = s.uniquePaths(7, 3)
print(r)
