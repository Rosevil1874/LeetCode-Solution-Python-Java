# 121 - 买卖股票的最佳时机


## 题解
```Java
class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) {
            return 0;
        }

        int min_price = Integer.MAX_VALUE;
        int max_profit = 0;

        for (int p:prices) {
            min_price = Math.min(min_price, p);
            max_profit = Math.max(max_profit, p - min_price);
        }
        return max_profit;
    }
}       
```