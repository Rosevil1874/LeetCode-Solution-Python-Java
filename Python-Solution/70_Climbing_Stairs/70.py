class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        a, b = 1, 2   # 1阶和2阶的方案分别为1种和2种，这是基本问题
        for _ in range(2, n):
            a, b = b, a + b
        return b

        
n = 2
# n = 3
s = Solution()
r = s.climbStairs(n)
print(r)
