class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        notHold = 0                      # 开始状态  
        hold = float('-inf')             # 不可能一开始就持有股票   
        for p in prices:
            hold = max(hold, notHold - p)        # 一直持有股票或买了股票
            notHold = max(notHold, hold + p)     # 一直未持有股票或卖了股票
        return notHold
        	
     
prices = [7,1,5,3,6,4]
s = Solution()
r = s.maxProfit(prices)
print(r)