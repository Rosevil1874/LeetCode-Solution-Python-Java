# 309 - 买卖股票的最佳时机含冷冻期


## 动态规划
我真是。。。很弱啊。。。  
这题感觉看大神的思路都有一点点困难的说。。。  
cr: [4-line Python solution, 52 ms](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/)

>思路：  
The key is 3 states and 5 edges for state transition. 3 states are `notHold (stock)`, `hold (stock)`, and `notHold_cooldown`. The initial values of the latter two are negative infinity since they are meaningless, i.e. you won't hold stocks at first and there's no cooldown at first. The 5 edges:
1. `hold` -----do nothing----->`hold`
2. `hold` -----sell----->`notHold_cooldown`
3. `notHold` -----do nothing -----> `notHold`
4. `notHold` -----buy-----> `hold`
5. `notHold_cooldown` -----do nothing----->`notHold`

最后取`max(hold, notHold, notHold_cooldown)`是因为交易序列可能在任意一种状态下结束。

```Java
class Solution {
    public int maxProfit(int[] prices) {
        int not_hold = 0;                   // 开始状态
        int hold = Integer.MIN_VALUE;       // 不能一开始就持有
        int not_hold_cooldown = Integer.MIN_VALUE;  // 不能一开始就冷冻

        for (int p: prices) {
            hold = Math.max(hold, not_hold - p);
            not_hold = Math.max(not_hold, not_hold_cooldown);
            not_hold_cooldown = hold + p;
        }
        return Math.max(hold, Math.max(not_hold, not_hold_cooldown));
    }
}
```