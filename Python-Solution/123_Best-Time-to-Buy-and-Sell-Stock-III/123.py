class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        notHold1 = 0                        
        notHold2 = 0                         
        hold1 = float('-inf')                
        hold2 = float('-inf')                
        for p in prices:
            hold1 = max(hold1, -p)                  # 借钱买了第一支股票
            notHold1 = max(notHold1, hold1 + p)     # 卖了第一支股票
            hold2 = max(hold2, notHold1 - p)        # 买了第二支股票
            notHold2 = max(notHold2, hold2 + p)     # 卖了第二支股票
        return notHold2
        	
     
prices = [3,3,5,0,0,3,1,4]
s = Solution()
r = s.maxProfit(prices)
print(r)