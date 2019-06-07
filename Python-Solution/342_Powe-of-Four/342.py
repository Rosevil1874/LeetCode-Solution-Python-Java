class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n -1) == 0) and (n & 0x55555555 == n)


        
# n = 1
# n = 16
n = 32
s = Solution()
r = s.isPowerOfFour(n)
print(r)