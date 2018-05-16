class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        notHold = 0                         # 开始状态
        hold = float('-inf')                # 不可能一开始就持有股票
        for p in prices:
            hold = max(hold, notHold - p - fee)         # 一直持有股票或买了股票
            notHold = max(notHold, hold + p)            # 一直未持有股票或卖了股票
        return notHold
        	
     
prices = [1,3,7,5,10,3]
fee = 3
s = Solution()
r = s.maxProfit(prices, fee)
print(r)