# 746 - 使用最小花费爬楼梯

## 题目描述
![problem](images/746.png)


## 方法
依次对每一步阶梯，记录从第0级或第1级开始走到这的最小花费。
```python
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
```
