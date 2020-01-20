# 198 - 打家劫舍

## 题目描述
![problem](images/189.png)

## 1. top-down recursive
小偷在一个房屋有两种选择，抢或不抢。抢劫房屋i的战利品是抢劫房屋i-2的最高战利品加上当前战利品，不抢房屋i的战利品是抢房屋i-1的最高战利品。 `loot(i) = Math.max( loot(i - 2) + currentHouseValue, loot(i - 1) )`

这个代码提交后的结果是Time Limit Exceeded。
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.loot(nums, len(nums) - 1)
        
    def loot(self, nums: List[int], i:int) -> int:
        if i < 0:
            return 0
        return max(nums[i] + self.loot(nums, i - 2), self.loot(nums, i - 1))
```

## 2. top-down recursive + memo

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*(len(nums) + 1)
        return self.loot(nums, memo, len(nums) - 1)
        
    def loot(self, nums: List[int], memo: List[int], i: int) -> int:
        if i < 0:
            return 0
        if memo[i] >= 0:
            return memo[i]
        else:
            curr_loot = max(nums[i] + self.loot(nums, memo, i - 2), self.loot(nums, memo, i - 1))
            memo[i] = curr_loot
            return curr_loot
```

## 3. bottom-up iterative + memo
memo[i]表示从第1家到第i-1家的最高战利品。时间复杂度：O(N), 空间复杂度：O(N)。
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        memo = [-1] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i + 1] = max(memo[i], memo[i - 1] + val)
        return memo[len(nums)]
```

## 4. bottom-up iterative + memo(2 variables)
计算下到下一户为止的最高战利品只需要用到前两户为止的最高战利品，因此不需要额外使用一个列表进行存储。
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        prev1 = 0   # 到前1户为止的最高战利品
        prev2 = 0   # 到前2户为止的最高战利品
        
        for num in nums:
            prev1, prev2 = max(prev1, prev2 + num), prev1
        return prev1
```