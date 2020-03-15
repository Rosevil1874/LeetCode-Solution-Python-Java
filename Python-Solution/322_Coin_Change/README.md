# 322 - [零钱兑换](https://leetcode.com/problems/coin-change/)

## 题目描述
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

**Example 1:**
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

**Example 2:**
Input: coins = [2], amount = 3
Output: -1

**Note:**
You may assume that you have an infinite number of each kind of coin.

## 题解

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # corner cases
        if not coins:
            return -1
        if not amount:
            return 0
            
        dp = [0] + [float('inf')] * amount

        # dp[i]: 凑齐价值i需要的最少的硬币数量
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] > amount else dp[amount]
```

变体：
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] > amount else dp[amount]
```