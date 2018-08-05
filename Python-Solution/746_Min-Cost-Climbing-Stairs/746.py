class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 0 or n == 1:
            return 0

        minCost0, minCost1 = cost[0], cost[1]
        for i in range(2, n):
            minCost0, minCost1 = minCost1, min(minCost0, minCost1) + cost[i]

        return min(minCost0, minCost1)
        
# cost = [10, 15, 20]      
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
s = Solution()
r = s.minCostClimbingStairs(cost)
print(r)
   