class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1) == 0)

        
# n = 1
# n = 16
n = 4
s = Solution()
r = s.isPowerOfTwo(n)
print(r)