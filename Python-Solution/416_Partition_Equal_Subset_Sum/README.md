# 416 - [分割等和子集](https://leetcode.com/problems/partition-equal-subset-sum/)

## 题目描述
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Note:**
Each of the array element will not exceed 100.
The array size will not exceed 200.
 

**Example 1:**
	Input: [1, 5, 11, 5]
	Output: true
	Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

**Example 2:**
	Input: [1, 2, 3, 5]
	Output: false
	Explanation: The array cannot be partitioned into equal sum subsets.


## 题解
我们需要找出是否能将序列分为两个子序列，使得他们的和均为sum(nums)/2。类似于背包问题中一个物品要么放进背包要么不放，这里的一个数字要么放进序列要么不放。dp[x]代表可以构造和为x的子序列。
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = [True] + [False] * target
        
        for i in range(1, len(nums)):
            for j in range(target, nums[i - 1] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[target]
```