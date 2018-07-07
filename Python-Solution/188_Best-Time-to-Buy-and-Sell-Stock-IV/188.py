class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n // 2:
            return self.quickSolve(prices)

        p = [ [0] * n for i in range(k + 1) ]
        for i in range(1, k + 1):
            tmpMax = -prices[0]
            for j in range(1, n):
                p[i][j] = max(p[i][j - 1], prices[j] + tmpMax)
                tmpMax = max(tmpMax, p[i][j] - prices[j])
        return p[k][n - 1]

    def quickSolve(self, prices):
        n = len(prices)
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
     
prices = [3,2,6,5,0,3]
s = Solution()
r = s.maxProfit(2, prices)
print(r)