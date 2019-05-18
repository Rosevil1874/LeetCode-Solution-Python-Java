class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        plus, need = 0, 0       # 需要加上plus满足unique，下一个数至少是 need 则满足条件
        for x in sorted(A):
            plus += max(need - x, 0)
            need = max(need + 1, x + 1)
        return plus
        	
        
# A = [1,2,2]
A = [3,2,1,2,1,7]

s = Solution()
r = s.minIncrementForUnique(A)
print(r)
    