import math
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            need = sum( math.ceil(x / mid) for x in piles )
            if need > H:
                left = mid + 1
            else:
                right = mid
        return left
        	
        
piles = [3,6,7,11]
H = 8

# piles = [30,11,23,4,20]
# H = 5

# piles = [30,11,23,4,20]
# H = 6
s = Solution()
r = s.minEatingSpeed(piles, H)
print(r)
    