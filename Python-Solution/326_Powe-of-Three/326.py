import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
        	return False

        maxInt = 0x7fffffff
        max3Power = 3 ** (math.log(maxInt) // math.log(3))		# 换底公式求最大幂次，再使用最大幂次求最大幂
        return max3Power % n == 0


        
# n = 1
# n = 16
n = 45
s = Solution()
r = s.isPowerOfThree(n)
print(r)