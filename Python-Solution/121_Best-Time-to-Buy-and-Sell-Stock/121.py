class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
        	maxProfit = max(maxProfit, prices[i] - minPrice)
        	minPrice = min(minPrice, prices[i])
        return maxProfit
        	
     
prices =  [7,1,5,3,6,4]

  
s = Solution()
r = s.maxProfit(prices)
print(r)