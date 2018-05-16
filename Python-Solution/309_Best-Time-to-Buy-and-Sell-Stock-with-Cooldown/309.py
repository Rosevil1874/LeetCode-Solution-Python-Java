class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        notHold = 0                         # 开始状态
        hold = float('-inf')                # 不可能一开始就持有股票
        notHold_cooldown = float('-inf')    # 不可能一开始就冷冻
        for p in prices:
            hold = max(hold, notHold - p)               # 一直持有股票或买了股票
            notHold = max(notHold, notHold_cooldown)    # 一直未持有股票或刚渡过冷冻期
            notHold_cooldown = hold + p                 # 刚卖掉了股票进入冷冻期
        return max(hold, notHold, notHold_cooldown)
        	
     
prices =[1, 2, 3, 0, 2]
s = Solution()
r = s.maxProfit(prices)
print(r)