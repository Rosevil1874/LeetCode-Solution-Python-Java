class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        cnt = 1
        i = 2
        while (i/2)*(i/2) <= N:
            if (N - i * (i - 1) // 2) % i == 0:
                a = (N - i * (i - 1) // 2) / i
                if a > 0:
                    cnt += 1
            i += 1
        return cnt
        
        
N = 2
s = Solution()
r = s.consecutiveNumbersSum(N)
print(r) 