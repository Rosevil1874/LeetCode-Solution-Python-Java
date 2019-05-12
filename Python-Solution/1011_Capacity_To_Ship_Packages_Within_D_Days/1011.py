class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        while left < right:
        	mid = (left + right) // 2
        	need, weight = 1, 0
        	for x in weights:
        		if weight + x > mid:
        			need += 1
        			weight = 0
        		weight += x
        	if need > D:
        		left = mid + 1
        	else:
        		right = mid
        return left
        

        

# weights = [1,2,3,4,5,6,7,8,9,10]
# D = 5

# weights = [3,2,2,4,1,4]
# D = 3

weights = [1,2,3,1,1]
D = 4
s = Solution()
r = s.shipWithinDays(weights, D)
print(r)
